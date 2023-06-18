# if-python-simple
A simple parser and lexical analyzer for Python's if conditional syntax

## Limitation
As this little project isn't purposed for full-suite parsing, it has
the its limitations. The limitations are based on the following CFG:
```
<statement> -> if <condition><optSpace>:<optSpace><action>
<condition> -> <variable><optSpace><operator><optSpace><variable>
<variable> -> p<variable> | q<variable> | r<variable> | s<variable> | t<variable> | epsilon
<operator> -> > | < | >= | <= | == | !=
<optSpace> -> " " | epsilon
<action> -> pass

```
