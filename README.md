# tmux-control

configure and control tmux

## setup

```Bash
sudo apt-get install \
    cmus             \
    elinks           \
    htop             \
    nvtop            \
    ranger           \
    tmux

sudo pip install tmux_control
```

## configurations

### analysis mode

This mode is designed to be ergonomic for running an analysis. The bottom terminal runs the main analysis code while ranger allows for quick viewing of ongoing analysis output files.

```
-----------------------
|                     |
|       ranger        |
|                     |
|                     |
|---------------------|
|                     |
|      terminal       |
|                     |
|                     |
-----------------------
```

### badass mode

```
-----------------------
| ranger   |          |
|----------|          |
| terminal |          |
|----------|          |
| htop     |  ranger  |
|----------|          |
| arXiv    |          |
|----------|          |
| cmus     |          |
-----------------------
```

### detail mode

This mode is designed to be a less fun version of badass mode.

```
-----------------------
|          |          |
| ranger   |          |
|----------|          |
| terminal |          |
|----------|  ranger  |
| htop     |          |
|----------|          |
| arXiv    |          |
|          |          |
-----------------------
```

### edit mode (default)

This mode is designed to be ergonomic for coding.

```
-----------------------
|          |          |
|          |          |
|          |          |
|          |          |
| terminal |  ranger  |
|          |          |
|          |          |
|          |          |
|          |          |
-----------------------
```

### Nvidia mode

This mode is designed to display system resource usage for a system featuring Nvidia hardware.

```
-----------------------
|                     |
|        htop         |
|                     |
|                     |
|---------------------|
|                     |
|        nvtop        |
|                     |
|                     |
-----------------------
```

### run mode

This special mode launches all of the scripts at a defined directory in separate windows. It is used by engaging the option `--run`, optionally together with the `--directory` option used to set the directory with a full or relative path (by default, the directory "scripts" at the working directory) and the `--extension` option used to define the extension of the scripts (by default, "sh", and which can be set to "none" for any extensions).

For example, the following command should run all files, regardless of extensions, at the directory `/home/user/run_scripts`:

```Bash
tmux-control.py --run --directory=/home/user/run_scripts --extension=none
```

```
-----------------------
|                     |
|                     |
|                     |
|                     |
|      scripts        |
|                     |
|                     |
|                     |
|                     |
-----------------------
```

### work mode

This mode is designed to be a compromise between analysis, edit and badass modes.

```
-----------------------
|                     |
|       ranger        |
|---------------------|
|                     |
|      terminal       |
|---------------------|
|          |          |
|  ranger  |  cmus    |
|          |          |
-----------------------
```

