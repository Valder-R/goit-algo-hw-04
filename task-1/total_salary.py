def total_salary(path):
    try:
        with open(path, "r", encoding = "utf-8") as file:
            lines = [el.strip() for el in file.readlines()]
            total = 0
            for line in lines :
                name, salary = line.split(",")
                total += int(salary)
            return total, total//len(lines)

    except Exception as e:
        print(f"{e} with file")


def main():
    salary_total, salary_average = total_salary("task-1/workers.txt")
    print(f"Загальна сума заробітної плати: {salary_total}, Середня заробітна плата: {salary_average}")


if __name__ == "__main__":
    main()