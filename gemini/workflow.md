# Workflows

---

## description: How to start the development server

1. Ensure you are in the project root directory.
2. Run the application using the following command to avoid Windows execution policies on the Streamlit executable:
   // turbo

```bash
python -m streamlit run app.py
```

---

## description: How to add a dependency

1. Use `uv add <package_name>` to add new packages to `pyproject.toml` and update the `uv.lock`.
