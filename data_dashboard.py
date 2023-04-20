'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a driver file.

Note:
The user interaction part is not finished yet and will be put in a separate file.
I will add some explanations for "category" later in the canvas.

If you want to test this program, I suggest you choose the USA because the data is moderate and easy to observe

'''


# driver file is the controller

# analysis is controller / function is controller
# class is model
# viewer 

# pandas dataframe 不可以拿来做 analysis
# 应该用list of objects

import tkinter as tk
from tkinter import ttk
import pandas as pd


from get_and_clean_art_data import *
from get_and_clean_artist_data import *
from filter_data_and_draw_charts import *
from viewer import *



def main():

    try:

        # 1. Extract and clean the data we need from the website
        # finally we get two lists of lists, art_data and artist_data
        content_of_arts = get_art_csv_file()
        work_title = get_work_title_from_art_table(content_of_arts)
        type, status, material, neighbourhood = get_other_info_from_art_table(content_of_arts)
        artist_id, year = get_artist_id_and_year_from_art_table(content_of_arts)
        art_data = get_public_art_data(work_title, type, status, material, neighbourhood, artist_id, year)

        content_of_artists = get_artist_csv_file()
        id, first_name, last_name = get_basic_info_from_artist_table(content_of_artists)
        country = get_country_from_artist_table(content_of_artists)
        artist_data = get_public_arist_data(id, first_name, last_name, country)


        # 2.create two data frames according to these two lists of lists
        # data frames are used in user interaction to provide a sequence of options in the user interaction)
        df_artist = pd.DataFrame(artist_data, columns=["artist id", "first name", "last name", "country"])
        df_art = pd.DataFrame(art_data, columns = ["work title", "artist id", "type", "status", "material", "neighbourhood", "year"])

        # data frame 可以用来生成objects
        # 但是一旦生成list of objects之后，就不能再用data frame进行后面的分析了

        # test
        # print(df_artist.head(4))
        # print(df_artist.describe())
        # print(df_art.head(4))
        # print(df_art.describe())
        # print(df_artist.info())
        # print(df_art.info())
        
        # class View (GUI class?)
        # put root in driver
        
        # 3. Start interacting with the user
        # user will choose the country of artists and the category of their artworks
        # create the GUI window

        create_start_page(df_art, df_artist)
        
        

    except NameError as ne:
        print("NameError occurred")
    except TypeError as te:
        print(type(te), te)
    except ValueError as ve:
        print(type(te), te)
    except Exception as e:
        print("Other errors occurred", type(e), e)


if __name__ == "__main__":
    main()

    