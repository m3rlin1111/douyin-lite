from PyInstaller.utils.hooks import collect_all

ctk_datas, ctk_binaries, ctk_hidden = collect_all("customtkinter")
pw_datas, pw_binaries, pw_hidden = collect_all("playwright")

a = Analysis(
    ["douyin_lite.py"],
    pathex=[],
    binaries=ctk_binaries + pw_binaries,
    datas=ctk_datas + pw_datas,
    hiddenimports=ctk_hidden + pw_hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        "openai", "faster_whisper", "torch", "transformers", "fastapi",
        "uvicorn", "module_2", "module_3", "module_4",
    ],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="DouyinLite",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
)
