import os
os.chdir('C:/Users/AmitPrakash/Desktop/python code')
with open ('GLLNS.txt','r') as text_file:
        with open('GLLNS_UPDATED.txt','w') as text_file_new:
                for line in text_file:
                        if  'T21100-1400678  7899' in line and  'SPD' in line and  ('GPRF' in line  or 'AHRF' in line  or 'CLRF' in line):
                                continue
                        else:
                                text_file_new.write(line)

				
