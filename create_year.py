import sys
from main import create_template_folder

def progress_bar(current, total, bar_length=30):
    fraction = current / total

    bar = int(fraction * bar_length) * '#'
    padding = int(bar_length - len(bar)) * '.'

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{bar}{padding}] {int(fraction*100)}%\t({current}/{total})', end=ending)

if len(sys.argv) == 3:
    year, days = sys.argv[1:]
else:
    year = input("Input the year you want to generate folders for: ")
    days = input("Input the day range you want to generate folders for (separated by a '-' e.g. 5-23): ")


year = int(year)
interval_begin, interval_end = [int(i) for i in days.split('-')]
length_interval = interval_end - interval_begin+1

for day in range(interval_begin, interval_end+1):
    progress_bar(day-interval_begin+1, length_interval, length_interval)
    create_template_folder(year, day)