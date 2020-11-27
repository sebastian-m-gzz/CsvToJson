# CsvToJson
Starts a web server which converts the contents 
of a csv file to a json and returns its data.

### Requirements
- Dockers
- Python 3

### How to use

#### Initialize for the first time

1. Clone this repo to the host machine.
2. Create a docker image.
    + Here we define ```csv2json``` which is the name of the image
    + The image name can be any identifier, as long as you keep up the consistence with it.
    ```
    docker build -t csv2json
    ```
3. Run image as a service
    + Here note port 5050 will be the one exposed on the host side.
    + Also notice that the ```/data_directory``` path is the absolute path in the host to where
    a ```employees.csv``` is expected to be, as it is the one that will be parsed into json.
    ```
    docker run -d -p 5050:6000 -v /data_directory:/usr/src/app/data csv2json
    ```
   As an alternative, run the image as a development service.
    ```
    docker run -it --rm -p 5050:6000 -v /data_directory:/usr/src/app/data csv2json
    ```
   
#### Modify content

+ Since we declared the container with a 'mirror' directory to a ```employees.csv``` file,
we just need to modify this file to expect to see changes (do not change the file name).