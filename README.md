# DigitToChinese
Convert number to Chinese characters.


```
python3 setup.py install
```

```
from DigitToChinese import converter

number = 1314
ifLower = False   # Default: True
chinese = converter(number, ifLower)
# '壹千叁百壹十肆'

