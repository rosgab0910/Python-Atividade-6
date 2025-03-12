def calcular_media_e_variacao(temperatura_maxima, temperatura_minima):
    media = (temperatura_maxima + temperatura_minima) / 2
    variacao = temperatura_maxima - temperatura_minima
    return media, variacao

def somar_digitos(numero):
    if not numero.isdigit():
        return "Valor inválido. Informe um número inteiro."

    soma = sum(int(digito) for digito in numero)
    return soma

def main():
    try:
        temperatura_maxima = float(input("Informe a temperatura máxima do dia: "))
        temperatura_minima = float(input("Informe a temperatura mínima do dia: "))

        media, variacao = calcular_media_e_variacao(temperatura_maxima, temperatura_minima)
        print(f"A média entre as temperaturas é: {media:.2f}")
        print(f"A variação entre as temperaturas é: {variacao:.2f}")

        numero = input("Informe um número para somar os seus dígitos: ")

        resultado_soma = somar_digitos(numero)
        print(f"A soma dos dígitos do número {numero} é: {resultado_soma}")
        
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido para as temperaturas.")

if __name__ == "__main__":
    main()