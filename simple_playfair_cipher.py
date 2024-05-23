class Playfair:
    def __init__(self, plain_text, key_word, key_table=[], cipher_list=[]):
        self.plain_text = plain_text
        self.key_word = key_word
        self.key_table = key_table
        self.cipher_list = cipher_list

    def makeTable(self):
        keytext=[]
        for a in self.key_word:
            if a not in keytext:
                keytext.append(a)
        print('keyword\n', keytext, '\n')

        alph = 'abcdefghijklmnopqrstuvwxyz'
        for a in alph:
            if a not in keytext:
                if a != 'j':
                    keytext.append(a)
                
        for i in range(5):
            self.key_table.append('')
        self.key_table[0] = keytext[0:5]
        self.key_table[1] = keytext[5:10]
        self.key_table[2] = keytext[10:15]        
        self.key_table[3] = keytext[15:20]
        self.key_table[4] = keytext[20:25]
        print('Table')
        for i in range(5):
            print(self.key_table[i])
        print('\n')

    def Encryption(self):
        chg_text=[]
        for a in self.plain_text:
            if a == 'j':
                a = 'i'
                chg_text.append(a)
            else:
                chg_text.append(a)

        for blank in chg_text:
            if blank==' ':
                chg_text.remove(' ')

        #print('chg_text\n', chg_text, '\n')
        
        n=0
        for i in range(int(len(chg_text)/2)):
            if chg_text[n] == chg_text[n+1]:
                chg_text.insert(n+1, 'x')
            n = n+2

        if len(chg_text)%2 == 1:
            chg_text.append("x")

        chg_text2=[]
        i=0
        for a in range(0, int(len(chg_text)/2)):
            chg_text2.append(chg_text[i:i+2])
            i=i+2
            
        i=j=0
        for a in chg_text2:
            for i in range(5):
                for j in range(5):
                    if self.key_table[i][j] == a[0]:
                        r1 = i
                        c1 = j
                for j in range(5):
                    if self.key_table[i][j] == a[1]:
                        r2 = i
                        c2 = j
            if r1 == r2:
                if c1 == 4:
                    c1 = -1
                if c2 == 4:
                    c2 = -1
                self.cipher_list.append(self.key_table[r1][c1+1])
                self.cipher_list.append(self.key_table[r2][c2+1])
            elif c1 == c2:
                if r1 == 4:
                    r1 = -1
                if r2 == 4:
                    r2 = -1
                self.cipher_list.append(self.key_table[r1+1][c1])
                self.cipher_list.append(self.key_table[r2+1][c2])
            else:
                self.cipher_list.append(self.key_table[r1][c2])
                self.cipher_list.append(self.key_table[r2][c1])
       
        cipher_text=''.join(self.cipher_list)
        #print('cipher_list\n', self.cipher_list, '\n')
        print('cipher_text\n', cipher_text, '\n')

    def Decryption(self):
        n=0
        org_list=[]
        for a in range(int(len(self.cipher_list)/2)):
            for i in range(5):
                for j in range(5):
                    if self.key_table[i][j] == self.cipher_list[n]:
                        r1 = i
                        c1 = j
                for j in range(5):
                    if self.key_table[i][j] == self.cipher_list[n+1]:
                        r2 = i
                        c2 = j
            if r1 == r2:
                if c1 == 0:
                    c1 = 5
                if c2 == 0:
                    c2 = 5
                org_list.append(self.key_table[r1][c1-1])
                org_list.append(self.key_table[r2][c2-1])
            elif c1 == c2:
                if r1 == 0:
                    r1 = 5
                if r2 == 0:
                    r2 = 5
                org_list.append(self.key_table[r1-1][c1])
                org_list.append(self.key_table[r2-1][c2])
            else:
                org_list.append(self.key_table[r1][c2])
                org_list.append(self.key_table[r2][c1])
            n = n+2

        for a in range(len(org_list)):
            if 'x' in org_list:
                org_list.remove('x')
        org_text=''.join(org_list)
        print('original_text\n', org_text, '\n')
        
#--------------------------------------------------

plaintext = 'we will invade north korea tomorrow’
print('plaintext\n', plaintext, '\n')
keyword = 'peninsula'
myEncryption = Playfair(plaintext, keyword)
myEncryption.makeTable()
myEncryption.Encryption()
myEncryption.Decryption()
