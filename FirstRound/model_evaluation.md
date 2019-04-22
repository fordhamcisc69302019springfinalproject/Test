## Logistics Regression
#### Summary
| Criteria  | Stats | Result |
| ---- | ----- | ------ |
| Correctly Classified Instances |  27751   | 85.2303% |
| Incorrectly Classified Instances  |   4809     |    14.7697%|
| Kappa statistic  |  |   0.5695 |
| Mean absolute error   |  |   0.2023 |
| Root mean squared error | | 0.3196 |
| Relative absolute error | | 55.3183% |
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

## Random Forest
#### Summary
| Criteria | Stats | Result |
| ---- | ----- | ------ |
| Correctly Classified Instances    |   27581      |         84.7082%|
| Incorrectly Classified Instances   |   4979      |         15.2918%|
| Kappa statistic             |  |             0.5634|
| Mean absolute error         |  |             0.1975|
| Root mean squared error       |  |           0.3271|
| Relative absolute error       |  |          54.0053%|
| Root relative squared error    |  |         76.5111%|
| Total Number of Instances       |     32560   |  |

#### Detailed Accuracy By Class
|  |TP Rate | FP Rate | Precision | Recall  | F-Measure | MCC  |  ROC Area | PRC Area | Class |
| ---- | ----- | ------ |---- | ----- | ---- | ----- | ---- | ----- | -----|
|| 0.919 |   0.379  |  0.884   |   0.919  |  0.901    |  0.565  |  0.896   |  0.962   |   <=50K|
        |  |         0.621  |  0.081   | 0.708    |  0.621  |  0.662   |   0.565 |   0.896   |  0.747   |   >50K|
|Weighted Avg.  |  0.847  |  0.307  |  0.842  |    0.847  |  0.844  |    0.565 |   0.896    | 0.910 |

#### Confusion Matrix
 | a   |  b  | Classification|
   | ---- | ----- | ------ |
 |22713 | 2006 |     a =  <=50K|
 | 2973 | 4868 |     b =  >50K|
