# Terminales & No Terminales

Para correr el programa solo se necesita de Python.
```bash
python terminal.py <flag> <textFile>
```

Hay 2 maneras de pasar parametross
- [Archivo de texto](#archivo-de-texto)
- [Input manual](#input-manual)   
- [Probar Todos los Archivos](#probar-todos-los-archivos)

---

### Archivo de texto
```bash
python terminal.py -f <textFile>
```
Programa leera el archivo de texto, cuya primera linea debe contener el numero n de lineas a leer seguido por la gramatica

### Input manual
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

### Probar Todos los Archivos
```bash
python terminal.py -a
```
Dentro del directorio donde se encuentra main, debera existir una carpeta llamada inputs con los archivos de texto que se vayan a probar siguiendo el formato.   
El script correra todas las pruebas.