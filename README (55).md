<!--

author:   Masub Makhdoom
email:    masub.makhdoom@ovgu.de
date:     29/04/2025
version:  31.0.0
language: en
narrator: UK English Female

repository: https://github.com/LiaScript/docs

logo:     img/logo.png

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css

link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css

import:   https://raw.githubusercontent.com/liaTemplates/ABCjs/main/README.md

link:     https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs
          https://fonts.googleapis.com/css2?family=Noto+Sans+Ogham

font:     Noto Sans Egyptian Hieroglyphs, Noto Sans Ogham
-->

## Markdown-Syntax

                           --{{0}}--
RStudio is an integrated development environment, or IDE, for the R programming language. It provides a user-friendly interface for writing code, analyzing data, and creating reports. RStudio helps students, researchers, and data analysts work more efficiently with R.
It includes a script editor, a console for running code, a workspace to view your variables, and a plots window to visualize your data. With RStudio, you can write R code, run it, and instantly see the results.
Whether you're doing statistical analysis, creating graphs, or building machine learning models, RStudio is a powerful tool to support your work.

Initial LIA-comment-tag for basic definitions:


```r

# Load required packages
library(readr)  # For reading CSV files
library(here)   # For project-relative paths

# Set working directory to project root (not always necessary with RProject, but good practice)
setwd(here::here())

# Read the CSV file
ai_competency_data <- read_csv("2024_25_Quant_Example_Data_AI_Competency.csv")

# Display the first few rows of the data
head(ai_competency_data)

# Display basic information about the dataset
glimpse(ai_competency_data)

```
# R project

                           --{{0}}--
An R Project is a way to organize your work in RStudio. It keeps all your files, code, and data in one place.
When you create an R Project, RStudio sets up a special folder. This folder contains everything related to your analysis, including scripts, datasets, and output files.
Using R Projects helps you stay organized and makes it easier to share your work with others. It also sets the working directory automatically, so you don’t need to change file paths each time.
R Projects are especially useful for larger tasks like data analysis, research projects, or academic assignments.

Here is example of r Project

```r

# Load required packages
library(readr)  # For reading CSV files
library(here)   # For project-relative paths

# Set working directory to project root (not always necessary with RProject, but good practice)
setwd(here::here())

# Read the CSV file
ai_competency_data <- read_csv("2024_25_Quant_Example_Data_AI_Competency.csv")

# Display the first few rows of the data
head(ai_competency_data)

# Display basic information about the dataset
glimpse(ai_competency_data)

```

