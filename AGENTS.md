
# AGENTS.md — InsurMinds Alpha Agents

## Projeto

Desafio 3 do programa InsurMinds: classificação supervisionada para prever
a sobrevivência de passageiros do Titanic.

## Integrantes e responsabilidades

- Vitor Malandrin Ferreira:
  arquitetura técnica, pipeline, Random Forest, integração, validação,
  geração das submissões e organização da entrega.

- José Leonardo Alves Vilela:
  análise exploratória, tratamento dos dados, engenharia de atributos,
  Regressão Logística e comparação técnica.

- Wagner Assis:
  requisitos, interpretação dos resultados, documentação, validação
  funcional e visão de negócio.

## Restrições obrigatórias

1. Nunca executar `git commit`, `git push`, `git merge` ou criar Pull Request.
2. Nunca trocar de branch.
3. Trabalhar somente na branch já selecionada pelo usuário.
4. Não modificar:
   - notebooks/work/vilela_eda_logistic.ipynb
   - docs/relatorio_desafio_3.md
   - docs/checklist_entrega.md
   - textos reservados ao Wagner
5. Não modificar arquivos dentro de `data/raw`.
6. Não incluir `.venv`, `.env`, credenciais ou dados originais no Git.
7. Não copiar código do notebook de referência.
8. O notebook externo deve ser usado apenas como referência conceitual.
9. Antes de alterar arquivos, executar:
   - `git branch --show-current`
   - `git status --short`
10. Ao terminar, apresentar:
   - arquivos alterados;
   - justificativa de cada alteração;
   - comandos de validação executados;
   - resultados;
   - pendências;
   - `git diff --stat`.

## Arquivos sob responsabilidade técnica do Vitor

- notebooks/work/vitor_pipeline_random_forest.ipynb
- notebooks/Desafio_3_Titanic.ipynb
- scripts/validate_project.py
- outputs/figures/
- outputs/submission/
- outputs/evidencias/
- requirements.txt, somente se realmente necessário

## Validações obrigatórias

Executar:

```powershell
python .\scripts\validate_project.py
.\.venv\Scripts\python.exe -m jupyter nbconvert `
  --to notebook `
  --execute .\notebooks\Desafio_3_Titanic.ipynb `
  --inplace `
  --ExecutePreprocessor.kernel_name=python3 `
  --ExecutePreprocessor.timeout=600
git status --short
git diff --stat
```
