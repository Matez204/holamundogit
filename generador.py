pintas=["corazones","treboles","picas","diamantes"]
valores=["A","J","K","Q"]+[(str(i))for i in range(2,11)]
mazo=[(u,p) for u in valores for p in pintas ]
for c in mazo:
    print(c)