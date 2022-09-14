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
  if initcmd == 'ze make passgen -z':
    print("Starting to ze make PassGenZ")
    os.system('cd ZCLI')
    os.system('git clone https://github.com/suryasr007/random-password-generator.git')
    os.system('cd random-password-generator')
    os.system('python3 password_generator.py')