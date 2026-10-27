# CHIP OS Agent
One-command installer for Ubuntu 22.04

Server:
bash <(curl -fsSL https://raw.githubusercontent.com/ssdogturdss/chip-os-agent/main/install.sh)

iPhone:
1. Open http://YOUR_SERVER_IP:3000 in Safari
2. Tap Share -> Add to Home Screen -> "CHIP Control"
3. Now you have native app to control server

API:
curl http://IP:8000/status
curl -X POST http://IP:8000/chat -d '{"message":"deploy latest"}'
