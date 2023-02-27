echo "Remove extra files"
sudo find . -type d -name __pycache__ -exec rm -r {} \+
sudo find . -type d -name .pytest_cache -exec rm -r {} \+
sudo find . -type f -name '*.db' -delete
sudo find . -type f -name '.coverage' -delete
sudo find . -type d -name htmlcov -exec rm -r {} \+
# sudo find . -type d -name .venv -exec rm -r {} \+        