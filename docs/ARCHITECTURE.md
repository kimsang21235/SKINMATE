# SKINMATE Architecture

## Request flow
1. User registers or logs in.
2. User uploads a face image from the analysis page.
3. `routes.py` validates the file and stores it in `uploads/` temporarily.
4. `analysis_service.py` resizes the image, checks whether a face exists, and runs TFLite models.
5. Recommendation and routine services turn scores into skincare advice.
6. The result is saved into SQLite and rendered back to the user.
7. History endpoints aggregate previous analysis records for chart rendering.

## Package responsibility
- `skinmate/auth.py`: authentication routes and session handling
- `skinmate/routes.py`: page routes, analysis flow, history API
- `skinmate/db.py`: SQLite connection management and runtime bootstrap
- `skinmate/services/analysis_service.py`: image scoring and fallback logic
- `skinmate/services/recommendation_service.py`: concern extraction and summary text
- `skinmate/services/routine_service.py`: routine payload generation for templates
- `skinmate/utils/`: reusable helpers for templates and image handling
- `skinmate/resources/`: TFLite models, seeded product DB, recommendation rules

## Why this structure works for a portfolio
- Keeps Flask entrypoint thin and readable
- Separates HTTP, business logic, persistence, and utility code
- Makes local execution possible without cloud dependencies
- Preserves a complete demo flow: auth → upload → analyze → recommend → history
