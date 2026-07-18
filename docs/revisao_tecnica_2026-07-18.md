# Revisão técnica do repositório — 18/07/2026

## Estado validado

- Os três CSVs oficiais estão presentes em `data/raw`.
- `train.csv` possui 891 linhas e 12 colunas.
- `test.csv` possui 418 linhas e 11 colunas.
- Não foram encontrados registros integralmente duplicados.
- O notebook oficial executa do início ao fim sem erro quando iniciado pela pasta `notebooks`.
- O notebook gera `outputs/submission/submission.csv` com 418 previsões.

## Qualidade dos dados

### Treino

- `Cabin`: 687 valores ausentes.
- `Age`: 177 valores ausentes.
- `Embarked`: 2 valores ausentes.

### Teste

- `Cabin`: 327 valores ausentes.
- `Age`: 86 valores ausentes.
- `Fare`: 1 valor ausente.

## Resultados iniciais do notebook

| Modelo | Accuracy validação | Precision | Recall | F1 | CV média | CV desvio |
|---|---:|---:|---:|---:|---:|---:|
| Regressão Logística | 0,8547 | 0,8413 | 0,7681 | 0,8030 | 0,8227 | 0,0250 |
| Random Forest | 0,8212 | 0,8246 | 0,6812 | 0,7460 | 0,8260 | 0,0172 |

O notebook selecionou Random Forest pela maior média de validação cruzada. A diferença para a Regressão Logística é pequena; a escolha final deve ser justificada e pode considerar estabilidade, interpretabilidade e pontuação no Kaggle.

## Pontos fortes

- Estrutura de pastas clara.
- Separação de branches e responsabilidades.
- Pipeline com imputação, codificação e modelos.
- Engenharia inicial de atributos (`FamilySize`, `IsAlone`, `Title`).
- Geração automática do arquivo de submissão.
- Documentação e checklist já preparados.

## Correções prioritárias

1. Tornar a localização de `data/raw` robusta para VS Code, Colab e execução pela raiz.
2. Ampliar a EDA: idade, tarifa, porto de embarque, estrutura familiar e dados ausentes.
3. Preencher as interpretações em Markdown dentro do notebook.
4. Salvar os gráficos finais em `outputs/figures`.
5. Criar `outputs/evidencias` para a captura do Kaggle.
6. Ajustar `.gitignore` para permitir versionar apenas `submission.csv` e imagens finais.
7. Não versionar `git-info.txt`, `estrutura-local.txt` ou ZIPs de revisão.
8. Registrar autor, URL e licença do notebook Kaggle antes de publicá-lo.
9. Corrigir no README o nome misto `insurminds_grupo_alpha-agents`.
10. Atualizar as branches do Vilela e Wagner a partir da `develop` antes do trabalho.

## Diferenciais recomendados

- comparação de baseline simples versus modelo com engenharia de atributos;
- `CabinDeck`, `FarePerPerson` e `TicketGroupSize`, desde que avaliados e justificados;
- análise de falsos positivos e falsos negativos;
- importância das variáveis;
- Model Card com objetivo, métricas, limitações e uso educacional;
- comparação das submissões dos dois modelos no Kaggle.
