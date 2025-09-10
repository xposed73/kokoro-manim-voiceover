#!/usr/bin/env python3
"""
Simple script to bump version in pyproject.toml
Usage: python bump_version.py [patch|minor|major]
"""

import re
import sys
from pathlib import Path

def get_current_version():
    """Get current version from pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found!")
        return None
    
    content = pyproject_path.read_text()
    match = re.search(r'version = "([^"]+)"', content)
    if match:
        return match.group(1)
    else:
        print("❌ Could not find version in pyproject.toml!")
        return None

def bump_version(version, bump_type):
    """Bump version based on type"""
    parts = [int(x) for x in version.split('.')]
    
    if bump_type == 'patch':
        parts[2] += 1
    elif bump_type == 'minor':
        parts[1] += 1
        parts[2] = 0
    elif bump_type == 'major':
        parts[0] += 1
        parts[1] = 0
        parts[2] = 0
    else:
        print(f"❌ Invalid bump type: {bump_type}")
        return None
    
    return '.'.join(map(str, parts))

def update_version(new_version):
    """Update version in pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    
    # Replace version line
    new_content = re.sub(
        r'version = "[^"]+"',
        f'version = "{new_version}"',
        content
    )
    
    pyproject_path.write_text(new_content)
    print(f"✅ Updated version to {new_version}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py [patch|minor|major]")
        print("\nExamples:")
        print("  python bump_version.py patch  # 0.1.3 -> 0.1.4")
        print("  python bump_version.py minor  # 0.1.3 -> 0.2.0")
        print("  python bump_version.py major  # 0.1.3 -> 1.0.0")
        return
    
    bump_type = sys.argv[1].lower()
    if bump_type not in ['patch', 'minor', 'major']:
        print("❌ Invalid bump type. Use: patch, minor, or major")
        return
    
    current_version = get_current_version()
    if not current_version:
        return
    
    new_version = bump_version(current_version, bump_type)
    if not new_version:
        return
    
    print(f"🔄 Bumping version from {current_version} to {new_version}")
    update_version(new_version)

if __name__ == "__main__":
    main()
