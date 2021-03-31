rep = 1

grenais = 0
inter = 0
empates = 0
gremio = 0

while rep == 1:
    gols_inter, gols_gremio = [int(x) for x in input().split()]
    grenais += 1
    if gols_inter > gols_gremio:
        inter += 1
    elif gols_inter == gols_gremio:
        empates += 1
    else:
        gremio += 1
    
    print("Novo grenal (1-sim 2-nao)")
    rep = int(input())

print("%s grenais" %(grenais))
print("Inter:%s" %(inter))
print("Gremio:%s" %(gremio))
print("Empates:%s" %(empates))

if inter>gremio:
    print("Inter venceu mais")
elif inter == gremio:
    print("Nao houve vencedor")
else:
    print("Gremio venceu mais")
