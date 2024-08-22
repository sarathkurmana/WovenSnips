# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['WovenSnips.py'],
    pathex=[],
    binaries=[],
    datas=[('fonts/Roboto-Regular.ttf', 'fonts'), ('WovenSnips.icns', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='WovenSnips',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='WovenSnips.icns',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='WovenSnips',
)
app = BUNDLE(
    coll,
    name='WovenSnips.app',
    icon='WovenSnips.icns',
    bundle_identifier='com.yourcompany.wovensnips',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSApplicationCategoryType': 'public.app-category.productivity',
        'CFBundleShortVersionString': '1.1.0',
    },
)
