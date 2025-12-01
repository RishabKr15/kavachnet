# Developer Setup Guide

This guide explains how to set up the KavachNet project on a new machine for development.

## 1. Prerequisites
Ensure the following are installed on the new system:
- **Python 3.11+**
- **Git**

## 2. Clone the Repository
Open a terminal and run:
```bash
git clone https://github.com/RishabKr15/kavachnet.git
cd kavachnet
```

## 3. Set Up Virtual Environment
You must create a fresh virtual environment and install dependencies.

### Windows
```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Install package in editable mode (Important for dev!)
pip install -e .
```

### Mac / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## 4. Verify Installation
Run the application to ensure everything is working:
```bash
python -m kavachnet.cli
```

## 5. Workflow for Updates

### Updating Data (Weekly)
To fetch new VPN IPs and auto-bump the version:
```bash
python scripts/enrich_data.py
git commit -am "Update data"
git push
```

### Updating Code
1. Edit the files.
2. Manually update version in `pyproject.toml` AND `src/kavachnet/__init__.py`.
3. Commit and push:
   ```bash
   git add .
   git commit -m "Fix bug in app.py"
   git push
   ```

## 6. Syncing Changes
If you switch between computers, always pull the latest changes first:
```bash
git pull
```
