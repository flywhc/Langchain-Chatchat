# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cli.py'],
    pathex=['C:\\Users\\flywh\\.conda\\envs\\chatchat'],
    binaries=[],
    datas=[('.\\server\\api_server\\static', 'chatchat\\server\\api_server\\static'), 
      ('.\\img', 'chatchat\\img'), ('.\\data', 'chatchat\\data'),
      ('.\\webui_pages', 'chatchat\\webui_pages'),
     ],
    hiddenimports=["streamlit", "streamlit_antd_components", "streamlit_chatbox", "streamlit_extras",
     "streamlit_paste_button", "streamlit_markdown", "streamlit_extras.bottom_container", "st_aggrid", "st_aggrid.grid_options_builder",
     "emoji", "chatchat.webui", "chatchat.server.file_rag.document_loaders" ],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['chatchat.ico'],
)
