#Dicionario

contexto = {
    'register': {
        'nome' : 'Marco',
        'idade' : 21,
        'qualidade' : 'Bonito',
    } 
}
if not('register' in contexto) :
    print('ta aqui')
print('to aqui')

print(contexto['register'])
