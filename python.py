# Python 300 code Basic to Advanced 
##Section 1 — Python Basics (1–20)
# 1. Hello World
print("Hello, World!")

# 2. Variables
name = "Sayem"
age = 22
print(name, age)

# 3. Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

# 4. Swap without temp
x, y = 5, 10
x, y = y, x
print(x, y)  # 10 5

# 5. Type checking
print(type(42), type(3.14), type("hi"), type(True))

# 6. Type casting
print(int("100"), float("3.5"), str(99), bool(0))

# 7. Input from user (string)
# val = input("Enter something: ")

# 8. Input as integer
# n = int(input("Enter number: "))

# 9. Arithmetic operators
print(7 + 3, 7 - 3, 7 * 3, 7 / 3, 7 // 3, 7 % 3, 7 ** 3)

# 10. Comparison operators
print(5 > 3, 5 == 5, 5 != 4, 5 <= 5)

# 11. Logical operators
print(True and False, True or False, not True)

# 12. Constants convention (uppercase)
PI = 3.14159
GRAVITY = 9.8

# 13. f-strings
temp = 36.6
print(f"Body temp is {temp}°C")

# 14. f-string with formatting
val = 3.14159
print(f"{val:.2f}")  # 3.14

# 15. Multi-line string
text = """Line 1
Line 2
Line 3"""
print(text)

# 16. Comments — single and multi
# eta single line comment
"""eta basically docstring-style block"""

# 17. None type
result = None
print(result is None)  # True

# 18. Walrus operator (:=)
if (n := 10) > 5:
    print(f"{n} is greater than 5")

# 19. Chained comparison
age = 25
print(18 <= age < 60)  # True

# 20. Ternary (conditional expression)
score = 75
grade = "Pass" if score >= 50 else "Fail"
print(grade)
```

---

## 🔤 Section 2 — Strings (21–45)

```python
# 21. String length
s = "competitive programming"
print(len(s))

# 22. Indexing & negative indexing
print(s[0], s[-1])

# 23. Slicing
print(s[0:11])      # competitive
print(s[::-1])      # reversed
print(s[::2])       # every 2nd char

# 24. Upper / lower / title
print("hello".upper(), "HELLO".lower(), "hello world".title())

# 25. strip / lstrip / rstrip
print("  spaces  ".strip())

# 26. replace
print("aaa".replace("a", "b"))

# 27. split
print("a,b,c".split(","))

# 28. join
print("-".join(["2025", "06", "25"]))

# 29. find & index
print("hello".find("l"), "hello".index("l"))

# 30. count occurrences
print("banana".count("a"))

# 31. startswith / endswith
print("file.py".endswith(".py"), "abc".startswith("ab"))

# 32. isdigit / isalpha / isalnum
print("123".isdigit(), "abc".isalpha(), "a1".isalnum())

# 33. zfill — pad with zeros
print("42".zfill(5))  # 00042

# 34. center / ljust / rjust
print("hi".center(10, "*"))

# 35. String repetition
print("=" * 20)

# 36. Check substring
print("py" in "python")

# 37. Iterate over characters
for ch in "abc":
    print(ch, end=" ")
print()

# 38. enumerate over string
for i, ch in enumerate("abc"):
    print(i, ch)

# 39. format() method
print("{} + {} = {}".format(2, 3, 5))

# 40. Named format
print("{name} is {age}".format(name="Sayem", age=22))

# 41. Raw string (no escape)
print(r"C:\new\path")

# 42. Multi-line f-string
a, b = 3, 4
print(f"""
a = {a}
b = {b}
sum = {a+b}
""")

# 43. casefold (aggressive lowercase)
print("STRASSE".casefold())

# 44. partition
print("key=value".partition("="))  # ('key', '=', 'value')

# 45. swapcase
print("Hello World".swapcase())
```

---

## 📋 Section 3 — Lists (46–70)

```python
# 46. Create & access
nums = [10, 20, 30, 40]
print(nums[0], nums[-1])

# 47. append / extend
nums.append(50)
nums.extend([60, 70])
print(nums)

# 48. insert at index
nums.insert(0, 5)
print(nums)

# 49. remove by value
nums.remove(5)
print(nums)

# 50. pop by index
last = nums.pop()
print(last, nums)

# 51. del statement
lst = [1, 2, 3, 4]
del lst[1]
print(lst)

# 52. index of element
print([10, 20, 30].index(20))

# 53. count occurrences
print([1, 1, 2, 3, 1].count(1))

# 54. sort (in place)
a = [3, 1, 2]
a.sort()
print(a)

# 55. sort descending
a.sort(reverse=True)
print(a)

# 56. sorted (new list)
print(sorted([3, 1, 2]))

# 57. sort by key
words = ["ccc", "a", "bb"]
print(sorted(words, key=len))

# 58. reverse
a = [1, 2, 3]
a.reverse()
print(a)

# 59. Slicing assignment
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30]
print(nums)

# 60. List copy (shallow)
orig = [1, 2, 3]
copy1 = orig.copy()
copy2 = orig[:]
print(copy1, copy2)

# 61. min / max / sum
print(min(nums), max(nums), sum(nums))

# 62. List from range
print(list(range(1, 11)))

# 63. Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = [x for sub in nested for x in sub]
print(flat)

# 64. Remove duplicates (keep order)
seen, out = set(), []
for x in [1, 2, 2, 3, 1]:
    if x not in seen:
        seen.add(x); out.append(x)
print(out)

# 65. zip two lists
names = ["a", "b"]; scores = [90, 80]
print(list(zip(names, scores)))

# 66. unzip
pairs = [(1, 'a'), (2, 'b')]
nums2, chars = zip(*pairs)
print(nums2, chars)

# 67. all / any
print(all([True, True]), any([False, True]))

# 68. List multiplication (careful with refs!)
row = [0] * 5
print(row)

# 69. 2D list properly
grid = [[0]*3 for _ in range(3)]
print(grid)

# 70. Find index with condition
data = [5, 8, 2, 9]
idx = next(i for i, v in enumerate(data) if v > 7)
print(idx)
```

---

## 🗂️ Section 4 — Tuples, Sets, Dicts (71–100)

```python
# 71. Tuple basics
t = (1, 2, 3)
print(t[0], len(t))

# 72. Single element tuple (comma needed!)
single = (5,)
print(type(single))

# 73. Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)

# 74. Star unpacking
first, *rest = [1, 2, 3, 4]
print(first, rest)

# 75. Tuple is immutable
# t[0] = 99  # TypeError

# 76. namedtuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)

# 77. Set creation
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}

# 78. Add / remove
s.add(4); s.discard(2)
print(s)

# 79. Union
print({1, 2} | {2, 3})

# 80. Intersection
print({1, 2, 3} & {2, 3, 4})

# 81. Difference
print({1, 2, 3} - {2})

# 82. Symmetric difference
print({1, 2} ^ {2, 3})

# 83. Subset / superset
print({1, 2}.issubset({1, 2, 3}))

# 84. frozenset (immutable set)
fs = frozenset([1, 2, 3])
print(fs)

# 85. Dict creation
d = {"name": "Sayem", "age": 22}
print(d["name"])

# 86. get with default
print(d.get("city", "Sylhet"))

# 87. Add / update
d["city"] = "Sylhet"
d.update({"age": 23})
print(d)

# 88. keys / values / items
print(list(d.keys()), list(d.values()))

# 89. Iterate dict
for k, v in d.items():
    print(k, "->", v)

# 90. pop from dict
d.pop("city")
print(d)

# 91. Dict comprehension
squares = {n: n**2 for n in range(5)}
print(squares)

# 92. Merge dicts (3.9+)
d1 = {"a": 1}; d2 = {"b": 2}
print(d1 | d2)

# 93. setdefault
d = {}
d.setdefault("list", []).append(1)
print(d)

# 94. defaultdict
from collections import defaultdict
dd = defaultdict(int)
for ch in "banana":
    dd[ch] += 1
print(dict(dd))

# 95. Counter
from collections import Counter
print(Counter("mississippi"))

# 96. Counter most_common
print(Counter("aabbbcccc").most_common(2))

# 97. Dict from two lists
keys = ["a", "b"]; vals = [1, 2]
print(dict(zip(keys, vals)))

# 98. Invert dict
d = {"a": 1, "b": 2}
print({v: k for k, v in d.items()})

# 99. Nested dict access
data = {"user": {"profile": {"name": "Sayem"}}}
print(data["user"]["profile"]["name"])

# 100. Check key exists
print("name" in {"name": "x"})
```

---

## 🔁 Section 5 — Control Flow (101–120)

```python
# 101. if / elif / else
x = 0
if x > 0: print("positive")
elif x < 0: print("negative")
else: print("zero")

# 102. for loop
for i in range(5):
    print(i, end=" ")
print()

# 103. while loop
i = 0
while i < 5:
    print(i, end=" "); i += 1
print()

# 104. break
for i in range(10):
    if i == 5: break
    print(i, end=" ")
print()

# 105. continue
for i in range(5):
    if i == 2: continue
    print(i, end=" ")
print()

# 106. for-else (runs if no break)
for i in range(3):
    pass
else:
    print("loop finished cleanly")

# 107. Nested loops
for i in range(2):
    for j in range(2):
        print(i, j)

# 108. range with step
print(list(range(0, 20, 5)))

# 109. reversed range
print(list(range(10, 0, -1)))

# 110. enumerate with start
for i, v in enumerate(["a", "b"], start=1):
    print(i, v)

# 111. Loop over dict keys
for k in {"a": 1, "b": 2}:
    print(k)

# 112. pass placeholder
def todo(): pass

# 113. Infinite loop with break
count = 0
while True:
    count += 1
    if count >= 3: break
print(count)

# 114. Match statement (3.10+)
status = 404
match status:
    case 200: print("OK")
    case 404: print("Not Found")
    case _: print("Unknown")

# 115. Match with pattern
point = (0, 5)
match point:
    case (0, y): print(f"On Y axis at {y}")
    case (x, 0): print(f"On X axis at {x}")
    case _: print("Somewhere")

# 116. Guard in match
num = 7
match num:
    case n if n % 2 == 0: print("even")
    case _: print("odd")

# 117. FizzBuzz (classic)
for i in range(1, 16):
    print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i)

# 118. Loop with index & value modify
arr = [1, 2, 3]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)

# 119. zip in loop
for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)

# 120. Conditional in loop
evens = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
print(evens)
```

---

## ⚙️ Section 6 — Functions (121–150)

```python
# 121. Basic function
def greet(name):
    return f"Hello {name}"
print(greet("Sayem"))

# 122. Default arguments
def power(base, exp=2):
    return base ** exp
print(power(3), power(3, 3))

# 123. Keyword arguments
def info(name, age):
    return f"{name}, {age}"
print(info(age=22, name="Sayem"))

# 124. *args
def total(*nums):
    return sum(nums)
print(total(1, 2, 3, 4))

# 125. **kwargs
def config(**opts):
    return opts
print(config(debug=True, level=5))

# 126. Mixed args
def func(a, b=2, *args, **kwargs):
    return a, b, args, kwargs
print(func(1, 3, 4, 5, x=10))

# 127. Return multiple values
def min_max(lst):
    return min(lst), max(lst)
lo, hi = min_max([3, 1, 9])
print(lo, hi)

# 128. Lambda
square = lambda x: x ** 2
print(square(5))

# 129. Lambda with map
print(list(map(lambda x: x*2, [1, 2, 3])))

# 130. Lambda with filter
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))

# 131. Lambda with sorted
pairs = [(1, 'b'), (2, 'a')]
print(sorted(pairs, key=lambda p: p[1]))

# 132. Recursion — factorial
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)
print(fact(5))

# 133. Recursion — fibonacci
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
print([fib(i) for i in range(8)])

# 134. Memoized fib
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n-1) + fib_fast(n-2)
print(fib_fast(50))

# 135. Docstring
def add(a, b):
    """Return sum of a and b."""
    return a + b
print(add.__doc__)

# 136. Nested function
def outer(x):
    def inner(y):
        return x + y
    return inner
add5 = outer(5)
print(add5(3))

# 137. Closure with state
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c = counter()
print(c(), c(), c())

# 138. Function as argument
def apply(fn, val):
    return fn(val)
print(apply(lambda x: x*10, 5))

# 139. Returning function
def multiplier(n):
    return lambda x: x * n
triple = multiplier(3)
print(triple(4))

# 140. Default mutable arg trap (fix)
def safe(item, lst=None):
    if lst is None: lst = []
    lst.append(item)
    return lst
print(safe(1), safe(2))

# 141. Positional-only (3.8+)
def pos_only(a, b, /):
    return a + b
print(pos_only(1, 2))

# 142. Keyword-only
def kw_only(*, name):
    return name
print(kw_only(name="Sayem"))

# 143. Unpacking args into function
def add3(a, b, c): return a+b+c
args = [1, 2, 3]
print(add3(*args))

# 144. Unpacking dict into function
kwargs = {"a": 1, "b": 2, "c": 3}
print(add3(**kwargs))

# 145. Type hints in function
def divide(a: float, b: float) -> float:
    return a / b
print(divide(10, 3))

# 146. Global keyword
counter_val = 0
def increment():
    global counter_val
    counter_val += 1
increment()
print(counter_val)

# 147. Function attributes
def tracked(): pass
tracked.calls = 0
print(tracked.calls)

# 148. Variable scope (LEGB)
x = "global"
def scope_test():
    x = "local"
    return x
print(scope_test(), x)

# 149. Higher-order with reduce
from functools import reduce
print(reduce(lambda a, b: a*b, [1, 2, 3, 4]))

# 150. partial function
from functools import partial
def mul(a, b): return a * b
double = partial(mul, 2)
print(double(7))
```

---

## 🧩 Section 7 — Comprehensions (151–165)

```python
# 151. List comprehension
print([x**2 for x in range(5)])

# 152. With condition
print([x for x in range(10) if x % 2 == 0])

# 153. With if-else
print(["even" if x%2==0 else "odd" for x in range(5)])

# 154. Nested comprehension
print([[i*j for j in range(3)] for i in range(3)])

# 155. Dict comprehension
print({x: x**2 for x in range(5)})

# 156. Set comprehension
print({x % 3 for x in range(10)})

# 157. Generator expression
gen = (x**2 for x in range(5))
print(sum(gen))

# 158. Comprehension over string
print([c.upper() for c in "abc"])

# 159. Filter + transform
print([x*2 for x in range(10) if x > 5])

# 160. Flatten with comprehension
matrix = [[1, 2], [3, 4]]
print([n for row in matrix for n in row])

# 161. Conditional dict comp
print({k: v for k, v in {"a": 1, "b": 2}.items() if v > 1})

# 162. zip in comprehension
print([a+b for a, b in zip([1, 2], [10, 20])])

# 163. enumerate in comprehension
print([(i, c) for i, c in enumerate("xy")])

# 164. Nested with condition
print([(i, j) for i in range(3) for j in range(3) if i != j])

# 165. Comprehension with function call
print([len(w) for w in ["hi", "world", "ok"]])
```

---

## 🏛️ Section 8 — OOP (166–200)

```python
# 166. Basic class
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says woof"
d = Dog("Rex")
print(d.bark())

# 167. Class & instance attributes
class Circle:
    pi = 3.14159          # class attribute
    def __init__(self, r):
        self.r = r        # instance attribute
    def area(self):
        return Circle.pi * self.r ** 2
print(Circle(5).area())

# 168. __str__ vs __repr__
class Book:
    def __init__(self, title): self.title = title
    def __str__(self): return f"Book: {self.title}"
    def __repr__(self): return f"Book({self.title!r})"
b = Book("Python")
print(str(b), repr(b))

# 169. Inheritance
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"
print(Cat().speak())

# 170. super()
class Base:
    def __init__(self, x): self.x = x
class Derived(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
d = Derived(1, 2)
print(d.x, d.y)

# 171. Multiple inheritance
class A:
    def hello(self): return "A"
class B:
    def world(self): return "B"
class C(A, B): pass
c = C()
print(c.hello(), c.world())

# 172. Method Resolution Order
print(C.__mro__)

# 173. Class method
class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
Counter.increment()
print(Counter.count)

# 174. Static method
class Math:
    @staticmethod
    def add(a, b): return a + b
print(Math.add(2, 3))

# 175. Property (getter)
class Temp:
    def __init__(self, c): self._c = c
    @property
    def fahrenheit(self):
        return self._c * 9/5 + 32
print(Temp(100).fahrenheit)

# 176. Property setter
class Account:
    def __init__(self): self._balance = 0
    @property
    def balance(self): return self._balance
    @balance.setter
    def balance(self, val):
        if val < 0: raise ValueError("Negative!")
        self._balance = val
a = Account()
a.balance = 100
print(a.balance)

# 177. __eq__ operator overload
class Vec:
    def __init__(self, x, y): self.x, self.y = x, y
    def __eq__(self, o): return self.x == o.x and self.y == o.y
print(Vec(1, 2) == Vec(1, 2))

# 178. __add__ overload
class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, o): return Vector(self.x+o.x, self.y+o.y)
    def __repr__(self): return f"Vector({self.x}, {self.y})"
print(Vector(1, 2) + Vector(3, 4))

# 179. __len__
class Team:
    def __init__(self, members): self.members = members
    def __len__(self): return len(self.members)
print(len(Team(["a", "b", "c"])))

# 180. __getitem__ (indexable)
class MyList:
    def __init__(self, data): self.data = data
    def __getitem__(self, i): return self.data[i]
ml = MyList([10, 20, 30])
print(ml[1])

# 181. __call__ (callable object)
class Adder:
    def __init__(self, n): self.n = n
    def __call__(self, x): return x + self.n
add10 = Adder(10)
print(add10(5))

# 182. Private attributes (name mangling)
class Secret:
    def __init__(self): self.__hidden = 42
    def reveal(self): return self.__hidden
print(Secret().reveal())

# 183. Class with __slots__
class Pt:
    __slots__ = ['x', 'y']
    def __init__(self, x, y): self.x, self.y = x, y
p = Pt(1, 2)
print(p.x)

# 184. isinstance & issubclass
print(isinstance(5, int), issubclass(Cat, Animal))

# 185. Abstract base class
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
print(Square(4).area())

# 186. Class variable shared
class Shared:
    items = []
a, b = Shared(), Shared()
a.items.append(1)
print(b.items)  # [1] — shared!

# 187. __dict__ inspection
class Obj:
    def __init__(self): self.a = 1; self.b = 2
print(Obj().__dict__)

# 188. hasattr / getattr / setattr
class Conf: pass
c = Conf()
setattr(c, "x", 10)
print(getattr(c, "x"), hasattr(c, "y"))

# 189. __lt__ for sorting objects
class Player:
    def __init__(self, score): self.score = score
    def __lt__(self, o): return self.score < o.score
    def __repr__(self): return str(self.score)
print(sorted([Player(3), Player(1), Player(2)]))

# 190. Enum
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
print(Color.RED, Color.RED.value)

# 191. Method chaining
class Builder:
    def __init__(self): self.parts = []
    def add(self, p):
        self.parts.append(p); return self
    def build(self): return "-".join(self.parts)
print(Builder().add("a").add("b").build())

# 192. Composition over inheritance
class Engine:
    def start(self): return "Engine started"
class Car:
    def __init__(self): self.engine = Engine()
    def start(self): return self.engine.start()
print(Car().start())

# 193. __contains__ (in operator)
class Box:
    def __init__(self, items): self.items = items
    def __contains__(self, x): return x in self.items
print(2 in Box([1, 2, 3]))

# 194. Class as factory
class Shape2:
    @classmethod
    def square(cls, s): return cls(s, s)
    def __init__(self, w, h): self.w, self.h = w, h
sq = Shape2.square(5)
print(sq.w, sq.h)

# 195. __iter__ (iterable class)
class CountDown:
    def __init__(self, n): self.n = n
    def __iter__(self):
        while self.n > 0:
            yield self.n
            self.n -= 1
print(list(CountDown(3)))

# 196. Polymorphism
shapes = [Square(2), Square(3)]
print([s.area() for s in shapes])

# 197. Mixin pattern
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
class User(JsonMixin):
    def __init__(self, name): self.name = name
print(User("Sayem").to_json())

# 198. dataclass
from dataclasses import dataclass
@dataclass
class Point3:
    x: int
    y: int
print(Point3(1, 2))

# 199. dataclass with defaults & methods
@dataclass
class Rect:
    w: int = 1
    h: int = 1
    def area(self): return self.w * self.h
print(Rect(4, 5).area())

# 200. Frozen dataclass (immutable)
@dataclass(frozen=True)
class Coord:
    lat: float
    lon: float
print(Coord(23.8, 90.4))
```

---

## 🛡️ Section 9 — Error Handling (201–215)

```python
# 201. Basic try/except
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 202. Catch multiple exceptions
try:
    int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# 203. except with else
try:
    val = int("42")
except ValueError:
    print("bad")
else:
    print(f"Got {val}")

# 204. finally (always runs)
try:
    print("try")
finally:
    print("cleanup")

# 205. Raise exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    check_age(-5)
except ValueError as e:
    print(e)

# 206. Custom exception
class InsufficientFunds(Exception):
    pass
try:
    raise InsufficientFunds("Not enough balance")
except InsufficientFunds as e:
    print(e)

# 207. Exception with attributes
class APIError(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code
try:
    raise APIError("Failed", 500)
except APIError as e:
    print(e.code)

# 208. Re-raise
try:
    try:
        raise ValueError("inner")
    except ValueError:
        print("caught, re-raising")
        raise
except ValueError:
    print("outer caught")

# 209. raise from (chaining)
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Math error") from e
except ValueError as e:
    print(e.__cause__)

# 210. assert
def sqrt(x):
    assert x >= 0, "x must be non-negative"
    return x ** 0.5
print(sqrt(16))

# 211. Catch generic Exception (last resort)
try:
    risky = [1][5]
except Exception as e:
    print(f"{type(e).__name__}: {e}")

# 212. Access traceback
import traceback
try:
    1 / 0
except ZeroDivisionError:
    print(traceback.format_exc().splitlines()[-1])

# 213. Exception group handling (try common ones)
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
print(safe_div(10, 0))

# 214. Suppress exception
from contextlib import suppress
with suppress(FileNotFoundError):
    open("nonexistent.txt")
print("continued anyway")

# 215. Validate input pattern
def parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 0
print(parse_int("abc"), parse_int("42"))
```

---

## 📁 Section 10 — File & I/O (216–230)

```python
# 216. Write to file
with open("test.txt", "w") as f:
    f.write("Hello File\n")

# 217. Read entire file
with open("test.txt") as f:
    print(f.read())

# 218. Read line by line
with open("test.txt") as f:
    for line in f:
        print(line.strip())

# 219. readlines into list
with open("test.txt") as f:
    lines = f.readlines()
print(lines)

# 220. Append mode
with open("test.txt", "a") as f:
    f.write("Second line\n")

# 221. Write multiple lines
with open("test.txt", "w") as f:
    f.writelines(["a\n", "b\n", "c\n"])

# 222. Check file exists
import os
print(os.path.exists("test.txt"))

# 223. JSON write
import json
data = {"name": "Sayem", "scores": [90, 85]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# 224. JSON read
with open("data.json") as f:
    loaded = json.load(f)
print(loaded)

# 225. JSON string conversion
print(json.dumps({"a": 1}))
print(json.loads('{"b": 2}'))

# 226. CSV write
import csv
with open("data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "age"])
    w.writerow(["Sayem", 22])

# 227. CSV read
with open("data.csv") as f:
    for row in csv.reader(f):
        print(row)

# 228. CSV DictReader
with open("data.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"])

# 229. pathlib (modern paths)
from pathlib import Path
p = Path("test.txt")
print(p.name, p.suffix, p.exists())

# 230. List directory
import os
print([f for f in os.listdir(".") if f.endswith(".txt")])
```

---

## 🔄 Section 11 — Iterators & Generators (231–245)

```python
# 231. Basic generator
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1
print(list(count_up(5)))

# 232. Generator expression
gen = (x*x for x in range(5))
print(next(gen), next(gen))

# 233. Infinite generator
def naturals():
    n = 1
    while True:
        yield n; n += 1
g = naturals()
print([next(g) for _ in range(5)])

# 234. yield from
def chain_gen():
    yield from [1, 2]
    yield from [3, 4]
print(list(chain_gen()))

# 235. Generator pipeline
def evens(nums):
    for n in nums:
        if n % 2 == 0: yield n
def squared(nums):
    for n in nums:
        yield n*n
print(list(squared(evens(range(10)))))

# 236. Custom iterator class
class Range2:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1
        return self.i - 1
print(list(Range2(4)))

# 237. iter() and next()
it = iter([10, 20, 30])
print(next(it), next(it))

# 238. iter with sentinel
# reads until 'STOP' — pattern example
data = iter(["a", "b", "STOP", "c"])
result = list(iter(lambda: next(data), "STOP"))
print(result)

# 239. Generator with state (running average)
def running_avg():
    total, count = 0, 0
    while True:
        val = yield (total / count if count else 0)
        total += val; count += 1
avg = running_avg()
next(avg)
print(avg.send(10), avg.send(20))

# 240. itertools.count
from itertools import count
c = count(10, 2)
print(next(c), next(c))

# 241. itertools.cycle
from itertools import cycle
cy = cycle([1, 2, 3])
print([next(cy) for _ in range(5)])

# 242. itertools.chain
from itertools import chain
print(list(chain([1, 2], [3, 4])))

# 243. itertools.islice (slice generator)
from itertools import islice
print(list(islice(naturals(), 3, 8)))

# 244. itertools.takewhile / dropwhile
from itertools import takewhile, dropwhile
print(list(takewhile(lambda x: x < 5, [1, 3, 6, 2])))
print(list(dropwhile(lambda x: x < 5, [1, 3, 6, 2])))

# 245. Lazy file reading generator
def read_chunks(text, size):
    for i in range(0, len(text), size):
        yield text[i:i+size]
print(list(read_chunks("abcdefg", 3)))
```

---

## 🎀 Section 12 — Decorators & Context Managers (246–265)

```python
# 246. Basic decorator
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_hi():
    print("hi")
say_hi()

# 247. Decorator with arguments passing
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@logged
def add(a, b): return a + b
print(add(2, 3))

# 248. Preserve metadata with functools.wraps
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
@timer
def task(): "docstring here"
print(task.__name__)

# 249. Decorator with parameters
def repeat(n):
    def deco(func):
        def wrapper(*a, **k):
            for _ in range(n):
                func(*a, **k)
        return wrapper
    return deco
@repeat(3)
def hello(): print("hello")
hello()

# 250. Timing decorator
import time
def measure(func):
    @wraps(func)
    def wrapper(*a, **k):
        start = time.perf_counter()
        r = func(*a, **k)
        print(f"{func.__name__}: {time.perf_counter()-start:.6f}s")
        return r
    return wrapper
@measure
def slow(): sum(range(100000))
slow()

# 251. Caching decorator (manual)
def cache(func):
    store = {}
    @wraps(func)
    def wrapper(*args):
        if args not in store:
            store[args] = func(*args)
        return store[args]
    return wrapper
@cache
def expensive(n): return n * n
print(expensive(4), expensive(4))

# 252. Class as decorator
class CountCalls:
    def __init__(self, func):
        self.func = func; self.count = 0
    def __call__(self, *a, **k):
        self.count += 1
        return self.func(*a, **k)
@CountCalls
def greet(): pass
greet(); greet()
print(greet.count)

# 253. Multiple decorators (stacked)
def bold(f):
    def w(): return "<b>" + f() + "</b>"
    return w
def italic(f):
    def w(): return "<i>" + f() + "</i>"
    return w
@bold
@italic
def text(): return "hi"
print(text())

# 254. property as decorator (recap)
class C:
    @property
    def value(self): return 42
print(C().value)

# 255. Basic context manager (with)
with open("test.txt", "w") as f:
    f.write("ctx")

# 256. Custom context manager (class)
class Timer:
    def __enter__(self):
        self.start = time.perf_counter(); return self
    def __exit__(self, *args):
        print(f"Elapsed: {time.perf_counter()-self.start:.6f}s")
with Timer():
    sum(range(10000))

# 257. contextlib.contextmanager
from contextlib import contextmanager
@contextmanager
def managed():
    print("setup")
    yield "resource"
    print("teardown")
with managed() as r:
    print(f"using {r}")

# 258. Context manager with exception handling
@contextmanager
def safe_open(path):
    f = open(path, "w")
    try:
        yield f
    finally:
        f.close()
with safe_open("test.txt") as f:
    f.write("safe")

# 259. Nested context managers
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("A"); b.write("B")

# 260. redirect stdout
import io
from contextlib import redirect_stdout
buf = io.StringIO()
with redirect_stdout(buf):
    print("captured")
print(f"Got: {buf.getvalue().strip()}")

# 261. Decorator returning value
def double_result(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k) * 2
    return wrapper
@double_result
def get_num(): return 21
print(get_num())

# 262. Singleton via decorator
def singleton(cls):
    instances = {}
    def get(*a, **k):
        if cls not in instances:
            instances[cls] = cls(*a, **k)
        return instances[cls]
    return get
@singleton
class DB:
    pass
print(DB() is DB())

# 263. Retry decorator
def retry(times):
    def deco(func):
        @wraps(func)
        def wrapper(*a, **k):
            for attempt in range(times):
                try:
                    return func(*a, **k)
                except Exception:
                    if attempt == times - 1: raise
        return wrapper
    return deco
@retry(3)
def maybe(): return "success"
print(maybe())

# 264. ExitStack (dynamic context managers)
from contextlib import ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(f"f{i}.txt", "w")) for i in range(2)]
    for f in files: f.write("x")
print("all closed")

# 265. Validation decorator
def positive_only(func):
    @wraps(func)
    def wrapper(n):
        if n < 0: raise ValueError("must be positive")
        return func(n)
    return wrapper
@positive_only
def sqrt(n): return n ** 0.5
print(sqrt(9))
```

---

## 🧮 Section 13 — Functional & itertools/collections (266–285)

```python
# 266. map basics
print(list(map(str, [1, 2, 3])))

# 267. map with multiple iterables
print(list(map(lambda x, y: x+y, [1, 2], [10, 20])))

# 268. filter
print(list(filter(None, [0, 1, "", "a", None])))

# 269. reduce
from functools import reduce
print(reduce(lambda a, b: a+b, range(1, 11)))

# 270. reduce with initial
print(reduce(lambda a, b: a*b, [1, 2, 3], 10))

# 271. sorted with multiple keys
data = [("Sayem", 22), ("Ali", 22), ("Bob", 20)]
print(sorted(data, key=lambda x: (x[1], x[0])))

# 272. itertools.combinations
from itertools import combinations
print(list(combinations([1, 2, 3], 2)))

# 273. itertools.permutations
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))

# 274. itertools.product
from itertools import product
print(list(product([1, 2], ["a", "b"])))

# 275. itertools.groupby
from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3)]
for key, grp in groupby(data, key=lambda x: x[0]):
    print(key, list(grp))

# 276. itertools.accumulate
from itertools import accumulate
print(list(accumulate([1, 2, 3, 4])))  # running sum

# 277. accumulate with operator
import operator
print(list(accumulate([1, 2, 3, 4], operator.mul)))

# 278. itertools.starmap
from itertools import starmap
print(list(starmap(pow, [(2, 3), (3, 2)])))

# 279. itertools.zip_longest
from itertools import zip_longest
print(list(zip_longest([1, 2], ["a"], fillvalue="?")))

# 280. collections.deque
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0); dq.append(4)
print(dq)

# 281. deque rotate
dq = deque([1, 2, 3, 4])
dq.rotate(1)
print(dq)

# 282. collections.OrderedDict move_to_end
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2)])
od.move_to_end("a")
print(list(od.keys()))

# 283. collections.ChainMap
from collections import ChainMap
defaults = {"color": "red"}
user = {"size": "L"}
cm = ChainMap(user, defaults)
print(cm["color"], cm["size"])

# 284. operator module helpers
from operator import itemgetter, attrgetter
people = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
print(sorted(people, key=itemgetter("age")))

# 285. functools.reduce for max
print(reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9]))
```

---

## 🚀 Section 14 — Advanced: typing, async, misc (286–300)

```python
# 286. Type hints — basic
from typing import List, Dict, Optional
def process(items: List[int]) -> int:
    return sum(items)
print(process([1, 2, 3]))

# 287. Optional & Union
from typing import Union
def find(x: int) -> Optional[str]:
    return "found" if x > 0 else None
print(find(5), find(-1))

# 288. Type alias
Vector = List[float]
def scale(v: Vector, f: float) -> Vector:
    return [x * f for x in v]
print(scale([1.0, 2.0], 3))

# 289. Callable type hint
from typing import Callable
def apply(fn: Callable[[int], int], x: int) -> int:
    return fn(x)
print(apply(lambda n: n*2, 5))

# 290. TypedDict
from typing import TypedDict
class Movie(TypedDict):
    title: str
    year: int
m: Movie = {"title": "Inception", "year": 2010}
print(m["title"])

# 291. Generic with TypeVar
from typing import TypeVar
T = TypeVar("T")
def first(items: List[T]) -> T:
    return items[0]
print(first([10, 20, 30]))

# 292. async function basics
import asyncio
async def fetch(x):
    await asyncio.sleep(0.01)
    return x * 2
print(asyncio.run(fetch(5)))

# 293. async gather (concurrent)
async def main():
    results = await asyncio.gather(fetch(1), fetch(2), fetch(3))
    return results
print(asyncio.run(main()))

# 294. async with timeout pattern
async def with_timeout():
    try:
        return await asyncio.wait_for(fetch(10), timeout=1.0)
    except asyncio.TimeoutError:
        return "timed out"
print(asyncio.run(with_timeout()))

# 295. unpacking in function call (recap, advanced)
def coords(x, y, z): return f"{x},{y},{z}"
point = {"x": 1, "y": 2, "z": 3}
print(coords(**point))

# 296. __init_subclass__ hook
class Plugin:
    registry = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls.__name__)
class A(Plugin): pass
class B(Plugin): pass
print(Plugin.registry)

# 297. Descriptor protocol
class Positive:
    def __set_name__(self, owner, name): self.name = "_" + name
    def __get__(self, obj, owner): return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value < 0: raise ValueError("must be positive")
        setattr(obj, self.name, value)
class Product:
    price = Positive()
    def __init__(self, price): self.price = price
print(Product(100).price)

# 298. Context-managed timing + generator (combined)
@contextmanager
def timed_block(label):
    s = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter()-s:.6f}s")
with timed_block("loop"):
    _ = [i**2 for i in range(10000)]

# 299. functools.singledispatch (function overloading)
from functools import singledispatch
@singledispatch
def describe(x): return f"unknown: {x}"
@describe.register
def _(x: int): return f"int: {x}"
@describe.register
def _(x: str): return f"str: {x}"
print(describe(5), describe("hi"))

# 300. Putting it together — mini pipeline
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name: str
    score: float

def top_students(students: List[Student], n: int) -> List[str]:
    return [s.name for s in sorted(students, key=lambda s: -s.score)[:n]]

roster = [Student("Sayem", 95), Student("Ali", 88), Student("Bob", 91)]
print(top_students(roster, 2))  # ['Sayem', 'Bob']
