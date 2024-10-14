from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('streamlit', include_py_files=False, include_datas=['**/*.*'])


#datas = copy_metadata("streamlit")
#datas += collect_data_files('streamlit', includes=['static', 'runtime'])

#datas = copy_metadata("streamlit_antd_components")
#datas = copy_metadata("streamlit_feedback")
#datas = copy_metadata("streamlit_paste_button")
#d#atas = copy_metadata("rapidocr_onnxruntime")
#datas = copy_metadata("unstructured")
#datas = copy_metadata("st_aggrid")

#module_collection_mode = 'py'
#hiddenimports = collect_submodules('chatchat.server.file_rag.document_loaders')