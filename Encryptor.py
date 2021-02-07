import time
import json
import random
import string
import sys


d = {
'a':['a65','6ba','7#m'], 'A':['bNt','%6f','zAS'],
'b':['#8t','$mn','97@'], 'B':['?vr','Z@4','9$%'],
'c':['%5s','Bs5','@7b'], 'C':['##s','Zq2','F56'],
'd':['>6b','5!o','^l7'], 'D':['R7M','b*6','M/?'],
'e':['b6!','C5#','&i0'], 'E':['Z1$','Zs5','@h&'],
'f':['fG$','i&0','-aQ'], 'F':['Z1~','<bF','Quf'],
'g':['O-0','3**','Qqe'], 'G':['+=l','^k9','xD?'],
'h':['56o','996','*we'], 'H':['!s4','Bf:','"gk'],
'i':['K~g','jk$','Vl%'], 'I':['Zq2','Bb6','7j9'],
'j':['[4[','m_1','er&'], 'J':['{[6','Np&','V7.'],
'k':['.m&','7.@','"bB'], 'K':['F2s','fV%','Gll'],
'l':['{t_',':*v','_--'], 'L':['#4V','|1X','F_p'],
'm':['?79',')bv','p:D'], 'M':['?_f','Qs_','=_d'],
'n':['XDD','~?5','Z~l'], 'N':['Fvd','!@1','!11'],
'o':['H0u','8fj','+7n'], 'O':['GSW','B^n','&h3'],
'p':['c3u','===','(}.'], 'P':['h#5','B.?','D2!'],
'q':['Bd8','h15','trl'], 'Q':['d$^','N()','Tr"'],
'r':['HiV',';q3','(0l'], 'R':['Cc#','M^^','!2@'],
's':['Lop','G##','56^'], 'S':['kL"','D5%','9)_'],
't':['|p~','Y-y','W67'], 'T':['!@3','#gG','^n>'],
'u':['<8U','x||',',vG'], 'U':['>?Z','Aq1','.vf'],
'v':['PO!','st*','A!h'], 'V':['ZzZ','7$h','Q[;'],
'w':['24B','4%3','J9*'], 'W':['(-+','++-','%g$'],
'x':['M[]','y"#','\5q'], 'X':['Bv>','||T','Wep'],
'y':['Np;','I4^','Em<'], 'Y':['{]%','!!f','BvW'],
'z':['/\@','Uf|','eB_'], 'Z':['!4*','4K&','$hl'],
',' :['g|/','|tf','#f5'] 
}

alist = ['a65','6ba','7#m']
blist = ['#8t','$mn','97@']
clist = ['%5,','Bs5','@7b']
dlist = ['>6b','5!o','^l7']
elist = ['b6!','C5#','&i0']
flist = ['fG$','i&0','-aQ']
glist = ['O-0','3**','Qqe']
hlist = ['56o','996','*we']
ilist = ['K~g','jk$','Vl%']
jlist = ['[4[','m_1','er&']
klist = ['.m&','7.@','"bB']
llist = ['{t_',':*v','_--']
mlist = ['?79',')bv','p:D']
nlist = ['XDD','~?5','Z~l']
olist = ['H0u','8fj','+7n']
plist = ['c3u','==-','(}.']
qlist = ['Bd8','h15','trl']
rlist = ['HiV',';q3','(0l']
slist = ['Lop','G##','56^']
tlist = ['|p~','Y-y','W67']
ulist = ['<8U','x||',',vG']
vlist = ['PO!','st*','A!h']
wlist = ['24B','4%3','J9*']
xlist = ['M[]','y"#','\5q']
ylist = ['Np;','I4^','Em<']
zlist = ['/\@','Uf|','eB_']

Alist = ['bNt','%6f','zAS']
Blist = ['?vr','Z@4','9$%']
Clist = ['##s','Zq2','F56']
Dlist= ['R7M','b*6','M/?']
Elist= ['Z1$','Zs5','@h&']
Flist= ['Z1~','<bF','Quf']
Glist= ['+=l','^k9','xD?']
Hlist= ['!s4','Bf:','"gk']
Ilist= ['Zq2','Bb6','7j9']
Jlist= ['{[6','Np&','V7.']
Klist= ['F2s','fV%','Gll']
Llist= ['#4V','|1X','F_p']
Mlist= ['?_f','Qs_','=_d']
Nlist= ['Fvd','!@1','!11']
Olist= ['GSW','B^n','&h3']
Plist= ['h#5','B.?','D2!']
Qlist= ['d$^','N()','Tr"']
Rlist= ['Cc#','M^^','!2@']
Slist= ['kL"','D5%','9)_']
Tlist= ['!@3','#gG','^n>']
Ulist= ['>?Z','Aq1','.vf']
Vlist= ['ZzZ','7$h','Q[;']
Wlist= ['(-+','++-','%g$']
Xlist= ['Bv>','||T','Wep']
Ylist= ['{]%','!!f','BvW']
Zlist= ['!4*','4K&','$hl']
commalist = ['g|/','|tf','#f5']

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:$#@!%^&*(){}~":;/\|+=-_[]<>'

def command_console():
    global cmd
    print("Type quit to exit")
    cmd = input("Encrypt or Decrypt? ")
    if cmd == 'encrypt':
        encrypt_console()
    elif cmd == 'decrypt':
        decrypt_console()
    elif cmd == 'instaE':
        InstaEncrypt_console()
    elif cmd == 'quit':
        sys.exit()
    else:
        print("Invalid Prompt")

def encrypt_console():
    E=input ('Enter text: ')
    inputword = list(E)
    print (inputword)
    if ' ' in inputword:
        X = inputword.count(' ')
        for l in range (0,X):
            inputword.remove(' ')
    print('Encrypting...')
    time.sleep(4)
    for key in d.keys():
        if key in inputword:
            for i in range(len(inputword)):
                if inputword[i] == key:
                    try:
                        inputword[i] = str(random.choice(d[key]))
                    except:
                        pass

    result = ''.join(inputword)
    target = result
    attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
    attemptNext = ''

    completed = False

    while completed == False:
        print(attemptThis)
        attemptNext = ''
        completed = True
        for i in range(len(target)):
            if attemptThis[i] != target[i]:
                completed = False
                attemptNext += random.choice(possibleCharacters)
            else:
                attemptNext += target[i]
        attemptThis = attemptNext
        time.sleep(0.1)
    filename = 'crypt.json'
    with open(filename, 'w') as f_obj:
        json.dump(result, f_obj)
    print ('Text encrypted into crypt file.')

def InstaEncrypt_console():
    E=input ('Enter text: ')
    inputword = list(E)
    print (inputword)
    if ' ' in inputword:
        X = inputword.count(' ')
        for l in range (0,X):
            inputword.remove(' ')
    print('Encrypting...')
    for key in d.keys():
        if key in inputword:
            for i in range(len(inputword)):
                if inputword[i] == key:
                    try:
                        inputword[i] = str(random.choice(d[key]))
                    except:
                        pass
    result = ''.join(inputword)
    print(result)
    filename = 'crypt.json'
    with open(filename, 'w') as f_obj:
        json.dump(result, f_obj)
    print ('Text encrypted into crypt file.')

def InstaEncrypt_email(E):
    inputword = list(E)
    print (inputword)
    if ' ' in inputword:
        X = inputword.count(' ')
        for l in range (0,X):
            inputword.remove(' ')
    print('Encrypting...')
    for key in d.keys():
        if key in inputword:
            for i in range(len(inputword)):
                if inputword[i] == key:
                    try:
                        inputword[i] = str(random.choice(d[key]))
                    except:
                        pass
    result = ''.join(inputword)
    return result


def decrypt_console(result = None):
        if result:
            pass
        else:
            with open ('crypt.json') as f_obj:
                result = json.load(f_obj)
        print(result)
        print("Decrypting...")
        possibilities = ['6ba','7#','#8','$mn','97@','%5','Bs5','@7b','>6b','5!','^l7','b6!','C5#','$i0','fG$','i&0','-aQ','O-0','3*','Q','56o','99','*we','K','jk','V','[4','m_1','er','.m&','7.@','"','{t',':*v','_-','?79',')bv','p:D','XD','~?5','Z~l','H0u','8fj','+7n','c3u','==','(}.','Bd8','h15','trl','Hi',';q3','(0','Lop','G#','5','|p','Y-y','W67','<8','x',',','PO','st','A','24','4%3','J9*','M[]','y"','\5q','Np','I4^','E','/','Uf','e]'
                             ]
        end_result = ('')
        n = 3
        E_ready = [result[i:i+n] for i in range(0, len(result), n)]
        if (' ') in E_ready:
            E_ready.remove(' ')
        for letter in E_ready:
            if letter == " ":
                end_result += ' '
            if letter in alist:
                end_result += 'a'
            if letter in blist:
                end_result += 'b'
            if letter in clist:
                end_result += 'c'
            if letter in dlist:
                end_result += 'd'
            if letter in elist:
                end_result += 'e'
            if letter in flist:
                end_result += 'f'
            if letter in glist:
                end_result += 'g'
            if letter in hlist:
                end_result += 'h'
            if letter in ilist:
                end_result += 'i'
            if letter in jlist:
                end_result += 'j'
            if letter in klist:
                end_result += 'k'
            if letter in llist:
                end_result += 'l'
            if letter in mlist:
                end_result += 'm'
            if letter in nlist:
                end_result += 'n'
            if letter in olist:
                end_result += 'o'
            if letter in plist:
                end_result += 'p'
            if letter in qlist:
                end_result += 'q'
            if letter in rlist:
                end_result += 'r'
            if letter in slist:
                end_result += 's'
            if letter in tlist:
                end_result += 't'
            if letter in ulist:
                end_result += 'u'
            if letter in vlist:
                end_result += 'v'
            if letter in wlist:
                end_result += 'w'
            if letter in xlist:
                end_result += 'x'
            if letter in ylist:
                end_result += 'y'
            if letter in zlist:
                end_result += 'z'

            if letter in Alist:
                end_result += 'A'
            if letter in Blist:
                end_result += 'B'
            if letter in Clist:
                end_result += 'C'
            if letter in Dlist:
                end_result += 'D'
            if letter in Elist:
                end_result += 'E'
            if letter in Flist:
                end_result += 'F'
            if letter in Glist:
                end_result += 'G'
            if letter in Hlist:
                end_result += 'H'
            if letter in Ilist:
                end_result += 'I'
            if letter in Jlist:
                end_result += 'J'
            if letter in Klist:
                end_result += 'K'
            if letter in Llist:
                end_result += 'L'
            if letter in Mlist:
                end_result += 'M'
            if letter in Nlist:
                end_result += 'N'
            if letter in Olist:
                end_result += 'O'
            if letter in Plist:
                end_result += 'P'
            if letter in Qlist:
                end_result += 'Q'
            if letter in Rlist:
                end_result += 'R'
            if letter in Slist:
                end_result += 'S'
            if letter in Tlist:
                end_result += 'T'
            if letter in Ulist:
                end_result += 'U'
            if letter in Vlist:
                end_result += 'V'
            if letter in Wlist:
                end_result += 'W'
            if letter in Xlist:
                end_result += 'X'
            if letter in Ylist:
                end_result += 'Y'
            if letter in Zlist:
                end_result += 'Z'
            if letter in commalist:
                end_result += ','
        print ('Crypt was successfully decrypted, result is: ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(end_result)
        return end_result