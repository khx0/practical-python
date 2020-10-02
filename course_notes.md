# course_notes.md

### 01 Introduction

* Python is a dynamically typed programming language. The perceived "type" of a variable might change as a program executes depending on the current value assigned to it.

* Python is case sensitive.

#### Interactive example snippet

```python
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
	print(pt.text)
```

### starting the course with python 3.7.6
```bash
bash $ python3
Python 3.7.6 (default, Feb 23 2020, 13:09:16) 
[Clang 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### fork the course repository via
```bash
bash $ git clone https://github.com/khx0/practical-python
bash $ cd practical-python
bash $
```
