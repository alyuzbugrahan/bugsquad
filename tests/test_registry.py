from bugsquad.registry import TOOL_FUNCTIONS, TOOL_SCHEMAS, execute_tool


def test_schemas_match_functions():
    schema_names = {schema["function"]["name"] for schema in TOOL_SCHEMAS}

    assert schema_names == set(TOOL_FUNCTIONS)


def test_execute_tool_runs_requested_tool(tmp_path):
    (tmp_path / "calc.py").write_text("x = 1\n", encoding="utf-8")

    result = execute_tool(tmp_path, "read_file", '{"path": "calc.py"}')

    assert result == "x = 1\n"


def test_execute_tool_accepts_empty_arguments(tmp_path):
    (tmp_path / "calc.py").touch()

    result = execute_tool(tmp_path, "list_files", "")

    assert result == "calc.py"


def test_execute_tool_unknown_tool(tmp_path):
    result = execute_tool(tmp_path, "delete_file", "{}")

    assert result.startswith("ERROR: Unknown tool 'delete_file'")


def test_execute_tool_invalid_json(tmp_path):
    result = execute_tool(tmp_path, "read_file", "{not json")

    assert result.startswith("ERROR: Arguments for 'read_file' are not valid JSON")


def test_execute_tool_arguments_not_an_object(tmp_path):
    result = execute_tool(tmp_path, "read_file", '["calc.py"]')

    assert result.startswith("ERROR: Arguments for 'read_file' must be a JSON object")


def test_execute_tool_wrong_arguments(tmp_path):
    result = execute_tool(tmp_path, "read_file", '{"dosya": "calc.py"}')

    assert result.startswith("ERROR: Wrong arguments for 'read_file'")