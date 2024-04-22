import pandas as pd
import numpy as np

def loadData(df, outputFile):
    try:
        with pd.ExcelWriter(outputFile) as writer:
            df.to_excel(writer, sheet_name='HR data', index=False)
        return True
    except Exception as e:
        print(f"Error occurred while saving to Excel: {e}")
        return False