# Introducción

El motivo de este repositorio es poder mostrar los stats de mis raspberrys

Para ello uso una raspberry pi zero junto con una pantalla tft de adafuit

# Necesidades previas

Necesitamos tener la raspberry actualizada junto con python3

Es necesario seguir las [indicaciones de adafruit](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/python-setup) para tener las librerías necesarias para poder mostrar la información en la pantalla

También es necesario tener instalado [paramiko](https://www.paramiko.org/installing.html) para poder realizar las conexiones ssh con los otros servidores/raspberrys

Otro paso muy importante para realizar la conexión es que cada uno de los raspberrys/servidores tengan la clave ssh de la raspberry en su `authorized_keys`

Por último, si queremos cambiar el formato de la fecha, tenemos que cambiar la línea donde se setea el locale por el nuestro

# Uso

Para poder empezar a mostrar la información se aconseja empezar primero mostrar la información en la
terminal, para ello tenemos que comentar la linea que llama a la función de mostrar en la pantalla y
descomentar la que muestra la información en la terminal

Una vez decidido dónde queremos mostrar la información, solo tenemos que ejecutar `python3 stats.py`

Si queremos que esto se ejecute al inicio de nuestra raspberry, solo tenemos que añadir la siguiente
línea a `/etc/rc.local` justo antes del `exit 0`:

`sudo -u USER python3 PATH/stats.py &`

Recuerda cambiar USER por tu usuario y PATH por el directorio en el que esté tu script

[Contacto](mailto:franciscoj.ruiz@gmail.com)

