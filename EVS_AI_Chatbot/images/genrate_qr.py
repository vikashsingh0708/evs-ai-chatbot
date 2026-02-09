import qrcode

pages = [
    "tulsi.html",
    "neem.html",
    "rose.html",
    "sunflower.html",
    "lotus.html",
    "mango.html",
    "aloevera.html",
    "bamboo.html",
    "peepal.html",
    "sheesham.html"
]

for page in pages:
    qr = qrcode.make(page)
    qr.save(page.replace(".html", "_QR.png"))

print(" All QR codes generated successfully!")
