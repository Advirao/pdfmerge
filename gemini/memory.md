# Memory

## User Preferences

- Prefers cleanly organized project structures.
- User is on a Windows machine.

## Known Issues & Workarounds

- **Streamlit Execution on Windows with UV**: Running the default `streamlit run` wrapper binary sometimes causes a "Failed to canonicalize script path" error. **Workaround**: Use `python -m streamlit run app.py` instead.
