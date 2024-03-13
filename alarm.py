alarm=int(input("Digite a hora que deverá esperar para o alarme tocar:"))
hr=int(input("Digite a sua hora atual:"))
toc=(alarm+hr)%24
print("seu alarme irá tocar de", toc, "horas")
