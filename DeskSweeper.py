import os
import sys
import shutil

##uncomment os.chdir for testing only
##os.chdir('C:\\your_test_directory_here')

filetypes = {
             "Images" : ['.jpg','.png','.gif', '.jfif', '.exif',
                         '.bmp', '.tiff','.bpg', '.ppm', '.pgm',
                         '.pbm', '.pnm', '.webp', '.hdr', '.heif'
                         ],
             "Videos" : ['.mkv','.avi','.mp4', '.webm', '.flv',
                         '.vob', '.ogv', '.ogg', '.drc', '.gifv',
                         '.mng', '.mov', '.qt', '.wmv', '.yuv',
                         '.rm', '.rmvb', '.asf', '.m4p', '.m4v',
                         '.mpg', '.mpeg', '.m2v', '.mp2', '.mpe',
                         '.mpv', '.svi', '.3gp', '.3g2', '.mxf',
                         '.roq', '.nsv', '.f4v', '.f4p', '.f4a',
                         '.f4b'
                         ],
             "Audio" : ['.3gp', '.aa','.mp3','.wav','.aac',
                        '.aax', '.act', '.aiff', '.amr', '.ape',
                        '.au', '.awb', '.dct', '.dss', '.dvf',
                        '.flac', '.gsm', '.iklax', '.ivs', '.m4a',
                        '.m4b', '.m4p', '.mmf', '.mp3', '.mpc',
                        '.msv', '.oga', '.opus', '.ra', '.rm',
                        '.raw', '.sln', '.tta', '.vox', '.wma',
                        '.wv'
                        ],
        "Compressed" : ['.7z', '.s7z', '.ace', '.afa', '.alz',
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
                        ],
         "Documents" : ['.doc', '.xls', '.txt', '.pdf', '.docx',
                        '.pptx', '.ppt', '.xlsx', '.epub', '.odt',
                        '.odp', '.ods', '.txt', '.rft', '.docm',
                        '.dotx', '.docb', '.dot', '.xlt', '.xlm',
                        '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb',
                        '.xla', '.xlam', '.xll', '.xlw', '.ppt',
                        '.pot', '.pps', '.pptm', '.potx', '.potm',
                        '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm',
                        '.accdb', '.accde', '.accdt', '.accdr', '.pub',
                        '.csv'
                        ],
          "Programs" : ['.exe', '.msi', '.action', '.app', '.ws',
                        '.workflow', '.cmd', '.com', '.command', '.cpl',
                        '.csh', '.gadget', '.inf', '.ins', '.inx',
                        '.ipa', '.isu', '.job', '.jse', '.ksh',
                        '.wsh', '.msc', '.msp', '.mst', '.osx',
                        '.out', '.paf', '.pif', '.prg', '.ps1',
                        '.reg', '.rgs', '.run', '.scr', '.sct',
                        '.shb', '.shs', '.u3p', '.vb', '.vbe', '.wsf',
                        '.vbscript'
                        ],
        "Databases" : ['.sql', '.bak', '.mdb', '.sqlite', '.pdb'
                       ],
          "Scripts" : ['.php', '.html', '.htm', '.asp', '.aspx',
                       '.json', '.js', '.css', '.pl', '.sh',
                       '.cs', '.bat', '.rss', '.py', '.java',
                       '.c', '.cshtml', '.phtml', '.vbs', '.php3',
                       '.html5', '.perl', '.f', '.bash', '.php5',
                       '.bin'
                       ]
            }

rootDir = ('DeskSweep\\')
cwd = os.getcwd()

# counters for moveFiles function
migratedFiles = 0 
duplicateFiles = 0

def makeFolder(filetypes):
    #for directory in list(filetypes.keys()):
    for directory in filetypes:
        try:
            os.makedirs(rootDir + directory)
            print(directory, 'created - OK!') 
        except FileExistsError:
            print(directory, 'exists - OK!')
            continue
        
def moveFiles(filetypes):
    files = os.listdir(cwd)
    for directory in filetypes:
        try:
            for file in files:
                if not file.startswith("DeskSweeper"):
                    if file.endswith(tuple(filetypes[directory])):
                        global migratedFiles
                        shutil.move(file, rootDir + directory)
                        print(file, ' moved ==> ', directory)
                        migratedFiles += 1
        except shutil.Error:
            global duplicateFiles
            print(file, ' already exists - not moved!')
            duplicateFiles += 1
            continue
        

#Begin output to terminal           
print(
'''!!!Ensure DeskSweeper.exe is run from within the directory you wish to clean!!!
DeskSweeper will create a DeskSweep folder and sort files into sub-folders by file type
Do you want DeskSweep to clean directory: ''' + cwd + '''?'''
)

start = input('\nPress Enter to Exit, or Y & Enter to continue: ').lower()
if start.startswith('y'):
    pass
else:
    sys.exit('Exited program')

print('\n\nFolder pre-check:')
makeFolder(filetypes)
print('\nBeginning file move:')           
moveFiles(filetypes)

print('\nTotal', migratedFiles, 'files moved')
print(duplicateFiles, 'duplicate not moved')

input("\n\nPress Enter to exit")
