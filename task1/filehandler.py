def file_handling():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_file, "w") as file:
            file.write(f"Word count: {word_count}")

        print(f"Word count ({word_count}) written to {output_file}.")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")

file_handling()
