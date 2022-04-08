# demo-attributes
tweaking git attributes to change the language displayed in github

# Step1: Create .gitattribtue file in root directory of your project.

### example 1:
Example of a `.gitattributes` file which reclassifies `.py` files as Java:

*.py linguist-language=Java

### example 2:
identify all .r files as python

*.r linguist-language=Python linguist-detectable

### example 3:
identify all files from folder1 as Scala

folder1/* linguist-language=Scala linguist-detectable
