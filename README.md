Conversor de Dólar para Real (BRL)
Este projeto tem como objetivo fornecer uma maneira simples de converter valores em dólares (USD) para reais (BRL) com base na cotação atual, utilizando uma API externa.

Objetivo do Código
O objetivo principal deste código é obter a cotação do dólar em relação ao real (BRL) de uma API externa e permitir que o usuário converta um valor em dólares para reais com base nessa cotação.

Estrutura do Código
1. Importação do módulo requests
O código utiliza o módulo requests para realizar uma requisição HTTP à API externa e obter a cotação do dólar. Esse módulo é amplamente utilizado para trabalhar com requisições HTTP em Python.

2. Função obter_cotacao()
Esta função é responsável por realizar a requisição à API e obter a cotação atual do dólar em relação ao real.

Passos principais:

Define a URL da API:
url = "https://v6.exchangerate-api.com/v6/c05a3ed4d54784176863ac20/latest/USD"
Realiza a requisição usando requests.get(url) e verifica se houve algum erro durante a requisição com response.raise_for_status().
Converte a resposta para formato JSON e extrai a cotação do real (BRL).
Se a chave result for 'success', retorna o valor da cotação em relação ao real.
Caso contrário, imprime uma mensagem de erro e retorna None.
Em caso de exceções durante a requisição (erro de rede, timeout, etc.), a função captura e imprime a exceção, retornando None.
3. Função main()
Esta função controla o fluxo principal do programa e interage com o usuário.

Passos principais:

Exibe uma mensagem de boas-vindas.
Chama a função obter_cotacao() para obter a cotação do dólar.
Se a cotação for obtida com sucesso, solicita ao usuário que informe um valor em dólares, realiza a conversão para reais e exibe o resultado.
Caso contrário, o programa informa que não foi possível obter a cotação no momento.
4. Execução principal (if __name__ == "__main__")
Esse bloco garante que a função main() seja executada apenas quando o script for executado diretamente, e não quando importado como módulo.


