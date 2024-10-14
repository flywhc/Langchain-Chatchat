from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('streamlit_paste_button', include_py_files=False, include_datas=['**/*.*'])
