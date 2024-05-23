# 다중치환 암호화 - 플레이페어 암호화

## 암호화 방법
다중치환 암호화 중 플레이페어 암호화를 활용하여 암호화/복호화를 구현했습니다.

- # 1. 클래스 생성
  
```python  
class Playfair:
```
<br>

- ## (1) 생성자 정의, 인스턴스 변수를 생성
  
```python 
def __init__(self, plain_text, key_word, key_table=[], cipher_list=[]):
  self.plain_text = plain_text
  self.key_word = key_word
  self.key_table = key_table
  self.cipher_list = cipher_list
```

- plain_text : 평문
- key_word : 암호화에 사용될 키워드
- key_table : 5x5 2차원 리스트 암호판
- cipher_list : 암호문(리스트)
<br>

- ## (2) 5x5 알파벳 암호판 생성 함수
  
```python
def makeTable(self):

  # 입력받은 key_word 변수에서 중복되는 알파벳을 제거하고 순서대로 keytext 리스트에 삽입
  keytext=[]
  for a in self.key_word:
    if a not in keytext:
      keytext.append(a)

  # ‘a’~‘z’ 알파벳 중 key_word에 사용되지 않은 글자를 keytext에 추가
  # (‘i’와 ‘j’는 같은 단어 취급을 위해 ‘j’는 key_table에서 제외)
  alph = 'abcdefghijklmnopqrstuvwxyz'
  for a in alph:
    if a not in keytext:
      if a != 'j':
        keytext.append(a)

  # key_table에 5개의 빈 공간을 만들고, 각 공간마다 5개의 keytext에 삽입된 알파벳을 2차원 리스트 key_table에 순서대로 삽입
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
```
<br>

- ## (3) 암호화 함수
```python
def Encryption(self):

  # 입력받은 plain_text에서 ‘j’를 ‘i’로 교체 후 chg_text 리스트에 삽입
  chg_text=[]
  for a in self.plain_text:
      if a == 'j':
          a = 'i'
          chg_text.append(a)
      else:
          chg_text.append(a)

  # chg_text에서 띄어쓰기 제거
  for blank in chg_text:
    if blank==' ':
      chg_text.remove(' ')

  # chg_text를 두 글자씩 끊었을 때 붙어있는 두 글자가 같을 경우에 사이에 ‘x’ 추가
  n=0
  for i in range(int(len(chg_text)/2)):
      if chg_text[n] == chg_text[n+1]:
          chg_text.insert(n+1, 'x')
      n = n+2

  # chg_text 총 글자수가 홀수일 경우 끝에 ‘x’ 추가하여 글자 수를 짝수로 변경
  if len(chg_text)%2 == 1:
    chg_text.append("x")

  # chg_text를 두 글자씩 끊어서 chg_text2리스트에 삽입
  chg_text2=[]
  i=0
  for a in range(0, int(len(chg_text)/2)):
    chg_text2.append(chg_text[i:i+2])
    i=i+2

  # 두 문자를 테이블과 비교하고, cipher_list에 삽입
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

    # 경우 1. 두 문자가 같은 행에 있는 경우
    # 각각 오른쪽 문자로 변경(맨 오른쪽 문자인 경우 맨 왼쪽 문자로 변경)
    if r1 == r2:
      if r1 == 4:
        r1 = -1
      if r2 == 4:
        r2 = -1
      self.cipher_list.append(self.key_table[r1][c1+1])
      self.cipher_list.append(self.key_table[r2][c2+1])

    # 경우 2. 두 문자가 같은 열에 있는 경우
    # 각각 아래쪽 문자로 변경(맨 아래쪽 문자인 경우 맨 위쪽 문자로 변경)
    elif c1 == c2:
      if r1 == 4:
        r1 = -1
      if r2 == 4:
        r2 = -1
      self.cipher_list.append(self.key_table[r1+1][c1])
      self.cipher_list.append(self.key_table[r2+1][c2])

    # 경우 3. 경우 1,2 둘 다 아닌 경우
    # 같은 행에서 두 문자의 열이 만나는 곳에 위치한 문자로 변경
    else:
      self.cipher_list.append(self.key_table[r1][c2])
      self.cipher_list.append(self.key_table[r2][c1])

  #join함수를 사용해서 cipher_list(리스트)를 cipher_text(문자열)로 변경 후 출력
  cipher_text=''.join(self.cipher_list)
  print('cipher_text\n', cipher_text, '\n')
```
<br>

- ## (4) 복호화 함수 정의
```python
def Decryption(self):

  # 두 글자씩 key_table과 비교 후 org_list에 삽입
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

    # 경우 1. 두 문자가 같은 행에 있는 경우
    # 각각 왼쪽 문자로 변경(맨 왼쪽 문자인 경우 맨 오른쪽 문자로 변경)
    if r1 == r2:
      if c1 == 0:
        c1 = 5
      if c2 == 0:
        c2 = 5
      org_list.append(self.key_table[r1][c1-1])
      org_list.append(self.key_table[r2][c2-1])

    # 경우 2. 두 문자가 같은 열에 있는 경우
    # 각각 위쪽 문자로 변경(맨 위쪽 문자인 경우 맨 아래쪽 문자로 변경)
    elif c1 == c2:
      if r1 == 0:
        r1 = 5
      if r2 == 0:
        r2 = 5
      org_list.append(self.key_table[r1-1][c1])
      org_list.append(self.key_table[r2-1][c2])

    # 경우 3. 경우 1,2 둘 다 아닌 경우
    # 같은 행에서 두 문자의 열이 만나는 곳에 위치한 문자로 변경
    else:
      org_list.append(self.key_table[r1][c2])
      org_list.append(self.key_table[r2][c1])
    n = n+2

  # org_list에 ‘x’ 문자 제거
  for a in range(len(org_list)):
    if 'x' in org_list:
      org_list.remove('x')

  # join함수를 사용해서 org_list(리스트)를 org_text(문자열)로 변경 후 출력
  org_text=''.join(org_list)
  print('original_text\n', org_text, '\n')
```
<br>

## *사용예시*
```python
plaintext = 'we will invade north korea tomorrow'
print('plaintext\n', plaintext, '\n')
keyword = 'peninsula'
myEncryption = Playfair(plaintext, keyword)
myEncryption.makeTable()
myEncryption.Encryption()
myEncryption.Decryption()
```
