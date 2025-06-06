# 🐍 Backend Setup Guide

> Python Flask API with Gemini AI and CDP AgentKit for onchain operations

---

## 📋 Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- [Rust](https://www.rust-lang.org/tools/install)
- Python 3.8+

---

## ⚙️ Environment Variables

Create a `.env` file in the backend directory:

```bash
CDP_API_KEY_NAME=         # Get from https://portal.cdp.coinbase.com/projects/api-keys
CDP_API_KEY_PRIVATE_KEY="" # Get from https://portal.cdp.coinbase.com/projects/api-keys
GOOGLE_API_KEY=           # Get from https://ai.google.dev/
NETWORK_ID=base-sepolia

# Optional wallet settings:
CDP_WALLET_ID=""
CDP_WALLET_SEED=""
```

---

## 🚀 Installation & Setup

### 1️⃣ Navigate to Backend Directory
```bash
cd backend
```

### 2️⃣ Create Conda Environment
```bash
# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate agent-backend
```

### 3️⃣ Start the Server
```bash
python index.py
```

The server will start on `http://localhost:5000`

---

## 🔧 Development Commands

### Environment Management
```bash
# Activate environment
conda activate agent-backend

# Deactivate environment
conda deactivate

# Update environment
conda env update -f environment.yml
```

### Adding Dependencies
```bash
# Install new package
conda install package_name

# Or use pip within the conda environment
pip install package_name

# Export updated environment
conda env export > environment.yml
```

---

## 📡 API Endpoints

### Chat Endpoint
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"input": "deploy a new ERC-20 token", "conversation_id": 0}'
```

### Get Deployed Assets
```bash
# Get deployed NFTs
curl http://localhost:5000/nfts

# Get deployed ERC-20 tokens
curl http://localhost:5000/tokens
```

---

## 💰 Wallet Management

⚠️ **Important**: When running your agent for the first time, the SDK will automatically generate a wallet. The wallet information will be logged to the console and saved to the SQLite database.

For production use, save your wallet information securely using the environment variables:
```bash
CDP_WALLET_ID="your-wallet-id"
CDP_WALLET_SEED="your-wallet-seed"
```

---

## 🛠️ Troubleshooting

### Common Issues

**Rust Installation Error**
```bash
# Make sure Rust is installed
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
```

**Environment Creation Failed**
```bash
# Remove existing environment and recreate
conda env remove -n agent-backend
conda env create -f environment.yml
```

**Package Installation Issues**
```bash
# Clear conda cache
conda clean --all

# Update conda
conda update conda
```

---

## 📊 Project Structure

```
backend/
├── agent/                 # Agent modules
│   ├── __init__.py
│   ├── custom_actions.py  # Custom agent actions
│   └── ...
├── environment.yml        # Conda environment file
├── index.py              # Flask application entry point
├── .env                  # Environment variables
└── README.md             # This file
```

---

**Backend Setup Complete! 🎉**