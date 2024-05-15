   # Chat usando Flask-SocketIO
## _Tutorial de cómo usar sockets y blueprint_
Este repo es utilizado para poder crear una sencilla aplicación de chat usando las librerías de flask-socketio y Blueprint.
1. Cómo primer paso es necesario crear el entorno virtual, puedes hacerlo desde cmd, porwershell o git bash:
    Para el caso de cmd y powershell:
    ```sh
    > virtualenv nombre-de-tu-entorno
    ```
    Para el caso de gitbash:
    ```sh
    $ python -m venv nombre-de-tu-entorno
    ```
2. Después debes activar tu entorno virtual usando el siguiente comando:
    cmd/powershell:
    ```sh
    > .\venv\Scripts\activate
    ```
    Git bash:
    ```sh
    $ source ./venv/Scripts/activate
    ```
3. Con el entorno activado se prosigue a instalar las librerias que vienen en el archivo requirements:
    ```sh
    > pip install -r requirements.txt
   ```