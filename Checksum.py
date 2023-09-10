import os
import sys
import subprocess

file1 = sys.argv[1].strip('"')
file2 = sys.argv[2].strip('"')
algorithm = sys.argv[3].strip('"')

if not os.path.isfile(file1):
    print(f"[py] File 1: {file1} does not exist")
    file1 = None
else:
    print(f"[py] File 1: {file1}")

print("[py] File 2:", file2)
print("[py] Algorithm:", algorithm)


def hash_file(file, algorithm):
    hash_value = subprocess.run(
        f'certutil -hashfile "{file}" {algorithm}', stdout=subprocess.PIPE
    )
    hash_value = hash_value.stdout.decode("utf-8").splitlines()[1]
    return hash_value


if file1 is not None:
    file1_hash = hash_file(file1, algorithm)
    print("[py] File 1 hash:", file1_hash)
file2_hash = hash_file(file2, algorithm)
print("[py] File 2 hash:", file2_hash)

if file1 is not None:
    if file1_hash == file2_hash:
        print("[py] FILES MATCH!")
    else:
        print("[py] FILES DO NOT MATCH!")
else:
    print("[py] File 1 does not exist, cannot compare hashes")
