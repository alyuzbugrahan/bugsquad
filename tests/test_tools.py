from bugsquad import tools
from bugsquad.tools import list_files, read_file, run_tests, edit_file




def test_read_file_return_content(tmp_path):
    (tmp_path / "hello.py").write_text("print('hi')", encoding = "utf-8")

    assert read_file(tmp_path, "hello.py") == "print('hi')"


def test_read_file_missing_file_returns_error(tmp_path):
    result = read_file(tmp_path, "missing.py")

    assert result.startswith("ERROR: File not found")


def test_file_blocks_path_outside_workspace(tmp_path):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (tmp_path / "secret.py").write_text("API_KEY=do-not-leak", encoding="utf-8")

    result = read_file(workspace, "../secret.py")

    assert result.startswith("ERROR: Path is outside the workspace")
    assert "do-not-leak" not in result


def test_list_files_includes_nested_files(tmp_path):
    (tmp_path / "main.py").touch()
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.py").touch()

    result = list_files(tmp_path)

    assert result.splitlines() == ["main.py", "src/app.py"]


def test_list_files_ignores_cache_dirs(tmp_path):
    (tmp_path / "app.py").touch()
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "__pycache__" / "app.cpython-313.pyc").touch()

    result = list_files(tmp_path)

    assert result.splitlines() == ["app.py"]


def test_list_files_empty_workspace_returns_message(tmp_path):
    result = list_files(tmp_path)

    assert result == "(workspace is empty)"


def test_run_tests_reports_passed(tmp_path):
    (tmp_path / "test_ok.py").write_text(
        "def test_ok():\n  assert 1 + 1 == 2\n", encoding="utf-8" 
    )

    result = run_tests(tmp_path)

    assert result.startswith("STATUS: PASSED")
    assert "1 passed" in result


def test_run_tests_reports_failed(tmp_path):
    (tmp_path / "test_bad.py").write_text(
        "def test_bad():\n  assert 1 + 1 == 3\n", encoding="utf-8"
    )

    result = run_tests(tmp_path)

    assert result.startswith("STATUS: FAILED")
    assert "1 failed" in result


def test_run_tests_stops_infinite_loop(tmp_path, monkeypatch):
    monkeypatch.setattr(tools, "TEST_TIMEOUT_SECONDS", 1)
    (tmp_path / "test_loop.py").write_text(
        "def test_loop():\n  while True:\n    pass\n", encoding = "utf-8"    
    )

    result = run_tests(tmp_path)

    assert result.startswith("ERROR: Tests did not finish")


# ---------- edit_file ----------

def test_edit_file_replaces_text(tmp_path):
    (tmp_path / "calc.py").write_text("x = 1\n", encoding="utf-8")

    result = edit_file(tmp_path, "calc.py", "x = 1", "x = 2")

    assert result.startswith("OK")
    assert (tmp_path / "calc.py").read_text(encoding="utf-8") == "x = 2\n"


def test_edit_file_refuses_test_files(tmp_path):
    original = "assert x == 6\n"
    (tmp_path / "test_calc.py").write_text(original, encoding="utf-8")

    result = edit_file(tmp_path, "test_calc.py", "== 6", "== 3")

    assert result.startswith("ERROR: Test files are read-only")
    assert (tmp_path / "test_calc.py").read_text(encoding="utf-8") == original


def test_edit_file_text_not_found(tmp_path):
    original = "x = 1\n"
    (tmp_path / "calc.py").write_text(original, encoding="utf-8")

    result = edit_file(tmp_path, "calc.py", "y = 5", "y = 6")

    assert result.startswith("ERROR: old_text was not found")
    assert (tmp_path / "calc.py").read_text(encoding="utf-8") == original


def test_edit_file_ambiguous_match(tmp_path):
    original = "x = 1\nx = 1\n"
    (tmp_path / "calc.py").write_text(original, encoding="utf-8")

    result = edit_file(tmp_path, "calc.py", "x = 1", "x = 2")

    assert "appears 2 times" in result
    assert (tmp_path / "calc.py").read_text(encoding="utf-8") == original


def test_edit_file_blocks_path_outside_workspace(tmp_path):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    original = "API_KEY=do-not-touch\n"
    (tmp_path / "secret.py").write_text(original, encoding="utf-8")

    result = edit_file(workspace, "../secret.py", "do-not-touch", "hacked")

    assert result.startswith("ERROR: Path is outside the workspace")
    assert (tmp_path / "secret.py").read_text(encoding="utf-8") == original


def test_edit_file_rejects_empty_old_text(tmp_path):
    original = "x = 1\n"
    (tmp_path / "calc.py").write_text(original, encoding="utf-8")

    result = edit_file(tmp_path, "calc.py", "", "y = 2")

    assert result.startswith("ERROR: old_text must not be empty")
    assert (tmp_path / "calc.py").read_text(encoding="utf-8") == original
    
    
