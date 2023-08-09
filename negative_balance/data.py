import pandas as pd
import numpy as np


class NBData(object):
    def __init__(self):
        return None
    
    def construct(self, df):
        """
        Given dataframe of column i, j, compute relationships between i and j
        """
        # Compute I_j and J_i
        I_j = {}
        J_i = {}
        for j in df.j.unique():
            I_j[j] = df[df.j == j].i.unique()
        for i in df.i.unique():
            J_i[i] = df[df.i == i].j.unique()
        ij_set = df[['i', 'j']].apply(tuple, axis=1).unique()
        return I_j, J_i, ij_set
    
    def toy(self):
        """
        Construct toy data attached to self, including:
        - I: set of accounts
        - J: set of banks
        - a_j: maximum balance for bank j
        - c_i: initial balance for account i
        - I_j: set of accounts for bank j
        - J_i: set of banks for account i
        """
        # Define data
        df = pd.DataFrame({
            'i': ["a1", "a2", "a3", "a3", "a3", "a4"],
            'j': ["b1", "b1", "b1", "b2", "b2", "b3"],
        })
        df['x'] = 1
        df = df.groupby(['i', 'j']).sum().reset_index()
        
        # Define sets
        self.I = df.i.unique()
        self.J = df.j.unique()
        
        # Define parameters to be random numbers
        self.c_i = {i: -5 for i in self.I}
        self.a_j = {j: 8 for j in self.J}
        
        # Define relationships
        self.I_j, self.J_i, self.ij_set = self.construct(df)
        
        print("Done!")
        
        return self