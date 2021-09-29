'''
Switch v/h screen size for appium-desktop
'''
'''
Switch v/h screen size for appium-desktop
'''

import os, sys, re, ctypes
import shutil

if ctypes.windll.shell32.IsUserAnAdmin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

dst_folder = r'C:\Users\%s\AppData\Local\Programs\Appium\resources\app\dist' % os.environ['USERNAME']
if not os.path.isdir(dst_folder):
    dst_folder = r'C:\Program Files\Appium\resources\app\dist'

update_file = 'renderer.e31bb0bc'
update_list_dst = [update_file+'.css', update_file+'.js']
update_list_ori = [update_file+'_ori.css', update_file+'_ori.js']
update_list_mod = [update_file+'_mod.css', update_file+'_mod.js']

os.chdir(os.path.abspath(os.path.dirname(__file__)))
ori_size = os.path.getsize(update_list_ori[0])
dst_size = os.path.getsize(os.path.join(dst_folder, update_list_dst[0]))
try:
    if dst_size != ori_size:
        print('restore appium file list to V')
        shutil.copyfile(update_list_ori[0], os.path.join(dst_folder, update_list_dst[0]))
        shutil.copyfile(update_list_ori[1], os.path.join(dst_folder, update_list_dst[1]))
    else:
        print('modify appium file list to H')
        shutil.copyfile(update_list_mod[0], os.path.join(dst_folder, update_list_dst[0]))
        shutil.copyfile(update_list_mod[1], os.path.join(dst_folder, update_list_dst[1]))
    input('Done, any key to exit')
except Exception as e:
    print(e)
    input('ERROR, contact automation team!')
