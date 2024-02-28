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

List Files

```bash
ls
```

Print Working Directory

```bash
pwd
# Example -> /home/user/Documents
```

Change Directory

```bash
cd <Directory>

# Example -> cd Documents
```

