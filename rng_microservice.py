import random
import time
from datetime import datetime


def main():
    while True:
        # Check if the microservice was called, handle if necessary
        if check_txt_file_contents("rng_pipe.txt", "request"):
            # Get a RNG
            print("Generating a random number...")
            num = rng_generator()

            # write the rng over
            write_to_txt_file("rng_pipe.txt", str(num))
        else:
            print("Waiting 1 second before checking the pipe again...")
            time.sleep(1)


def rng_generator():
    """Returns a psuedo random number between 1-5. uses the current datetime to ensure it is random on each call"""
    current_time = datetime.now()
    seed = int(current_time.timestamp())
    random.seed(seed)
    return random.randrange(1, 6, 1)


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


if __name__ == "__main__":
    main()