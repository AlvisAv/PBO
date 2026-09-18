# Langkah 2
import mypackage.alfa
print (mypackage.alfa.FunctionA())

# Langkah 3 (Contoh code yang menghasilkan error)
#print (mypackage.beta.FunctionB())

# Langkah 4
import mypackage.beta
print (mypackage.beta.FunctionB())

# Langkah 5
import mypackage.subpackage1.subpackageA.gama as gama
print(gama.FunctionC())

# Langkah 6
import mypackage.subpackage1.subpackageA.delta as delta
print (delta.FunctionD())

# Langkah 7
from mypackage.subpackage2 import epsilon
print (epsilon.FunctionE())

# Langkah 8
from mypackage.subpackage2 import zeta
print (zeta.FunctionF())