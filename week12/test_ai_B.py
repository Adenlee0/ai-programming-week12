import pytest

from load_scores import load_scores


def test_헤더를_건너뛰고_쉼표가_포함된_이름을_읽는다(tmp_path):
  path = tmp_path / "scores.csv"
  path.write_text('이름,점수\n"홍,길동",85\n', encoding="utf-8")

  kept, skipped = load_scores(path)

  assert kept == [("홍,길동", 85)]
  assert skipped == []


def test_헤더만_있는_파일은_빈_결과를_반환한다(tmp_path):
  path = tmp_path / "header_only.csv"
  path.write_text("이름,점수\n", encoding="utf-8")

  assert load_scores(path) == ([], [])


def test_빈_파일은_빈_결과를_반환한다(tmp_path):
  path = tmp_path / "empty.csv"
  path.write_text("", encoding="utf-8")

  assert load_scores(path) == ([], [])


def test_없는_파일이면_FileNotFoundError를_발생시킨다(tmp_path):
  with pytest.raises(FileNotFoundError):
    load_scores(tmp_path / "missing.csv")


@pytest.mark.parametrize(
  "score, expected_valid",
  [(-1, False), (0, True), (1, True), (99, True), (100, True), (101, False)],
)
def test_점수_범위의_경계값(score, expected_valid, tmp_path):
  path = tmp_path / "boundary.csv"
  path.write_text(f"이름,점수\n홍길동,{score}\n", encoding="utf-8")

  kept, skipped = load_scores(path)

  if expected_valid:
    assert kept == [("홍길동", score)]
    assert skipped == []
  else:
    assert kept == []
    assert len(skipped) == 1
    assert skipped[0][0] == 2
    assert skipped[0][1] == f"홍길동,{score}"
    assert skipped[0][2]


def test_잘못된_행은_줄번호와_사유를_기록하고_계속_읽는다(tmp_path):
  path = tmp_path / "invalid.csv"
  path.write_text(
    "이름,점수\n"
    "정상,80\n"
    "이름만\n"
    "이름,\n"
    "문자,abc\n"
    ",90\n"
    "정상2,100\n",
    encoding="utf-8",
  )

  kept, skipped = load_scores(path)

  assert kept == [("정상", 80), ("정상2", 100)]
  assert [item[0] for item in skipped] == [3, 4, 5, 6]
  assert all(item[1] and item[2] for item in skipped)


def test_중복_이름은_건너뛰고_기록한다(tmp_path):
  path = tmp_path / "duplicates.csv"
  path.write_text("이름,점수\n홍길동,80\n홍길동,90\n", encoding="utf-8")

  kept, skipped = load_scores(path)

  assert kept == [("홍길동", 80)]
  assert len(skipped) == 1
  assert skipped[0][0] == 3
  assert skipped[0][1] == "홍길동,90"
  assert skipped[0][2]

