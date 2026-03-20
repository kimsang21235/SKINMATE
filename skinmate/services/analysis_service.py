from __future__ import annotations

import math
from functools import lru_cache
from pathlib import Path

import cv2
import numpy as np
from flask import current_app

try:
    import tensorflow as tf
except Exception:  # pragma: no cover
    tf = None


MODEL_RANGES = {
    "moisture": (0.5, 4.5),
    "elasticity": (1.0, 4.0),
    "wrinkle": (0.5, 4.5),
}


def _score_from_range(raw_value: float, metric: str) -> float:
    low, high = MODEL_RANGES[metric]
    score = ((raw_value - low) / (high - low)) * 100.0
    return round(max(0.0, min(100.0, score)), 1)


@lru_cache(maxsize=3)
def _load_interpreter(model_path: str):
    if tf is None:
        return None
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter


def _predict_metric(image_path: str | Path, metric: str) -> float:
    model_path = str(Path(current_app.config["MODEL_DIR"]) / f"model_test_{metric}.tflite")
    fallback = current_app.config["DEFAULT_FALLBACK_SCORES"][metric]
    if tf is None or not Path(model_path).exists():
        return fallback

    try:
        interpreter = _load_interpreter(model_path)
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        image = cv2.imread(str(image_path))
        if image is None:
            return fallback
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        width = int(input_details[0]["shape"][2])
        height = int(input_details[0]["shape"][1])
        image = cv2.resize(image, (width, height))

        input_data = np.expand_dims(image, axis=0)
        expected_dtype = input_details[0]["dtype"]
        if expected_dtype == np.float32:
            input_data = input_data.astype(np.float32) / 255.0
        else:
            input_data = input_data.astype(expected_dtype)

        interpreter.set_tensor(input_details[0]["index"], input_data)
        interpreter.invoke()
        raw = float(interpreter.get_tensor(output_details[0]["index"])[0][0])
        return _score_from_range(raw, metric)
    except Exception:
        return fallback


def _infer_skin_type(scores: dict[str, float]) -> str:
    moisture = scores["moisture"]
    wrinkle = scores["wrinkle"]
    elasticity = scores["elasticity"]

    if moisture < 35:
        return "건성" if wrinkle >= 45 else "복합 건성"
    if moisture > 72 and elasticity >= 55:
        return "지성" if wrinkle < 55 else "복합 지성"
    if 40 <= moisture <= 70 and elasticity >= 50 and wrinkle >= 45:
        return "중성"
    if moisture > 65:
        return "복합 지성"
    return "복합 건성"


def get_skin_scores(image_path: str | Path) -> dict[str, float | str]:
    scores = {
        "moisture": _predict_metric(image_path, "moisture"),
        "elasticity": _predict_metric(image_path, "elasticity"),
        "wrinkle": _predict_metric(image_path, "wrinkle"),
    }
    scores["skin_type"] = _infer_skin_type(scores)
    return scores
