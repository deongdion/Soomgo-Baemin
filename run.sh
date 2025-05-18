#!/data/data/com.termux/files/usr/bin/bash

echo "Starting mitmproxy on localhost:3000..."
./mitmproxy --listen-host 127.0.0.1 --listen-port 3000 -s script.py