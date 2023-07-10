from cx_Freeze import setup, Executable

executables = [Executable("menu.py")]

options = {
    'build_exe': {
        'packages': ['numpy', 'matplotlib'],
        'includes': ['pandas', 'seaborn']
    }
}

setup(
    name="menu.py",
    version="1.0",
    description="Descrição do Executável",
    executables=executables
)
