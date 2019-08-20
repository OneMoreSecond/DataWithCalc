# DataWithCalc

DataWithCalc is a tool for storing data and calculations on data together. It enables us to manage all data generated from calculations easily. 

Any data format and calculation format could be supported. The calculated data can be cached for further computations.

```
Raw data -----------
                   |--> Calculations
Calculated data ----         |
      ^                      |
      |                      |
      ------------------------
```

### Concepts

##### Data Module

The data module is used to support certain data type.

##### Calculation Module

The calculation module is used to support certain calculation type.

##### Package

A DataWithCalc package consists of data, calculation and configuration. The configuratioin includes the computation graph and attributes of data and calculations.