# Sphinx Documentation

# Virtual environment
```
# windows

python -m venv venv

 source ./venv/Scripts/activate

```

## Sphinx server setup

```
sphinx-quickstart

mkdir docs
sphinx-build -b html ./source ./docs
cd docs
# new termninal ind docs directory
python -m http.server

```