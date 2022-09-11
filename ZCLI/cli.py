import os
print('Welcome to ZCLI.')
initcmd = input('$ ')
while True:
  if initcmd == 'ze make pip':
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
    os.system('python3 get-pip.py')
  if initcmd == 'ze pyg':
    GetPackage = input('PackageName: ').strip()
    os.system(f'pip install {GetPackage}')
