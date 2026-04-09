# _CARELOG_

![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Licença](https://img.shields.io/badge/licença-MIT-green)

---

## DESCRIÇÃO DO PROBLEMA REAL

Muitas pessoas, especialmente estudantes e trabalhadores com rotinas intensas, negligenciam hábitos básicos de autocuidado — como beber água regularmente, escovar os dentes, se alimentar em horários adequados e dormir o suficiente. Essa negligência, muitas vezes invisível no dia a dia, acumula consequências físicas e mentais ao longo do tempo. A ausência de uma ferramenta simples e acessível para lembrar e registrar esses hábitos contribui para que muitas pessoas não consigam manter uma rotina saudável.

## PROPOSTA DA SOLUÇÃO

O **Checklist de Autocuidado e Hidratação** é uma aplicação desktop com interface gráfica (GUI) desenvolvida em Python com Tkinter. A aplicação apresenta uma lista organizada de hábitos diários divididos em três categorias — Hidratação, Autocuidado e Alimentação — permitindo que o usuário marque os itens concluídos ao longo do dia, acompanhe seu progresso por meio de uma barra visual e salve o estado para consulta posterior.

## PÚBLICO-ALVO

Estudantes, trabalhadores e qualquer pessoa que deseje criar e manter hábitos básicos de autocuidado de forma simples, sem necessidade de internet ou cadastro.

## FUNCIONALIDADES PRINCIPAIS

A aplicação oferece as seguintes funcionalidades:

- Checklist interativo com itens de Hidratação, Autocuidado e Alimentação.
- Barra de progresso visual indicando quantos itens foram concluídos.
- Salvamento automático do progresso em arquivo JSON local.
- Carregamento do estado salvo ao reabrir a aplicação.
- Botão para reiniciar o checklist do dia.

## TECNOLOGIAS UTILIZADAS

| Tecnologia | Finalidade |
|---|---|
| Python 3.10+ | Linguagem principal |
| Tkinter | Interface gráfica (GUI) nativa |
| JSON | Persistência de dados local |
| pytest | Testes automatizados |
| ruff | Linting e análise estática |
| GitHub Actions | Integração Contínua (CI) |

## ESTRUTURA DO PROJETO

```
checklist-autocuidado/
├── src/
│   ├── __init__.py
│   ├── app.py          # Interface gráfica principal
│   └── checklist.py    # Lógica de negócio (testável)
├── tests/
│   ├── __init__.py
│   └── test_checklist.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── CHANGELOG.md
├── pyproject.toml
├── README.md
└── requirements.txt
```

## INSTRUÇÕES DE INSTALAÇÃO

**Pré-requisito:** Python 3.10 ou superior instalado. O Tkinter já vem incluído na instalação padrão do Python.

**1. Clone o repositório:**

```bash
git clone https://github.com/SEU_USUARIO/checklist-autocuidado.git
cd checklist-autocuidado
```

**2. (Opcional) Crie e ative um ambiente virtual:**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
```

**3. Instale as dependências de desenvolvimento:**

```bash
pip install -r requirements.txt
```

## Instruções de Execução

Para iniciar a aplicação, execute o seguinte comando na raiz do projeto:

```bash
python src/app.py
```

A janela da aplicação será aberta automaticamente. Marque os itens concluídos, acompanhe seu progresso e clique em **Salvar Progresso** para registrar o estado do dia.

## Instruções para Rodar os Testes

```bash
pytest tests/ -v
```

A saída exibirá cada teste com seu resultado (PASSED / FAILED).

## INSTRUÇÕES PARA RODAR O LINT 

```bash
ruff check src/ tests/
```

Se não houver problemas, nenhuma saída será exibida. Caso existam, o ruff indicará o arquivo, a linha e a descrição do problema.

## VERSÃO ATUAL

**1.0.0** — consulte o [CHANGELOG.md](CHANGELOG.md) para o histórico de alterações.

## AUTOR

**Gabriela Vieira Baptista**
Bootcamp II — Turma B — 2026/1

## REPOSITÓRIO PÚBLICO
https://github.com/gabrielavieirab/bootcampll_1.git 
