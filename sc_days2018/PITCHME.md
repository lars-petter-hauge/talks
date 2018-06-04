## Python 3

Note:
Agenda:
 - Brief history
 - Flaws in Python2
 - New features Python3

 ---

### Why Python 3
* Rectify design flaws
* >There should be one - and preferably only one - obvious way to do it
* Not possible to implement without breaking backwards compatibility

---
### Python Releases
IMAGE HERE..

Note:
Release dates:
 - 0.9 1991
 - 1.0 1994
 - 2.0 2000
 - 3.0 2008
 - 2.7 2010
 - 3.4 2014
 - 3.6 2016

---
### Python 3 Readiness
IMAGE HERE..

Note:
- Not intended: futures
- Deprecated (new package for Py3): google_test, Beautiful soup
- Should run Py3: ansible, Fabric

---
### Python 3 Arguments

* Fixed Flaws from Python2
* New Features

---
### Python 2 Issues

---
### Compare Everything!

In Python 2 it is possible to compare across types

```python
'one' < 2
False
```

* In Python 3 comparing different types raises a TypeError

```python
5 < '5'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-191465458398> in <module>()
----> 1 5 < '5'

TypeError: '<' not supported between instances of 'int' and 'str'
```
---
### Compare Everything!
* Implicit compare (sort(), max()..)
```python
sib_ages=[('Eirik', 30), ('Kristian', '23'), ('Jean-Paul', 60)]

sorted(sib_ages, key=lambda x:(x[1]))

[('Eirik', 30), ('Jean-Paul', 60), ('Kristian', '23')]
```
---
### Try-catch

---
### Extend Object

---
### String Handling

* In Python 2 the 'str' type only handles ASCII
* The 'unicode' was introduced in Python 2 to handle symbols other than ASCII
* Bytearray exist, but no byte type.
* The 'encode' and 'decode' allows to change type, but also requires an
* encoding - there are roughly 100 different encodings in Python 2.

Note:
 - ASCII (American Standard Code for Information Interchange) standardized in 1968
 - Defined bytes 0 to 127; 128 to 255 was used individually to defined accented
   characters. Different schemes existed in different places in the world.
 - What happends if you have the wrong scheme - or if you would like to use two
   different schemes in the same document -> hence the birth of unicode.
---
### String Handling
* Python 3 string type is instead <class 'str'>, which by default is unicode.
```python
>>> print('strings are now utf-8 \u03BCnico\u0394é!')
strings are now utf-8 μnicoΔé!
```
* Python 3 has both byte and bytearray
>>> print('Both byte',type(b'bytes..'),' and bytearray',
>>> type(bytearray(b'bytearrays')))
Both byte <class 'bytes'>  and bytearray <class 'bytearray'>
---
### List comprehension

* In Python 2 the iterator leaks
```python
>>> i = 0
>>> my_list = [i for i in xrange(5)]
>>> print (i)
4
```

---
### Input as raw_input

---
### Print

* Print in Python 3 is a function call.

```python
>>> x = 1; y = 2; print(f"{x} + {y} = {x + y}")
1 + 2 = 3
```

---
### Python 3 New Features

---
### Iterators are all

---
### Key Arguments

---
### Matrix Manipulation

---
### Format Literals

---
### Asyncio

```python
async def help_me(name, x):
    print ("Helping " + name)
    await asyncio.sleep(x)
    if x < 10:
        print("Finished helping " + name + ", that was easy!")
    else:
        print("Finished with " + name + ", he's a bit slower")

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(help_me("Lars Petter", 15)),
         asyncio.ensure_future(help_me("Sveinung", 5))]

loop.run_until_complete(asyncio.gather(*tasks))
```
gives:
```python
Helping Lars Petter
Helping Sveinung
Finished helping Sveinung, that was easy!
Finished with Lars Petter, he's a bit slower
```
---
### Function Annotations

---
### Pathlib
