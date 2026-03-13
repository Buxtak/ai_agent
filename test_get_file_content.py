from functions.get_file_content import get_file_content

print("Test for lorem.txt")
print(get_file_content("calculator", "lorem.txt"))

print("Test for main.py")
print(get_file_content("calculator", "main.py"))

print("Test for pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Test for /bin/cat")
print(get_file_content("calculator", "/bin/cat"))

print("Test for pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
