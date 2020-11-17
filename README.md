# Populate Firestore
Publish multiple documents with data from an excel file to firestore


# Installation
1. [Clone](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository locally
2. Open a terminal, navigate to the root folder of this repository and run this command to install all packages <br>
  `pip install -r requirements.txt`


# Usage
1. [Generate](https://firebase.google.com/docs/admin/setup#initialize-sdk) a private key file for your [service account](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk) from firebase.
2. Rename the file to 'firebasekey' without the quotes
3. Copy the file the root folder of this repository

## Add Documents to firestore
4. In main.py, on line 54, modify the sheet name to the name of the sheet in your excel workbook. I.e <br>
  `sheet_name = 'sheet1'` <br>
_where 'sheet1' is the name of your sheet_

5. Prepare your data. [Instructions below](https://github.com/Egahi/populate-firestore/blob/main/README.md#preparing-your-data)
6. In main.py, on line 105, modify the file_path to the location of your excel workbook, it's name included in the path. I.e <br>
  `file_path = 'path/inner-path/your_file.xlsx'` <br>
_where 'path/inner-path/your_file.xlsx' is the path to your file_

## Get Documents by state to firestore
4. In main.py, on line 114, modify the state to the name of the state whose documents you want to retrieve. I.e <br>
  `state = u'Jigawa'` <br>
_where 'Jigawa' is the state in question_

## Run code
* Open a terminal, navigate to the root folder of this repository and run this command <br>
  `py main.py`
  
  
# Preparing your data
1. The data **MUST** be structure in a table with cells of same sizes <br>
**Do NOT MERGE ANY CELLS**
2. Each column **MUST** have header
3. Captitalize the first letter of each column header to be consistent with other entries

| State | Location | Latitude | Longitude |
| ----- | -------- | -------- | --------- |
| State1 | Location1 | 0.00 | 0.00 |
| ... | ... | ... | ... |
| State n | Location n | 0.00 | 0.00 |

_ps: You can add other columns at the start or in between but **Latitude and Longitude (in that order) MUST be the last two columns**"_

Just in case you missed it, **UNMERGE AND MERGE CELLS**
