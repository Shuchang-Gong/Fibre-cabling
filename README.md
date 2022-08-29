
# Option Pricing EXCEL plugin Project

-------------

----

### Environment Setting
This project is to implement functions in the EXCEL. We use C# and EXCELDna package to complete the project. 

- The C# framework version is 4.7.2.
- The ExcelDna.Integration version is 1.5.1.
- The ExcelDna.IntelliSense version  is 1.5.1.
- The MathNet.Numerics version is 5.0.0.
---
### ExcelDna Package

- This package is used to create .xll file. 
- ExcelDna [Homepage](https://excel-dna.net/)
- ExcelDna [Github-Page](https://github.com/Excel-DNA/ExcelDna)
---

### C-sharp codes

- All code is encapsulated in one file (Func1.cs).
- There are comments in the file for people to maintain the code.
---

### XLL File

- There are two DNA files. These DNA files ref to the dll file which generate from the C-sharp codes. 
- Using the ExcelDnaPack.exe file to generate the dll files to xll file.
- There are two xll file. One ending with 64 prepares to system with 64 bits. Another prepares to system with 32 bits. 
- Attention!  Using dll packages in the C-sharp code should be included in the same main dll file. 
- DnaFunc64-packed.xll and DnaFunc64-packed.xll is the final EXCEL plugin applications.
---
