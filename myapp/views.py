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
        print(circuit)
        simulator = Aer.get_backend('qasm_simulator')
        result= execute(circuit, backend = simulator, shots =1).result()
        counts= result.get_counts()

        object_list=[counts]
      


        return object_list
       

  
# Create your views here.

# Create your views here.
def index(request):
   
 

    context = {}
    return render(request, 'index.html', context)




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
        print(circuit)
        simulator = Aer.get_backend('qasm_simulator')
        result= execute(circuit, backend = simulator, shots =1).result()
        counts= result.get_counts()
        claves = counts.keys()
        for clave in claves:
            binario = clave
        
        final = "Tu numero secreto es: " + binario

        object_list=[final, circuit]
      


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


class Adivinar(ListView):
   
    template_name = 'adivinar.html'
    
      
    def get_queryset(self):
        ns= 1000

        query = self.request.GET.get('q')
        n =query

        if n== '1000':
            boo = True
        else:
            boo = False
        paridad = 0

        contador = -1

        for i in n:
            contador = contador + 1
           
            if (contador == 0) and (i is '1'):
                paridad = 1
                
            
        if boo== 1:
            final= "Has acertado el número!"  
        else:       
            final= "Has fallado"  

        if paridad == 1:
            final2 = "La paridad es 1"
        else:
            final2 = "La paridad es 0"
        object_list=[final, final2]
      


        return object_list
       
def Pintar(request):
    context = {}
    return render(request, 'graficos.html', context)
  