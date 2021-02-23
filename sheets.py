import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pip._vendor.distlib.compat import raw_input
import datetime

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("test").sheet1

data = sheet.get_all_records()


def fillData():
    cell_list = sheet.range('A2:A21')
    cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i, val in enumerate(cell_values):  # gives us a tuple of an index and value
        cell_list[i].value = val  # use the index on cell_list and the val from cell_values

    sheet.update_cells(cell_list)

def addItems():
    new_value = input("type the new ID: ")
    sheet.update_cell(2, 1, new_value)  # Update one cell


def duplicates():
    val = sheet.range('A2:A21')

    x = input("Type the new ID: ")

    for x in val:
        if x in val:
            sheet.update_cell(2, 1, x)
            sheet.update_cell(2, 7, datetime)
        else:
            break




fillData() #function to fill data in google

addItems() #function to add new IDs in google

duplicates() #function to search duplicates and add date and time