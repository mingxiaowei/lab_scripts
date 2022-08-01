# HCN Data Analysis Scripts
## Set Up 
* Folder layout:
```
\current directory 
  \experiment folder 
    \lab notebook.rtf
    \Cell1
    \Cell2
    \...
  \HCN_scripts (folder from this repo) 
```
* Within each cell folder, determine the file for HCN recording and adds "HCN" in its file name
    * For example, change `20220729_Cell1_0001.abf` to be `20220729_Cell1_0001_HCN.abf`
    * Do this for each cell 
## Run scripts 
* In the terminal, `cd` into the directory that contains both the experiment folder and the script folder
    * Run `python3 -m HCN_scripts`
    * All outputs will be written into a `csv` file 
## Output
The output `csv` file includes: 
* Experiment date + title 
* A list of blockers
* Internal solution 
* Mouse information
    * A list of genotype 
    * Gender 
    * DOB 
    * Age in days 
* Cell information
    * Statistics from the membrane test 
    * Cell depth (soma to dendrite)
    * HCN current at each voltage step
 
