from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

service = QiskitRuntimeService(channel="ibm_quantum", token="5c637bdb0dbf0622b494355f6b37089c0669ff9773c4cbd2aaf61cca27d8623390b8ac5bd3557c538b8dc93cc50e3e34a43f680325c6055f72bb29b37b5627da")
 
# Bell Circuit
qr = QuantumRegister(2, name="qr")
cr = ClassicalRegister(2, name="cr")
qc = QuantumCircuit(qr, cr, name="bell")
qc.h(qr[0])
qc.cx(qr[0], qr[1])
qc.measure(qr, cr)
 
with Session(service, backend="ibm_kyoto") as session:
    sampler = Sampler(session=session)
 
    print("hej")
    job = sampler.run(qc, shots=1024)
    print("hej2")
    print(f"Job ID: {job.job_id()}")
    print(f"Job result: {job.result()}")