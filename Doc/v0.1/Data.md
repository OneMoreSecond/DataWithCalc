# Data

## Data module

A data module contains code used to process a data type. Data modules are placed in ```DataWithCalc/DataModules``` and can be called by the DataWithCalc engine.

The data module should contains a class derived from ```DataModules.Data.Data```. The type of a data instance will be represented by the corresponding data module, so the engine could call the data module to process the data.
