"""
Testes automatizados para o módulo checklist.
"""

import json
import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from checklist import (
    ITENS_PADRAO,
    calcular_progresso,
    carregar_estado,
    desmarcar_item,
    marcar_item,
    obter_todos_itens,
    percentual_progresso,
    reiniciar_checklist,
    salvar_estado,
)

# ─── Testes: obter_todos_itens ────────────────────────────────────────────────

def test_obter_todos_itens_retorna_lista():
    """Deve retornar uma lista não vazia."""
    itens = obter_todos_itens()
    assert isinstance(itens, list)
    assert len(itens) > 0


def test_obter_todos_itens_contem_hidratacao():
    """Deve conter itens da categoria Hidratação."""
    itens = obter_todos_itens()
    assert "Beber 1 copo de água ao acordar" in itens


def test_obter_todos_itens_quantidade_correta():
    """Quantidade total deve bater com a soma das categorias."""
    esperado = sum(len(v) for v in ITENS_PADRAO.values())
    assert len(obter_todos_itens()) == esperado


# ─── Testes: calcular_progresso ───────────────────────────────────────────────

def test_calcular_progresso_nenhum_marcado():
    """Com nenhum item marcado, concluídos deve ser 0."""
    marcados = {}
    concluidos, total = calcular_progresso(marcados)
    assert concluidos == 0
    assert total > 0


def test_calcular_progresso_um_item_marcado():
    """Com um item marcado, concluídos deve ser 1."""
    item = obter_todos_itens()[0]
    marcados = {item: True}
    concluidos, total = calcular_progresso(marcados)
    assert concluidos == 1


def test_calcular_progresso_todos_marcados():
    """Com todos os itens marcados, concluídos deve igualar total."""
    marcados = {item: True for item in obter_todos_itens()}
    concluidos, total = calcular_progresso(marcados)
    assert concluidos == total


# ─── Testes: percentual_progresso ────────────────────────────────────────────

def test_percentual_zero_quando_vazio():
    """Percentual deve ser 0.0 quando nenhum item está marcado."""
    assert percentual_progresso({}) == 0.0


def test_percentual_cem_quando_completo():
    """Percentual deve ser 100.0 quando todos os itens estão marcados."""
    marcados = {item: True for item in obter_todos_itens()}
    assert percentual_progresso(marcados) == 100.0


def test_percentual_entre_zero_e_cem():
    """Percentual deve estar entre 0 e 100 para qualquer estado parcial."""
    itens = obter_todos_itens()
    marcados = {itens[0]: True}
    pct = percentual_progresso(marcados)
    assert 0.0 < pct < 100.0


# ─── Testes: marcar_item ─────────────────────────────────────────────────────

def test_marcar_item_valido():
    """Deve marcar o item como True."""
    item = obter_todos_itens()[0]
    resultado = marcar_item({}, item)
    assert resultado[item] is True


def test_marcar_item_invalido_levanta_erro():
    """Deve levantar ValueError para item inexistente."""
    with pytest.raises(ValueError):
        marcar_item({}, "Item que não existe")


def test_marcar_item_nao_altera_original():
    """O dicionário original não deve ser modificado."""
    original = {}
    item = obter_todos_itens()[0]
    marcar_item(original, item)
    assert item not in original


# ─── Testes: desmarcar_item ───────────────────────────────────────────────────

def test_desmarcar_item_valido():
    """Deve desmarcar o item (setar False)."""
    item = obter_todos_itens()[0]
    marcados = {item: True}
    resultado = desmarcar_item(marcados, item)
    assert resultado[item] is False


def test_desmarcar_item_invalido_levanta_erro():
    """Deve levantar ValueError para item inexistente."""
    with pytest.raises(ValueError):
        desmarcar_item({}, "Item fantasma")


# ─── Testes: reiniciar_checklist ─────────────────────────────────────────────

def test_reiniciar_retorna_todos_falso():
    """Todos os itens devem estar False após reiniciar."""
    estado = reiniciar_checklist()
    assert all(v is False for v in estado.values())


def test_reiniciar_contem_todos_itens():
    """O estado reiniciado deve conter todos os itens."""
    estado = reiniciar_checklist()
    for item in obter_todos_itens():
        assert item in estado


# ─── Testes: salvar e carregar estado ────────────────────────────────────────

def test_salvar_e_carregar_estado():
    """O estado salvo deve ser igual ao carregado."""
    item = obter_todos_itens()[0]
    marcados = {item: True}
    with tempfile.TemporaryDirectory() as tmpdir:
        caminho = os.path.join(tmpdir, "estado.json")
        salvar_estado(caminho, marcados)
        carregado = carregar_estado(caminho)
    assert carregado == marcados


def test_carregar_estado_arquivo_inexistente():
    """Deve retornar dicionário vazio se o arquivo não existir."""
    resultado = carregar_estado("/caminho/que/nao/existe.json")
    assert resultado == {}


def test_salvar_cria_arquivo_json_valido():
    """O arquivo salvo deve ser um JSON válido."""
    marcados = {obter_todos_itens()[0]: True}
    with tempfile.TemporaryDirectory() as tmpdir:
        caminho = os.path.join(tmpdir, "estado.json")
        salvar_estado(caminho, marcados)
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    assert isinstance(dados, dict)
