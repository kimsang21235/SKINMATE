# Security Checklist Before Pushing to GitHub

Check these items before each push:

1. `.env` is not staged.
2. `instance/` database files are not staged.
3. `uploads/` and `skinmate/static/uploads_temp/` contain only `.gitkeep`.
4. No API keys, OAuth credentials, tokens, or private links are hardcoded in source files.
5. Run `git status` and inspect the staged files before `git commit`.

Useful command:

```bash
git status
grep -RIn "AIza\|client_secret\|SECRET_KEY=\|access_token\|token" .
```
