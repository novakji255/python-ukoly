print("zadej cislo a:") 
a = int(input())  

print("zadej cislo b:") 
b = int(input())

if a > b:     
    a, b = b, a  
    
print("zadej cislo c:") 
c = int(input())

if a > c:     
    a, c = c, a 
if b > c:     
    b, c = c, b      
    
    print(f"cisla v poradi: {a}, {b}, {c}")
    print(f"pismenka v poradi: {a}, {b}, {c}")