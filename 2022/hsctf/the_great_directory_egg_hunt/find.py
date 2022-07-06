import os

with open("dir.zip", "rb") as f:
    data = f.read()

data = data.split(b"file.txt")[1:]

for i, d in enumerate(data):
    if not d.startswith(b"Nope"):
        path = data[i-1][-40:].decode()
        output = os.popen(f"unzip -p dir.zip {path}file.txt").read()
        if "Nope" not in output:
            print(output)
            print(path)
            break

print(path.replace("/", ''))