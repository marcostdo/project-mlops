# Projeto MLOps - Arquitetura

## Visão Geral
Este projeto implementa uma arquitetura de MLOps para gerenciar o ciclo de vida de modelos de aprendizado de máquina, desde o desenvolvimento até a produção.

## Apresentação (Video)

[![Video](https://img.youtube.com/vi/aDDhuXXv2uk/0.jpg)](https://www.youtube.com/watch?v=aDDhuXXv2uk)

## Considerações
A ideia inicial era implementar a esteira para realizar a criação dos recursos utilizados dentro da conta aws e assim tornar possível a reprodução da mesma estrutura na conta de quem fizesse o fork do projeto, sendo necessário apenas criar sua conta implementar algumas configurações requeridas, mas considerando o tempo e a complexidade de implementação de alguns serviços, mudei a abordagem e segui apenas com o case principal mas mantive a esteira criada em **.github** e o bucket utilizado no projeto foi criado por ela.

## Diagrama da Arquitetura
Abaixo está um diagrama representando a arquitetura geral do projeto:

![Diagrama da Arquitetura](img/diagram.png)

## Componentes da Arquitetura

### 1. **Ingestão de Dados**
- Local: `src/data/`
- Scripts para coleta, limpeza e transformação de dados.


