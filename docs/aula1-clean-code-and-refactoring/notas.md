# Notas do Projeto

## Visão Geral

Ao longo do curso, vamos desenvolver uma variação do Uber, onde um motorista pode se cadastrar para fazer corridas para passageiros.

## Funcionamento

Em linhas gerais (mais detalhes serão informados ao longo do projeto):

- O passageiro se cadastra na plataforma fornecendo nome, email e CPF.
- O motorista se cadastra na plataforma fornecendo nome, email, CPF e placa do carro.
- Inicialmente, ambos devem ter avaliação igual a 5 e número de corridas igual a 0.
- Após cada corrida, a avaliação e o número de corridas de cada um são atualizados.
- O motorista pode estar nos status: fora de serviço, ocupado ou disponível.
- O passageiro digita as coordenadas de origem e destino e solicita a corrida.
- O motorista visualiza os dados da corrida e pode aceitá-la.
- Após aceite, o passageiro aguarda pelo motorista.
- Ao chegar, o motorista inicia a corrida e durante a corrida, o trajeto vai sendo atualizado com os trechos percorridos, atualizando também o preço.
- No final, o motorista finaliza a corrida e o pagamento é processado.
- O motorista pode avaliar o passageiro depois da corrida finalizada.
- O passageiro pode avaliar o motorista depois da corrida finalizada.

## Aula 1

### Use Case

Calcular o preço da corrida.

| Campo | Valor |
|---|---|
| URL | `/calculate_ride_price` |
| Método | `POST` |
| Input | `distance`, `date` |
| Output | `price` |

## Aula 2

### Use Case

Cadastrar passageiro.

| Campo | Valor |
|---|---|
| URL | `/passengers` |
| Método | `POST` |
| Input | `name`, `email`, `document` |
| Output | `passenger_id` (`uuid`) |

### Use Case

Cadastrar motorista.

| Campo | Valor |
|---|---|
| URL | `/drivers` |
| Método | `POST` |
| Input | `name`, `email`, `document`, `car plate` |
| Output | `driver_id` (`uuid`) |

## Observações

- O documento (CPF) deve ser validado utilizando o algoritmo fornecido, que deve ser refatorado.
- Crie uma API REST para receber as requisições e utilize um banco de dados de sua preferência para persistir os dados.