from bug3_logic import find_max, count_pass


def test_find_max_returns_largest_middle_and_last_scores():
    assert find_max([70, 85, 60, 95]) == 95


def test_find_max_checks_every_position():
    assert find_max([10, 20, 30]) == 30
    assert find_max([95, 85, 70, 60]) == 95


def test_find_max_handles_negative_scores():
    assert find_max([-5, -10, -1, -8]) == -1


def test_count_pass_includes_default_cutoff_boundary():
    assert count_pass([60, 60, 59]) == 2


def test_count_pass_counts_all_scores_at_or_above_cutoff():
    assert count_pass([70, 85, 95]) == 3


def test_count_pass_supports_custom_cutoff():
    assert count_pass([79, 80, 81], cutoff=80) == 2


def test_count_pass_handles_empty_list():
    assert count_pass([]) == 0
