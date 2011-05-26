#
# Copyright © 2011 Toby Ho
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the “Software”), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished 
# to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
prototype.py - A tiny python library that simulates prototype inheritence in javascript

# create a new type using @constructor
>>> from prototype import *
>>> @constructor
... def Person(this, first, last):
...   this.firstName = first
...   this.lastName = last
...
>>> Person
<constructor 'Person'>

# initialize an instance
>>> bird = Person('Charlie', 'Parker')
>>> bird.firstName
'Charlie'
>>> bird.lastName
'Parker'

# dynamically add attributes
>>> bird.instrument = 'alto sax'
>>> bird.instrument
'alto sax'

# unset attributes just return None
>>> print bird.age
None

# add methods to the instance
>>> def sing(this):
...   print '%s sings!!' % this.lastName
...
>>> bird.sing = sing
>>> bird.sing()
Parker sings!!

# use the prototype chain to add properties and methods to the type
>>> def getName(this):
...   return '%s %s' % (this.firstName, this.lastName)
...
>>> Person.prototype.name = property(getName)
>>> bird.name
'Charlie Parker'
>>> def greet(this):
...   print 'Hello, my name is %s' % this.name
...
>>> Person.prototype.greet = greet
>>> bird.greet()
Hello, my name is Charlie Parker
>>> monk = Person('Thelonious', 'Monk')
>>> monk.greet()
Hello, my name is Thelonious Monk

# property setter
>>> def setName(this, name):
...   first, last = name.split(' ')
...   this.firstName = first
...   this.lastName = last
...
>>> Person.prototype.name = property(getName, setName)
>>> bird.name = 'Dizzy Gillespie'
>>> bird.firstName
'Dizzy'
>>> bird.lastName
'Gillespie'

# property deleter
>>> def deleteName(this):
...   print 'Deleting %s.' % this.name
...   del this.firstName
...   del this.lastName
...
>>> Person.prototype.name = property(getName, setName, deleteName)
>>> del bird.name
Deleting Dizzy Gillespie.
>>> bird.name
'None None'

# using prototype inheritence
>>> father = Person('Tom', 'Bard')
>>> son = Person('Tommy', 'Bard')
>>> son.__proto__ = father
>>> father.eyeColor = 'blue'
>>> son.eyeColor
'blue'

# prototype chain relationships
>>> assert son.__proto__ == father
>>> assert son.constructor == father.constructor == Person
>>> assert father.__proto__ == Person.prototype
>>> assert Object.prototype.constructor == Object
>>> assert Person.prototype.constructor == Person
>>> assert Person.prototype.__proto__ == Object.prototype

# should work with lists
>>> father.children = [son]
>>> len(father.children)
1

# multi-level inheritence
>>> grandson = Person('Tony', 'Bard')
>>> grandson.__proto__ = son
>>> grandson.eyeColor
'blue'
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()