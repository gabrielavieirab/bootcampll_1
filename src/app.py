"""
Checklist de Autocuidado e Hidratação
Versão: 1.0.0
Autor: Aluno
"""

import json
import os
import tkinter as tk
from tkinter import messagebox

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "historico.json")

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

COR_FUNDO = "#F7F9FC"
COR_PAINEL = "#FFFFFF"
COR_PRIMARIA = "#6C9BCF"
COR_SECUNDARIA = "#A8D5BA"
COR_TEXTO = "#2E3A4E"
COR_SUBTEXTO = "#7A8FA6"
COR_BORDA = "#DDE6F0"
FONTE_TITULO = ("Segoe UI", 18, "bold")
FONTE_SECAO = ("Segoe UI", 12, "bold")
FONTE_ITEM = ("Segoe UI", 10)
FONTE_RODAPE = ("Segoe UI", 9)


def carregar_historico():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_historico(dados):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def calcular_progresso(estados):
    total = sum(len(v) for v in ITENS_PADRAO.values())
    marcados = sum(1 for var in estados.values() if var.get())
    return marcados, total


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Checklist de Autocuidado e Hidratação")
        self.geometry("620x720")
        self.resizable(True, True)
        self.configure(bg=COR_FUNDO)
        self.estados = {}
        self._construir_interface()
        self._carregar_estado()

    def _construir_interface(self):
        # Cabeçalho
        cabecalho = tk.Frame(self, bg=COR_PRIMARIA, pady=18)
        cabecalho.pack(fill="x")
        tk.Label(
            cabecalho,
            text="Checklist de Autocuidado",
            font=FONTE_TITULO,
            bg=COR_PRIMARIA,
            fg="#FFFFFF",
        ).pack()
        tk.Label(
            cabecalho,
            text="Cuide de você todos os dias 💧",
            font=FONTE_RODAPE,
            bg=COR_PRIMARIA,
            fg="#D6EAF8",
        ).pack()

        # Barra de progresso
        self.frame_progresso = tk.Frame(self, bg=COR_FUNDO, pady=10)
        self.frame_progresso.pack(fill="x", padx=24)
        self.label_progresso = tk.Label(
            self.frame_progresso,
            text="Progresso: 0 / 0",
            font=FONTE_RODAPE,
            bg=COR_FUNDO,
            fg=COR_SUBTEXTO,
        )
        self.label_progresso.pack(anchor="w")
        self.canvas_barra = tk.Canvas(
            self.frame_progresso, height=12, bg=COR_BORDA, highlightthickness=0
        )
        self.canvas_barra.pack(fill="x", pady=(2, 0))

        # Área rolável
        container = tk.Frame(self, bg=COR_FUNDO)
        container.pack(fill="both", expand=True, padx=24, pady=8)

        canvas = tk.Canvas(container, bg=COR_FUNDO, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.frame_scroll = tk.Frame(canvas, bg=COR_FUNDO)

        self.frame_scroll.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.create_window((0, 0), window=self.frame_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        # Seções de itens
        for secao, itens in ITENS_PADRAO.items():
            self._criar_secao(self.frame_scroll, secao, itens)

        # Botões
        frame_botoes = tk.Frame(self, bg=COR_FUNDO, pady=12)
        frame_botoes.pack(fill="x", padx=24)

        btn_salvar = tk.Button(
            frame_botoes,
            text="Salvar Progresso",
            command=self._salvar_estado,
            bg=COR_PRIMARIA,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
        )
        btn_salvar.pack(side="left", padx=(0, 10))

        btn_limpar = tk.Button(
            frame_botoes,
            text="Reiniciar Checklist",
            command=self._limpar_estado,
            bg=COR_BORDA,
            fg=COR_TEXTO,
            font=("Segoe UI", 10),
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
        )
        btn_limpar.pack(side="left")

        # Rodapé
        tk.Label(
            self,
            text="v1.0.0 — Checklist de Autocuidado e Hidratação",
            font=FONTE_RODAPE,
            bg=COR_FUNDO,
            fg=COR_SUBTEXTO,
        ).pack(pady=(0, 8))

    def _criar_secao(self, parent, titulo, itens):
        frame_secao = tk.Frame(parent, bg=COR_PAINEL, bd=0, relief="flat")
        frame_secao.pack(fill="x", pady=(0, 12))

        # Barra colorida lateral
        cor_lateral = COR_PRIMARIA if titulo == "Hidratação" else (
            COR_SECUNDARIA if titulo == "Autocuidado" else "#F4C2A1"
        )
        barra = tk.Frame(frame_secao, bg=cor_lateral, width=5)
        barra.pack(side="left", fill="y")

        conteudo = tk.Frame(frame_secao, bg=COR_PAINEL, padx=14, pady=10)
        conteudo.pack(side="left", fill="both", expand=True)

        tk.Label(
            conteudo,
            text=titulo,
            font=FONTE_SECAO,
            bg=COR_PAINEL,
            fg=COR_TEXTO,
        ).pack(anchor="w", pady=(0, 6))

        for item in itens:
            var = tk.BooleanVar()
            self.estados[item] = var

            linha = tk.Frame(conteudo, bg=COR_PAINEL)
            linha.pack(fill="x", pady=2)

            cb = tk.Checkbutton(
                linha,
                text=item,
                variable=var,
                font=FONTE_ITEM,
                bg=COR_PAINEL,
                fg=COR_TEXTO,
                activebackground=COR_PAINEL,
                selectcolor=COR_PAINEL,
                anchor="w",
                command=self._atualizar_progresso,
            )
            cb.pack(anchor="w")

    def _atualizar_progresso(self):
        marcados, total = calcular_progresso(self.estados)
        self.label_progresso.config(text=f"Progresso: {marcados} / {total} itens concluídos")
        largura = self.canvas_barra.winfo_width()
        self.canvas_barra.delete("all")
        if total > 0 and largura > 0:
            proporcao = marcados / total
            self.canvas_barra.create_rectangle(
                0, 0, int(largura * proporcao), 12, fill=COR_PRIMARIA, outline=""
            )

    def _salvar_estado(self):
        dados = {item: var.get() for item, var in self.estados.items()}
        salvar_historico(dados)
        marcados, total = calcular_progresso(self.estados)
        messagebox.showinfo(
            "Salvo!",
            f"Progresso salvo com sucesso!\n{marcados} de {total} itens concluídos.",
        )

    def _carregar_estado(self):
        historico = carregar_historico()
        for item, var in self.estados.items():
            if item in historico:
                var.set(historico[item])
        self._atualizar_progresso()

    def _limpar_estado(self):
        confirmado = messagebox.askyesno(
            "Reiniciar", "Deseja reiniciar o checklist de hoje?"
        )
        if confirmado:
            for var in self.estados.values():
                var.set(False)
            salvar_historico({})
            self._atualizar_progresso()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
