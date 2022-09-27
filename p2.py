import pandas as pd
# construct the pd dataframe
placement = pd.DataFrame(columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

i = 0
# start for loops
for l1 in ['quarry', 'factory', 'market']:
    i = i + 1
    for l2 in ['quarry', 'factory', 'market']:
        i = i + 1
        for l3 in ['quarry', 'factory', 'market']:
            i = i + 1
            for l4 in ['quarry', 'factory', 'market']:
                i = i + 1
                for l5 in ['quarry', 'factory', 'market']:
                    i = i + 1
                    for l6 in ['quarry', 'factory', 'market']:
                        i = i + 1
                        for l7 in ['quarry', 'factory', 'market']:
                            i = i + 1
                            for l8 in ['quarry', 'factory', 'market']:
                                i = i + 1
                                for l9 in ['quarry', 'factory', 'market']:
                                    i = i + 1
                                    for l10 in ['quarry', 'factory', 'market']:
                                        i = i + 1
                                        for l11 in ['quarry', 'factory', 'market']:
                                            i = i + 1
                                            for l12 in ['quarry', 'factory', 'market']:
                                                i = i + 1
                                                # combine every items into one file
                                                placement.loc[i] = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]

# output all results as csv file
placement.to_csv('a2.csv')
