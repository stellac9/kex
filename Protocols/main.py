from bb84 import BB84Scheme
from e91 import E91Scheme
from b92 import B92Scheme
from core import QKDResults

"""
Used to execute everything and print out result
"""
if __name__ == "__main__":
    error_allowed = 0.4
    # three instances with no eavesdropper
    bb84 = BB84Scheme(False)
    e91 = E91Scheme(False)
    b92 = B92Scheme(False)
    # run() returns of type QKDResults, with input number of "shots"
    bb84_res = bb84.run(1000000, error_allowed) 
    e91_res = e91.run(1000000, error_allowed)
    b92_res = b92.run(1000000, error_allowed)

    # three instances with an eavesdropper
    bb84_e = BB84Scheme(True)
    #e91_e = E91Scheme(True)
    #b92_e = B92Scheme(True)
    bb84_e_res = bb84_e.run(1000000, error_allowed)
    #e91_e_res = e91_e.run(1000000)
    #b92_e_res = b92_e.run(1000000)
    
    # prints result of running QKD schemes (with and without eavesdropper)
    # in terms of raw key efficiency and qubit error rate
    print("\n")
    print("BB84 number of runs:\t", bb84_res.n_runs(), "\n")
    print("BB84 e number of runs:\t", bb84_e_res.n_runs(), "\n")
    print("E91 number of runs:\t", e91_res.n_runs(), "\n")
    print("B92 number of runs:\t", b92_res.n_runs(), "\n")
    
    
    print("BB84 RKE:\t", bb84_res.rke(), "\n")
    #print("BB84 (w/ eve) RKE:\t", bb84_e_res.rke(), "\n")
    print("BB84 QBER:\t", bb84_res.qber(), "\n")
    #print("BB84 (w/ eve) QBER:\t", bb84_e_res.qber(), "\n")
    print("E91 RKE:\t", e91_res.rke(), "\n")
    #print("E91 (w/ eve) RKE:\t", e91_e_res.rke(), "\n")
    print("E91 QBER:\t", e91_res.qber(), "\n")
    #print("E91 (w/ eve) QBER:\t", e91_e_res.qber(), "\n")
    print("B92 RKE:\t", b92_res.rke(), "\n")
    #print("B92 (w/ eve) RKE:\t", b92_e_res.rke(), "\n")
    print("B92 QBER:\t", b92_res.qber(), "\n")
    #print("B92 (w/ eve) QBER:\t", b92_e_res.qber(), "\n")
