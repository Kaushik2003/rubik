# 🪄 AI Onchain Agent — RUBIK  
**Gemini + CDP AgentKit + Base Chain + Next.js + Flask**

> Transform natural language into onchain actions with AI-powered blockchain interactions

---

## 📋 Overview

This project enables the creation of an **AI agent** capable of performing **onchain operations** on **Base (Base Sepolia)**. It features:

- A **Python backend** that integrates **Gemini** with **CDP AgentKit** to execute blockchain actions
- A **Next.js frontend** providing an **AI-powered chat interface** to interact with the agent

---

## ✨ Key Features

- 🤖 **AI-Powered Chat Interface** — Natural language → onchain actions
- 🔗 **Onchain Operations** via AgentKit:
  - Deploy and interact with **ERC-20 tokens**
  - Create and manage **NFTs**
  - Check **wallet balances**
  - Request funds from **faucet**
- 📡 **Real-time Updates** with **Server-Sent Events (SSE)**
- 📱 **Responsive, modern UI** (Tailwind CSS)
- 🔐 **Wallet Integration** via AgentKit
- 🌍 **Multi-language Support**

---

## 🛠️ Tech Stack

| Layer      | Technologies |
|------------|-------------|
| Frontend   | Next.js 14, React, Tailwind CSS, TypeScript, Biome, Bun |
| Backend    | Python, Flask, LangChain, Gemini, CDP AgentKit, SQLite |
| Blockchain | Base Sepolia, Coinbase Developer Platform AgentKit |

---

## 📁 Monorepo Structure

```
├── backend/     # Python Flask API (AgentKit + Gemini)
└── frontend/    # Next.js chat interface (React + Tailwind)
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <repo-root>
```

## 🐍 Backend Setup (Python + Flask)

### Prerequisites
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)
- [Rust](https://rustup.rs/)
- Python 3.8+

### Environment Variables
Create a `.env` file in `/backend`:

```env
CDP_API_KEY_NAME=       # Get from https://portal.cdp.coinbase.com/projects/api-keys
CDP_API_KEY_PRIVATE_KEY=""
GOOGLE_API_KEY=         # Get from https://ai.google.dev/
NETWORK_ID=base-sepolia

# Optional wallet settings:
CDP_WALLET_ID=""
CDP_WALLET_SEED=""
```

### Install Dependencies & Run

```bash
cd backend
conda env create -f environment.yml
conda activate agent-backend
python index.py
```

### API Usage Examples

**Run onchain action:**
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"input": "deploy a new ERC-20 token", "conversation_id": 0}'
```

**Retrieve deployed NFTs:**
```bash
curl http://localhost:5000/nfts
```

**Retrieve deployed ERC-20s:**
```bash
curl http://localhost:5000/tokens
```

## ⚛️ Frontend Setup (Next.js + React)

### Prerequisites
- [Bun](https://bun.sh/)

### Environment Variables
Create a `.env.local` in `/frontend`:

```env
NEXT_PUBLIC_API_URL=http://localhost:5000
# For production: set this to deployed backend URL (with https://)
```

### Install Dependencies & Run

```bash
cd frontend
bun i
bun dev
```

### Development Commands

```bash
bun run format    # Format code (Biome)
bun run lint      # Lint code
bun run ci:check  # Run CI checks
```

---

## 🌐 Deploying to Replit

### Backend Secrets
```json
{
  "CDP_API_KEY_NAME": "get from https://portal.cdp.coinbase.com/projects/api-keys",
  "CDP_API_KEY_PRIVATE_KEY": "get from https://portal.cdp.coinbase.com/projects/api-keys",
  "GOOGLE_API_KEY": "get from https://ai.google.dev/",
  "NETWORK_ID": "base-sepolia"
}
```

### Frontend Secrets
```json
{
  "NEXT_PUBLIC_API_URL": "your backend deployment URL here (include https://)"
}
```

### 💡 Deployment Tips
1. Deploy backend first → get URL → set `NEXT_PUBLIC_API_URL` → deploy frontend
2. ⚠️ **Important:** SQLite resets on Replit deploy — securely save wallet ID and seed if moving to Mainnet

---

## 📊 Project Status

- ✅ Working demo
- ✅ ERC-20 and NFT interactions
- ✅ SSE-enabled chat stream
- ✅ Replit deployable templates
- ✅ Multi-language support
- 🚧 Custom actions → easy extension via `agent/custom_actions`

---

## 📄 License

MIT License

---

## 🙏 Acknowledgements

- [Coinbase Developer Platform (CDP)](https://docs.cdp.coinbase.com/)
- [LangChain](https://langchain.com/)
- [Google Gemini](https://ai.google.dev/)
- [Base](https://base.org/)

---

**Happy BUIDLing! 🚀**