from path import Path


def create_dir_write_file():
    try:
        Path.makedirs('test')
    except FileExistsError as e:
        print(e)
    Path.touch('test/my_file')
    f = Path('test/my_file')
    f.write_text("Un po’ di Italia nella sua tazza!")
    print(f.read_text())


if __name__ == '__main__':
    create_dir_write_file()