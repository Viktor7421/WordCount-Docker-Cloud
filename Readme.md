# Guia de uso

Levantar el docker con el siguiente comando:
```
docker build -t tarea2 .
```

Ejecutar el programa con el siguiente programa:
```
docker run --mount type=bind,source=${PWD}/volumen,target=/app/volumen tarea2
```

Para que funcione el main.py debe tener la ruta del archivo a leer y este debe estar en la carpeta llamada `volumen`. En esa misma carpeta se debe encontrar el archivo que recivira los resultados.

```
-volumen
    -movies.csv
    -output_file.txt
```