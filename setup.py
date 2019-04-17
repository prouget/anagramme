from cx_Freeze import setup, Executable

setup(
    name = "ProdesMots",
    version = "1.0.0",
    description = "recherche de mots par dictionnaire",
    executables = [Executable("Anagramme.py")],
)