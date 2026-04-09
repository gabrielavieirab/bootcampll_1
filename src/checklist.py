"""
Módulo de lógica de negócio do Checklist de Autocuidado e Hidratação.
Versão: 1.0.0
"""

import json
import os

ITENS_PADRAO = {
    "Hidratação": [
        "Beber 1 copo de água ao acordar",
        "Beber 2 copos de água pela manhã",
        "Beber 2 copos de água à tarde",
        "Beber 2 copos de água à noite",
        "Beber 1 copo de água antes de dormir",
    ],
    "Autocuidado": [
        "Escovar os dentes (manhã)",
        "Escovar os dentes (noite)",
        "Tomar banho",
        "Passar protetor solar",
        "Fazer alongamento ou exercício leve",
        "Dormir pelo menos 7 horas",
        "Fazer uma pausa de 5 minutos sem tela",
    ],
    "Alimentação": [
        "Tomar café da manhã",
        "Almoçar em horário regular",
        "Jantar em horário regular",
        "Evitar ultraprocessados hoje",
    ],
}


def obter_todos_itens():
    """Retorna lista plana com todos os itens do checklist."""
    todos = []
    for itens in ITENS_PADRAO.values():
        todos.extend(itens)
    return todos


def calcular_progresso(marcados: dict) -> tuple[int, int]:
    """
    Calcula o progresso do checklist.

    Args:
        marcados: dicionário {item: bool} com estado de cada item.

    Returns:
        Tupla (concluídos, total).
    """
    todos = obter_todos_itens()
    total = len(todos)
    concluidos = sum(1 for item in todos if marcados.get(item, False))
    return concluidos, total


def percentual_progresso(marcados: dict) -> float:
    """
    Retorna o percentual de conclusão do checklist (0.0 a 100.0).

    Args:
        marcados: dicionário {item: bool}.

    Returns:
        Float representando o percentual.
    """
    concluidos, total = calcular_progresso(marcados)
    if total == 0:
        return 0.0
    return round((concluidos / total) * 100, 2)


def marcar_item(marcados: dict, item: str) -> dict:
    """
    Marca um item como concluído.

    Args:
        marcados: estado atual.
        item: nome do item a marcar.

    Returns:
        Novo dicionário com o item marcado.

    Raises:
        ValueError: se o item não existir no checklist.
    """
    todos = obter_todos_itens()
    if item not in todos:
        raise ValueError(f"Item '{item}' não encontrado no checklist.")
    novo = dict(marcados)
    novo[item] = True
    return novo


def desmarcar_item(marcados: dict, item: str) -> dict:
    """
    Desmarca um item.

    Args:
        marcados: estado atual.
        item: nome do item a desmarcar.

    Returns:
        Novo dicionário com o item desmarcado.

    Raises:
        ValueError: se o item não existir no checklist.
    """
    todos = obter_todos_itens()
    if item not in todos:
        raise ValueError(f"Item '{item}' não encontrado no checklist.")
    novo = dict(marcados)
    novo[item] = False
    return novo


def reiniciar_checklist() -> dict:
    """Retorna um dicionário com todos os itens desmarcados."""
    return {item: False for item in obter_todos_itens()}


def salvar_estado(caminho: str, marcados: dict) -> None:
    """
    Salva o estado do checklist em arquivo JSON.

    Args:
        caminho: caminho do arquivo.
        marcados: estado atual.
    """
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(marcados, f, ensure_ascii=False, indent=2)


def carregar_estado(caminho: str) -> dict:
    """
    Carrega o estado do checklist de um arquivo JSON.

    Args:
        caminho: caminho do arquivo.

    Returns:
        Dicionário com o estado carregado, ou dicionário vazio se não existir.
    """
    if not os.path.exists(caminho):
        return {}
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
