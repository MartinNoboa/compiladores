# Terminales & No Terminales

Para correr el programa solo se necesita de Python.
```bash
python terminal.py <flag> <textFile>
```

Hay 2 maneras de pasar parametross
- [Archivo de texto](textFile)
- [Input manual](manual)   

---

### Archivo de texto {#texFile}
```bash
python terminal.py -f <textFile>
```
Programa leera el archivo de texto, cuya primera linea debe contener el numero n de lineas a leer seguido por la gramatica

### Input manual {#manual}
```bash
python terminal.py -i
```
Primero se ingresa el numero n de lineas seguido por las n lineas a procesar
```bash
8
E -> T EPrime
EPrime -> + T EPrime
EPrime -> ' '
T -> F TPrime
TPrime -> * F TPrime
TPrime -> ' '
F -> ( E )
F -> id
```