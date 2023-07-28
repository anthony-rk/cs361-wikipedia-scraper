import time


def main():
    # Write the request over
    print("Writing 'request' to rng_pipe.txt")
    write_to_txt_file("rng_pipe.txt", "request")

    while check_txt_file_contents("rng_pipe.txt", "request") or check_txt_file_contents("rng_pipe.txt", ""):
        print("Waiting 1 second before checking the pipe...")
        time.sleep(1)

    pipe_contents = read_from_txt_file("rng_pipe.txt")
    rng_num = int(pipe_contents)

    # Now you can use rng_num for your service!
    print(f"Received {rng_num} from the rng_pipe.txt file")
    print("Goodbye!")


def check_txt_file_contents(file_path, str_to_check):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

            if file_content.strip() == str_to_check:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False


def write_to_txt_file(file_path, str_to_write):
    try:
        with open(file_path, 'w') as file:
            file.write(str_to_write)
        print("File written successfully.")
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")


def read_from_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
