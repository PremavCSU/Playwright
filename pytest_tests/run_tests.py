#!/usr/bin/env python3
"""
Pytest runner for Amazon.com test suite
"""
import subprocess
import sys

def run_all_tests():
    """Run all pytest tests"""
    cmd = ["python", "-m", "pytest", "pytest_tests/", "-v", "--tb=short"]
    return subprocess.run(cmd, cwd=".")

def run_specific_test(test_name):
    """Run a specific test file"""
    cmd = ["python", "-m", "pytest", f"pytest_tests/test_{test_name}.py", "-v"]
    return subprocess.run(cmd, cwd=".")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        run_specific_test(test_name)
    else:
        run_all_tests()