# Deploying the model

## Challenge:

The virtual private server on the company's Web Service cloud is used to run programs that help perform calculations on large data sets. Recently, the performance of some programs has
degraded.

Technical support has recommended that processes that consume a lot of main memory should be deleted. Unfortunately, the command-line shell that you use only lets you delete processes that form a single contiguous segment of a given fixed size. The size of a contiguous segment is the number of contiguous processes in main memory.

Find the minimum amount of main memory used by all of your processes in your instance after you delete a contiguous segment of processes.

Example:

```bash
process = [10, 4, 8, 13, 201
m = 2
```

Select a fixed contiguous segment size of m = 2. The best single contiguous segment of size 2 to delete is the segment composed of process 5, which is 20KB, and process 4, which is 13KB. This results in the minimum total main memory consumption of 10KB + 4KB + 8KB = 22KB. Return 22.

![Alt text](/leet_code/challenge_img.png "Title")

The `cd` command allows you to change directories. Assuming you are at the directory where you issued the cloning command, type the following on your terminal.

```bash
cd Fake-News-Detection-Machine-Learning-Pipeline
```

This will bring you to the project directory.

## Using Python Virtual Environment with Conda

### Prerequisites: Have [conda](https://docs.conda.io/en/latest/) installed on your local machine.

I used Conda as an environment management system so that all the dependencies you need for this ungraded lab are stored in an isolated environment.

Conda includes a lot of libraries so if you are only installing it to complete this lab , we suggest using [miniconda](https://docs.conda.io/en/latest/miniconda.html), which is a minimal version of conda.

### 1. Creating a virtual Environment

Now we assume that you either successfully installed conda or that it was previously available in your system. The first step is creating a new developing environment. Let's set a new environment with python 3.9.7 with this command:

```bash
conda create --name ml-thesis-env python=3.9.7
```

After successfully creating the environment, you need to activate it by issuing this command:

```bash
conda activate ml-thesis-env
```

At this point, you will do all your libraries installation and work in this environment. So, whenever working on this ungraded lab, check the ml-lab environment is active (in the terminal prompt you will see this when the virtual envioroment is activated).

### 2. Installing dependencies using PIP

Before proceeding, double check that you are currently on the `ML-Model-Production` directory, which includes the `requirements.txt` file. This file lists all the required dependencies and their respective versions. Now use the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

This command can take a while to run depending on the speed of your internet connection. Once this step completes you should be ready to spin up jupyter lab and begin working on the notebook.

Note: After installing dependencies we have to now add virtual env to jupyter lab by doing this:

```bash
conda install ipykernel
```

```bash
ipython kernel install --user --name=<any_name_for_kernel>
```

```bash
conda deactivate
```

an the activate the enviroment again:

```bash
conda activate ml-thesis-env
```

In case you want to delete kernel with the virtual env:

```bash
jupyter kernelspec remove <kernel-name>
```

### 3. Launching Jupyter Lab

Jupyter lab was installed during the previous step so you can launch it with this command:

```bash
jupyter lab
```

After execution, you will see some information printed on the terminal. Usually the lab opens after you type the previous command on temrinal or you might need to authenticate to use Jupyter lab. For this, copy the token that appears on your terminal, head over to [http://localhost:8888/](http://localhost:8888/) and paste it there.

### 4. Running the notebook

Within Jupyter lab you should be in the same directory where you used the `jupyter lab` command.

Look for the `Notebooks.ipynb` file and open it to begin the ungraded lab.

To stop jupyter lab once you are done with the lab just press `Ctrl + C` (Windows) or `Cmd + C` (Mac) twice on terminal.

### And... that's it! You deployed my Machine learning model! :)
