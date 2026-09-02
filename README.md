# Análise LHE no Google Colab

Este repositório é um exemplo público de análise de eventos em nível de gerador
para o canal `pp → H → γγ`, comparado ao fundo contínuo `pp → γγ` sem Higgs.
Ele foi preparado a partir do template FIS01214 e contém um notebook integrado
com `pandas.DataFrame`.

## Execução no Google Colab

1. No GitHub, use **Code → Download ZIP** para baixar este repositório e baixe
   também o notebook de interesse: o
   `notebooks/analise-consolidada-dataframe-estudante.ipynb` é a versão guiada
   para gerar código com Gemini, enquanto
   `notebooks/analise-consolidada-dataframe.ipynb` é a referência completa.
2. Abra o notebook no Colab e, no painel **Arquivos**, envie o `.ipynb` e o ZIP
   para o mesmo ambiente. O ZIP é o arquivo de dados da análise.
3. Na seção `0. Preparação no Google Colab`, peça ao agente para localizar e
   descompactar o ZIP, entrar na pasta extraída e inflar
   `data/sinal.lhe.gz` e `data/fundo.lhe.gz` com `gzip`, preservando os arquivos
   `.gz`. Confirme a presença das versões comprimida e descomprimida.
4. Execute as células restantes na ordem. Os caminhos esperados são relativos
   à pasta `notebooks/` e apontam para `../data/`.

Esta variante não requer instalação: o Colab já fornece Python, NumPy, Pandas,
Matplotlib e IPython. A análise mostra leitura tabular, seleção, cutflow,
massas invariantes, normalização e uma estimativa simplificada de seção de
choque. Na versão estudante, use o Gemini para gerar o código de cada célula,
cole-o e revise os resultados antes de prosseguir.

## Física e limitações

Os arquivos `sinal.lhe.gz` e `fundo.lhe.gz` correspondem, respectivamente, a
`pp → H → γγ` e ao contínuo `pp → γγ` sem Higgs. O pico de massa invariante dos
fótons ilustra a assinatura do Higgs. Os eventos estão no nível de gerador:
não há reconstrução, resolução de detector, trigger, pileup ou calibração.
Portanto, a seção de choque estimada é didática e deve ser interpretada junto
com a aceitação, eficiência e luminosidade adotadas.
