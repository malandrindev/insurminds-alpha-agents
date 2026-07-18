from __future__ import annotations

from pathlib import Path

import pandas as pd


TRAIN_COLUMNS = [
    "PassengerId",
    "Survived",
    "Pclass",
    "Name",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Ticket",
    "Fare",
    "Cabin",
    "Embarked",
]
TEST_COLUMNS = [column for column in TRAIN_COLUMNS if column != "Survived"]
SUBMISSION_COLUMNS = ["PassengerId", "Survived"]
SUBMISSION_FILENAMES = [
    "submission_random_forest.csv",
    "submission.csv",
]
FIGURE_FILENAMES = [
    "confusion_matrix_random_forest.png",
    "feature_importance_random_forest.png",
    "model_metrics_comparison.png",
]


def fail(message: str) -> None:
    print(f"[ERRO] {message}")
    raise SystemExit(1)


def read_csv(path: Path, root: Path) -> pd.DataFrame:
    relative_path = path.relative_to(root)
    try:
        return pd.read_csv(path)
    except Exception as error:
        fail(f"Não foi possível ler {relative_path}: {error}")


def validate_raw_data(root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw_dir = root / "data" / "raw"
    train_path = raw_dir / "train.csv"
    test_path = raw_dir / "test.csv"
    sample_path = raw_dir / "gender_submission.csv"

    for path in (train_path, test_path, sample_path):
        if not path.is_file():
            fail(f"Arquivo de dados ausente: {path.relative_to(root)}")

    train = read_csv(train_path, root)
    test = read_csv(test_path, root)
    sample = read_csv(sample_path, root)

    if train.columns.tolist() != TRAIN_COLUMNS:
        fail(
            "train.csv possui colunas ou ordem inesperadas: "
            f"{train.columns.tolist()}"
        )
    if test.columns.tolist() != TEST_COLUMNS:
        fail(
            "test.csv possui colunas ou ordem inesperadas: "
            f"{test.columns.tolist()}"
        )
    if sample.columns.tolist() != SUBMISSION_COLUMNS:
        fail(
            "gender_submission.csv possui colunas ou ordem inesperadas: "
            f"{sample.columns.tolist()}"
        )

    if train["PassengerId"].isna().any():
        fail("train.csv contém PassengerId ausente")
    if test["PassengerId"].isna().any():
        fail("test.csv contém PassengerId ausente")
    if train["PassengerId"].duplicated().any():
        fail("train.csv contém PassengerId duplicado")
    if test["PassengerId"].duplicated().any():
        fail("test.csv contém PassengerId duplicado")
    if train["Survived"].isna().any():
        fail("train.csv contém Survived ausente")
    if not train["Survived"].isin([0, 1]).all():
        fail("train.csv contém valores de Survived diferentes de 0 e 1")

    if len(sample) != len(test):
        fail(
            "gender_submission.csv possui quantidade de linhas diferente "
            f"de test.csv: {len(sample)} != {len(test)}"
        )
    if sample.isna().any().any():
        fail("gender_submission.csv contém valores ausentes")
    if sample["PassengerId"].duplicated().any():
        fail("gender_submission.csv contém PassengerId duplicado")
    if not sample["PassengerId"].reset_index(drop=True).equals(
        test["PassengerId"].reset_index(drop=True)
    ):
        fail("PassengerId de gender_submission.csv não está alinhado ao test.csv")
    if not sample["Survived"].isin([0, 1]).all():
        fail(
            "gender_submission.csv contém valores de Survived "
            "diferentes de 0 e 1"
        )

    print("[OK] Dados brutos localizados e estrutura validada")
    print(f"[OK] train.csv: {len(train)} linhas x {train.shape[1]} colunas")
    print(f"[OK] test.csv: {len(test)} linhas x {test.shape[1]} colunas")
    return train, test


def validate_submission(path: Path, test: pd.DataFrame, root: Path) -> None:
    relative_path = path.relative_to(root)

    if not path.is_file():
        fail(f"Arquivo de submissão ausente: {relative_path}")

    submission = read_csv(path, root)

    if submission.columns.tolist() != SUBMISSION_COLUMNS:
        fail(
            f"{relative_path} deve conter exatamente as colunas "
            "PassengerId e Survived, nessa ordem"
        )
    if len(submission) != len(test):
        fail(
            f"{relative_path} deve conter {len(test)} linhas, "
            f"mas contém {len(submission)}"
        )
    if submission.isna().any().any():
        fail(f"{relative_path} contém valores ausentes")
    if submission["PassengerId"].duplicated().any():
        fail(f"{relative_path} contém PassengerId duplicado")
    if not submission["PassengerId"].reset_index(drop=True).equals(
        test["PassengerId"].reset_index(drop=True)
    ):
        fail(f"PassengerId de {relative_path} não está alinhado ao test.csv")
    if not submission["Survived"].isin([0, 1]).all():
        fail(f"{relative_path} contém valores de Survived diferentes de 0 e 1")

    print(
        f"[OK] {relative_path}: {len(submission)} linhas, "
        "colunas e valores válidos"
    )


def validate_figure(path: Path, root: Path) -> None:
    relative_path = path.relative_to(root)

    if not path.is_file():
        fail(f"Figura ausente: {relative_path}")
    if path.stat().st_size == 0:
        fail(f"Figura vazia: {relative_path}")

    print(f"[OK] {relative_path}: arquivo não vazio")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    _, test = validate_raw_data(root)

    submission_dir = root / "outputs" / "submission"
    for filename in SUBMISSION_FILENAMES:
        validate_submission(submission_dir / filename, test, root)

    figures_dir = root / "outputs" / "figures"
    for filename in FIGURE_FILENAMES:
        validate_figure(figures_dir / filename, root)

    print("[OK] Projeto validado com sucesso")


if __name__ == "__main__":
    main()
