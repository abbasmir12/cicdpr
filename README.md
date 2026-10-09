# Freebuff Flask App — CI/CD Learning Project

A tiny Flask app used to learn CI/CD with GitLab CI, GitHub Actions, and Render.

## Project Structure

```
├── app.py           # Flask application
├── requirements.txt   # Python dependencies
├── .gitlab-ci.yml    # GitLab CI/CD pipeline config
└── .github/
    └── workflows/
        └── ci.yml    # GitHub Actions CI/CD pipeline config
```

## Local Development

```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000/
```

## What You'll Learn

### 1. GitLab CI/CD (`.gitlab-ci.yml`)
- **Stages**: `install` → `test` → `deploy`
- **Jobs**: runs in parallel/series based on dependencies
- **Conditional execution**: `only:` / `when:` controls when jobs run
- Push to `main` triggers the pipeline automatically
- Final `deploy` job is `manual` — you click "Play" in the GitLab UI to trigger it

### 2. GitHub Actions (`.github/workflows/ci.yml`)
- **Workflows**: defined in YAML under `.github/workflows/`
- **Triggers**: `push`, `pull_request`, or `workflow_dispatch` (manual)
- **Jobs**: run on `ubuntu-latest` runners
- **Actions**: reusable tasks like `actions/checkout`, `actions/setup-python`, `actions/cache`
- The `deploy` job will only run on push to `main`

### 3. Render Deployment
- Push code to `main` → Render auto-builds and deploys
- Start command: `python app.py`
- Environment vars: `FLASK_ENV=production`, `PORT` (Render sets this)
- Render exposes your app at a `.onrender.com` URL

## Next Steps

1. Push this repo to GitLab (or GitHub)
2. Set up CI/CD pipelines
3. Connect Render for deployment
4. Watch your first pipeline run!

## License

MIT
