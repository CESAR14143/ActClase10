def main() :
   #introduce el codigo
   pass
   def operacion(x,y,z):
   if z == "s":
        op = x+y
   elif z == "r":
        op = x-y
   elif z == "m":
        op = x*y
   elif z== "d":
        op = x/y
   return op

def main():
    x = int(input("introducir valor 1: "))
    y = int(input("introducir valor 2: "))
    z = input("introducir clave  (s, r, m, d): ")
    print("resultado: "+str(operacion(x,y,z)))
    
main()  





if __name__=='__main__':
    main()
