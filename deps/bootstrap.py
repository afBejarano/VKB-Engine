#!/usr/bin/env python3
"""
Simple dependency bootstrap script for VKB-Engine project.
Downloads and configures dependencies based on bootstrap.json.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def clone_repository(url, tag, target_dir):
    """Clone a git repository with a specific tag."""
    print(f"Cloning {url} (tag: {tag}) to {target_dir}")
    
    # Remove existing directory if it exists
    if os.path.exists(target_dir):
        print(f"Removing existing {target_dir}")
        subprocess.run(f"rm -rf {target_dir}", shell=True)
    
    # Clone repository
    success, output = run_command(f"git clone {url} {target_dir}")
    if not success:
        print(f"Failed to clone {url}: {output}")
        return False
    
    # Checkout specific tag
    success, output = run_command(f"git checkout {tag}", cwd=target_dir)
    if not success:
        print(f"Failed to checkout tag {tag}: {output}")
        return False
    
    return True

def main():
    script_dir = Path(__file__).parent
    bootstrap_file = script_dir / "bootstrap.json"
    
    if not bootstrap_file.exists():
        print(f"Error: {bootstrap_file} not found!")
        sys.exit(1)
    
    # Load dependencies
    with open(bootstrap_file, 'r') as f:
        config = json.load(f)
    
    deps_dir = script_dir / "src"
    deps_dir.mkdir(exist_ok=True)
    
    print("Bootstrapping dependencies...")
    
    for dep in config["dependencies"]:
        name = dep["name"]
        url = dep["url"]
        tag = dep["tag"]
        target_dir = deps_dir / name
        
        print(f"\nProcessing {name}...")
        
        if not clone_repository(url, tag, target_dir):
            print(f"Failed to bootstrap {name}")
            continue
        
        print(f"Successfully bootstrapped {name}")
    
    print("\nBootstrap complete!")

if __name__ == "__main__":
    main()
