# Créé par Dell, le 04/09/2022 en Python 3.7
def search_word(word):
    z=zipfile.ZipFile("readonly/small_img.zip")
    L=z.infolist()
    z.extractall()
    names=z.namelist()
    #for n in names:
    #image=Image.open(n)
    #display(image)
    list_img={}
    for n in names:
        text = pytesseract.image_to_string(Image.open(n))
        if word in text:
            img = cv.imread(n)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            image=Image.open(n)
            for x,y,w,h in faces:
                image.crop((x,y,x+w,y+w))
                max_size=(100,100)
                image.thumbnail(max_size)
                #image.save("new_n.png")
                if image not in list_img:
                    list_img["n"]="image"

    for img in list_img.values():
        contact_sheet=Image.new("RGB", (500,300))
        x=0
        y=0
        contact_sheet.paste(img, (x, y) )
        if x+100 == contact_sheet.width:
            x=0
            y=y+100
        else:
            x=x+100
        print("Results found in {}".format(list_img.keys()))
        display(contact_sheet)

