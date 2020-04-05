# import module lớp trừu tượng
from abc import ABC, abstractmethod 
  
# tạo ra một lớp mẹ đa giác nói chung
class Polygon(ABC): 
  
    # abstract method 
    def noofsides(self): 
        #placeholder
        pass

# lớp con tam giác  
class Triangle(Polygon): 
  
    # viết thuộc tính riêng kế thừa từ hàm noofsides
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 

# lớp con ngũ giác 
class Pentagon(Polygon): 
    
    # viết thuộc tính riêng cho ngũ giác
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
 
 # lớp con lục giác  
class Hexagon(Polygon): 
    
    # viết thuộc tính riêng cho lục giác
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
# lớp con tứ giác 
class Quadrilateral(Polygon): 
    
    # viết thuộc tính riêng cho tứ giác
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 

# định nghĩa theo class 
# Driver code 
R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides()