import requests


def obter_cotacao():
    # URL da API para obter a cotação do dólar
    url = "https://v6.exchangerate-api.com/v6/c05a3ed4d54784176863ac20/latest/USD"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição
        dados = response.json()

        # Verificar se a API retornou com sucesso
        if dados['result'] == 'success':
            # Obtendo a cotação do Real
            cotacao_real = dados['conversion_rates']['BRL']
            return cotacao_real
        else:
            print("Erro ao obter dados da API.")
            return None
    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)
        return None


def main():
    print("Bem-vindo ao programa de cotação do dólar!")
    cotacao = obter_cotacao()

    if cotacao:
        print(f"A cotação atual do dólar em relação ao real é: R$ {cotacao:.2f}")
        valor_em_dolar = float(input("Digite o valor em dólares que deseja converter para reais: $ "))
        valor_convertido = valor_em_dolar * cotacao
        print(f"Valor em reais: R$ {valor_convertido:.2f}")
    else:
        print("Não foi possível obter a cotação no momento. Tente novamente mais tarde.")


if __name__ == "__main__":
    main()
