# MachineLearning

TPs de la materia Machine Learning (Aprendizaje Automatico) del ITBA

## Setup

Se recomienda utilizar Python 3.8. Se puede instalar con [pyenv](https://github.com/pyenv/pyenv) con el comando `pyenv install 3.8.6`, y se recomienda crear un entorno para evitar conflictos con las dependencias:
```bash
python -m venv ~/.venv/MachineLearning
source ~/.venv/MachineLearning/bin/activate
```
Para instalar las dependencias:
```bash
pip install -r requirements.txt
```

La dependencia `jupyterlab` se encuentra en el archivo de dependencias. Para iniciar una sesión de Jupyter Lab, correr el comando:
```bash
jupyter lab
```

Para instalar los archivos comunes de Machine Learning como un paquete de pip, correr el siguiente comando:
```bash
cd src
pip install -e mlcommon
```
