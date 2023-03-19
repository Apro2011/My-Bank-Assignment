import csv
from myapp.models import BankDetails

def run():
    with open('bank_data/bank_branches.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            object_dict = {key: value for key, value in zip(header, row)}
            object_dict["bank_id"] = int(object_dict['bank_id'])
            BankDetails.objects.create(**object_dict)
