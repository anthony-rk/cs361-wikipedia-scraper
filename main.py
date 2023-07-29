from selenium import webdriver
from selenium.webdriver.common.by import By

import random
from datetime import datetime


def main():
    print("------------------------------------------------------------------------")
    print("------------------------------------------------------------------------")
    print("Welcome to the Wiki from the command line program!\n")

    print("This program will allow you to enter a wiki topic to receive the response in your terminal.\n")

    response = input("Enter 1 if you would like see an example of the program in action, anything else will continue to the main program: ")

    if response == "1":
        show_example()

    while True:
        response = get_input_from_user()

        if response == "exit" or response == "q":
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print("Thanks for using the program, goodbye!\n")
            exit()

        url = "https://en.wikipedia.org/wiki/" + response

        # Example of calling the driver on your local machine:
            # driver = webdriver.Chrome('/Users/MyUsername/Downloads/chromedriver')

        driver = webdriver.Chrome()
        driver.get(url)

        # Check if the page exists
        if check_wiki_page_exists(driver.page_source):
            title_element = driver.find_elements(By.CLASS_NAME, "mw-page-title-main")

            # Print the Wiki Title
            print("\nThe Wiki contents for " + response + " are as follows:")

            divs_for_p_tags = driver.find_elements(By.CLASS_NAME, "mw-parser-output")

            # Some wikis have multiple mw-parser-output class divs, the last one is the one that has the paragraph data
            elements = divs_for_p_tags[-1].find_elements(By.TAG_NAME, 'p')

            # Print the Wiki paragraphs
            for e in elements:
                print(e.text)
                print("\n")

            driver.quit()
        else:
            # Display error message for invalid input
            print("Invalid input. Please try again.")


def get_input_from_user():
    print("Type exit or q to quit to program, otherwise follow the next prompt to use the program.")
    wiki_topic = input("Please enter the wiki page you would like to see: ")

    # convert multiple words to wiki style. "Tom Hanks" would become "tom_hanks"
    converted_wiki_topic = wiki_topic.lower().replace(" ", "_")

    # return "https://en.wikipedia.org/wiki/" + converted_wiki_topic
    return converted_wiki_topic


def check_wiki_page_exists(page_source):
    # Check if the page exists
    if "Wikipedia does not have an article with this exact name." in page_source:
        return False
    return True


def show_example():
    url = "https://en.wikipedia.org/wiki/tom_hanks"

    driver = webdriver.Chrome()
    driver.get(url)

    title_element = driver.find_elements(By.CLASS_NAME, "mw-page-title-main")

    # Print the Wiki Title
    # print(title_element.text)

    divs_for_p_tags = driver.find_elements(By.CLASS_NAME, "mw-parser-output")

    # Some wikis have multiple mw-parser-output class divs, the last one is the one that has the paragraph data
    elements = divs_for_p_tags[-1].find_elements(By.TAG_NAME, 'p')

    # Print the Wiki paragraphs
    for e in elements:
        print(e.text)
        print("\n")

    driver.quit()


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

