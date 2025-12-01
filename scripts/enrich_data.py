import os
import sys
import re
from pathlib import Path

# Add src to path so we can import kavachnet
sys.path.append(str(Path(__file__).parent.parent / "src"))

from kavachnet.vpn_checker import refresh_cache

PROJECT_ROOT = Path(__file__).parent.parent
DATA_FILE = PROJECT_ROOT / "src" / "kavachnet" / "data" / "vpn_ip_list.txt"
PYPROJECT_FILE = PROJECT_ROOT / "pyproject.toml"
INIT_FILE = PROJECT_ROOT / "src" / "kavachnet" / "__init__.py"

def bump_version(current_version):
    major, minor, patch = map(int, current_version.split('.'))
    return f"{major}.{minor}.{patch + 1}"

def update_version_in_file(file_path, pattern, new_version):
    with open(file_path, 'r') as f:
        content = f.read()
    
    new_content = re.sub(pattern, lambda m: m.group(0).replace(m.group(1), new_version), content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)

def get_current_version(file_path, pattern):
    with open(file_path, 'r') as f:
        content = f.read()
    match = re.search(pattern, content)
    if match:
        return match.group(1)
    raise ValueError(f"Could not find version in {file_path}")

def main():
    print(f"--- Enriching Data ---")
    print(f"Target File: {DATA_FILE}")
    
    # Ensure the file exists (create empty if not)
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.touch()

    # Run the enrichment
    refresh_cache(cache_path=str(DATA_FILE))
    
    print(f"\n--- Bumping Version ---")
    # Get current version from pyproject.toml
    current_version = get_current_version(PYPROJECT_FILE, r'version = "(\d+\.\d+\.\d+)"')
    new_version = bump_version(current_version)
    
    print(f"Current Version: {current_version}")
    print(f"New Version:     {new_version}")
    
    # Update pyproject.toml
    update_version_in_file(PYPROJECT_FILE, r'version = "(\d+\.\d+\.\d+)"', new_version)
    
    # Update __init__.py
    update_version_in_file(INIT_FILE, r'__version__ = "(\d+\.\d+\.\d+)"', new_version)
    
    print(f"\n--- Done! ---")
    print(f"1. Review changes: git diff")
    print(f"2. Commit changes: git commit -am 'Enrich data and bump to v{new_version}'")
    print(f"3. Push to GitHub: git push")
    print(f"4. Create Release: Create tag v{new_version} on GitHub to trigger PyPI publish.")

if __name__ == "__main__":
    main()
