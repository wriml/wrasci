"""
WRASCI → IPA Unicode — outil en ligne de commande
Usage : python wrasci_to_ipa.py "gb a tl"
"""
import sys
from wrasci import to_ipa, validate


def main():
    if len(sys.argv) < 2:
        print("Usage : python wrasci_to_ipa.py <chaine-wrasci>")
        sys.exit(1)

    chaine = " ".join(sys.argv[1:])
    valide, erreurs = validate(chaine)

    if not valide:
        print("Erreur WRASCI :", file=sys.stderr)
        for e in erreurs:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    print(to_ipa(chaine))


if __name__ == "__main__":
    main()
