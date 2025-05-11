# Projeto MLOps - Arquitetura

## Visão Geral
Este projeto implementa uma arquitetura de MLOps para gerenciar o ciclo de vida de modelos de aprendizado de máquina, desde o desenvolvimento até a produção.

## Explicação do Projeto

[![Video](https://img.youtube.com/vi/Z9FtrRq0rc0/0.jpg)](https://www.youtube.com/watch?v=Z9FtrRq0rc0)

## Estrutura do Projeto
Abaixo está a estrutura geral do projeto:

```
project-mlops/
├── data/                # Dados brutos e processados
├── notebooks/           # Notebooks para exploração e prototipagem
├── src/                 # Código-fonte do projeto
│   ├── data/            # Scripts para manipulação de dados
│   ├── models/          # Treinamento e avaliação de modelos
│   ├── pipelines/       # Definição de pipelines de MLOps
│   └── utils/           # Funções auxiliares
├── tests/               # Testes automatizados
├── configs/             # Configurações e hiperparâmetros
├── artifacts/           # Modelos treinados e outros artefatos
├── docker/              # Configurações para containerização
├── ci-cd/               # Scripts e configurações de CI/CD
├── img/                 # Imagens e diagramas
└── README.md            # Documentação do projeto
```

## Diagrama da Arquitetura
Abaixo está um diagrama representando a arquitetura geral do projeto:

![Diagrama da Arquitetura](img/diagram.png)

## Componentes da Arquitetura

### 1. **Ingestão de Dados**
- Local: `src/data/`
- Scripts para coleta, limpeza e transformação de dados.

### 2. **Treinamento de Modelos**
- Local: `src/models/`
- Código para treinar, validar e salvar modelos.

### 3. **Pipelines**
- Local: `src/pipelines/`
- Definição de pipelines para automação do fluxo de trabalho.

### 4. **Testes**
- Local: `tests/`
- Testes unitários e de integração para garantir a qualidade do código.

### 5. **Implantação**
- Local: `docker/` e `ci-cd/`
- Configurações para containerização e automação de implantação.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Orquestração:** Prefect, Airflow
- **Containerização:** Docker
- **CI/CD:** GitHub Actions
- **Monitoramento:** Prometheus, Grafana

## Como Executar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/project-mlops.git
    ```
2. Configure o ambiente:
    ```bash
    cd project-mlops
    pip install -r requirements.txt
    ```
3. Execute os pipelines:
    ```bash
    python src/pipelines/main.py
    ```

## Contribuição
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
