import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'prices': [4545,56666,77777]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
