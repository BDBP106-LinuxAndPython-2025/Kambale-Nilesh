# import pandas as pd
#
#
# class CDataProcessor:
#     def __init__(self, df):
#         self.sample = df.shape[0]
#         self.features = df.shape[1]
#
#     def PrintDataInfo(self):
#         print("Sample(Rows):", self.sample)
#         print("features(columns):", self.features)
#
# class CCSVProcessor(CDataProcessor):
#     def __init__(self, filename):
#         self.filename = filename
#         self.dfData =pd.DataFrame()
#
#     def LoadData(self):
#         self.dfData = pd.read_csv(self.filename)
#         super().__init__(self.dfData)
#         print(f'file name from data loaded : {self.filename}')
#
#     def ConvertToJson(self,json_file=None):
#         if json_file is None:
#             json_file = self.filename.replace('.csv','.json')
#         self.dfData.to_json(json_file,orient='records',indent=4)
#         print(f'json file converted to json file : {json_file}')
#
# class CJSONProcessor(CDataProcessor):
#     def __init__(self, filename):
#         self.filename = filename
#         self.dfData =pd.DataFrame()
#
#     def LoadData(self):
#         self.dfData = pd.read_json(self.filename)
#         super().__init__(self.dfData)
#         print(f'file name from data loaded : {self.filename}')


import pandas as pd

# Base class
class CDataProcessor:
    def __init__(self, df):
        self.samples = df.shape[0]
        self.features = df.shape[1]

    def PrintDataInfo(self):
        print(f"Samples (Rows): {self.samples}")
        print(f"Features (Columns): {self.features}")

# CSV Processor
class CCSVProcessor(CDataProcessor):
    def __init__(self, filename):
        self.filename = filename
        self.dfData = pd.DataFrame()  # initially empty

    def LoadData(self):
        self.dfData = pd.read_csv(self.filename)
        super().__init__(self.dfData)  # parent initialized with actual data
        print(f"CSV file loaded: {self.filename}")

    def ConvertToJson(self, json_file=None):
        if json_file is None:
            json_file = self.filename.replace('.csv', '.json')
        self.dfData.to_json(json_file, orient='records', indent=4)
        print(f"CSV converted to JSON: {json_file}")

# JSON Processor
class CJSONProcessor(CDataProcessor):
    def __init__(self, filename):
        self.filename = filename
        self.dfData = pd.DataFrame()  # initially empty

    def LoadData(self):
        self.dfData = pd.read_json(self.filename)
        super().__init__(self.dfData)  # parent initialized with actual data
        print(f"JSON file loaded: {self.filename}")








