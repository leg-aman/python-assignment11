import pandas as pd
import matplotlib.pyplot as plt

# load a dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100,150,200,250,300,350],
    "Expenses": [80,120,180,200,220,300]
}
df = pd.DataFrame(data)

# Line plot
df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title= "sales vs expense")
plt.show()

# Bar plot
df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
plt.show()