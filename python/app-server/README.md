# Docker in AWS
## Install Flask using venv
1. update system
2. install venv package
    ```bash
    sudo apt install -y python3-venv
    ```
3. Create venv work space
    ```bash
    sudo python3 -m venv venv
    ```
4. Use root user
    ```bash
    sudo su
    ```
3. Active work space
    ```bash
    source venv/bin/activate
    ```
4. Install flask
    ```bash
    pip3 install Flask
    ```
5. Out env
    ```bash
    deactivate
    ```

## Create Image
1. Create requirements file
    ```bash
    python3 -m pip freeze > requirements.txt
    ```
2. Build image
    ```bash
    sudo docker build --tag python-docker .
    ```

## Run Containers
1. Create port and publish image as container
    ```bash
    sudo docker run --publish 8080:8080 python-docker
    ```
2. Check connection
    ```bash
    curl localhost:8080
    ```