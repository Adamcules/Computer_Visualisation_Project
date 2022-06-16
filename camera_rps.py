import time
import numpy as np

def get_prediction():
    import model_download_code
    p_list = model_download_code.prediction[0]
    max_value = max(p_list)
    ind_value = (np.where(p_list == max_value))[0]
    if ind_value == 0:
        return "Nothing"
    elif ind_value == 1:
        return "Rock"
    elif ind_value == 2:
        return "Paper"
    elif ind_value == 3:
        return "Scissors"

print (get_prediction())

