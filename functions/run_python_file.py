import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if valid_target_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args:
            command.extend(args)
        helper = subprocess.run(
            command,
            capture_output=True,
            cwd=working_dir_abs,
            text=True,
            timeout=30,
        )

        return_string = ""

        if helper.returncode != 0:
            return_string += f"Process exited with code {helper.returncode}"
        if not helper.stdout and not helper.stderr:
            return_string += "No output produced"
        if helper.stdout:
            return_string += f"STDOUT:\n{helper.stdout}"
        if helper.stderr:
            return_string += f"STDERR:\n{helper.stderr}"
        return return_string
    except Exception as e:
        return f"Error: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file with a given prompt, or a given directory, or a given filepath",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="arguments that are passed to determine what's to be executed",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
