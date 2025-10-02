from flask import Flask, render_template, request, redirect, url_for
from quantum_rng import quantum_card, quantum_coin
from quantum_ml import run_quantum_anomaly_detection

try:
    from pqc_demo import run_pqc_demo
except ImportError:
    def run_pqc_demo():
        return {"supported": False, "error": "PQC libraries not installed"}

app = Flask(__name__)

@app.route('/')
def index():
    """Enhanced homepage with quantum-themed design"""
    return render_template('index.html')

@app.route('/card')
def card():
    """Quantum random card draw demonstration"""
    try:
        card = quantum_card()
        return render_template('card.html', card=card)
    except Exception as e:
        # Fallback for demonstration
        import random
        suits = ['♠', '♥', '♦', '♣']
        values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
        fallback_card = f"{random.choice(values)}{random.choice(suits)}"
        return render_template('card.html', card=fallback_card)

@app.route('/coin')
def coin():
    """Quantum coin flip demonstration"""
    try:
        outcome = quantum_coin()
        print(f"Quantum coin result: {outcome}")  # Debug output
        return render_template('coin.html', outcome=outcome)
    except Exception as e:
        print(f"Quantum coin error: {e}")  # Debug output
        # Fallback for demonstration
        import random
        fallback_outcome = random.choice(["Heads", "Tails"])
        return render_template('coin.html', outcome=fallback_outcome)

@app.route('/fraud', methods=['GET', 'POST'])
def fraud():
    """Quantum machine learning fraud detection"""
    try:
        results = run_quantum_anomaly_detection()
        # Ensure results have the expected structure
        if not isinstance(results, dict):
            results = {"anomalies": [], "scores": [], "error": "Invalid results format"}
        if "anomalies" not in results:
            results["anomalies"] = []
        if "scores" not in results:
            results["scores"] = []
    except Exception as e:
        # Fallback demonstration data
        import random
        import numpy as np
        
        # Generate sample data for demonstration
        n_users = 15
        scores = [random.uniform(-2, 2) for _ in range(n_users)]
        # Mark users with very low scores as anomalies
        anomalies = [i for i, score in enumerate(scores) if score < -1.5]
        
        results = {
            "anomalies": anomalies,
            "scores": scores,
            "error": f"Quantum ML error: {str(e)}"
        }
    
    return render_template('fraud.html', results=results)

@app.route('/pqc')
def pqc():
    """Post-quantum cryptography demonstration"""
    try:
        result = run_pqc_demo()
    except Exception as e:
        result = {
            'supported': False,
            'success': False,
            'error': f'PQC demonstration error: {str(e)}',
            'shared_secret': 'N/A'
        }
    
    return render_template('pqc.html', result=result)

@app.errorhandler(404)
def not_found_error(error):
    """Custom 404 error page"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page"""
    return render_template('index.html'), 500

import os

if __name__ == "__main__":
    # Render sets the PORT environment variable dynamically
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host='0.0.0.0', port=port)


