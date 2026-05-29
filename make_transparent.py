from pathlib import Path
from PIL import Image

FILES = [
    Path("assets/uniform/linkedin.png"),
    Path("assets/uniform/gmail.png"),
]

THRESH = 240

for p in FILES:
    if not p.exists():
        print(f"Missing: {p}")
        continue
    img = Image.open(p).convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        r,g,b,a = item
        # If pixel is near-white and fully opaque, make it transparent
        if a > 0 and r >= THRESH and g >= THRESH and b >= THRESH:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(p)
    print(f"Converted {p} -> transparent background")

print("Done")
