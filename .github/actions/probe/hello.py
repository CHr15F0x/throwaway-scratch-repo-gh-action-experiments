import pathlib
import sys

marker = (pathlib.Path(__file__).parent / "MARKER").read_text().strip()
print(f"hello.py ran from {pathlib.Path(__file__).parent} marker={marker} python={sys.version.split()[0]}")
