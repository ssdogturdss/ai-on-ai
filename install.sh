#!/bin/bash
set -e
echo "🤖 Installing CHIP AI Agent for Ubuntu 22.04..."
sudo apt update
sudo apt install -y python3 python3-pip nodejs npm git curl ufw nginx
pip3 install fastapi uvicorn python-multipart openai anthropic supabase pydantic
npm install -g pm2
# Clone self if needed
if [ ! -f "agent/main.py" ]; then
  echo "Already in repo"
fi
# Setup .env
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "⚠️ EDIT .env with your keys: nano .env"
fi
# Systemd service
sudo cp deploy/chip-agent.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable chip-agent
sudo systemctl restart chip-agent
# Firewall
sudo ufw allow 8000/tcp
sudo ufw allow 3000/tcp
echo "✅ Agent running on http://$(curl -s ifconfig.me):8000"
echo "📱 iPhone Control: http://$(curl -s ifconfig.me):3000"
echo "Logs: pm2 logs or journalctl -u chip-agent -f"
