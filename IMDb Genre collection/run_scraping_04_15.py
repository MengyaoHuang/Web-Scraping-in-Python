from  utils import  *
from data_processing import Boxofficemojo_genre


# run collection
for i in range(len(Boxofficemojo_genre)):
    Boxofficemojo_genre['imdb_genre_text'][i] = imdblink_extraction(Boxofficemojo_genre['imdblink'][i])
    # process
    if i % 200 == 0:
        print(i)

# split column of lists into multiple columns
# https://stackoverflow.com/questions/44663903/pandas-split-column-of-lists-of-unequal-length-into-multiple-columns
genre_df = Boxofficemojo_genre.imdb_genre_text.apply(pd.Series).add_prefix('Genre_')
result = pd.concat([Boxofficemojo_genre, genre_df], axis=1, sort=False)
# storage
result.to_csv("Boxofficemojo_genre_2004_2015.csv")