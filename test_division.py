def division(a,b):
   return a / b

def test_division():
   assert division(6,3) == 2
   assert division(9,3) == 3
   assert division(5, 2) == 2.5
   assert division('6', 3)
   assert division(6, '3')
   assert division(4, 0)
   assert division(2, 3)
   assert division('a', 3)
   assert division(3, 'a')