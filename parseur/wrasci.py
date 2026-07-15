"""
WRASCI — Parseur de référence Python
Convertit une chaîne WRASCI en liste de tokens phonétiques.
"""

def parse(chaine: str) -> list[str]:
    """
    Parse une chaîne WRASCI en liste de tokens.
    Espace simple = séparateur de tokens.
    Double espace = espace orthographique ordinaire.
    """
    # Remplacer le double espace par un marqueur temporaire
    SPACE_MARKER = "\x00"
    chaine = chaine.replace("  ", SPACE_MARKER)
    tokens = chaine.split(" ")
    # Restaurer les espaces orthographiques
    return [t.replace(SPACE_MARKER, " ") for t in tokens if t]


def validate(chaine: str) -> tuple[bool, list[str]]:
    """
    Valide qu'une chaîne WRASCI respecte la doctrine alphanumérique.
    Retourne (valide, liste_erreurs).
    """
    errors = []
    import re
    # Après remplacement du double espace, seuls [a-z0-9 ] autorisés
    cleaned = chaine.replace("  ", "")
    if not re.match(r'^[a-z0-9 ]*$', cleaned):
        invalid = set(re.findall(r'[^a-z0-9 ]', cleaned))
        errors.append(
            f"Caractères non alphanumériques détectés : {invalid}"
        )
    return (len(errors) == 0, errors)


# Table de référence WRASCI → IPA Unicode
WRASCI_TO_IPA = {
    # Voyelles
    "i":    "i",    "y":    "y",    "ib":   "ɨ",    "ub":   "ʉ",
    "um":   "ɯ",    "u":    "u",    "ic":   "ɪ",    "yc":   "ʏ",
    "uc":   "ʊ",    "e":    "e",    "eu":   "ø",    "ei":   "ɘ",
    "ob":   "ɵ",    "eo":   "ɤ",    "o":    "o",    "shwa": "ə",
    "3i":   "ɛ",    "oe":   "œ",    "3":    "ɜ",    "3u":   "ɞ",
    "vr":   "ʌ",    "oo":   "ɔ",    "ae":   "æ",    "ar":   "ɐ",
    "a":    "a",    "aoe":  "ɶ",    "ao":   "ɑ",    "aou":  "ɒ",
    # Consonnes — occlusives et nasales
    "p":    "p",    "b":    "b",    "t":    "t",    "d":    "d",
    "ttr":  "ʈ",    "dtr":  "ɖ",    "c":    "c",    "cj":   "ɟ",
    "k":    "k",    "g":    "g",    "q":    "q",    "gq":   "ɢ",
    "glot": "ʔ",    "m":    "m",    "mv":   "ɱ",    "n":    "n",
    "ntr":  "ɳ",    "ny":   "ɲ",    "ng":   "ŋ",    "ngq":  "ɴ",
    # Fricatives
    "ph":   "ɸ",    "bh":   "β",    "f":    "f",    "v":    "v",
    "tht":  "θ",    "dht":  "ð",    "s":    "s",    "z":    "z",
    "sh":   "ʃ",    "zh":   "ʒ",    "str":  "ʂ",    "ztr":  "ʐ",
    "cc":   "ç",    "jc":   "ʝ",    "x":    "x",    "gh":   "ɣ",
    "ch":   "χ",    "rfr":  "ʁ",    "hph":  "ħ",    "phv":  "ʕ",
    "h":    "h",    "hv":   "ɦ",
    # Approximantes et latérales
    "r":    "r",    "rq":   "ʀ",    "r1":   "ɾ",    "r1tr": "ɽ",
    "vh":   "ʋ",    "ra":   "ɹ",    "ratr": "ɻ",    "j":    "j",
    "w":    "w",    "l":    "l",    "ltr":  "ɭ",    "ly":   "ʎ",
    "lk":   "ʟ",    "ls":   "ɬ",    "lv":   "ɮ",
    # Non-pulmoniques
    "clb":  "ʘ",    "cld":  "ǀ",    "cla":  "ǃ",    "clp":  "ǂ",
    "cll":  "ǁ",    "bimp": "ɓ",    "dimp": "ɗ",    "jimp": "ʄ",
    "gimp": "ɠ",    "qimp": "ʛ",    "kp":   "k͡p",   "gb":   "g͡b",
    "ts":   "t͡s",   "dz":   "d͡z",   "tsh":  "t͡ʃ",   "dzh":  "d͡ʒ",
    # Autres symboles
    "wsh":  "ʍ",    "wy":   "ɥ",    "hch":  "ʜ",    "rgh":  "ʢ",
    "epl":  "ʡ",    "csh":  "ɕ",    "jzh":  "ʑ",    "l1":   "ɺ",
    "shx":  "ɧ",
    # Modificateurs
    "lg":   "ː",    "slg":  "ˑ",    "nas":  "̃",     "asp":  "ʰ",
    "ej":   "ʼ",    "lab":  "ʷ",    "pal":  "ʲ",    "nvx":  "̥",
    "vx":   "̬",     "atr":  "̘",     "rtr":  "̙",
    "ustp": "ꜛ",    "dstp": "ꜜ",    "glr":  "↗",    "glf":  "↘",
    # Tons
    "thh":  "̋",     "th":   "́",     "tm":   "̄",     "tl":   "̀",
    "tll":  "̏",     "tlh":  "̌",     "thl":  "̂",
    "tmh":  "᷄",    "tml":  "᷅",    "tlhl": "᷈",
}


def to_ipa(chaine: str) -> str:
    """
    Convertit une chaîne WRASCI en IPA Unicode.
    Les modificateurs sont attachés au caractère précédent.
    """
    tokens = parse(chaine)
    result = []
    MODIFICATEURS = {
        "lg", "slg", "nas", "asp", "ej", "lab", "pal",
        "nvx", "vx", "atr", "rtr",
        "thh", "th", "tm", "tl", "tll", "tlh", "thl",
        "tmh", "tml", "tlhl", "ustp", "dstp", "glr", "glf"
    }
    for token in tokens:
        if token == " ":
            result.append(" ")
        elif token in WRASCI_TO_IPA:
            ipa = WRASCI_TO_IPA[token]
            if token in MODIFICATEURS and result:
                # Attacher le modificateur au dernier caractère
                result[-1] = result[-1] + ipa
            else:
                result.append(ipa)
        else:
            result.append(f"[?{token}]")  # token inconnu
    return "".join(result)


if __name__ == "__main__":
    tests = [
        ("gb a tl", "[g͡bà]"),
        ("i nas th", "[ĩ́]"),
        ("sh w a", "[ʃwa]"),
    ]
    print("Tests WRASCI → IPA\n")
    for wrasci, attendu in tests:
        resultat = to_ipa(wrasci)
        statut = "✓" if resultat == attendu else f"✗ (attendu {attendu})"
        print(f"  {wrasci:20} → {resultat:15} {statut}")
