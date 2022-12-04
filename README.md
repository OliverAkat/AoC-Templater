# AoC-Templater

## Usage
To create a folder structure for the current year and day
```bash
$ python main.py
```

To create a folder structure for any year and any interval of days
```bash
$ python create_year.py [year] [days (start-end)]
```

## Folder structure
       [year]/        		Files and folders pertaining to the year
	   └─ day[day]/        		All the files pertaining to the day
	      ├─ day[day].py		The file you will write your soulutions in 
	      ├─ input			The file with the input data
	      └─ sample			Optional file where you can put any sample input

Change template.py to your liking :)
