# Alpha Agents

Repositório de trabalho dos desafios do programa InsurMinds I2A2.

## Integrantes e responsabilidades

| Integrante | Responsabilidade principal |
|---|---|
| Vitor | Estrutura do projeto, pipeline, integração, Random Forest, submissão e entrega |
| Vilela | EDA, tratamento dos dados, engenharia de atributos, Regressão Logística e comparação dos modelos |
| Wagner | Requisitos, interpretação dos resultados, documentação, validação funcional e visão de seguros |

## Estratégia de branches

- `main`: somente versões finais e entregues.
- `develop`: integração das atividades antes da entrega.
- `feature/desafio3-eda-modelagem-vilela`: desenvolvimento do Vilela.
- `feature/desafio3-pipeline-integracao-vitor`: desenvolvimento do Vitor.
- `docs/desafio3-relatorio-wagner`: documentação do Wagner.

Nenhum integrante deve desenvolver diretamente na `main`.

## Fluxo de trabalho

1. Atualizar a branch local:
   ```bash
   git switch develop
   git pull
   ```
2. Entrar na própria branch:
   ```bash
   git switch <nome-da-branch>
   git merge develop
   ```
3. Desenvolver, testar e registrar alterações:
   ```bash
   git add .
   git commit -m "tipo: descrição objetiva"
   git push
   ```
4. Abrir Pull Request para `develop`.
5. Outro integrante revisa antes do merge.
6. Quando a entrega estiver validada, abrir Pull Request de `develop` para `main`.

## Padrão de commits

- `feat:` nova funcionalidade
- `fix:` correção
- `docs:` documentação
- `test:` testes
- `chore:` configuração e manutenção

Exemplos:

```text
feat: adiciona análise de sobrevivência por classe
feat: implementa pipeline de random forest
docs: documenta critérios de escolha do modelo
fix: corrige geração do arquivo de submissão
```

## Desafio 3 — Titanic

### Arquivos esperados

Colocar os arquivos do Kaggle em:

```text
data/raw/train.csv
data/raw/test.csv
```

### Execução

1. Criar ambiente Python ou abrir o notebook no Google Colab.
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Executar:
   ```text
   notebooks/Desafio_3_Titanic.ipynb
   ```

### Entregáveis

- Notebook `.ipynb`;
- arquivo `submission.csv`;
- captura da pontuação válida no Kaggle.

## Estrutura

```text
insurminds_grupo_alpha-agents/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── checklist_entrega.md
│   ├── decisoes_tecnicas.md
│   └── relatorio_desafio_3.md
├── notebooks/
│   └── Desafio_3_Titanic.ipynb
├── outputs/
│   ├── figures/
│   └── submission/
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── TASKS.md
├── requirements.txt
└── setup_repository.ps1
```
