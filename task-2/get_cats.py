def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]
            cats = list()
            for line in lines :
                id, name, age = line.split(",")
                cats.append({"id": id, "name": name, "age": age })
            return cats

    except Exception as e:
        print(f"{e} with file")


def main():
    cats_info = get_cats_info("task-2/cats.txt")
    print(cats_info)


if __name__ == "__main__":
    main()