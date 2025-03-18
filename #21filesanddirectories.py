from pathlib import Path

#absolutepath eg C:\Program Files\Microsoft
#relativepath 

path=Path()
for file in path.glob("*.*"):
    print(file)