from mathematical import task_5_my_module_math as base_math
from mathematical.task_7_my_module_math2 import exp

x = base_math.mul # Плохой приём
y = base_math._START_MULT # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)

x = base_math.div(12, 5)
z = exp(2, 3)
print(x)
print(z)
