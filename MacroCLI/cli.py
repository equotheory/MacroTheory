import os
print('Welcome to MCLI (MacroCLI)')
initcmd = input('$ ')
while True:
  if initcmd == 'mc set tool=pip':
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
    os.system('python3 get-pip.py')
  if initcmd == 'mc get':
    GetPackage = input('PackageName: ').strip()
    os.system(f'pip install {GetPackage}')
  if initcmd == 'mc get+ver':
    GetPackage = input('PackageName: ').strip()
    GetPackageVer = (input('Version: ').strip())
    os.system(f'pip install {GetPackage}=={float(GetPackageVer)}')
  if initcmd == 'mc run':
    GetPackage = input('Dir+file: ').strip()
    os.system(f'python3 -m macro {GetPackage}')
