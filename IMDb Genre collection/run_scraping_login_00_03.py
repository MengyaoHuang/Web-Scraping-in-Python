from utils import *
from data_processing import *


# Box Offic Mojo by IMDbPro link
Boxofficemojo_genre_2000 = dic_to_frame(bl_2000, 2000)
Boxofficemojo_genre_2001 = dic_to_frame(bl_2001, 2001)
Boxofficemojo_genre_2002 = dic_to_frame(bl_2002, 2002)
Boxofficemojo_genre_2003 = dic_to_frame(bl_2003, 2003)
# Append and merge
Boxofficemojo_genre_2000_2003 = Boxofficemojo_genre_2000.append(Boxofficemojo_genre_2001, ignore_index = True)
Boxofficemojo_genre_2000_2003 = Boxofficemojo_genre_2000_2003.append(Boxofficemojo_genre_2002, ignore_index = True)
Boxofficemojo_genre_2000_2003 = Boxofficemojo_genre_2000_2003.append(Boxofficemojo_genre_2003, ignore_index = True)
# intermediate test
print(len(Boxofficemojo_genre_2000_2003))

# collected log-in needed link through "See more details at IMDbPro"
Boxofficemojo_genre_2000_2003['login_link'] = np.nan
Boxofficemojo_genre_2000_2003['imdb_idList'] = np.nan
for j in range(len(Boxofficemojo_genre_2000_2003)):
    temp_url = Boxofficemojo_genre_2000_2003['bomlink'][j]
    temp_login_url = login_link_extraction(temp_url)
    Boxofficemojo_genre_2000_2003['login_link'][j] = temp_login_url
    Boxofficemojo_genre_2000_2003['imdb_idList'][j] = extract_movie_id(temp_login_url)
    # progress
    if j % 50 == 0:
        print(j)
# intermediate test
print("ID extraction done!")

# fillin genres once setup driver and successfully login
Boxofficemojo_genre_2000_2003['imdb_genre_textList'] = np.nan
result_frame = get_pageSource_genre(launch_selenium(), Boxofficemojo_genre_2000_2003, 'imdb_genre_textList')

# split column of lists into multiple columns
# https://stackoverflow.com/questions/44663903/pandas-split-column-of-lists-of-unequal-length-into-multiple-columns
genre_df = result_frame.imdb_genre_textList.apply(pd.Series).add_prefix('Genre_')
result_frame = pd.concat([result_frame, genre_df], axis=1, sort=False)
# storage
result_frame.to_csv("Boxofficemojo_genre_2000_2003.csv")

"""
import ast
import pandas as pd
result_frame = pd.read_csv("Boxofficemojo_genre_2000_2003.csv")
result_frame = result_frame[["bomtitle","bomlink","year","login_link", "imdb_idList", "imdb_genre_textList"]]
for i in range(len(result_frame)):
  res = ast.literal_eval(result_frame['imdb_genre_textList'][i])
  res = [element.strip() for element in res]
  result_frame['imdb_genre_textList'][i] = sorted(list(set(res)))
"""


