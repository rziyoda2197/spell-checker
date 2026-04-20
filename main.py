class SpellChecker:
    def __init__(self):
        self.sozlar = {
            "apple": "elma",
            "banana": "banan",
            "cherry": "cherry",
            "date": "date",
            "elderberry": "elderberry"
        }

    def tozalash(self, soz):
        soz = soz.lower()
        return soz

    def tekshirish(self, soz):
        tozalanmagan_soz = self.tozalash(soz)
        if tozalanmagan_soz in self.sozlar:
            return self.sozlar[tozalanmagan_soz]
        else:
            return tozalanmagan_soz

    def spell_check(self, sozlar):
        natijalar = []
        for soz in sozlar:
            natija = self.tekshirish(soz)
            natijalar.append((soz, natija))
        return natijalar

spell_checker = SpellChecker()
sozlar = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Grape"]
natijalar = spell_checker.spell_check(sozlar)
for soz, natija in natijalar:
    print(f"{soz}: {natija}")
```

Kodni ishga tushirish uchun, siz sozlar ro'yxatiga qo'shgan so'zlarni o'zgartiring.
