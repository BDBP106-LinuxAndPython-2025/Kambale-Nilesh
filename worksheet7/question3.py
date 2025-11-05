# (3) Create a base class, CDataProcessor with two properties - samples and features - and
# a method PrintDatasetInfo(). The two properties are initialized using the number of
# rows and columns of a Pandas dataframe that is passed to the constructor during object
# creation. The PrintDatasetInfo() method should print the number of samples and
# features.
# Derive a new class, CCSVProcessor from the CDataProcessor class. This derived
# class should have two properties - filename and dfData - The filename is initialized
# to path of the CSV file specified during object creation. The dfData is initialized to
# empty dataframe. The CCSVProcessor class should contain two methods - LoadData()
# and ConvertToJSON() - LoadData should load the CSV data into a dfData property of
# this class (use Pandas read csv method). It should also invoke its parent class __init__method passing the dfData, so that, parent’s samples and features are populated cor-
# rectly. ConvertToJSON() should create a new JSON file using the dfData (use Pandas
# to json method)
# a. Create an instance object of CCSVProcessor using the file titanic.csv. Load the
# data and invoke PrintDatasetInfo() to print the number of samples and features
# in this dataset.
# b. Create an object of CCSVProcessor using the file ODI-Batting_Cricket_Analytics.csv.
# This file is copied in my Google drive code folder. Load the data and invoke
# ConvertToJSON() method to create a new ODI-Batting_Cricket_Analytics.JSON file.
# c. Create an object of CJSONProcessor(), load the data and invoke PrintDatasetInfo()
# to print the number of features and columns of this dataset.

# from DATAprocessor import CCSVProcessor, CJSONProcessor
#
# # a. CCSVProcessor with titanic.csv
# csv1 = CCSVProcessor("titanic.csv")
# csv1.LoadData()
# csv1.PrintDataInfo()
#
# # b. CCSVProcessor with ODI-Batting_Cricket_Analytics.csv
# csv2 = CCSVProcessor("ODI-Batting_Cricket_Analytics.csv")
# csv2.LoadData()
# csv2.ConvertToJson("ODI-Batting_Cricket_Analytics.json")

# # c. CJSONProcessor demo
# json_proc = CJSONProcessor("ODI-Batting_Cricket_Analytics.json")
# json_proc.LoadData()
# json_proc.PrintDataInfo()

from DATAprocessor import CCSVProcessor, CJSONProcessor

# a. CCSVProcessor with titanic.csv
csv1 = CCSVProcessor("titanic.csv")
csv1.LoadData()
csv1.PrintDataInfo()

# b. CCSVProcessor with ODI-Batting_Cricket_Analytics.csv
csv2 = CCSVProcessor("ODI-Batting_Cricket_Analytics.csv")
csv2.LoadData()
csv2.ConvertToJson("ODI-Batting_Cricket_Analytics.json")

# c. CJSONProcessor demo
json_proc = CJSONProcessor("ODI-Batting_Cricket_Analytics.json")
json_proc.LoadData()
json_proc.PrintDataInfo()
