param(
    [string]$RemoteUrl = ""
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git não encontrado. Instale o Git antes de executar este script."
}

if (-not (Test-Path ".git")) {
    git init
}

git add .
git commit -m "chore: cria estrutura inicial do Desafio 3"
git branch -M main

git switch -c develop
git branch "feature/desafio3-eda-modelagem-vilela"
git branch "feature/desafio3-pipeline-integracao-vitor"
git branch "docs/desafio3-relatorio-wagner"

if ($RemoteUrl -ne "") {
    git remote add origin $RemoteUrl
    git push -u origin main
    git push -u origin develop
    git push -u origin "feature/desafio3-eda-modelagem-vilela"
    git push -u origin "feature/desafio3-pipeline-integracao-vitor"
    git push -u origin "docs/desafio3-relatorio-wagner"
}

Write-Host ""
Write-Host "Repositório configurado."
Write-Host "Branch atual: develop"
Write-Host ""
Write-Host "Branches:"
git branch
