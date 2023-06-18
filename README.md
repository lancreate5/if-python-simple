# if-python-simple
A simple parser and lexical analyzer for Python's if conditional syntax

## 🚀 Installation (ID)
### Gunakan via Google Colab
Untuk menggunakan porgram ini tanpa harus melakukan install, anda bisa kunjungi tautan
<a href="https://colab.research.google.com/drive/1wFp_Mf6hgLcEDsIg1tfZLjTzdGoPK-Ji?usp=sharing">Google Colab</a>. 

### Gunakan secara lokal
Untuk menggunakan program di komputer anda secara lokal, ikuti langkah berikut:
1. Pastikan Python telah terinstall. Lakukan pengecekan dengan `py --version` atau `python3 --version`
2. Unduh repositori ini atau clone dengan `git clone https://github.com/lancreate5/if-python-simple`
3. Buka terminal dan ubah current directory menjadi direktori tempat anda menyimpan source code
4. Tentukan input yang ingin anda masukkan dengan mengedit `input.txt`. Satu baris menyatakan satu input. Lebih dari
satu baris bisa ditulis di file tersebut
5. Jalankan program dengan `py main.py` atau `python3 main.py`

## 🚀 Installation (EN)
### Use via Google Colab
To use this program without any installation, you could visit this
<a href="https://colab.research.google.com/drive/1wFp_Mf6hgLcEDsIg1tfZLjTzdGoPK-Ji?usp=sharing">Google Colab</a>. 

### Use locally
To use the program on your computer locally, follow these steps:
1. Ensure that Python had installed on your computer. Check its installation by running `py --version` or `python3 --version` on your terminal
2. Download this repository or clone it with `git clone https://github.com/lancreate5/if-python-simple`
3. Open up your terminal and change your current directory to the directory where you stored the source code
4. Determine the input you want to give to the program by editing `input.txt`. One line represents one input. More than one line could be
written on the file
5. Run the program by `py main.py` or `python3 main.py`

## 🌟 Extra Feature
- The lexical analyzer could pinpoint where your mistake you've made
- The parser could give you the details of the mistake you've made and also provides you with some recommendation

## 🚧 Limitation
As this little project isn't purposed for full-suite parsing, it has
the its limitations. The limitations are based on the following CFG:

```
<statement> -> if <condition> : <action>
<condition> -> <variable> <operator> <variable> | <boolean>
<boolean> -> True | False 
<variable> -> p | q | r | s | t
<operator> -> > | < | >= | <= | == | !=
<action> -> pass
```

In summary, the string that this program would accept has to follow
these criterias:
- The variable should to be 1 character long in maximum
- The variable name could only consist of these letters: p, q, r, s, t
- The action accepted is restricted to `pass`
