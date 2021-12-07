Feature: Login

  Scenario: Login Positivo
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho "teste@iterasys.com.br" e "senha"
    And clico em Login
    Then exibe a mensagem de pagina expirada

  Scenario Outline: Varios Logins Positivos
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho "<email>" e "<senha>"
    And clico em Login
    Then exibe a mensagem de pagina expirada
    Examples:
      | email                  | senha  |
      | teste1@iterasys.com.br | 123456 |
      | teste2@iterasys.com.br | abcdef |
