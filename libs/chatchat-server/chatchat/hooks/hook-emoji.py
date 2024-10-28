from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('emoji', include_py_files=False, include_datas=['**/*.*'])
