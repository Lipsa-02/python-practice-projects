#program for copying an image
#ImagecopyEx.py
try:
    with open("C:\\Users\\lipsa\\OneDrive\\Desktop\\IMAGES\\dog12.jpg","rb") as rp:
        with open("whitedog.jpg","wb") as wp:
            srcfile=rp.read()
            wp.write(srcfile)
            print("Image file copied")
except FileNotFoundError:
    print("file does not exist")

