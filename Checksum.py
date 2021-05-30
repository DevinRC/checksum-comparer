import subprocess
import os

directory_items = {}
algorithm_list = ["MD5", "SHA1", "SHA256"]
for i, j in enumerate(os.scandir()):
    directory_items[i+1] = j

print("Files in Directory: ")
for i in list(directory_items.keys()):
    print(f'\t{i}. {directory_items.get(i).name}')

file_number = int(input("Enter the file number: "))
file = directory_items.get(file_number)

print("\nHashing Algorithms: ")
for i, j in enumerate(algorithm_list):
    print(f'\t{i+1}. {j}')

algorithm = int(input("\nEnter the Algorithm Number: "))
user_hashvalue = input("Enter the hashvalue (Press enter to skip): ")

response = subprocess.run(f"certutil -hashfile \"{file.name}\" {algorithm_list[algorithm-1]}", stdout=subprocess.PIPE)
real_hashvalue = response.stdout.decode('utf-8').splitlines()[1]
print();
print(f"Generated {algorithm_list[algorithm-1]} value:", real_hashvalue)
if(user_hashvalue != ""):
    print("User:", user_hashvalue)
    # print(real_hashvalue == user_hashvalue)
    print("\nChecksums are Matching!" if real_hashvalue.lower() == user_hashvalue.lower() else "Checksums are not Matching")

hold = input()
