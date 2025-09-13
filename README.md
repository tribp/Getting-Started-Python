# Getting-Started-Python
Essentials Python topics

**TOC/**
1. OOP

    1.1 @property
    1.2 methods
        - "normal" method
        - @classmethod
        - @staticmethod


### 1.1 @property

The **@property** decorator allows you to add specific logic when read, write or delete a property

see example: [@property example](./code/property_decorator.py)

### 1.2 Methods

There are 3 types of methods

    - normal -> uses 'self' as first aurgument
    - **@classmethod** -> uses 'cls' as first arhument -> impact on the class itself (global vars or alternative constructors with'from')
    - **@staticmethod** -> **NO 'self' or 'cls'** -> works like a **regular** method

**Tip:** If 'self' or 'class' is not accessed in he method than it is a static method ! 

see example: [methods example](./code/methods.py)
