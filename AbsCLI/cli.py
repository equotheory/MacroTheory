import os
print('Welcome to AbsCLI.')
initcmd = input('$ ')
while True:
  if initcmd == 'abs setup':
    filename = input('filename(eg. main.abr): ')
    try:
      os.system(f'python3 -m abros {filename}')
    except:
      print('AbsCLI Render=*/')
  elif initcmd == 'abs -render:first:setup':
    filename = input('filename(eg. main.abr): ')
    os.system(f'python3 -m abros {filename}')
  elif initcmd == 'abs load pip':
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
  elif initcmd == 'abs create pip':
    os.system('python3 get-pip.py')
  elif initcmd == 'abs load abr':
    os.system('touch start.abr')
    print('File Created: start.abr')
  elif initcmd == 'abs load abr -n':
    askname = input('Name of File: ')
    os.system(f'touch {askname}.abr')