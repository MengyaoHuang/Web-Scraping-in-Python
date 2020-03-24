import pandas as pd
import numpy as np

# read table and set up initial fillin columns
# From year 2004 to year 2015
Boxofficemojo_genre =  pd.read_csv("Boxofficemojo_genre.csv", encoding="iso-8859-1")
Boxofficemojo_genre['imdb_genre_text'] = np.nan

# collection Top 200 from website below
bl_2000 = "https://www.boxofficemojo.com/year/2000/?ref_=bo_yl_table_21"
bl_2001 = "https://www.boxofficemojo.com/year/2001/?ref_=bo_yl_table_21"
bl_2002 = "https://www.boxofficemojo.com/year/2002/?ref_=bo_yl_table_21"
bl_2003 = "https://www.boxofficemojo.com/year/2003/?ref_=bo_yl_table_21"