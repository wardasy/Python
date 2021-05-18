#Name: Wardah Shekh Yousef ID: 209011501
#Name: Naseem Ali  ID: 312343668


''' Part 1 '''

inches_to_meters = lambda x : x * 0.0254
inches_to_feets = lambda x : x * (1 / 12)
miles_to_feets = lambda x : x * 5280

composition = lambda f,g : lambda x : f(g(x))

opposite = lambda f : lambda x : x * (1 / f(1))

""" 
 1 inches = 0.0254 meters
 1 meters = 1/0.0254 inches

 1 / f(1) => opposite unit

"""

feets_to_inches = opposite(inches_to_feets)
miles_to_inches = composition(feets_to_inches , miles_to_feets)
miles_to_meters = composition(inches_to_meters , miles_to_inches)
inches_to_miles = opposite(miles_to_inches)
feets_to_miles = composition(inches_to_miles , feets_to_inches)
feets_to_meters = composition(inches_to_meters , feets_to_inches)
meters_to_miles = opposite(miles_to_meters)
meters_to_feets = opposite(feets_to_meters)
meters_to_inches = opposite(inches_to_meters)


"""

#Examples

print(inches_to_meters(10))
print(feets_to_inches(10))
print(miles_to_inches(10))
 
 
"""


''' Part 2 '''

''' Q.1 '''

class Inches:
    
    def __init__(self , value) :
        ''' Constructor if its number of string if nether number nor string throw
        an exception else check format of string if its string and save the value 
        or throw an exception according to the type(unit) '''
        if type(value) == float or type(value) == int:
            self.value = value
        else :
            if type(value) == str :
                if 'in' in value :
                    value = value.replace("in", "")
                    self.value = float(value)
                else :
                    raise Exception("Format Error : {0}".format(value))
            else :
                raise Exception("Type Error : {0}".format(type(value)))

    def __str__(self):
        ''' return a string with unit '''
        return '{0} in'.format(self.value)
    
    def __repr__(self):
        ''' return a string with Class name and it's value'''
        return 'Inches({0})'.format(self.value)

class Meters:
    def __init__(self , value) :
        ''' Constructor if its number of string if nether number nor string throw
        an exception else check format of string if its string and save the value 
        or throw an exception according to the type(unit) '''
     
        if type(value) == float or type(value) == int:
            self.value = value
        else :
            if type(value) == str :
                if 'm' in value :
                    value = value.replace("m", "")
                    self.value = float(value)
                else :
                    raise Exception("Format Error : {0}".format(value))
            else :
                raise Exception("Type Error : {0}".format(type(value)))

    def __str__(self):
        ''' return a string with unit '''
        return '{0} m'.format(self.value)
    
    def __repr__(self):
        ''' return a string with Class name and it's value'''
        return 'Meters({0})'.format(self.value)


'''

 #Examples

for v in [25.8 , "25.8 in" , "25.8 ft" , [] , Inches] :
    try:
        print(str(Inches(v)))
    except Exception as e:
        print(e)
        
        
print(str(Inches(2.8)))
print(repr(Inches(2.8)))

print(str(Meters(2.8)))
print(repr(Meters(2.8)))

print(str(eval(repr(Inches(25.8)))))
m = eval(repr(Meters(25.8)))
print(m.value)

'''

''' Q.2 '''

""" Given Shmython """
### Our custom OOP
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized object instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    return cls


def make_feets_class():
    def __init__(self , value):
        if type(value) == float or type(value) == int:
            self['set']('value', value)
        else :
            if type(value) == str :
                if 'ft' in value :
                    value = value.replace("ft", "")
                    self['set']('value' ,float(value))
                else :
                    raise Exception("Format Error : {0}".format(value))
            else :
                raise Exception("Type Error : {0}".format(type(value)))
    
    
    def __str__(self):
        ''' return a string with unit '''
        return '{0} ft'.format(self['get']('value'))
    
    def __repr__(self):
        ''' return a string with Class name and it's value'''
        return "Feets['new']({0})".format(self['get']('value'))

    def __type__(self):
        return 'Feets'
    
    return make_class(locals())


def make_miles_class():
    def __init__(self , value):
        if type(value) == float or type(value) == int:
            self['set']('value', value)
        else :
            if type(value) == str :
                if 'mi' in value :
                    value = value.replace("mi", "")
                    self['set']('value' ,float(value))
                else :
                    raise Exception("Format Error : {0}".format(value))
            else :
                raise Exception("Type Error : {0}".format(type(value)))

    def __str__(self):
        ''' return a string with unit '''
        return '{0} mi'.format(self['get']('value'))
    
    def __repr__(self):
        ''' return a string with Class name and it's value'''
        return "Miles['new']({0})".format(self['get']('value'))

    def __type__(self):
        return 'Miles'

    return make_class(locals())


''' Q.3 '''

def to_str(f):
    
    ''' if Python class return str if shmython return by dictionary '''
    
    if type(f) == Inches or type(f) == Meters :
        return str(f)    
    else :
        return f['get']('__str__')()

def to_repr(f):
    ''' if Python class return repr if shmython return by dictionary '''
    
    if type(f) == bool :
        return f
    
    else :    
        if type(f) == Inches or type(f) == Meters :
            return repr(f)
    
        else :
            return f
    
def type_of(f):
    ''' if Python class return value if shmython return by dictionary '''
    
    try:
        if type(f) == Inches or type(f) == Meters :
            return f.value
    
        else :
            return f['get']('__type__')()
    except :
        pass
        #return type_of(f) #if it's TreeNode(TreeNode) Object
    
"""

#Examples

 
Feets = make_feets_class()
f = Feets['new']('25.8 ft')
print(f['get']('__str__')())
print(to_str(f))
print(f['get']('__repr__')())
print(to_repr(f))

Miles = make_miles_class()
m = Miles['new'](25.8)
print(m['get']('__str__')())
m = eval(to_repr(Miles['new'](25.8)))
print(m['get']('value'))
print(to_repr(Inches(25.8)))


"""


""" Part 3 """

def ConvertAnyTypeToInches(f):
    
    res = 0
    
    
    if type(f) == Inches :
        res = f.value
    
    if type(f) == Meters :
        res = meters_to_inches(f.value)
    
    elif type_of(f) == 'Miles' :
        res = miles_to_inches(f['get']('value'))
    
    elif type_of(f) == 'Feets' :
        res = feets_to_inches(f['get']('value'))
    
    return res


def SameTypeOfPython(var):
    if type(var) == Inches or type(var) == Meters :
        return True
    return False


def apply(action , f_Unit , s_Unit):
    """ Check first Parameter f_Unit if its Python Class or Shmython Instance """
    
    
    if action == 'eq' or action == '==' or action == 'gt' or action == '>':
        
        first , second = 0 , 0
        
        #Convert Everything to Inches And Compare
        
        first = ConvertAnyTypeToInches(f_Unit)
        second = ConvertAnyTypeToInches(s_Unit)
        
        
        if action == 'eq' or action == '==' :
            return first == second
    
        elif action == 'gt' or action == '>':
            return first > second
     
    else :
        
        
        #same type or python or shmython
        if SameTypeOfPython(f_Unit) == SameTypeOfPython(s_Unit) :
            if type(f_Unit) == Inches or type(f_Unit) == Meters :
                firstUnit = ConvertAnyTypeToInches(f_Unit)
                secondUnit = ConvertAnyTypeToInches(s_Unit)
        
                if action == 'add' :
                    f_Unit.value = firstUnit + secondUnit
                    return str(f_Unit)
        
                elif action == 'sub':
                    f_Unit.value = firstUnit - secondUnit
                    return str(f_Unit)
        
            else :
        
                
                firstUnit = ConvertAnyTypeToInches(f_Unit)
                secondUnit = ConvertAnyTypeToInches(s_Unit)
        
                if action == 'add' :
                    f_Unit['set']('value' , firstUnit + secondUnit)
                    return str(f_Unit)
        
                elif action == 'sub' :
                    f_Unit['set']('value' , firstUnit - secondUnit)
                    return str(f_Unit)
                
        else :
            if SameTypeOfPython(f_Unit) == True and SameTypeOfPython(s_Unit) == False :

                firstUnit = ConvertAnyTypeToInches(f_Unit)
                secondUnit = ConvertAnyTypeToInches(s_Unit)
        
        
                if action == 'add' :
                    f_Unit.value = firstUnit + secondUnit
                    return str(f_Unit)
        
                elif action == 'sub':
                    f_Unit.value = firstUnit - secondUnit
                    return str(f_Unit)
        
            elif SameTypeOfPython(f_Unit) == False and SameTypeOfPython(s_Unit) == True :
        
        
                firstUnit = ConvertAnyTypeToInches(f_Unit)
                secondUnit = ConvertAnyTypeToInches(s_Unit)
        
                if action == 'add' :
                    f_Unit['set']('value' , firstUnit + secondUnit)
                    return str(f_Unit)
        
                elif action == 'sub' :
                    f_Unit['set']('value' , firstUnit - secondUnit)
                    return str(f_Unit)
                

        
        
Feets = make_feets_class()
Miles = make_miles_class()

'''
print(apply('add' , Inches(1) , Meters(1.5)))
print(to_repr(apply('gt', Miles['new'](1) , Inches(1.5))))
print(to_repr(apply('gt', Inches(1.5) , Miles['new'](1) )))
print(to_repr(apply('>', Feets['new'](1) , Inches(1.5))))
print(to_repr(apply('>', Inches(1.5), Feets['new'](1))))
print(to_repr(apply('eq', Feets['new'](1) , Inches(feets_to_inches(1)))))
print(to_repr(apply('eq', Inches(1.5) , Feets['new'](inches_to_feets(1.5)))))
print(to_repr(apply('==', Feets['new'](1) , Inches(1.5))))
print(to_repr(apply('==', Inches(1.5) , Feets['new'](1))))
''' 

def ConvertToMeters(f):
    if type(f) == Meters :
        return f.value
    elif type(f) == Inches:
        return inches_to_meters(f.value)
    
    return 0 #in case of error

def coerce_apply(action , f_Unit , s_Unit):
    
    first , second = f_Unit.value , s_Unit.value
    
    if type(f_Unit) != type(s_Unit) :
        
        first , second = ConvertToMeters(f_Unit) , ConvertToMeters(s_Unit)
    
    else :
        if type(f_Unit) != Meters :
            first , second = ConvertToMeters(f_Unit) , ConvertToMeters(s_Unit)
            
    #Now We Have Same Class (Meters)
    if action == 'add' :
        return repr(Meters(first + second))
    
    elif action == 'sub' :
        return repr(Meters(first - second))

'''
print(coerce_apply('add', Meters(1.5) , Inches(1)))
print(coerce_apply('add', Inches(1) , Meters(1.5)))
print(coerce_apply('sub', Meters(1) , Inches(1.5)))
print(coerce_apply('sub', Inches(1.5) , Meters(1.5)))
'''

""" Part 4 """




class ValueExistsException(Exception):
    
    def __init__(self , value):
        self.error_msg = "Same Value Exists : {0}".format(value)
        super(Exception , self).__init__(self.error_msg)

class ValueNotExistsException(Exception):
    def __init__(self , value):
        self.error_msg = "Same Not Exist : {0}".format(value)
        super(Exception , self).__init__(self.error_msg)

class EmptyTreeException(Exception):
    def __init__(self):
        self.error_msg = "The Tree Is Empty"
        super(Exception , self).__init__(self.error_msg)



class TreeNode:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None
        self.isPython = self.GetType(value)
    
    def GetChildren(self):
        children = []
        
        if self.left != None :
            children.append(self.left)
        
        if self.right != None :
            children.append(self.right)
            
        return children

    #Get Current Type of Some Class
    def GetType(self, Class):
        try:
                        
            if type(Class.value) == Inches or type(Class.value) == Meters :
                return True
            return False

        except:
            return False
    
    def Insert(self , currentNode , newNode):
        
        isPython = True
        
        
        if self.GetType(newNode) == False :
            isPython = False
            
        if currentNode.value == newNode.value :
            raise ValueExistsException(repr(currentNode))
        
        
        if apply('>' , currentNode.value , newNode.value) == False :
            if currentNode.left == None :
                if isPython == True :
                    currentNode.left = newNode
                else :
                    currentNode.left = newNode
                    
                return currentNode
            else :
                currentNode.left.Insert(currentNode.left, newNode)
        
        else :
            if currentNode.right == None :
                if isPython == True :
                    currentNode.right = newNode
                else :
                    currentNode.right = newNode
                return currentNode
            else :
                currentNode.right.Insert(currentNode.right, newNode)
    
    def Search(self , currentNode , value):
        if currentNode == None :
            return None
        elif currentNode.value == value :
            return currentNode
        elif value < currentNode.value :
            return self.Search(currentNode.left,value)
        else :
            return self.Search(currentNode.right, value)
        
    def height(self , Node):
        if Node == None :
            return -1
        if self.GetType(Node) == True :
            leftHeight = self.height(Node.left)
            rightHeight = self.height(Node.right)
        
            if leftHeight > rightHeight :
                return leftHeight + 1
        
            return rightHeight + 1
        return 0
    def in_order(self , Node):
        
        if Node != None:
            return (self.in_order(Node.left) + [Node.value] + self.in_order(Node.right))
        else :
            return []
    
    def delete(self , node , value):
        
        if node == None :
            return node #None
        
        if self.GetType(node) == False :
            
            
            if node.value['get']('value') > value :
                node.left = self.delete(node.left, value)
        
            elif node.value['get']('value') < value :
                node.right = self.delete(node.right, value)
        
            else :
            
                #One Child Or No Children
            
                if node.left == None :
                    tmp = node.right
                    node = None
                    return tmp
            
                elif node.right == None :
                    tmp = node.left
                    node = None 
                    return tmp
            
                #Node with 2 children
            
                tmp = self.minValue(node.right)
                node.value = tmp.value
                node.right = self.delete(node.right, tmp.value)
        
            return node
        
        
        else :
        
            if node.value.value > value :
                node.left = self.delete(node.left, value)
        
            elif node.value.value < value :
                node.right = self.delete(node.right, value)
        
            else :
            
                #One Child Or No Children
            
                if node.left == None :
                    tmp = node.right
                    node = None
                    return tmp
            
                elif node.right == None :
                    tmp = node.left
                    node = None 
                    return tmp
            
                #Node with 2 children
            
                tmp = self.minValue(node.right)
                node.value = tmp.value
                node.right = self.delete(node.right, tmp.value)
        
            return node
    
    def minValue(self , node):
        current = node
        while current.left != None :
            current = current.left
            
        return current
    
    def __repr__(self):
        
        
        res = 'TreeNode({0}'.format(repr(self.value))
        
        if self.isPython == True :
        
            if self.left != None :
                res += ',left={0}'.format(repr(self.left.value))
            elif self.right != None :
                res += ',right={0}'.format(repr(self.right.value))
        else :
        
            if self.left != None :
                res += ',left={0}'.format(self.left.value['get']('__repr__')())
            elif self.right != None :
                res += ',right={0}'.format(self.right.value['get']('__repr__')())
            
        res += ')'
            
        return res
    
    def __str__(self):
        return self.__repr__()
    
class BSTree:
    
    def __init__(self):
        self.root = None  

    def delete(self , node):
        if self.root == None :
            raise EmptyTreeException()
        
        deleteResult = self.root.delete(self.root, node.value)
        
        if deleteResult == None :
            raise EmptyTreeException()
        
        return deleteResult
    
    def height(self , node = None):
        
        #search for specific node height
        if node != None :
            heightResult = self.root.height(node)
        else : #height of the tree
            heightResult = self.root.height(self.root)
    
        if heightResult == 0 :
            raise EmptyTreeException()
        
        return heightResult
    
    def in_order(self):
        return self.root.in_order(self.root)
    
    def search(self , node):
        
        if self.root == None :
            raise EmptyTreeException()
        
        searchResult = self.root.delete(self.root, node.value)
        
        if searchResult == None :
            raise EmptyTreeException()
        
        return searchResult

    def insert(self , Node):
        
        startedIndex = 0
        
        #insert a list
        if type(Node) == list : 
            if self.root == None :
                self.root = TreeNode(Node[0])
                startedIndex = 1
                
            for item in Node[startedIndex:] :
                self.root.Insert(self.root, TreeNode(item))
        
        
        else : 
            #insert single node
            if self.root == None :
                self.root = TreeNode(Node)
            else :
                self.root.Insert(self.root, TreeNode(Node))
        
    def __str__(self):
        
        
        tree = 'BSTree({0}'.format(self.root.__str__())
        
        if self.root != None :
        
            tree += ',left={0}'.format(self.sub_tree(self.root.left))
            tree += ',right={0}'.format(self.sub_tree(self.root.right))
        
        tree += ')'
        return tree
    
    
    def sub_tree(self , node):
        
        if node != None :
            if TreeNode.GetType(self, node) == True :
                self.sub_tree(node.left)
                return node.__str__()
                self.sub_tree(node.right)
              
    def __repr__(self):
        return self.__str__()
    

'''
try :

    Feets = make_feets_class()
    Miles = make_miles_class()
    
    tree = BSTree()
    print(tree)
    tree.insert(Meters(10))
    tree.insert(Inches(10))
    tree.insert(Feets['new'](10))
    tree.insert(Miles['new'](10))
    
    print(tree)
    print(tree.in_order())
    print('-- in order print after insert -----------------------------')
    for v in tree.in_order() :
        if(isinstance(v, dict)) :
            print(v['get']('__str__')() , end = ' = ')
        else :
            print(v , end = " = ")
    
        print(apply('add' , Meters(0) , v))
            
    tree.delete(Meters(0.254))
    print('-- in order print after delete -----------------------------')
    for v in tree.in_order() :
        if(isinstance(v, dict)) :
            print(v['get']('__str__')() , end = ' = ')
        else :
            print(v , end = " = ")
    
        print(apply('add' , Meters(0) , v))

except Exception as e:
    print('An Exception has been thrown :', "'{0}'".format(e))
'''