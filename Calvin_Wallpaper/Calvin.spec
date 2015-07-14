# -*- mode: python -*-
a = Analysis(['Calvin.py'],
             pathex=['/home/akshay/SideProjects/Calvin_Wallpaper'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Calvin',
          debug=False,
          strip=None,
          upx=True,
          console=True )
