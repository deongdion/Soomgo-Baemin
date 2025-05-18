#!/data/data/com.termux/files/usr/bin/bash

echo "Updating Termux and installing dependencies..."
pkg update -y && pkg upgrade -y
pkg install python wget -y

echo "Downloading and installing mitmproxy..."
wget https://snapshots.mitmproxy.org/10.4.2/mitmproxy-10.4.2-linux-arm64.tar.gz
tar -xzf mitmproxy-10.4.2-linux-arm64.tar.gz
rm mitmproxy-10.4.2-linux-arm64.tar.gz

echo "Installing Python mitmproxy package..."
pip install mitmproxy

echo "Setup complete! Run './run.sh' to start mitmproxy."