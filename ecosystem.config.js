module.exports = {
  apps: [
    {name:"chip-agent", script:"agent/main.py", interpreter:"python3"},
    {name:"chip-ui", script:"npm", args:"run start --prefix control-ui"}
  ]
}
