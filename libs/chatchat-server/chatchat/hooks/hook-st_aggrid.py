from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('st_aggrid', include_py_files=False, include_datas=['**/*.*'])
