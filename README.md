# python-devops-wikipedia

Python devops es una implementación sencilla de una api en FastApi que permite hacer requests a wikipedia.

## Objetivo

El objetivo de este proyecto era aprender el flujo de trabajo de DevOps, basandose en la entrega continua y el desarrollo continuo (CI/CD) desde el principio del proyecto.

Seguí [este video](https://www.youtube.com/watch?v=YB-_FsssK8E) para realizar este proyecto

## Demo
Demo de las acciones de github 
![image](https://github.com/user-attachments/assets/00e7047c-6206-4e7c-93ec-a460372b8698)

Estado actual de las acciones de github de este proyecto:
[![Python application test with Github Actions](https://github.com/darthpedroo/python-devops/actions/workflows/devops.yml/badge.svg)](https://github.com/darthpedroo/python-devops/actions/workflows/devops.yml)


## Funcionalidades

### Makefile

- Instalar dependencias del proyecto
- Formatear el codigo con [black](https://pypi.org/project/black/)
- Aplciar un Linter con [pylint](https://pypi.org/project/pylint/)
- Testear el código 
- Buildear una imagen con Docker
- Correr la imagen

Las acciones de este Makefile se ejecutan en las acciones de github al hacer un test

## Prerequisitos

- Choco ( para instalar make )
- Make

[Ayuda para instalar make en windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)

Aclaración: No es necesario tener make instalado, el proyecto se puede ejecutar con python simplemente pero la idea del proyecto es probar como funciona un archivo Make.

## Instalación

Instalar las dependencias

```bash
make install
```

## Uso

### Ejecutar la api rest de Flask:
```bash
python .\main.py
```

Resultado esperado: 

### Usar el paquete logic desde la linea de comandos

```bash
python.exe .\cli-fire.py <nombre-funcion> <parametro 1> <parametro 2>
```
Ejemplo:
```bash
python.exe .\cli-fire.py search_wiki "Pepe"
```
## Como usar Makefile


Para ejecutar cualquier comando hay que escribir el comando en la terminal.

`make install`:Instala las dependencias del proyecto y descarga los corpus de TextBlob.

`make format`: Formatea el código con black.

`make lint`: Aplica el linter pylint en los archivos Python

`make test`: Ejecuta los tests con pytest

`make build`: Construye la imagen de Docker con la etiqueta deploy-fastapi

`make run`: Ejecuta el contenedor Docker

`make deploy`: Hace un deploy de la app. (No implementado)

`make all`: Ejecuta todos los comandos mostrados arriba


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
