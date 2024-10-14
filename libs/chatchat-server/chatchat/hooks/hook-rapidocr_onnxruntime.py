from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('rapidocr_onnxruntime', include_py_files=False, include_datas=['**/*.*'])
