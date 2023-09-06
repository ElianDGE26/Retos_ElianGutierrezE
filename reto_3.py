
#DEFINICION DE LOS DICCIONARIOS

producto = {}

categoria = {}

dictResulta = {}

#PARA CREAR EL DICCIONARIO DE CATEGORIA

cat = int(input("Digite cuantos categorias va a ingresar : "))

for cat in range(cat):
    id_cat = input("Digite el id de la categoria : ")
    nombrecat = input("Digite el nombre de la categoria : ")

    categoria [cat+1] = {
    
    "id_cat" : id_cat, 
    "nombre_cat" : nombrecat

    }

print(categoria)

#PARA CREAR EL DICCIONARIO DE PRODUCTOS


x = int(input("Digite cuantos productpos va a ingresar : "))

for num in range(x):
    id_prod = input("Digite el id de producto : ")
    nombreprod = input("Digite el nombre del producto : ")
    precio = input("Digite el precio del producto : ")
    id_cat = input("Digite el id de la categoria : ")

    producto[num+1] = {"id" : id_prod, 
    "nombreprod" : nombreprod, 
    "precio" : precio, 
    "id_cat" : id_cat
    }

print(producto)

#PARA RECORRER LOS DOS DICCIONARIOS Y COMPARAR LA INFORMACION QUE ESTÁN EN LAS DOS
for n in range(len(producto)):
    for b in range(len(categoria)):
        if producto[n+1]["id_cat"] in categoria[b+1]["id_cat"]:
            idn = producto[n+1]["id"]
            nombreproducto = producto[n+1]["nombreprod"]
            nombrecat = categoria[b+1]["nombre_cat"]

            dictResulta[n+1] = { 
                "id de producto " : idn,
                "nombre del producto" : nombreproducto,
                "nombre de la categoria " : nombrecat
            }
print(dictResulta)            




