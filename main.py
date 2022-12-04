import requests
import os
import datetime

session_header = 'YOUR_SESSION_COOKIE'

# Change windows folder separators to windows
current_wd = os.getcwd().replace('\\', '/')

def create_template_folder(year, day):
    folder_path = f"{current_wd}/{year}"
    file_name = f'day{day}'
    dir_name = f'{folder_path}/{file_name}'

    # Fetches the input file for the day and year
    r = requests.post(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session_header})

    # Creates the year folder if it does not exist
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

    # Creates the day folder if it does not already exist
    if not os.path.isdir(dir_name):
        # Creates the directory
        os.mkdir(dir_name)

        # Creates a template file for the day
        with open(f'{current_wd}/template.py', 'r') as template_file, open(f'{dir_name}/{file_name}.py', 'a') as out_file:
            out_file.write(template_file.read())

        # Creates the input file and writes the puzzle input to it
        with open(f'{dir_name}/input', 'a') as input_file:
            input_file.write(r.text)

        # Creates the file containing sample files
        with open(f'{dir_name}/sample', 'a') as sample_file:
            pass

# Takes the current day and year if the file is run directly
if __name__ == '__main__':
    dy = datetime.datetime.now().day
    yr = datetime.datetime.now().year
    create_template_folder(yr, dy)