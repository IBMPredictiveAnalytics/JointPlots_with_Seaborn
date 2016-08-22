
import pandas as pd
import bokeh
from bokeh.charts import output_file, Donut
from bokeh.io import show, save
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

import sys

if len(sys.argv) > 1 and sys.argv[1] == "-test":
    import os
    df = pd.read_csv("Datasets/DRUG1N.csv")
    y_field = "Na"
    x_field = "K"
    output_option = 'output_to_screen'
    output_path = '/tmp/foo.html'
    sz=10
    title_font_size = 32
    title = "Test Test Test Test Test Test"
    kind="scatter"
    color="green"
else:
    import spss.pyspark.runtime
    ascontext = spss.pyspark.runtime.getContext()
    sc = ascontext.getSparkContext()
    sqlCtx = ascontext.getSparkSQLContext()
    df = ascontext.getSparkInputData().toPandas()
    y_field = '%%y_field%%'
    x_field = '%%x_field%%'
    kind = '%%kind%%'
    output_option = '%%output_option%%'
    output_path = '%%output_path%%'
    sz = int('%%output_size%%')
    title_font_size = int('%%title_font_size%%')
    title = '%%title%%'
    color='%%color%%'

g = sns.jointplot(x_field, y_field, data=df,
                   size=sz,kind=kind,color=color,dropna=True)

ax = g.ax_joint


ax.set_title(title,fontsize=title_font_size,y=1.2)


# g.gcf().ylabel(y_field,fontsize=output_font_size)

if output_option == 'output_to_file':
    if not output_path:
        raise Exception("No output path specified")
else:
    output_path="/tmp/output.svg"

g.savefig(output_path)

if output_option == 'output_to_screen':
    # import matplotlib.pyplot as plt
    # plt.show()
    import webbrowser
    webbrowser.open(output_path)
    print("Output should open in a browser window")
else:
    print("Output should be saved on the server to path: "+output_path)
