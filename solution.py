""" Question 1 """

def make_matrix(rows , colmns , mat):
    
    ''''Creating a Dispatch to Get Access to the Matrix variables '''
    def dispatch(cmd):
        if cmd == 0 :
            return rows
        elif cmd == 1 :
            return colmns
        elif cmd == 2:
            return mat
    
    return dispatch



def AddMatrix(m1 , m2):
  
    if m(m1) != m(m2) or n(m1) != n(m2) :
        print('The Two matrix must be same Dimension')
        return make_matrix(0 , 0 , [])
    
    cols = m(m1)
    rows = n(m1)
    mat1 = matrix(m1)
    mat2 = matrix(m2)
    
    newMatrix = []
    for i in range(rows * cols) :
        newMatrix.append(mat1[i] + mat2[i])

    return make_matrix(rows , cols , newMatrix)

def PrintMatrix(mat):
    '''Get Dimension and matrix it self'''
    
    cols = m(mat)
    rows = n(mat)
    matr = matrix(mat)
    
    for i in range(rows * cols) :
        '''Print New Line except for the first ROW'''
        if i % cols == 0 and i != 0:
            print()
        print(matr[i] , end = ' ')

def MulMatrix(m1 , m2):
    
    '''
        m1 => m1*n1 X m2*n2 => (n1 == m2)
        newSize => m1Xn2
    '''
    
    firstMatrixRow = n(m1)
    firstMatrixCol = m(m1)
    secondMatrixRow = n(m2)
    secondMatrixCol = m(m2)
    
    mat1 = matrix(m1)
    mat2 = matrix(m2)
    
    if firstMatrixCol != secondMatrixRow:
        print('The first matrix column number must be the same as second matrix row')
        return make_matrix(0 , 0 , [])
    """
     1 2 3      => 123456
     4 5 6
     
     3 4
     5 6        => 346733
     7 8
     
     34  40
     79  94
     
    """
    newlst = []
    
    for i in range(firstMatrixRow * secondMatrixCol) :
        rowIndex = (i // firstMatrixRow) * firstMatrixCol
        colIndex = i % secondMatrixCol
        sum=0 
        for _ in range(firstMatrixCol) :
            
            sum += (mat1[rowIndex] * mat2[colIndex]) 
            rowIndex += 1
            colIndex += secondMatrixCol
            
        newlst.append(sum)
    
   
    return make_matrix(firstMatrixRow , secondMatrixCol , newlst)
    


def InvertMatrix(ma):
    row = n(ma)
    col = m(ma)
    
    mat = matrix(ma)
    
    """ 
    1 2 3
    4 5 6
    
    (123456)
    
    1 4
    2 5
    3 6
    
    (142536)
    
    """
    newlst = []
    count = 0
    
    for _ in range(0 , row * col , row) :
        for j in range(count , row * col , col) :
            newlst.append(mat[j])
        count += 1
    
    return make_matrix(col , row , newlst)
    
def m(mat):
    """ return columns """
    return mat(1)


def n(mat):
    """ return rows """
    return mat(0)


def matrix(mat):
    """ return matrix """
    return mat(2)

    
m1 = make_matrix(2, 3, [1,2,3,4,5,6])
m2 = make_matrix(3, 2, [3,4,5,6,7,8])


''' PrintMatrix(MulMatrix(m1, m2))'''



""" Question 2 """


def data_preprocessing(data):
    return clean(list(data.split(',')))
 
def clean(data):
    return complete_filter(list(filter(lambda x : len(x) == 1 or x == '', data)))

def complete_filter(data):
    
    for i in range(len(data)) :
        
        if data[i] == '' :
            data[i] = (int(data[i - 1]) + int(data[i + 1])) //2

    return list(map(lambda x : int(x) , data))


def data_processing_histogram(data , min_dt , max_dt):
    lst = []
    found ,count = 0 , 0
    
    for item in data :
        if lst != [] :
            for var in lst :
                if item == var[0] :
                    found = 1
            if found == 0 :
                for var in data :
                    if var == item :
                        count += 1
                lst.append((item , count))
        else :
            for var in data :
                if var == item :
                    count += 1
            
            lst.append((item , count))        
        
        found = 0
        count = 0
    
    return lst
    
def data_preprocessing_range(data , min_dt , max_dt):
    min , max , avg = max_dt,min_dt,0
    
    for item in data :
        if item > max :
            max = item
        if item < min :
            min = item
        avg += item
    
    avg = avg / (len(data))
    return tuple((min , avg , max))

'''
data = "1,1,,100,3,5,5,5,,1,2,3"
min_val , max_val = 0 , 10
data = data_preprocessing(data) 
print(data)
print(data_preprocessing_range(data, min_val, max_val))
print(data_processing_histogram(data, min_val, max_val))
'''


""" Question 3 """

def make_date(day = None , month = None , year = None):
    
    d , m , y = day , month , year
    
    if day == None:
        d = 1
    if month == None:
        m = 1
    if year == None:
        y = 2017

    def View(format = None):
        
        if format == None :
            print('{0}/{1}/{2}'.format(d , m , y))
        elif format == 'mdy' :
            print('{0}/{1}/{2}'.format(m , d , y))
        elif format == 'ymd' :
            print('{0}/{1}/{2}'.format(y , m , d))
        else:
            print('format error')
    
    def Set(prop , val):
        nonlocal d,m,y
        if prop == 'day' :
            d = val
        elif prop == 'month' :
            m = val
        elif prop == 'year' :
            y = val
    
    def Get(prop):
        if prop == 'day' :
            return d
        elif prop == 'month' :
            return m
        elif prop == 'year' :
            return y
    
    def NextDate():
        
        nonlocal m,d,y
        maxDays = 0
        ''' 31 Days'''
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            maxDays = 31
        elif m == 2 :
            maxDays = 28    
        else :
            maxDays = 30
        
        if d == maxDays :
            d = 1
            m += 1
            if m > 12 :
                m = 1
                y += 1
        else :
            d += 1
                
    def DaysBetween(d2):
        if y == d2('get')('year') and m == d2('get')('month') :
            return abs(d - d2('get')('day'))
        else :
            return -1
    
    def dispatch(msg):
        if msg == 'view' :
            return View
        elif msg == 'set' :
            return Set
        elif msg == 'get' :
            return Get
        elif msg == 'nextdate' :
            NextDate()
        elif msg == 'days between dates' :
            return DaysBetween
        else :
            return 'Command Was Not Found'
    return dispatch

'''    
d1 = make_date()
d2 = make_date(23,1,2018)
d1('view')()
d2('view')()
d1('set')('year' , 2018)
d1('set')('month' , 1)

print(d1('days between dates')(d2))
'''



""" Question 4 """

def make_sequence(sequence):
    
    def all_filter(f = None):
        return tuple(filter(f , sequence))
    
    def return_filter(f = None):
        
        index = 0
        res = tuple(filter(f , sequence))
        
        def next():
            nonlocal index
            print(res[index])
            index += 1
            if index >= len(res) :
                index = 0
            
        def rev():
            nonlocal index
            print(res[len(res) - index - 1])
            index += 1
            if index < 0 :
                index = len(res) - 1
            
        return {'next' : next , 'reverse' : rev}
    
    def reverse():
        return tuple(list(sequence[::-1]))
    
    def extend(seq):
        nonlocal sequence
        sequence = list(sequence)
        for item in seq :
            sequence.append(item)
        return tuple(sequence)
    
    def clear():
        nonlocal sequence
        sequence = tuple()
    
    dispatch = {'all_filter' : all_filter , 'return_filter' : return_filter , 'reverse' : reverse
                ,'extend' : extend , 'clear' : clear}
    
    return dispatch

'''
a = make_sequence((1,2,3,4,5))
b = make_sequence([1,2,3,4,5])

p1 = a['return_filter'](lambda x : x < 4)

p1['next']()

for _ in range(5) :
    p1['next']()


print(a['reverse']())
print(a['extend'](a['all_filter'](lambda x: x%2!=0)))
print(a['all_filter'](lambda x: x>2))
a['clear']()
print(a['all_filter']())
'''
    
    
    
""" Question 5 """
def make_mutable_rlist(Constructor = None):
    
    content = empty_rlist
    index = 0
    
    if Constructor != None :
        content = Constructor['getContent']()
        
    def getContent():
        return content
    
    def push_first(value):
        nonlocal content
        content = addToList(value , content)
        
    def strr():
        return str(content)
    
    def insert(index , obj):
        nonlocal content
        content.insert(index, obj)
    def slice(startIndex , endIndex):
        
        newArr = content[startIndex:endIndex]
        it = make_mutable_rlist()
        
        for i in range(len(newArr) - 1 , -1 , -1) :
            it['push_first'](newArr[i])
        return it
    
    def get_iterator():

        index = 0
        
        def next():
            nonlocal index
            if index >= len(content) :
                return "No More Items"
            index += 1
            return content[index - 1]
        
        def hasNext():  
            nonlocal index
            if index < len(content) :
                return True
            return False
        
        return {'hasNext' : hasNext , 'next' : next}
    
    return {'getContent' : getContent , 'push_first' : push_first , 'str' : strr , 'insert' : insert ,'slice' : slice , 'get_iterator' : get_iterator}
    
empty_rlist = []

def addToList(first , rest):

    arr = []
    
    arr.append(first)
    for item in rest :
        arr.append(item)
    
    return arr


my_list = make_mutable_rlist()
for x in range(4) :
    my_list['push_first'](x)
print(my_list['str']())

my_list['insert'](1,5)
print(my_list['str']())

print(my_list['slice'](0,2)['str']())

your_list = make_mutable_rlist(my_list)
print(your_list['str']())

it = my_list['get_iterator']()
while it['hasNext']():
    print(it['next']())    

