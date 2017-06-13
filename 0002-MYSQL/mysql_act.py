
#目标：200个16个大小写英文、数字组成的激活码 
#类似xxxx-xxxx-xxxx-xxxx
import random,string
import pymysql
CHRLIST=string.ascii_letters+string.digits
codelist=[]
#test repeat
#CHRLIST='1234'
def single_code(lens):
    code=''
    for x in range(lens):
        i=random.randint(0,CHRLIST.__len__()-1)
        code+=CHRLIST[i]
    return '-'.join(code[i:i+4] for i in range(0,len(code),4))
 
def many_code(lens,n):   
    c=0
    while True:
        code=single_code(lens)
        if code in codelist:
            c=c
        else:
            codelist.append(code)
            c=c+1 
        if c==n:
            break
    print(len(codelist))
#many_code(长度，激活码数量)
many_code(16,200)


conn = pymysql.connect(user='root',password='password',database='test')
cursor = conn.cursor()
cursor.execute('''create table if not exists actcode(
    id smallint primary key,
    code varchar(50) not null);
    ''')
cursor.execute('delete from actcode')
for i,_code in enumerate(codelist):
    cursor.execute('insert actcode(id,code) values (%s,"%s")'%(i,_code))
conn.commit()
cursor.close()
conn.close()