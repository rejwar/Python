# QuantumSimulation.py
from qiskit.providers.aer import AerSimulator
from qiskit import transpile

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

result = simulator.run(compiled_circuit).result()
counts = result.get_counts()
print(counts)
