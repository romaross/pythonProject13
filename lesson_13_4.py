'''Создать скрипт, который принимает имя фамилию и возраст в качестве параметров и дописывает их в csv файл'''
import sys
import argparse
import csv

print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',
                    required=True)
parser.add_argument('-ln', '--last-name',
                    required=True)
parser.add_argument('-a', '--age', required=True)
args = parser.parse_args()
print(args)
print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Age:', args.age)

with open("classmates.csv", mode="w") as csvfile:
    file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
    file_writer.writerow(["First_name", "Last_name", "Age"])
    file_writer.writerow([args.first_name, args.last_name, args.age])
