"""Backend de gráficos Matplotlib para execução no Google Colab.

O notebook usa somente a pequena API exposta por ``matplotlib.pyplot``.
Manter este módulo com o nome ``root_plotting`` evita alterar todas as células
do notebook, mas a versão Colab não depende de PyROOT, ROOT ou JSROOT.
"""

from __future__ import annotations

import re
import unicodedata

import matplotlib.pyplot as _plt
import numpy as np


def _normalizar_rotulo(valor):
    """Converte rótulos ROOT/TLatex usados no roteiro para texto Matplotlib."""
    texto = str(valor)
    especiais = {
        "m_{#gamma#gamma}": r"$m_{\gamma\gamma}$",
        "m_{visivel}": r"$m_{\mathrm{visivel}}$",
        "#it{p}_{T,#gamma#gamma}": r"$p_{T,\gamma\gamma}$",
        "#it{p}_{T} #gamma_{lider} [GeV]": r"$p_T\,\gamma_{\mathrm{lider}}$ [GeV]",
        "#it{p}_{T} #gamma_{sublider} [GeV]": r"$p_T\,\gamma_{\mathrm{sublider}}$ [GeV]",
        "Maior |#eta| #gamma": r"Maior $|\eta_\gamma|$",
        "#Delta #eta #gamma#gamma": r"$\Delta\eta_{\gamma\gamma}$",
        "#Delta #phi #gamma#gamma": r"$\Delta\phi_{\gamma\gamma}$",
        "#Delta R #gamma#gamma": r"$\Delta R_{\gamma\gamma}$",
    }
    for origem, destino in especiais.items():
        texto = texto.replace(origem, destino)
    substituicoes = {
        "#it{p}_{T}": r"$p_T$",
        "#Delta": r"$\Delta$",
        "#gamma": r"$\gamma$",
        "#eta": r"$\eta$",
        "#phi": r"$\phi$",
        "#mu": r"$\mu$",
        "#theta": r"$\theta$",
        "#lambda": r"$\lambda$",
    }
    for origem, destino in substituicoes.items():
        texto = texto.replace(origem, destino)
    texto = re.sub(r"(?<![#A-Za-z])DeltaR(?![A-Za-z])", r"$\Delta R$", texto, flags=re.IGNORECASE)
    texto = re.sub(r"(?<![#A-Za-z])Delta(?![A-Za-z])", r"$\Delta$", texto, flags=re.IGNORECASE)
    for nome, simbolo in (("gamma", r"$\gamma$"), ("eta", r"$\eta$"), ("phi", r"$\phi$")):
        texto = re.sub(rf"(?<![#A-Za-z]){nome}(?![A-Za-z])", simbolo, texto, flags=re.IGNORECASE)
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(caractere for caractere in texto if not unicodedata.combining(caractere))


class _Eixo:
    """Adaptador mínimo para normalizar rótulos sem alterar a API do notebook."""

    def __init__(self, eixo):
        self._eixo = eixo

    def __getattr__(self, nome):
        atributo = getattr(self._eixo, nome)
        if nome in {"set_xlabel", "set_ylabel", "set_title"}:
            return lambda texto, *args, **kwargs: atributo(_normalizar_rotulo(texto), *args, **kwargs)
        return atributo


class _Figura:
    def __init__(self, figura):
        self._figura = figura

    def __getattr__(self, nome):
        atributo = getattr(self._figura, nome)
        if nome == "suptitle":
            return lambda texto, *args, **kwargs: atributo(_normalizar_rotulo(texto), *args, **kwargs)
        return atributo

    def colorbar(self, mappable, ax=None, **kwargs):
        """Encaminha o colorbar, removendo o wrapper do eixo quando necessário."""
        eixo = ax._eixo if isinstance(ax, _Eixo) else ax
        if "label" in kwargs:
            kwargs["label"] = _normalizar_rotulo(kwargs["label"])
        return self._figura.colorbar(mappable, ax=eixo, **kwargs)


class _PyplotAdapter:
    """Subconjunto de pyplot usado pelos notebooks FIS01214."""

    def subplots(self, *args, **kwargs):
        figura, eixos = _plt.subplots(*args, **kwargs)
        if isinstance(eixos, np.ndarray):
            eixos_adaptados = np.asarray([_Eixo(eixo) for eixo in eixos.flat], dtype=object).reshape(eixos.shape)
        else:
            eixos_adaptados = _Eixo(eixos)
        return _Figura(figura), eixos_adaptados

    def show(self):
        return _plt.show()

    def __getattr__(self, nome):
        return getattr(_plt, nome)


plt = _PyplotAdapter()
