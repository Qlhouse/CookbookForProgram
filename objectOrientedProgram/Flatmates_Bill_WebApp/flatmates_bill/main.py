from flat import Bill, Flatmate
from reports import PdfReport, FileSharer


# CLI for user
bill_amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2021: ")

name1 = input("What is your name? ")
days_in_house1 = int(
    input(f"How many days did {name1} stay in the house duiring the bill period? "))

name2 = input("What is the name of your flatmate? ")
days_in_house2 = int(
    input(f"How many days did {name2} stay in the house duiring the bill period? "))

bill = Bill(bill_amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} payed: ", flatmate1.pays(bill, co_flatmate=flatmate2))
print(f"{flatmate2.name} payed: ", flatmate2.pays(bill, co_flatmate=flatmate1))

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
