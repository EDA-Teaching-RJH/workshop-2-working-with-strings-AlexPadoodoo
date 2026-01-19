import math  

def main():

    A = int(input("Enter the Length of the first side (A): ")) #TO DO  
    B = int(input("Enter the Length of the first side (B): "))
    C = pythag(A,B)
    print(C)

def pythag(A,B):
#TO DO  
    t = A**2 + B**2
    result = math.sqrt(t)
    return result

main()
