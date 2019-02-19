## Insight Data Engineering Data Challenge
#### Fiona Fan

### Approach
* My main approach is to construct a Prescription class that takes in the input, and a drugbook/drug class that can aggregate the input without losing too much informaiton.
* I have written three unit tests in Python, in src/test_pharmacy_counting.py. The testing code is incorporated into the shell script.
* New test cases are sampled from the large dataset.
* The code should be run in Python3

### Running
* For testing, please run `\insight_testsuite\run_tests.sh`.
* For normal running, please put the input in `\input\itcont.txt`. The output will be in `output\top_cost_drug.txt`
* I am not sure why my git cannot pass the structure test on the website, but this should be in the right format for structure.