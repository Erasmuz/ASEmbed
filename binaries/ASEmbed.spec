# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/unpackTK.py'), os.path.join(HOMEPATH,'support/useTK.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), '../ASEmbed.py', os.path.join(HOMEPATH,'support/removeTK.py')],
             pathex=['../helper', '/Users/erasmuz/Projects/ASEmbed/source/pyinstaller-1.5'])
pyz = PYZ(a.pure)
exe = EXE(TkPKG(), pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'ASEmbed'),
          debug=False,
          strip=False,
          upx=True,
          console=1 , icon='../../binaries/ASEmbed.ico')
app = BUNDLE(exe,
             name=os.path.join('dist', 'ASEmbed.app'))
