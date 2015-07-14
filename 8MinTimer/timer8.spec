# -*- mode: python -*-
a = Analysis(['timer8.py'],
             pathex=['/home/akshay/SideProjects/8MinTimer'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='timer8',
          debug=False,
          strip=None,
          upx=True,
          console=True )
