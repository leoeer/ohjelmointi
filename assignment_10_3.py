import unicodedata

def main():
    print("IPA:\n")
    ipa = ["\u0250", "\u0251", "\u0252", "\u0253", "\u0254"]
    for n in ipa:
        print(n, unicodedata.name(n), "\n")

    print("Cyrillic Supplement:\n")
    cyrillic = ["\u0500", "\u050A", "\u050D", "\u050F", "\u0507"]
    for i in cyrillic:
        print(i, unicodedata.name(i),"\n")

    print("1-5:\n")
    valmiit = ["ŵ", "Φ", "Ӫ", "ʔ", "‱"]
    for c in valmiit:
        print(c, "  ", hex(ord(c)), "    ", unicodedata.name(c))

main()