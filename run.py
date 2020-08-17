import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)
from CM.CM_TUW9.bottom_up_hdm import zonStat_selectedArea as zs
import CM.CM_TUW9.run_cm as CM9


def execute(building_strd_info_csv, output_dir):
    heatDensityRaster = output_dir + os.sep + 'Heat_Density_Map.tif'
    gfaDensityRaster = output_dir + os.sep + 'GFA_Density_Map.tif'
    outputs = zs(building_strd_info_csv, heatDensityRaster, gfaDensityRaster)
    return {"Absolute heat demand": outputs[0]}


if __name__ == "__main__":
    output_dir = path + os.sep + 'Outputs'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    from pprint import pprint
    building_strd_info_csv = path + '/Inputs/sample_buildingsDB_BUHDM.csv'
    outputs = execute(building_strd_info_csv, output_dir)
    pprint(outputs)
