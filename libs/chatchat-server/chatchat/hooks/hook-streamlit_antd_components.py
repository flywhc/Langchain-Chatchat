from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('streamlit_antd_components', include_py_files=False, include_datas=['**/*.*'])
