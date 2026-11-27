import pytest

from load_scores import load_scores


def test_정상적인_csv와_bom_공백_중복_이름을_읽는다(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "\ufeff이름,점수\n홍길동, 85 \n 홍길동 ,0\n김영희,100\n\n",
        encoding="utf-8",
    )

    kept, skipped = load_scores(path)

    assert kept == [("홍길동", 85), ("홍길동", 0), ("김영희", 100)]
    assert skipped == []


def test_헤더만_있는_csv는_빈_결과를_반환한다(tmp_path):
    path = tmp_path / "header_only.csv"
    path.write_text("이름,점수\n", encoding="utf-8")

    assert load_scores(path) == ([], [])


def test_빈_줄은_건너뛴_기록에_포함하지_않는다(tmp_path):
    path = tmp_path / "blank_lines.csv"
    path.write_text("이름,점수\n\n홍길동,80\n\n", encoding="utf-8")

    kept, skipped = load_scores(path)

    assert kept == [("홍길동", 80)]
    assert skipped == []


def test_없는_파일이면_FileNotFoundError를_그대로_발생시킨다(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "missing.csv")


@pytest.mark.parametrize(
    "score, expected_kept",
    [
        (-1, False),
        (0, True),
        (1, True),
        (99, True),
        (100, True),
        (101, False),
    ],
)
def test_점수_범위의_경계값(score, expected_kept, tmp_path):
    path = tmp_path / "boundary.csv"
    path.write_text(f"이름,점수\n홍길동,{score}\n", encoding="utf-8")

    kept, skipped = load_scores(path)

    assert (len(kept) == 1) is expected_kept
    assert (len(skipped) == 1) is not expected_kept
    if expected_kept:
        assert kept == [("홍길동", score)]
    else:
        assert skipped == [(2, f"홍길동,{score}", "점수가 0~100 밖")]


def test_잘못된_행은_정확한_줄번호_원본과_사유로_기록한다(tmp_path):
    path = tmp_path / "invalid_rows.csv"
    path.write_text(
        "이름,점수\n"
        "정상,80\n"
        "열이하나\n"
        "열,개수,초과\n"
        ",90\n"
        "이름,   \n"
        "문자,abc\n"
        "하한미만,-1\n"
        "상한초과,101\n",
        encoding="utf-8",
    )

    kept, skipped = load_scores(path)

    assert kept == [("정상", 80)]
    assert skipped == [
        (3, "열이하나", "열 개수가 2가 아님"),
        (4, "열,개수,초과", "열 개수가 2가 아님"),
        (5, ",90", "이름이 비어 있음"),
        (6, "이름,   ", "점수가 비어 있음"),
        (7, "문자,abc", "점수가 정수가 아님"),
        (8, "하한미만,-1", "점수가 0~100 밖"),
        (9, "상한초과,101", "점수가 0~100 밖"),
    ]
