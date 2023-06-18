# if-python-simple
A simple parser and lexical analyzer for Python's if conditional syntax

## Limitation
As this little project isn't purposed for full-suite parsing, it has
the its limitations. The limitations are based on the following CFG:
```
<statement> -> if <condition> : <action>
<condition> -> <variable> <operator> <variable>
<variable> -> p<variable> | q<variable> | r<variable> | s<variable> | t<variable> | epsilon
<operator> -> > | < | >= | <= | == | !=
<action> -> pass

```
