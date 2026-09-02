# Análise LHE no Google Colab

Este repositório é um exemplo público de análise de eventos em nível de gerador
para o canal `pp → H → γγ`, comparado ao fundo contínuo `pp → γγ` sem Higgs.
Ele foi preparado a partir do template FIS01214 e contém um notebook integrado
com `pandas.DataFrame`.

## Execução

Abra `notebooks/analise-consolidada-dataframe.ipynb` no Google Colab. Faça
upload do notebook e do ZIP deste repositório no painel **Arquivos**, descompacte
o ZIP e confirme `data/sinal.lhe.gz` e `data/fundo.lhe.gz`. O Colab já fornece
Python, NumPy, Pandas e Matplotlib; não é necessário instalar pacotes nesta
variante. Execute as células na ordem para ver a leitura, seleção, cutflow,
massas invariantes, normalização e estimativa simplificada de seção de choque.

## Física e limitações

Os eventos são simulados no nível de gerador. O pico de massa invariante dos
fótons ilustra a assinatura do Higgs, mas não representa uma medida experimental
com detector real: não há reconstrução, resolução, trigger, pileup ou
calibração. Os resultados servem como demonstração didática reproduzível.
