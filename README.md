# Chat-Flask-SocketIO
1. Cómo primer paso es necesario crear el entorno virtual, puedes hacerlo desde cmd, porwershell o git bash:
    Para el caso de cmd y powershell:
    {% filename %}command-line{% endfilename %}
    > virtualenv nombre-de-tu-entorno
    Para el caso de gitbash:
    {% filename %}command-line{% endfilename %}
    $ python -m venv nombre-de-tu-entorno
2. Después debes activar tu entorno virtual usando el siguiente comando:
    cmd/powershell:
    {% filename %}command-line{% endfilename %}
    > .\venv\Scripts\activate
    Git bash:
    {% filename %}command-line{% endfilename %}
    $ source ./venv/Scripts/activate
3. Teniendo lo anterior se prosigue a instalar las librerias que vienen en el archivo requirements:
    > pip install -r requirements.txt