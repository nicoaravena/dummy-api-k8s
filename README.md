# dummy-api-k8s

Dummy api

## Install
```
$ python -m virtualenv .venv --python=python3
$ .venv/bin/python -m pip install -U -r requirements.txt
```
## Execute

With FastAPI:
```
$ .venv/bin/fastapi dev api/main.py
```

Or with uvicorn:
```
$ .venv/bin/uvicorn api.main:app
```

## Use database

1. Execute both sql files contained in `./model`
2. Create a copy of `settings.cfg.dist` and modify the [saas_db] and [instance] with your database config
3. Restart the fastapi script.
