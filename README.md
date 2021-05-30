# checksum-comparer
An easy-to-use CLI Checksum Comparison tool written in Python that generates and compares the checksum of two files within the current directory.  
_**Note:** Requires a working Python installation to function_  
_**Important:**_ This tool will only work on Windows Operating Systems.

## Supported Algorithms:
* MD5
* SHA1
* SHA256

## How to use:
* Clone the repository
* Take the file named "Checksum.py" and place it in the directory which contains the file whose checksum needs to be generated
* Run the script 
* The script will auto-detect the files present in the directory it was placed in and ask the user to select one
* Next, the user must select any one of the three supported algorithms
* If the user already has the expected hashvalue (from a website, or from the source) it can be entered in the next prompt. Else, hitting Enter will skip this step and display the hashvalue immediately without any comparisons.
* The status of the comparison of the expected hashvalue that was entered by the user and the generated hashvalue (be it matching or not matching) will be displayed finally.
* Finally, the comparison result between the generated and expected (user entered) hash values will be displayed
