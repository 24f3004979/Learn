# Basic ML setup
First step is to know what domain we have to make our project for and use the right tool for the required setup.

## Seting up tensorflow with GPU acceleration

Standard path way for GPU setup
`cannot dlopen some GPU libraries`
Default cuda setup with pip
`pip install tensorflow[and-cuda]`

Basic gpu testing script to run
Simple library listing code for knowing that library detected your GPU machine.
`import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
`nvidia-smi` Basic check up for the gpu

fix code for automatically linkig the required paths for GPU detection
`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cuda_runtime/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cublas/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cudnn/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cufft/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/curand/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cusolver/lib:$(python -c 'import site; print(site.getsitepackages()[0])')/nvidia/cusparse/lib
`

## Command break down
Environment variable initialization for the virtual environement
export LD_LIBRARY_PATH=

$LD_LIBRARY_PATH: <- colns for separation for the paths,
Using simple inline python command line | site.getsitepakages()[0] listing simple paths about the pakages where they are installed into, 

Simple fix for geting NVIDIA GPU loading into the fedora linux environment.
 
