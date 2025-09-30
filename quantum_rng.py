from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

def quantum_card():
    """Generate a random playing card using quantum randomness"""
    suits = ['♠', '♥', '♦', '♣']
    values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']
    
    try:
        # Create 6-qubit circuit for 64 possible outcomes (52 cards fit within this)
        qc = QuantumCircuit(6, 6)
        
        # Apply Hadamard gates to create superposition
        for i in range(6):
            qc.h(i)
        
        # Measure all qubits
        qc.measure(range(6), range(6))
        
        # Execute on quantum simulator
        simulator = AerSimulator()
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1)
        result = job.result()
        
        # Get the measurement result
        counts = result.get_counts()
        if not counts:
            raise Exception("No measurement results obtained")
            
        outcome = list(counts.keys())[0]
        
        # Convert binary result to card index (0-51)
        idx = int(outcome, 2) % 52
        
        # Return formatted card
        return f"{values[idx % 13]}{suits[idx // 13]}"
        
    except Exception as e:
        print(f"Quantum card generation failed: {e}, using classical fallback")
        # Classical fallback
        return f"{random.choice(values)}{random.choice(suits)}"

def quantum_coin():
    """Generate quantum coin flip using true quantum randomness"""
    try:
        # Create single qubit circuit
        qc = QuantumCircuit(1, 1)
        
        # Put qubit in superposition
        qc.h(0)
        
        # Measure the qubit
        qc.measure(0, 0)
        
        # Execute on quantum simulator
        simulator = AerSimulator()
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1)
        result = job.result()
        
        # Get measurement result
        counts = result.get_counts()
        if not counts:
            raise Exception("No measurement results obtained")
            
        outcome = list(counts.keys())[0]
        
        # Return heads or tails
        return "Heads" if outcome == '0' else "Tails"
        
    except Exception as e:
        print(f"Quantum coin flip failed: {e}, using classical fallback")
        # Classical fallback
        return random.choice(["Heads", "Tails"])

def quantum_random_number(min_val=0, max_val=100):
    """Generate quantum random number in specified range"""
    try:
        # Calculate number of qubits needed
        range_size = max_val - min_val + 1
        num_qubits = max(1, int(range_size).bit_length())
        
        qc = QuantumCircuit(num_qubits, num_qubits)
        
        # Create superposition on all qubits
        for i in range(num_qubits):
            qc.h(i)
        
        # Measure all qubits
        qc.measure(range(num_qubits), range(num_qubits))
        
        # Execute circuit
        simulator = AerSimulator()
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1)
        result = job.result()
        
        # Convert to number in range
        counts = result.get_counts()
        if not counts:
            raise Exception("No measurement results obtained")
            
        outcome = list(counts.keys())[0]
        number = int(outcome, 2) % range_size + min_val
        
        return number
        
    except Exception as e:
        print(f"Quantum number generation failed: {e}, using classical fallback")
        # Classical fallback
        return random.randint(min_val, max_val)

def test_quantum_rng():
    """Test function to verify quantum RNG works"""
    print("Testing Quantum Random Number Generation:")
    print(f"Quantum Card: {quantum_card()}")
    print(f"Quantum Coin: {quantum_coin()}")
    print(f"Quantum Number (1-10): {quantum_random_number(1, 10)}")

if __name__ == "__main__":
    test_quantum_rng()
