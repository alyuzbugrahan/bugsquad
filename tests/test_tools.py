from bugsquad.tools import read_file


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

