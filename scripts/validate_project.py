from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


def fail(message: str) -> None:
    print(f"[ERRO] {message}")
    raise SystemExit(1)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    raw = root / "data" / "raw"
    train_path = raw / "train.csv"
    test_path = raw / "test.csv"
    sample_path = raw / "gender_submission.csv"

    for path in (train_path, test_path, sample_path):
        if not path.exists():
            fail(f"Arquivo ausente: {path.relative_to(root)}")

    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    sample = pd.read_csv(sample_path)

    required_train = {
        "PassengerId", "Survived", "Pclass", "Name", "Sex", "Age",
        "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked",
    }
    required_test = required_train - {"Survived"}

    if set(train.columns) != required_train:
        fail(f"Colunas inesperadas em train.csv: {train.columns.tolist()}")
    if set(test.columns) != required_test:
        fail(f"Colunas inesperadas em test.csv: {test.columns.tolist()}")
    if sample.columns.tolist() != ["PassengerId", "Survived"]:
        fail("gender_submission.csv não possui o formato esperado")
    if train["PassengerId"].duplicated().any():
        fail("PassengerId duplicado em train.csv")
    if test["PassengerId"].duplicated().any():
        fail("PassengerId duplicado em test.csv")
    if not set(train["Survived"].unique()).issubset({0, 1}):
        fail("Survived contém valores diferentes de 0 e 1")

    print("[OK] Dados localizados e estrutura validada")
    print(f"[OK] train.csv: {train.shape[0]} linhas x {train.shape[1]} colunas")
    print(f"[OK] test.csv: {test.shape[0]} linhas x {test.shape[1]} colunas")
    print("\nValores ausentes — treino:")
    print(train.isna().sum()[lambda s: s > 0].sort_values(ascending=False))
    print("\nValores ausentes — teste:")
    print(test.isna().sum()[lambda s: s > 0].sort_values(ascending=False))


if __name__ == "__main__":
    main()
