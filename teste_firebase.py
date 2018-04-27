from firebase import firebase

firebase= firebase.FirebaseApplication('https://ep1-desoft-b702d.firebaseio.com/')

#teste= firebase.get('/Loja1', None )
#a=(input("loja"))
#x = (input("produto"))
#y= int(input("quantidade"))
#z = int(input("preco"))

#teste=firebase.post(a,{x:y})
#teste1 = firebase.post(a,{"Preco {}".format(x):z})
teste2= firebase.get('biro', None)

print(teste2)