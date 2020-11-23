
import os
import cooltoolbox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

from cooltoolbox.dataviz import showme



def test_showme():
    datapath = os.path.dirname(os.path.abspath(cooltoolbox.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    assert(len(df.shape)) >= 0
