from functions.run_python_file import run_python_file

print("main.py")
print(run_python_file("calculator", "main.py"))

print("Test for main.py, [3 + 5]")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Test for tests.py")
print(run_python_file("calculator", "tests.py"))

print("Test for ../main.py")
print(run_python_file("calculator", "../main.py"))

print("Test for nonexistent.py")
print(run_python_file("calculator", "nonexistent.py"))

print("Test for lorem.txt")
print(run_python_file("calculator", "lorem.txt"))
