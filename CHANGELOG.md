# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
e o projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [1.0.0] — 2026-04-09

### Adicionado
- Interface gráfica (GUI) com Tkinter, design minimalista em cores claras.
- Checklist organizado em três categorias: Hidratação, Autocuidado e Alimentação.
- Barra de progresso visual indicando itens concluídos.
- Persistência de dados em arquivo JSON local.
- Funcionalidade de salvar e reiniciar o checklist.
- Módulo de lógica de negócio separado (`checklist.py`) para facilitar testes.
- Testes automatizados com `pytest` cobrindo todos os comportamentos principais.
- Linting configurado com `ruff`.
- Pipeline de Integração Contínua (CI) com GitHub Actions.
- `README.md` completo com instruções de instalação, execução e uso.
- `pyproject.toml` com metadados e versionamento semântico `1.0.0`.
