from django.shortcuts import render
import qiskit
from qiskit import *
from qiskit import IBMQ
from django.views.generic import ListView

class Insertar(ListView):
   
    template_name = 'resultados.html'
    
      
    def get_queryset(self):
        query = self.request.GET.get('q')
        secretnumber =query
    
        circuit= QuantumCircuit(len(secretnumber)+1,len(secretnumber))
        circuit.h(range(len(secretnumber)))

        circuit.draw(output='mpl')
        circuit.x(len(secretnumber))
        circuit.h(len(secretnumber))
        circuit.barrier()

        for ii, yesno in enumerate(reversed(secretnumber)):
            if yesno =='1':
                circuit.cx(ii, len(secretnumber))


        circuit.barrier()
        circuit.h(range(len(secretnumber)))
        circuit.barrier()
        circuit.measure(range(len(secretnumber)),range(len(secretnumber)))
        #circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5])
        circuit.draw(output='mpl')
        simulator = Aer.get_backend('qasm_simulator')
        result= execute(circuit, backend = simulator, shots =1).result()
        counts= result.get_counts()

        object_list=[counts]
      


        return object_list
       

  
# Create your views here.
def index(request):
   
    
    secretnumber ='101001'

    circuit= QuantumCircuit(len(secretnumber)+1,len(secretnumber))
    circuit.h(range(len(secretnumber)))

    circuit.draw(output='mpl')
    circuit.x(len(secretnumber))
    circuit.h(len(secretnumber))
    circuit.barrier()

    for ii, yesno in enumerate(reversed(secretnumber)):
        if yesno =='1':
         circuit.cx(ii, len(secretnumber))


    circuit.barrier()
    circuit.h(range(len(secretnumber)))
    circuit.barrier()
    circuit.measure(range(len(secretnumber)),range(len(secretnumber)))
    #circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5])
    circuit.draw(output='mpl')
    simulator = Aer.get_backend('qasm_simulator')
    result= execute(circuit, backend = simulator, shots =1).result()
    counts= result.get_counts()
    print(counts)



    context = {'counts': counts}
    return render(request, 'index.html', context)
