# Quantum Poker PoC Demo

## Features

- Quantum random card draws & coin flips using Qiskit
- Quantum ML anomaly (fraud) detection demo with One-Class SVM
- (Optional) Post-Quantum Cryptography handshake simulation (Kyber)
- All endpoints unified in one Flask web demo

## Setup
1. Install dependencies:
    pip install -r requirements.txt
2. (Optional) Generate TLS certificates for HTTPS demo:
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
3. Run:
    python app.py
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Notes
- For live PQC, you need `oqs-python` and a system-compatible liboqs library.
- Real user session data can be connected in `quantum_ml.py`.
