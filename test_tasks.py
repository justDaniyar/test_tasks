import pandas as pd
from datetime import datetime as dt
from pymongo import MongoClient
from pyexcelerate import Workbook, Style, Format, Color
import json

data = {"id": [1, 
               2, 
               3, 
               4, 
               5, 
               6, 
               7],
        "name": ["Alex", 
                 "Justin", 
                 "Set", 
                 "Carlos", 
                 "Gareth", 
                 "John", 
                 "Bob"],
        "surname": ["Smur", 
                    "Forman", 
                    "Carey", 
                    "Carey", 
                    "Chapman", 
                    "James", 
                    "James"],
        "age": [21, 
                25, 
                35, 
                40, 
                19, 
                27, 
                25],
        "job": ["Python Developer", 
                "Java Developer", 
                "Project Manager", 
                "Enterprise Architect", 
                "Python Developer", 
                "IOS Developer", 
                "Python Developer"],
        "datetime": pd.to_datetime(["2022-01-01T09:45:12", 
                                    "2022-01-01T11:50:25", 
                                    "2022-01-01T10:00:45",
                                    "2022-01-01T09:07:36", 
                                    "2022-01-01T11:54:10", 
                                    "2022-01-01T09:56:40", 
                                    "2022-01-01T09:52:45"],
                                    format="%Y-%m-%dT%H:%M:%S")
       }

df = pd.DataFrame(data)

client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
database = client["test_task"]

def task_1():
    """
    Performs the first task
    """
    df_copy = df.copy()

    is_developer = df_copy["job"].str.contains("Developer")
    is_age_between_18_and_21 = ((df_copy["age"] > 18) 
                                & (df_copy["age"] <= 21))
    df_copy.loc[(is_developer & is_age_between_18_and_21), 
                "time_to_enter"] = dt.strptime("09:00:00", 
                                               "%H:%M:%S").time()
    df_copy.loc[~(is_developer & is_age_between_18_and_21), 
                "time_to_enter"] = dt.strptime("09:15:00",
                                               "%H:%M:%S").time()

    data = [df_copy.columns] + list(df_copy.values)

    workbook = Workbook()
    worksheet = workbook.new_sheet(sheet_name="task_1",
                                   data=data)
    worksheet.set_col_style(6, 
                            Style(format=Format("yyyy-mm-dd hh:mm:ss")))
    worksheet.set_col_style(7, 
                            Style(format=Format("hh:mm:ss")))
    workbook.save("task_1.xlsx")

    collection = database["18MoreAnd21andLess"]
    records = json.loads(df_copy.T.to_json(date_format="iso")).values()
    collection.insert_many(records)


def task_2():
    """
    Performs the second task
    """
    df_copy = df.copy()

    is_not_manager_or_developer = ~df_copy["job"].str.contains(pat="Developer|Manager",
                                                               regex=True)
    is_age_more_or_equal_than_35 = df_copy["age"] >= 35
    df_copy.loc[(is_not_manager_or_developer
                 & is_age_more_or_equal_than_35), 
                "time_to_enter"] = dt.strptime("11:00:00",
                                               "%H:%M:%S").time()
    df_copy.loc[~(is_not_manager_or_developer
                  & is_age_more_or_equal_than_35), 
                "time_to_enter"] = dt.strptime("09:30:00",
                                               "%H:%M:%S").time()

    data = [df_copy.columns] + list(df_copy.values)
    workbook = Workbook()
    worksheet = workbook.new_sheet(sheet_name="task_2",
                                   data=data)
    worksheet.set_col_style(6,
                            Style(format=Format("yyyy-mm-dd hh:mm:ss")))
    worksheet.set_col_style(7,
                            Style(format=Format("hh:mm:ss")))
    workbook.save("task_2.xlsx")

    collection = database["35AndMore"]
    records = json.loads(df_copy.T.to_json(date_format="iso")).values()
    collection.insert_many(records)


def task_3():
    """
    Performs the third task
    """
    df_copy = df.copy()

    is_architect = df_copy["job"].str.contains("Architect")
    df_copy.loc[is_architect, 
                "time_to_enter"] = dt.strptime("10:30:00",
                                               "%H:%M:%S").time()
    df_copy.loc[~is_architect,
                "time_to_enter"] = dt.strptime("09:10:00",
                                               "%H:%M:%S").time()

    data = [df_copy.columns] + list(df_copy.values)
    workbook = Workbook()
    worksheet = workbook.new_sheet(sheet_name="task_3",
                                   data=data)
    worksheet.set_col_style(6,
                            Style(format=Format("yyyy-mm-dd hh:mm:ss")))
    worksheet.set_col_style(7,
                            Style(format=Format("hh:mm:ss")))
    workbook.save("task_3.xlsx")

    collection = database["ArchitectEnterTime"]
    records = json.loads(df_copy.T.to_json(date_format="iso")).values()
    collection.insert_many(records)

task_1()
task_2()
task_3()
    

