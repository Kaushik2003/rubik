# Poetry to Conda Migration Steps

## 1. Install Conda (if not already installed)
Download and install Miniconda or Anaconda from:
- Miniconda: https://docs.conda.io/en/latest/miniconda.html
- Anaconda: https://www.anaconda.com/products/distribution

## 2. Create the Conda Environment
```bash
# Navigate to your backend directory
cd backend

# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate agent-backend
```

## 3. Remove Poetry Files
```bash
# Remove Poetry configuration files
rm pyproject.toml
rm poetry.lock
```

## 4. Update Your Workflow

### Development Setup:
```bash
# Activate environment
conda activate agent-backend

# Run your application
python index.py
```

### Adding New Dependencies:
```bash
# Method 1: Add to environment.yml and update environment
conda env update -f environment.yml

# Method 2: Install directly and then export
conda install package_name
# or
pip install package_name

# Export current environment (optional)
conda env export > environment.yml
```

### Sharing Environment:
```bash
# Others can recreate your environment with:
conda env create -f environment.yml
```

## 5. Update Documentation
Update your README.md and CONTRIBUTING.md files to reflect the new conda setup instead of poetry commands.

## 6. Verify Installation
```bash
# Check if all packages are installed correctly
conda list

# Test your application
python index.py
```

## Common Conda Commands
```bash
# List environments
conda env list

# Remove environment
conda env remove -n agent-backend

# Update all packages
conda update --all

# Deactivate environment
conda deactivate
```