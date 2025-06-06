# 📦 Poetry to Conda Migration Guide

> Step-by-step guide to migrating your Python project from Poetry to Conda

---

## 🚀 Migration Steps

### 1️⃣ Install Conda (if not already installed)

Download and install **Miniconda** or **Anaconda** from:

- **Miniconda**: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda**: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

### 2️⃣ Create the Conda Environment

```bash
# Navigate to your backend directory
cd backend

# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate agent-backend
```

### 3️⃣ Remove Poetry Files

```bash
# Remove Poetry configuration files
rm pyproject.toml
rm poetry.lock
```

### 4️⃣ Update Your Workflow

#### Development Setup
```bash
# Activate environment
conda activate agent-backend

# Run your application
python index.py
```

#### Adding New Dependencies

**Method 1**: Add to `environment.yml` and update environment
```bash
conda env update -f environment.yml
```

**Method 2**: Install directly and then export
```bash
conda install package_name
# or
pip install package_name

# Export current environment (optional)
conda env export > environment.yml
```

#### Sharing Environment
```bash
# Others can recreate your environment with:
conda env create -f environment.yml
```

### 5️⃣ Update Documentation

Update your `README.md` and `CONTRIBUTING.md` files to reflect the new conda setup instead of poetry commands.

### 6️⃣ Verify Installation

```bash
# Check if all packages are installed correctly
conda list

# Test your application
python index.py
```

---

## 🔧 Common Conda Commands

| Action | Command |
|--------|---------|
| **List environments** | `conda env list` |
| **Remove environment** | `conda env remove -n agent-backend` |
| **Update all packages** | `conda update --all` |
| **Deactivate environment** | `conda deactivate` |
| **Activate environment** | `conda activate agent-backend` |
| **Export environment** | `conda env export > environment.yml` |
| **Install package** | `conda install package_name` |
| **Search for package** | `conda search package_name` |

---

## 📋 Quick Reference

### Before (Poetry)
```bash
# Install dependencies
poetry install

# Run application
poetry run python index.py

# Add dependency
poetry add package_name
```

### After (Conda)
```bash
# Create environment
conda env create -f environment.yml

# Activate and run
conda activate agent-backend
python index.py

# Add dependency
conda install package_name
```

---

## ✅ Migration Checklist

- [ ] Install Conda (Miniconda/Anaconda)
- [ ] Create environment from `environment.yml`
- [ ] Test environment activation
- [ ] Remove Poetry files (`pyproject.toml`, `poetry.lock`)
- [ ] Update documentation
- [ ] Verify application runs correctly
- [ ] Update CI/CD scripts (if any)
- [ ] Share new setup with team members

---

**Migration Complete! 🎉**