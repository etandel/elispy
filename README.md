About
---

Embedded S-expressions for python

Usage
---

```python
from elispy import interpret, if_
from elispy.prelude import *

s_exp = (if_, (eq, (mul, 21, 2), 42)
         "don't panic!",
         "panic!")
print(interpret(s_exp))  # --> "don't panic!"
```
