"""Starter tests for Week 9 Homework.

Run with:

    pytest -q

These tests are a starter set. You must add at least one meaningful test of
your own before submitting.
"""

from src.challenges import analyze_lanterns


def test_analyze_lanterns_full_starter_data():
    expected_lanterns = {
        "river-dragon",
        "blue-crane",
        "moon-rabbit",
        "gold-tiger",
        "white-lotus",
        "red-kite",
    }

    lantern_log = [
        ("river-dragon", "North Gate"),
        ("blue-crane", "River Walk"),
        ("moon-rabbit", "River Walk"),
        ("river-dragon", "North Gate"),
        ("gold-tiger", "Market Street"),
        ("silver-fox", "Market Street"),
        ("red-kite", "South Bridge"),
    ]

    correct_sections = {
        "river-dragon": "North Gate",
        "blue-crane": "River Walk",
        "moon-rabbit": "River Walk",
        "gold-tiger": "Market Street",
        "white-lotus": "Temple Road",
        "red-kite": "Temple Road",
    }

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["seen_lanterns"] == {
        "river-dragon",
        "blue-crane",
        "moon-rabbit",
        "gold-tiger",
        "silver-fox",
        "red-kite",
    }
    assert result["missing_lanterns"] == {"white-lotus"}
    assert result["unexpected_lanterns"] == {"silver-fox"}
    assert result["duplicate_lanterns"] == {"river-dragon"}
    assert result["count_by_section"] == {
        "North Gate": 2,
        "River Walk": 2,
        "Market Street": 2,
        "South Bridge": 1,
    }
    assert result["wrong_section_lanterns"] == {
        "red-kite": {
            "expected": "Temple Road",
            "actual": "South Bridge",
        }
    }


def test_analyze_lanterns_empty_input():
    result = analyze_lanterns(set(), [], {})

    assert result["seen_lanterns"] == set()
    assert result["missing_lanterns"] == set()
    assert result["unexpected_lanterns"] == set()
    assert result["duplicate_lanterns"] == set()
    assert result["count_by_section"] == {}
    assert result["wrong_section_lanterns"] == {}


def test_analyze_lanterns_detects_duplicate_lanterns():
    expected_lanterns = {"moon-rabbit"}
    lantern_log = [
        ("moon-rabbit", "River Walk"),
        ("moon-rabbit", "River Walk"),
    ]
    correct_sections = {"moon-rabbit": "River Walk"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["duplicate_lanterns"] == {"moon-rabbit"}


def test_analyze_lanterns_detects_wrong_section():
    expected_lanterns = {"red-kite"}
    lantern_log = [
        ("red-kite", "South Bridge"),
    ]
    correct_sections = {"red-kite": "Temple Road"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["wrong_section_lanterns"] == {
        "red-kite": {
            "expected": "Temple Road",
            "actual": "South Bridge",
        }
    }


def test_analyze_lanterns_ignores_unexpected_lantern_for_wrong_section():
    expected_lanterns = {"red-kite"}
    lantern_log = [
        ("silver-fox", "Market Street"),
    ]
    correct_sections = {"red-kite": "Temple Road"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["unexpected_lanterns"] == {"silver-fox"}
    assert result["wrong_section_lanterns"] == {}


def test_analyze_lanterns_log_empty_but_expected_lanterns_exist():
    expected_lanterns = {"river-dragon", "blue-crane"}
    lantern_log = []
    correct_sections = {
        "river-dragon": "North Gate",
        "blue-crane": "River Walk",
    }

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["seen_lanterns"] == set()
    assert result["missing_lanterns"] == {"river-dragon", "blue-crane"}
    assert result["unexpected_lanterns"] == set()
    assert result["duplicate_lanterns"] == set()
    assert result["count_by_section"] == {}
    assert result["wrong_section_lanterns"] == {}


def test_analyze_lanterns_expected_lantern_correct_then_wrong_section():
    expected_lanterns = {"gold-tiger"}
    lantern_log = [
        ("gold-tiger", "Market Street"),
        ("gold-tiger", "River Walk"),
    ]
    correct_sections = {"gold-tiger": "Market Street"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["seen_lanterns"] == {"gold-tiger"}
    assert result["missing_lanterns"] == set()
    assert result["unexpected_lanterns"] == set()
    assert result["duplicate_lanterns"] == {"gold-tiger"}
    assert result["count_by_section"] == {
        "Market Street": 1,
        "River Walk": 1,
    }
    assert result["wrong_section_lanterns"] == {
        "gold-tiger": {
            "expected": "Market Street",
            "actual": "River Walk",
        }
    }
