from __future__ import annotations

import os
from pathlib import Path
import cv2


def allowed_file(filename: str, allowed_extensions: set[str]) -> bool:
    return "." in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def is_face_image(image_path: str | Path) -> bool:
    try:
        image = cv2.imread(str(image_path))
        if image is None:
            return False
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(60, 60))
        return len(faces) > 0
    except Exception:
        return False


def resize_image_if_needed(filepath: str | Path, max_size_mb: float = 1.0, max_dimension: int = 1024) -> None:
    filepath = Path(filepath)
    max_size_bytes = int(max_size_mb * 1024 * 1024)
    if not filepath.exists() or filepath.stat().st_size <= max_size_bytes:
        return

    image = cv2.imread(str(filepath))
    if image is None:
        return

    h, w = image.shape[:2]
    if max(h, w) > max_dimension:
        ratio = max_dimension / float(max(h, w))
        image = cv2.resize(image, (int(w * ratio), int(h * ratio)), interpolation=cv2.INTER_AREA)

    quality = 90
    success, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, quality])
    if not success:
        return

    while buffer.nbytes > max_size_bytes and quality > 20:
        quality -= 5
        success, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, quality])
        if not success:
            return

    filepath.write_bytes(buffer.tobytes())
