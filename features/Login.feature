Feature: Login

  Scenario: Login Positivo
    Given que acesso o portal Blazedemo
    When clico em Home
    Then exibe a pagina de Login
    When preencho "email" e "senha"
    And clico em Login
    Then exibe a mensagem de pagina expirada

