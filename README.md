# bile_acid_img

**ANSC499 Final Project**

This repository contains code and analysis for exploring how different bile acid treatments affect the counts of M0, M1, and M2 macrophage phenotypes using image‑based cell segmentation.

## Table of Contents

- [Overview](#overview)  
- [Dependencies](#dependencies)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Output](#output)  


## Overview

Under various bile acid treatments, we segment and count macrophages (M0, M1, M2) from TIFF images using Cellpose, and then compare the total cell counts across conditions.

## Dependencies

- Python 3.8+  
- numpy  
- matplotlib  
- scikit-image  
- cellpose  

You can install everything at once:

```bash
pip install numpy matplotlib scikit-image cellpose
```
## Usage
 python cell_count.py ./Bile\ Acid\ BMDM\ Images --output_csv ./cell_counts.csv --annotate_dir ./annotated_images

## Output
all labeled figure in annotated_images folder
cell counts in cell_count.csv
statistic analysis in R markdown format

