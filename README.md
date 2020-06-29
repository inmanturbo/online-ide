### Clear Linux* OS `machine-learning-ui` container image with
- [Jupyter php](https://litipk.github.io/Jupyter-PHP-Installer/) *Copyright (c) 2015-2017 Litipk* and 
- [Bash](https://github.com/takluyver/bash_kernel) *Copyright (c) 2015, Thomas Kluyver and contributors*  
kernels and gui web dev/web scraping ready environment in the browser. 

#### Installs open source git extension for Jupyter Lab, source and BSD 3-Clause License found here: 
- https://github.com/jupyterlab/jupyterlab-git *Copyright (c) 2017, Project Jupyter Contributors All rights reserved.*
#### Dockerfile also installs open source (MIT) laravel installer found here: 
- https://github.com/laravel/installer *Copyright (c) Taylor Otwell*

## Clone this repo

```bash
git clone https://github.com/inmanturbo/online-ide.git
```

## Change into cloned repo directory
```bash
cd online-ide
```
## Build this image
```bash
docker build -t mylab/online-ide .
```
## Run in container
```bash
docker run -it -p 8888:8888/tcp -p 8000:8000 -p 8080:8080 -m 4G mylab/online-ide
```
<pre> Grab the url with the token from your terminal output 
and paste it into your broswers address bar </pre>

## up and running with laravel
### start a bash notebook inside juptyer lab

```bash
cd root && laravel new myfirstproject
```

    [32mCrafting application...[39m
    [32mLoading composer repositories with package information[39m
    [32mInstalling dependencies (including require-dev) from lock file[39m
    [32mPackage operations: 97 installs, 0 updates, 0 removals[39m
      - Installing [32mdoctrine/inflector[39m ([33m2.0.3[39m): Loading from cache
     ...
     ...
    [32mPackage manifest generated successfully.[39m
    [33mApplication ready! Build something amazing.[39m


and that's it!

### up and running with django
```bash
cd root && virtualenv django-env
```

    created virtual environment CPython3.8.3.final.0-64 in 309ms
      creator CPython3Posix(dest=/django-env, clear=False, global=False)
      seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/.local/share/virtualenv/seed-app-data/v1.0.1)
      activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator



```bash
source django-env/bin/activate
```

    (django-env) 


```bash
python -m pip install django
```

    Requirement already satisfied: django in /django-env/lib/python3.8/site-packages (3.0.7)
    Requirement already satisfied: asgiref~=3.2 in /django-env/lib/python3.8/site-packages (from django) (3.2.10)
    Requirement already satisfied: pytz in /django-env/lib/python3.8/site-packages (from django) (2020.1)
    Requirement already satisfied: sqlparse>=0.2.2 in /django-env/lib/python3.8/site-packages (from django) (0.3.1)
    (django-env) 


```bash
django-admin startproject firstproject
```

    (django-env) 



# Original README below

# Clear Linux* OS `machine-learning-ui` container image

<!-- Required -->
## What is this image?

`clearlinux/machine-learning-ui` is a Docker image with `machine-learning-ui` running on top of the
[official clearlinux base image](https://hub.docker.com/_/clearlinux). 

<!-- application introduction -->
> Machine Learning UI provides the machine learning framework with Jupiter notebook with the 
> benefits of Clear Linux OS.

For other Clear Linux* OS
based container images, see: https://hub.docker.com/u/clearlinux

## Why use a clearlinux based image?

<!-- CL introduction -->
> [Clear Linux* OS](https://clearlinux.org/) is an open source, rolling release
> Linux distribution optimized for performance and security, from the Cloud to
> the Edge, designed for customization, and manageability.

Clear Linux* OS based container images use:
* Optimized libraries that are compiled with latest compiler versions and
  flags.
* Software packages that follow upstream source closely and update frequently.
* An aggressive security model and best practices for CVE patching.
* A multi-staged build approach to keep a reduced container image size.
* The same container syntax as the official images to make getting started
  easy. 

To learn more about Clear Linux* OS, visit: https://clearlinux.org.

<!-- Required -->
## Deployment:

### Deploy with Docker
The easiest way to get started with this image is by simply pulling it from
Docker Hub. 

1. Pull the image from Docker Hub: 
    ```
    docker pull clearlinux/machine-learning-ui
    ```

2. Start a container using the examples below:

    ```
    docker run -p 8888:8888 -it clearlinux/machine-learning-ui
    ```
    
<!-- Optional -->
### Deploy with Kubernetes
This image can also be deployed on a Kubernetes cluster, such as
[minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/).The
following example YAML template files are provided in the repository as
reference for Kubernetes deployment:

   * [`machine-learning-ui-deployment.yaml`](https://github.com/clearlinux/dockerfiles/blob/master/machine-learning-ui/machine-learning-ui-deployment.yaml):
     example to provide jupyter notebook service.

To deploy the image on a Kubernetes cluster:

1. Review the contents of the template file and edit appropriately for your needs.

2. Deploy machine-learning-ui-deployment.yaml.
    ```
    kubectl create -f machine-learning-ui-deployment.yaml
    ```

3. Navigate to http://<nodeip>:30001 in your browser, where 30001 is the port number defined in your service..

<!-- Required -->
## Build and modify:

The Dockerfiles for all Clear Linux* OS based container images are available at
https://github.com/clearlinux/dockerfiles. These can be used to build and
modify the container images.

1. Clone the clearlinux/dockerfiles repository.
    ```
    git clone https://github.com/clearlinux/dockerfiles.git
    ```

2. Change to the directory of the application:
    ```
    cd machine-learning-ui/
    ```

3. Build the container image:
    ```
    docker build -t clearlinux/machine-learning-ui .
    ```

   Refer to the Docker documentation for [default build arguments](https://docs.docker.com/engine/reference/builder/#arg).
   Additionally:
   
   - `swupd_args` - specifies arguments to pass to the Clear Linux* OS software
     manager. See the [swupd man pages](https://github.com/clearlinux/swupd-client/blob/master/docs/swupd.1.rst#options)
     for more information.

<!-- Required -->
## Licenses

All licenses for the Clear Linux* Project and distributed software can be found
at https://clearlinux.org/terms-and-policies
