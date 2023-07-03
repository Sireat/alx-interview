# :book: 0x01. Lockboxes
## Topics Covered
1. Python.
2. Lockboxes.

# :computer: Tasks.
## [0. Lockboxes](0-lockboxes.py)
### Task requirements.
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

  *  Prototype: def canUnlockAll(boxes)
  *  boxes is a list of lists
  *  You can assume all keys will be positive integers
      *  There can be keys that do not have boxes
  *  The first box boxes[0] is unlocked
  *  Return True if all boxes can be opened, else return False
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```

```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

### :wrench: Task setup.
```bash
# Create task file and set write permission.
touch ./0-lockboxes.py
chmod +x ./0-lockboxes.py
./0-lockboxes.py

# Lint the code.
pycodestyle ./0-lockboxes.py
pep8 ./0-lockboxes.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py
```

### :heavy_check_mark: Solution.
> [:point_right:  Open 0-lockboxes.py](0-lockboxes.py)

# :books: References
1. [Python Lists](https://www.w3schools.com/python/python_lists.asp)
1. [Python sum() Function](https://www.w3schools.com/python/ref_func_sum.asp)

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhatsApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
