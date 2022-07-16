import os
print('Welcome to AmpCLI.')
initcmd = input('$ ')
while True:
  if initcmd == 'amp setup':
    filename = input('filename(eg. main.abr): ')
    try:
      os.system(f'python3 -m amphire {filename}')
    except:
      print('AmpCLI Render=*/')
  elif initcmd == 'amp -render:first:setup':
    filename = input('filename(eg. main.abr): ')
    os.system(f'python3 -m amphire {filename}')
  elif initcmd == 'amp load pip':
    os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
  elif initcmd == 'amp create pip':
    os.system('python3 get-pip.py')
  elif initcmd == 'amp load vsc':
      print('Coming Soon.')
  elif initcmd == 'amp load abr':
    os.system('touch start.abr')
    print('File Created: start.abr')
  elif initcmd == 'amp load abr -n':
    askname = input('Name of File: ')
    os.system(f'touch {askname}.abr')