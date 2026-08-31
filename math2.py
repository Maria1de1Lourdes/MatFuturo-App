import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
# Configuração da página — deve ser o primeiro comando do Streamlit
st.set_page_config(
    page_title="Equação do 2º Grau",
    page_icon="📈",
    layout="centered"
)
# CSS
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #9DCC9B;
    }
    [data-testid="stHeader"] {
        background-color: ##9DCC9B;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Caminho da pasta do aplicativo
PASTA_APP = Path(__file__).parent
CAMINHO_LOGO = PASTA_APP / "Foto.jpg"
# Exibir logo
if CAMINHO_LOGO.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(CAMINHO_LOGO), use_container_width=True)
else:
    st.warning("⚠️ A imagem Foto.jpg não foi encontrada.")
# Título
st.title("📈 Equação do 2º Grau")
st.write("Equação no formato:")
st.latex(r"ax^2 + bx + c = 0")
# Entrada dos valores
a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)
b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)
c = st.number_input(
    "Digite o valor de c",
    value=0,
    step=1
)
# Botão calcular
if st.button("Calcular", use_container_width=True):
    # Caso a = 0
    if a == 0:
        st.error("❌ O valor de 'a' não pode ser 0 em uma equação do 2º grau.")
    else:
        # Cálculo do delta
        delta = b**2 - 4*a*c
        # Resultado do delta
        st.subheader("📐 Delta")
        st.latex(f"\\Delta = b^2 - 4ac")
        st.latex(f"\\Delta = ({b})^2 - 4({a})({c})")
        st.latex(f"\\Delta = {delta}")
        # Equação
        st.subheader("📝 Equação")
        if b >= 0 and c >= 0:
            st.latex(f"{a}x^2 + {b}x + {c} = 0")
        elif b < 0 and c >= 0:
            st.latex(f"{a}x^2 - {abs(b)}x + {c} = 0")
        elif b >= 0 and c < 0:
            st.latex(f"{a}x^2 + {b}x - {abs(c)} = 0")
        else:
            st.latex(f"{a}x^2 - {abs(b)}x - {abs(c)} = 0")
        # Delta negativo
        if delta < 0:

            st.error(
                "❌ Como Δ < 0, a equação não possui raízes reais."
            )
        # Delta igual a zero
        elif delta == 0:
            x = -b / (2 * a)
            st.success("✅ A equação possui uma única raiz real.")
            st.subheader("🎯 Resultado")
            st.success(f"x = {x:.2f}")
            # Resolução
            st.subheader("📚 Resolução")
            st.latex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}")
            st.latex(
                f"x = \\frac{{-({b}) \\pm \\sqrt{{{delta}}}}}{{2({a})}}"
            )
            st.latex(f"x = {x:.2f}")
        # Delta positivo
        else:
            # Fórmula de Bhaskara
            x1 = (-b + np.sqrt(delta)) / (2 * a)
            x2 = (-b - np.sqrt(delta)) / (2 * a)
            st.success("✅ A equação possui duas raízes reais.")
            # Resultado
            st.subheader("🎯 Resultado")
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"x₁ = {x1:.2f}")
            with col2:
                st.success(f"x₂ = {x2:.2f}")
            # Resolução
            st.subheader("📚 Resolução")
            st.write("Utilizando a fórmula de Bhaskara:")
            st.latex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}")
            st.latex(
                f"x_1 = \\frac{{-({b}) + \\sqrt{{{delta}}}}}{{2({a})}}"
            )
            st.latex(
                f"x_1 = {x1:.2f}"
            )
            st.latex(
                f"x_2 = \\frac{{-({b}) - \\sqrt{{{delta}}}}}{{2({a})}}"
            )
            st.latex(
                f"x_2 = {x2:.2f}"
            )
        # Gráfico da função
        st.subheader("📊 Gráfico da função")
        # Vértice
        xv = -b / (2 * a)
        yv = a * xv**2 + b * xv + c
        # Define uma região adequada para o gráfico
        if delta >= 0:
            x_min = min(x1, x2, xv) - 5 if delta > 0 else xv - 5
            x_max = max(x1, x2, xv) + 5 if delta > 0 else xv + 5
        else:
            x_min = xv - 10
            x_max = xv + 10
        x = np.linspace(x_min, x_max, 500)
        y = a * x**2 + b * x + c
        fig, ax = plt.subplots(figsize=(8, 5))
        # Parábola
        ax.plot(
            x,
            y,
            linewidth=2,
            color="blue",
            label=f"y = {a}x² + {b}x + {c}"
        )
        # Eixos
        ax.axhline(
            y=0,
            linewidth=1,
            color="black"
        )
        ax.axvline(
            x=0,
            linewidth=1,
            color="black"
        )
        # Marcar raízes
        if delta > 0:

            ax.scatter(
                [x1, x2],
                [0, 0],
                s=100,
                color="red",
                zorder=5,
                label="Raízes"
            )
        elif delta == 0:
            ax.scatter(
                [xv],
                [0],
                s=100,
                color="red",
                zorder=5,
                label="Raiz"
            )
        # Marcar vértice
        ax.scatter(
            [xv],
            [yv],
            s=100,
            color="green",
            zorder=5,
            label=f"Vértice ({xv:.2f}, {yv:.2f})"
        )
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Gráfico da Função do 2º Grau")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)
# Rodapé
st.divider()
st.caption("📚 Calculadora de Equação do 2º Grau")
