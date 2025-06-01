
//# QuantumSuperposition.py
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)  # Apply Hadamard gate to create superposition
qc.measure_all()
qc.draw('mpl')
