# Jetson Documentation - UTEQ

## Running the Docker Container
### Launching the container
```bash
git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
cd jetson-inference
docker/run.sh
```

### Running Applications

To run example programs inside the container:
```bash
cd build/aarch64/bin
./video-viewer /dev/video0
./imagenet images/jellyfish.jpg images/test/jellyfish.jpg
./detectnet images/peds_0.jpg images/test/peds_0.jpg
```
# Basic commands on terminal

___
List Files

```bash
ls
```

___
Print Working Directory

```bash
pwd
# Example -> /home/user/Documents
```

___
Change Directory

```bash
cd <Directory>

# Example -> cd Documents

cd .. # Move a level up

cd # Move to home

```

___
Copy

```bash
cp <file> <destination>

# Example -> cp hello.txt directory/
```
___
Remove

```bash
rm <file>
# Example -> rm hello.txt

rm -rf <directory>
# Example -> rm directory/
```

___
Move file

```bash
mv <origen> <destination>
# Example -> mv hello.txt directory/
```

___ 
Rename file

```bash
mv <originalName> <newName>
# Example -> mv hello.txt hola.txt
```

