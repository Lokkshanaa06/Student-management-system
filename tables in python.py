'''
from tabulate import tabulate

data = [["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]]

table = tabulate(data, headers="firstrow", tablefmt="grid")
print(table)

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "Los Angeles"])
table.add_row(["Charlie", 35, "Chicago"])

print(table)
'''

import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"],
        "Age": [30, 25, 35],
        "City": ["New York", "Los Angeles", "Chicago"]}

df = pd.DataFrame(data)
print(df)
