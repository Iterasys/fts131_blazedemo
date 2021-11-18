Feature: Compra de Passagem Aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site Blazedemo
    # Parametros fixos
    When pesquiso passagens de 'Sao Paulo' a 'New York'
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi emitida

  Scenario: Viagem de Boston a Dublin
    Given que acesso o portal Blazedemo
    # Parametros fixos
    When pesquiso passagens de 'Boston' a 'Dublin'
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi emitida