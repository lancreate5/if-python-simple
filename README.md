# if-python-simple
A simple parser and lexical analyzer for Python's if conditional syntax

## 🚀 Installation (ID)
### Gunakan via Google Colab
Untuk menggunakan porgram ini tanpa harus melakukan install, anda bisa kunjungi tautan
<a href="https://colab.research.google.com/drive/1wFp_Mf6hgLcEDsIg1tfZLjTzdGoPK-Ji?usp=sharing">Google Colab</a>. 

### Gunakan secara lokal

## 🚀 Installation (EN)
### Use via Google Colab
To use this program without any installation, you could visit this
<a href="https://colab.research.google.com/drive/1wFp_Mf6hgLcEDsIg1tfZLjTzdGoPK-Ji?usp=sharing">Google Colab</a>. 

### Use locally

## 🚧 Limitation
As this little project isn't purposed for full-suite parsing, it has
the its limitations. The limitations are based on the following CFG:

```
<statement> -> if <condition> : <action>
<condition> -> <variable> <operator> <variable> | <boolean>
<boolean> -> True | False <variable> -> p | q | r | s | t
<operator> -> > | < | >= | <= | == | !=
<action> -> pass
```

In summary, the string that this program would accept has to follow
these criterias:
    - The variable should to be 1 character long in maximum
    - The variable name could only consist of these letters: p, q, r, s, t
    - The action accepted is restricted to `pass`
