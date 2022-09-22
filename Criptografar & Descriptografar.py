from pybase64 import _pybase64 as b64

escolha = int(input('Digite 1 se deseja criptografar e 2 se deseja descriptografar: '))

if escolha == 1:
    mensagem_original = input('Digite a senha a ser criptografada: ')

    mensagem_criptografada = b64.b64encode(bytes(mensagem_original, 'UTF-8'))
    print('--------CRIPTOGRAFIA--------')
    mensagem_criptografada = str(mensagem_criptografada)
    mensagem_criptografada = mensagem_criptografada.strip("b'")
    print('Mensagem criptografada: {} '.format(mensagem_criptografada))
elif escolha == 2:
    print("Caso não digite uma criptografia válido obterá erro!")
    mensagem_criptografada = str(input("Digite a senha a ser descriptografada: "))
    mensagem_original = "b'{}'".format(mensagem_criptografada)
    mensagem_original = b64.b64decode(mensagem_original)
    print('--------DESCRIPTOGRAFIA--------')
    mensagem_original = str(mensagem_original)
    mensagem_original = mensagem_original.strip("b'")
    print('Mensagem descriptografada: {}'.format(mensagem_original))
