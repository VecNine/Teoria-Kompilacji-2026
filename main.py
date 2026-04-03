from scanner import Scanner

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = "plik.html"
    try:
        with open(input_file, "r",encoding = "utf-8") as f:
            source_code = f.read()

        scanner = Scanner(source_code)
        scanner.scan()
        scanner.to_html(output_file)
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku o nazwie '{input_file}'.")
        print("Upewnij się, że plik znajduje się w tym samym folderze co skrypt.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")