# coding: utf-8
import numpy as np
import pandas as pd
import yaml
from pyFAST.input_output import TurbSimFile
import pyFAST.case_generation.case_gen as case_gen
from pyFAST.input_output import FASTInputFile
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

def gen_siv_viv_cases(yaml_file):
    """Generate a set of OpenFAST cases to investigate effect of SIV/VIV 

    Inputs:
       yaml_file: 

    Outputs:
       None: Files written to appropriate folders
    """
    
    ref_dir   = '/scratch/asharma/siv_viv/q4_2023/template'  # Folder where the fast input files are located (will be copied)
    main_file = '/scratch/asharma/siv_viv/q4_2023/template/IEA-15-240-RWT-Monopile.fst'  # Main file in ref_dir, used as a template
    work_dir = '/scratch/asharma/siv_viv/q4_2023/cases/locked_rotor'     # Output folder (will be created)
    PARAMS = []
    case_list = yaml.load(open(yaml_file), Loader=yaml.UnsafeLoader)['siv_viv_cases']
    for yc in case_list:
        ws = yc['ws']
        for yaw in yc['yaw']:
            print(yaw, ' ', ws)
            p = {}
            p['__name__'] = 'yaw_{:04.1f}_ws_{:04.1f}'.format(yaw, ws)
            p['EDFile|NacYaw'] = '{:04.4f}'.format( yaw )
            p['InflowFile|HWindSpeed'] = '{:04.4f}'.format( ws )
            PARAMS.append(p)

    fastfiles=case_gen.templateReplace(PARAMS, ref_dir, outputDir=work_dir, removeRefSubFiles=True, main_file=main_file, oneSimPerDir=True)
    
    # for l in lamda_range:
    #     f = FASTInputFile('lamda_{:04.1f}_phase_{:04.1f}_umean_{:04.1f}/InflowFile_UAero.dat'.format(l, phase, umean))
    #     for i in f:
    #         if ( (type(i['value']) == str) and ('BTS_FILE' in i['value']) ):
    #             i['value'] = '"UAero_lamda_{:04.1f}_phase_{:04.1f}_umean_{:04.1f}.bts"'.format(l, phase, umean)
    #             break
    #     f.write()


if __name__=="__main__":
    gen_siv_viv_cases('/scratch/asharma/siv_viv/q4_2023/cases/locked_rotor/case_list.yaml')
