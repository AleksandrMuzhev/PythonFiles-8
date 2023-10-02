import os

folder = os.path.join(os.getcwd(), "taskThree")

files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


def count_lines(file_path):
    with open(file_path, encoding="utf-8") as file:
        return sum(1 for line in file)


sorted_files = sorted(files, key=lambda x: count_lines(os.path.join(folder, x)))

result_file = os.path.join(folder, "result.txt")

with open(result_file, "w", encoding="utf-8") as result:
    for file_name in sorted_files:
        file_path = os.path.join(folder, file_name)
        lines_count = count_lines(file_path)
        if lines_count > 0:
            result.write(f"{file_name}\n{lines_count}\n")
        with open(file_path, encoding="utf-8") as file:
            result.write(file.read())
        result.write("\n")

print("Обновление файлов завершено.")

with open(result_file, "r", encoding="utf-8") as xs:
    xs.read()
