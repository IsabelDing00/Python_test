from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Students Name", ["Isabel", "Dylan", "Chris"])
table.add_column("Gender", ["F", "M", "M"])


# Manully change the table style 
table.align = "l"