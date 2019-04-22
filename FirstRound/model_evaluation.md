## Logistics Regression
#### Summary
| Name | Stats | Result |
| ---- | ----- | ------ |
| Correctly Classified Instances |  27751   | 85.2303 % |
| Incorrectly Classified Instances  |   4809     |    14.7697 %|
| Kappa statistic  |  |   0.5695 |
| Mean absolute error   |  |   0.2023 |
| Root mean squared error | | 0.3196 |
| Relative absolute error | | 55.3183 % |
| Root relative squared error | | 74.74% |
| Total Number of Instances | 32560 |  |   

#### Detailed Accuracy By Class
|  |TP Rate | FP Rate | Precision | Recall  | F-Measure | MCC  |  ROC Area | PRC Area | Class |
| ---- | ----- | ------ |---- | ----- | ---- | ----- | ---- | ----- | -----|
|  |  0.931 | 0.397 |  0.881 | 0.931 | 0.905 |  0.574| 0.906  | 0.967  |    <=50K |
 |    |  0.603  |  0.069  |  0.736    |  0.603   | 0.663   |   0.574  |  0.906     |0.767    |  >50K |
|Weighted Avg.  |  0.852   | 0.318  |  0.846    |  0.852  |  0.847      |0.574 |   0.906   |  0.919    |

#### Confusion Matrix
 |    a  |   b |  Classification |
 | ---- | ----- | ------ |
 | 22713 | 2006 |     a =  <=50K |
 | 2973 | 4868 |     b =  >50K |
