# Package Structure

A DataWithCalc package consists of data, calculation and configuration. The configuratioin includes the computation graph and attributes of data and calculations.

A package will be stored as a folder. The configuration will be stored inside it. Data and calculations can be stored either inside or outside the package folder.

## Data and Calculations

Each instance of data and calculations is stored in a file or folder. A instance can't be placed in the position occupied by other instances.

External instances are stored outside the package folder, so you can read or write existing files without copying or moving them. Their absolute paths are stored in the configuration.

Internal instances are stored inside the package folder, so they can be distributed with the package. Datas are stored under a subfolder named ```Data``` and calculations are stored under a subfolder named ```Calculations```. Their relative paths to the corresponding folder are stored in the configuration.

If some calculations are common, you may implement it in a calculation module instead of a calculation instance for better sharing across packages.

## Configuration

The configuration is stored under a subfolder named ```DataWithCalcConfig```. The data information is stored in  ```DataWithCalcConfig/Data```, the calculation information is stored in ```DataWithCalcConfig/Calculation```, and the computation graph information is stored in ```DataWithCalcConfig/Graph```
