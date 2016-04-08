import os
import sys
import shutil

##uncomment os.chdir for testing only
##os.chdir('D:\\Desktop')

rootDir = ('DeskSweep\\')
imgDir = (rootDir + 'Images')
vidDir = (rootDir + 'Videos')
audDir = (rootDir + 'Audio')
zipDir = (rootDir + 'Compressed')
docDir = (rootDir + 'Documents')
proDir = (rootDir + 'Programs')
dbsDir = (rootDir + 'Databases')
scptDir = (rootDir + 'Scripts')

files = os.listdir(os.getcwd())
folders = [rootDir, imgDir, vidDir, audDir, zipDir, docDir, proDir, dbsDir, scptDir]

imgExt = ['.jpg','.png','.gif', '.jfif', '.exif',
          '.bmp', '.tiff','.bpg', '.ppm', '.pgm',
          '.pbm', '.pnm', '.webp', '.hdr', '.heif'
          ]

vidExt = ['.mkv','.avi','.mp4', '.webm', '.flv',
          '.vob', '.ogv', '.ogg', '.drc', '.gifv',
          '.mng', '.mov', '.qt', '.wmv', '.yuv',
          '.rm', '.rmvb', '.asf', '.m4p', '.m4v',
          '.mpg', '.mpeg', '.m2v', '.mp2', '.mpe',
          '.mpv', '.svi', '.3gp', '.3g2', '.mxf',
          '.roq', '.nsv', '.f4v', '.f4p', '.f4a',
          '.f4b'
          ]

audExt = ['.3gp', '.aa','.mp3','.wav','.aac',
          '.aax', '.act', '.aiff', '.amr', '.ape',
          '.au', '.awb', '.dct', '.dss', '.dvf',
          '.flac', '.gsm', '.iklax', '.ivs', '.m4a',
          '.m4b', '.m4p', '.mmf', '.mp3', '.mpc',
          '.msv', '.oga', '.opus', '.ra', '.rm',
          '.raw', '.sln', '.tta', '.vox', '.wma',
          '.wv'          
          ]

zipExt = ['.7z', '.s7z', '.ace', '.afa', '.alz',
          '.iso', '.arc', '.arj', '.b1', '.ba',
          '.bh', '.cab', '.car', '.cfs', '.cpt',
          '.dar', '.dd', '.dgc', '.dmg', '.ear',
          '.gca', '.ha', '.hki', '.ice', '.jar',
          '.kgb', '.lzh', '.lha', '.lzx', '.pak',
          '.partimg', '.paq6', '.paq7', '.paq8', '.pea',
          '.pim', '.pit', '.qda', '.rar', '.rk',
          '.sda', '.sea', '.sen', '.sfx', '.shk',
          '.sit', '.sitx', '.sqx', '.tar.gz', '.tgz',
          '.tar.Z', '.tar.brz2', '.tbz2', '.tar.lzma', '.tlz',
          '.uc', '.uc0', '.uc2', '.ucn', '.ur2',
          'ue2', '.uca', '.uha', '.war', '.wim',
          '.xar', '.xp3', '.yz1', '.zip', '.zipx',
          '.zoo', '.zpaq', '.zz', '.gz'
          ]

docExt = ['.doc', '.xls', '.txt', '.pdf', '.docx',
          '.pptx', '.ppt', '.xlsx', '.epub', '.odt',
          '.odp', '.ods', '.txt', '.rft', '.docm',
          '.dotx', '.docb', '.dot', '.xlt', '.xlm',
          '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb',
          '.xla', '.xlam', '.xll', '.xlw', '.ppt',
          '.pot', '.pps', '.pptm', '.potx', '.potm',
          '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm',
          '.accdb', '.accde', '.accdt', '.accdr', '.pub',
          '.csv'
          ]

proExt = ['.exe', '.msi', '.action', '.app', '.ws',
          '.workflow', '.cmd', '.com', '.command', '.cpl',
          '.csh', '.gadget', '.inf', '.ins', '.inx',
          '.ipa', '.isu', '.job', '.jse', '.ksh',
          '.wsh', '.msc', '.msp', '.mst', '.osx',
          '.out', '.paf', '.pif', '.prg', '.ps1',
          '.reg', '.rgs', '.run', '.scr', '.sct',
          '.shb', '.shs', '.u3p', '.vb', '.vbe', '.wsf',
          '.vbscript'
          ]

dbsExt = ['.sql', '.bak', '.mdb', '.sqlite', '.pdb'
          ]

scptExt = ['.php', '.html', '.htm', '.asp', '.aspx',
           '.json', '.js', '.css', '.pl', '.sh',
           '.cs', '.bat', '.rss', '.py', '.java',
           '.c', '.cshtml', '.phtml', '.vbs', '.php3',
           '.html5', '.perl', '.f', '.bash', '.php5',
           '.bin'
           ]

# counters for moveFile function
migratedFiles = 0 
duplicateFiles = 0


def makeFolder(folders):
    for folder in folders:
        try:
            os.mkdir(str(folder))
            print(folder, 'created - OK!')
        except FileExistsError:
            print(folder, 'exists - OK!')
            continue
        
def upperCaseExt(ext):
    extUpperCase = [item.upper() for item in ext]
    ext.extend(extUpperCase)
    return ext

def moveFile(ext, directory):
    for file in files:
        if not file.startswith("DeskSweeper"):
            try:
                global migratedFiles
                upperCaseExt(ext)
                if file.endswith(tuple(ext)): 
                    shutil.move(file, directory)
                    print(file, ' moved ==> ', directory)
                    migratedFiles += 1               
            except shutil.Error:
                global duplicateFiles
                print(file, ' already exists - not moved!')
                duplicateFiles += 1
                continue
        

# Begin output to terminal           
print('!!!Ensure DeskSweeper.exe is run from within the directory you wish to clean!!!\n')
print('DeskSweeper will create a DeskSweep folder and sort files into sub-folders by file type\n\n')
print('Do you want DeskSweep to clean directory:', os.getcwd(), '?')

start = input('Press Enter to Exit, or Y & Enter to continue: ').lower()
if start.startswith('y'):
    pass
else:
    sys.exit('Exited program')

print('\n\nFolder pre-check:')
makeFolder(folders)

print('\nBeginning file move:')
moveFile(imgExt, imgDir)
moveFile(vidExt, vidDir)
moveFile(audExt, audDir)
moveFile(zipExt, zipDir)
moveFile(docExt, docDir)
moveFile(proExt, proDir)
moveFile(dbsExt, dbsDir)
moveFile(scptExt, scptDir)

print('\nTotal', migratedFiles, 'files moved')
print(duplicateFiles, 'duplicate not moved')

input("\n\nPress Enter to exit")
