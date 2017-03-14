# CUDA-Sublime-Text-Snippets

This package adds some CUDA functions snippets for Sublime Text.
## Installation ##
## Package Control (recommended) ##
The easiest way to install the CUDA Snippets is by using **Package Control**. 

 - Open Package Control (or hit Ctrl+Shift+P or Cmd+Shift+P) 
 - Type *install* and hit enter 
 - Type *CUDA Snippets* and hit enter again

## Cloning the Repository ##

You can manually install the package by using Git.

 - Navigate to Sublime’s Packages directory 
 - Run git clone https://github.com/LitLeo/CUDA-Sublime-Text-Snippets

To find out where the Packages directory is, you can go to Preferences and Browse packages…. This will open the directory in your file explorer.

## Downloading the Archive ##

If you don’t have Package Control or Git, you can also download the package. However you really should be using Package Control, because the process is simpler.

 - Open https://github.com/LitLeo/CUDA-Sublime-Text-Snippets in your
   browser
 - On the right hand side there is a Download ZIP button – click it 
 - Go to Preferences and Browse packages… which opens the Packages
   directory

## Problem ##

CUDA code is almost the same as C++ code, but I cann't use c++ packages, such as C++ sinppets, in CUDA C++ files.
https://forum.sublimetext.com/t/how-to-enable-c-sublime-package-in-cuda-files-cu-cuh/19014

The Temporary Solution:
Add several frequently-used c++ snippets.

Changed Snippets:
Remove function note and semicolon(;) of all snippets. - Extract the archive inside the Packages directory

## History ##

# v1.1.1 #
Before:
cudaFree(void* devPtr);
/*Frees memory on the device.*/ 

Now
cudaFree(void* devPtr)

# v1.2.0 #

New Snippets:
Add keywords snippets, such as 

__global__
__host__
__forceinline__
__managesharedd__
dim3
char2
char4
......


Thanks