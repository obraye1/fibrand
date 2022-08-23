import random 
def base_ten(a, b, c, d):
    return ( (d * 10) ^ 0 ) + ( (c * 10) ^ 1)  + ( (b * 10) ^ 2 ) +  ((a * 10) ^ 3)

nd = 0

while nd <= 2:
    
    i = random.randint(0,1)
    j = random.randint(0,1)
    k = random.randint(0,1)
    m = random.randint(0,1)
    baseTen = base_ten(i,j,k,m)
    print(f'{i}{j}{k}{m} in base two To base Ten is {baseTen}')
    nd += 1





    