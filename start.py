
import time
import re
from  start_check import start_process
option='1'
#option=input('Selection mode：1、单个网址 2、多个网址\n')
if option=='1':
    while True:
        url = input('请输入网址：')
        start = time.time ()
        proess = start_process (url)
        end = time.time ()
        print (end - start)
        for ii in range(len(proess)):
            print(proess[ii])
        pass_false = re.search ('错误', str (proess))
        doubt_false = re.search ('待确认', str (proess))
        if pass_false:
            print ('=============================Flase=============================')
        elif doubt_false:
            print ('=============================Doubt=============================')
        else:
            print(True)

if option=='2':
    i=0
    print('输入已完成请按“e”')
    urllist =[]
    while True:
        i=i+1
        url = input ('请输入第'+str(i)+'个网址：')
        if url =='e':
            break
        urllist.append(url)
    True_count=0
    False_count=0
    doubt_count=0
    for o in urllist:
        proess = start_process(o)
        o2=o.replace('https://lemonhd.org/','').replace('details_movie.php?id=','details_movie.php_id=')
        pass_false = re.search('错误', str(proess))
        doubt_false=re.search('待确认', str(proess))
        if pass_false:
            False_count=False_count+1
            print (o, False,False)
            f=open('False/'+o2.strip()+'.txt','w',encoding='utf8')
            f.write(o+'\n')
            for ii in range (len (proess)):
                #print (proess[ii])
                f.write(str(proess[ii])+'\n')
            f.close()
            f3 = open ('Questionable_All.txt', 'w', encoding='utf8')
            f3.write (o)
            f3.close ()
        elif doubt_false:
            doubt_count=doubt_count+1
            f2 = open ('Doubt/' + o2.strip()+'.txt', 'w',encoding='utf8')
            f2.write (o + '\n')
            print (o, False)
            for ii in range (len (proess)):
                #print (proess[ii])
                f2.write (str (proess[ii])+'\n')
            f2.close()
            f3=open ('Questionable_All.txt', 'w',encoding='utf8')
            f3.write(o)
            f3.close()
        else:
            print(o,True)
            True_count=True_count+1
    print('True:'+str(True_count),'False:'+str(False_count),'doubt:'+str(doubt_count))
end = time.time()
'''print ('已释放程序内存，5分钟后窗口将自动关闭')
time.sleep (300)'''
