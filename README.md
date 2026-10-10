# Pigpy
### Write your program in pigpy (python but every word is translated into pig latin), then run it via this python script and you'll get an output (in pig latin of course)! 

*atherray ironicay hattay ouyay unray away ranslatedtay ersionvay ofay ythonpay hroughtay away ythonpay criptsay otay ranslatetay itway intoway ythonpay otay inallyfay unray itway hroughtay ythonpay*
rather ironic that you run a translated version of python through a python script to translate it into python to finally run it through python

### Devlog 1: 10/10/26 (DD/MM/YY)
I'm sure it'll come as a massive shock to everybody that pigpy has some flaws as a programming language...

#### What I got done:
* Made the translation function as well as some other parts
* Configured the first commit so that its usable as a translator for standalone words the user inputs (this is temporary - will be removed for the final program)

#### The flaws:
* Every english word can only translate to one pig latin word, however multiple english words can **translate to the same pig latin word**
* An important example for programming is 'in' and 'win'.
  - Add 'way' to in because it starts a vowel, and you get **inway**
  - Move w to the end of the word then add 'ay' because win starts with a consonant, and you again get **inway**
* 'in' is commonly used in python in lines like:
  -'for variable in range(num):
  - or 'if variable in list:'
  
So how can you tell those two words apart when translating from pig latin to english? **YOU CAN'T.**

#### Possible solutions:
- I now have to figure out how 
