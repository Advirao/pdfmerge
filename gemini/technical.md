# Technical Architecture

## Architecture

- **Frontend/Backend**: Streamlit (`app.py`) serves as both the frontend UI and the backend logic handler.
- **PDF Processing**: Handled in-memory using `io.BytesIO()` and the `pypdf.PdfWriter` class. This means files aren't saved to disk during the merging process.

## Key Files

- `app.py`: Main application code, handles the UI and the merge logic.
- `pyproject.toml` / `uv.lock`: Dependency definitions and locks (managed by `uv`).
- `README.md`: Project documentation.

## Running the App

To run the app locally, use the following bash command:

```bash
python -m streamlit run app.py
```
