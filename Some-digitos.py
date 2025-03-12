def somar_digitos(numero):
   
    if not numero.isdigit():
        return "Valor inválido. Informe um número inteiro."
   
    soma = sum(int(digito) for digito in numero)
    return soma

def main():

    numero = input("Informe um número inteiro: ")

    resultado = somar_digitos(numero)

    if isinstance(resultado, int):
        print(f"A soma dos dígitos do número {numero} é: {resultado}")
    else:
        print(resultado)

if __name__ == "__main__":
    main()