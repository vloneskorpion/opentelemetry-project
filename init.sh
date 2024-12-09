#!/bin/bash
CERT_DIR="/etc/nginx/certs"

if [ ! -f "$CERT_DIR/fullchain.pem" ] || [ ! -f "$CERT_DIR/privkey.pem" ]; then
    echo "Generating self-signed SSL certificates..."
    mkdir -p "$CERT_DIR"
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout "$CERT_DIR/privkey.pem" \
        -out "$CERT_DIR/fullchain.pem" \
        -subj "/CN=localhost"
    echo "Self-signed certificates generated."
else
    echo "SSL certificates already exist."
fi
