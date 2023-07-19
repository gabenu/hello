t = 0
n = 4 # La chiva es el indice 0
t += 1
print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
t += 1
noquiere = []
t += 1
llama = 1
t += 1
sacar = 0
t += 1
while llama < n :
    t += 1
    print(f"Hay que llamar al animal{llama} para que saque al animal{sacar}")
    t += 1
    noquiere.insert(0, f"el animal{llama} no quiere sacar al animal{sacar}")
    t += 1
    sacar = llama
    t += 1
    llama += 1
    t += 1
    for i in noquiere:
        t += 1
        print(i)
        t += 1
    print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar")
    t += 1
print(t)
