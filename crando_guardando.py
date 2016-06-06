def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.close()

#def leertxtenlista():
#    archi=open('datos.txt','r')
#    lineas=archi.readlines()
#    print lineas
#    archi.close()

def leertxtenlista():
    archi=open('datos.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        print li
    archi.close()

def enumerar():
	enumere=open('datos.txt')
	for i, lineas in enumerate(enumere):
		if i>1:
			break
		print "la linea",i,"es:",lineas
	enumere.close()
enumerar()
creartxt()
grabartxt()
leertxtenlista()

