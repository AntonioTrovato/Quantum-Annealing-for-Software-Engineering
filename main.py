import random
import numpy as np
from Incident import Incident
from qiskit import BasicAer
from qiskit.utils import algorithm_globals
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import QAOA

#First of all, I've to instanciate dictionaries of controls and incidents
controls = {
    #control_key : control_name
    1 : "Information Backup",
    2 : "Capacity Management",
    3 : "Off-Site Equipment Security",
    4 : "Physical Entry Controls",
    5 : "Restriction Of Access To Information",
    6 : "Management Of Secret Information Authentication",
    7 : "Equipment Maintenance",
    8 : "Clock Synchronization",
    9 : "Supply Facilities",
    10 : "Secret authentication and information management",
    11 : "Network Controls"
}

threats = {
    #threat_key : [threat_name, control_key1, control_key2, ...]
    1 : ["Denial Of Service", 1, 2],
    2 : ["Theft", 3],
    3 : ["Social Engineering", 4, 10],
    4 : ["Monitoring Errors", 5, 6],
    5 : ["Failure Of Physical Or Logical Origin", 7],
    6 : ["System Crashes Due To Resource Exhaustion", 2],
    7 : ["Abuse Of Access Privileges", 5],
    8 : ["Configuration Errors", 8],
    9 : ["Maintenance Errors", 1],
    10 : ["Inadequate Temperature Or Humidity Conditions", 9],
    11 : ["Failure Of Communication Services", 11]
}

#the list of estimated time of resolution
estimated_times = [6,24,8,40,24,8,24,2,6,72,8]

#penalty = max(estimated_times)+1
penalty = 73

#Now I've to make the dataset (of 14 incidents)
incidents = []
for _ in range(14):
    threat_key = random.randint(1,11)
    threat_list = threats.get(threat_key)
    #if the list contains just the threat name, we have to choose another threat
    while(len(threat_list) < 2):
        threat_key = random.randint(1,11)
        threat_list = threats.get(threat_key)
    threat_name = threat_list[0]
    control_key = threat_list.pop(random.randint(1,len(threat_list)-1))
    control_name = controls[control_key]
    estimated_time = estimated_times[threat_key-1]
    incident = Incident(threat_key, threat_name, control_key,control_name, estimated_time)
    incidents.append(incident)

#I need to know the ffected controls
actual_controls = {}
for incident in incidents:
    control_id = incident.get_control_id()
    if actual_controls.keys().__contains__(control_id):
        threat_list = actual_controls.get(control_id)
        threat_list.append(incident.get_threat_id())
        threat_list.sort()
    else:
        actual_controls[control_id] = [incident.get_threat_id()]

def create_QUBO_problem(linear_terms,quadratic_terms):
    qubo = QuadraticProgram()
    for i in range(1,len(linear_terms)+1):
        qubo.binary_var('x%s' % (i))

    #apply the penalty for each linear term
    for threat_list in actual_controls.values():
        for threat_id in threat_list:
            linear_terms[threat_id-1] -= 73

    qubo.minimize(linear=linear_terms,quadratic=quadratic_terms)

    return qubo

#generating the linear terms (biases)
linear_terms = np.array(estimated_times)

#dclaring a dictrionary for the quadratic terms (coupling weights)
quadratic = {}

#filling the dictionary
for threat_list in actual_controls.values():
    for i in threat_list:
        for j in threat_list:
            if(j>i):
                try:
                    quadratic[i,j] += 2*penalty
                except:
                    quadratic[i,j] = 2*penalty

qubo = create_QUBO_problem(linear_terms,quadratic)
print(qubo)

#inizializing the optimizer
algorithm_globals.random_seed = 10598

quantum_instance = QuantumInstance(
    BasicAer.get_backend("qasm_simulator"),
    seed_simulator=algorithm_globals.random_seed,
    seed_transpiler=algorithm_globals.random_seed,
)

qaoa_mes = QAOA(quantum_instance=quantum_instance, initial_point=[0.0, 0.0])

#using the minimum eigen solver to istanciate the minimum eigen optimizer
qaoa = MinimumEigenOptimizer(qaoa_mes)

print("Wait.......")
qaoa_result = qaoa.solve(qubo)
print(qaoa_result)