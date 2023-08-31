import math
import csv
import random
import json
import os

dmt = ";"
fields = ["a", "b", "c"]
file = "pp.csv"

def genCSV(count: int, file: str) -> None:
    max = 100
    min = -100
    print(f'genCSV file={file}')
    with open(file, "w", encoding="utf8") as f:
        writer = csv.DictWriter(f, delimiter=dmt, fieldnames=fields, lineterminator="\r")
        writer.writeheader()
        for _ in range(0, count):
            writer.writerow({fields[0]: random.randint(min, max), fields[1]: random.randint(min, max), fields[2]: random.randint(min, max)})

def verificationFile(file: str) -> bool:
    if os.path.exists(file):
        return True
    else:
        return False


def my_decorator(func):
    print("retry")
    print(__name__)
    result = {}
    if verificationFile(file):
        with open(file, "r", encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=dmt)
            count = 0
            for row in reader:
                temp = []
                a = int(row[fields[0]])
                b = int(row[fields[1]])
                c = int(row[fields[2]])
                temp = func(a, b, c)
                result[count] = {fields[0]: a, fields[1]: b, fields[2]: c, "result": temp}
                count += 1
    return result


@my_decorator
def equation(a: int, b: int, c: int) -> list:
    result = []
    if a == 0:
        return None
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        x = -b / (2 * a)
        result.append(x)
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        result.append(x1)
        result.append(x2)
    return result



def readCSVFile(file: str) -> list:
    result = []
    with open(file, "r", encoding="utf8") as f:
        reader = csv.DictReader(f, delimiter=dmt)
        for row in reader:
            a = int(row[fields[0]])
            b = int(row[fields[1]])
            c = int(row[fields[2]])
            result.append([a, b, c])
    return result

def toWrite(func):
    def wrapper_toWrite(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_toWrite


@toWrite
def writeJsonFile(file: str, data: dict) -> None:
    print(file)
    with open(file, "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    print(__name__, 1)
    genCSV(50, "pp.csv")

    temp = equation
    writeJsonFile("Result.json", temp)
    for i in temp:
        print(temp[i])