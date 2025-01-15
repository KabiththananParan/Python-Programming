from zipfile import ZipFile

zipFile_loc = "recipe-page-main.zip"

with ZipFile(zipFile_loc, 'r') as zip_object:
    zip_object.extractall()


# List of files are archived in the zip file

print(zip_object.namelist())

