# Mars Climate Orbiter Project
This repository contains a set of scripts that compare the execution time of two functions used to convert metric units. These scripts were created to replicate the scenario that led to the loss of the Mars Climate Orbiter by NASA in 1998, caused by a mix-up of metric and imperial units.

## Code 1
The first script assumes that the input metric values are already in the correct format, and provides a function to perform the conversion. The function is defined as follows:

```
def no_need_to_convert_metric(value):
  return value / 1000
```

## Code 2
The second script checks the input metric format and converts the values if necessary. It provides a function that performs the conversion based on the input unit. The function is defined as follows:

```
def convert_metric2(value, unit):
    if unit.lower() == "meters":
        return value / 1000
    elif unit.lower() == "kilometers":
        return value * 1000
    elif unit.lower() == "feet":
        return value / 3280.84
    elif unit.lower() == "miles":
        return value * 1.60934
    else:
        raise ValueError("Invalid unit: {}".format(unit))
```

## Performance Test
Both scripts are tested for performance using the time module in Python. The scripts are run 10 times, and the execution time is measured for 100,000 iterations of the conversion function. The average execution time is calculated for each script, and the percentage difference between the two is also calculated. The script determines which function is faster based on the percentage difference.

## Results
The results of the performance test are printed to the console in a clear and concise way. The average execution time of Code 1 and Code 2 are displayed, as well as the percentage difference between the two. The script also displays a message indicating which function is faster based on the percentage difference.

## Conclusion
This repository demonstrates the importance of unit consistency, and how a small mistake in units can lead to catastrophic results. By comparing the execution time of the two scripts, we also demonstrate the importance of code efficiency and how small changes in code can make a big difference in performance.