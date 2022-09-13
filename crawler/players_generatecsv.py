from goodbooks_crawler import GB_Crawler
from random import randint
import pandas as pd
import time
import json

def main():
    goodbooks_books_csv_path = '../gb/books.csv'
    df = pd.read_csv(goodbooks_books_csv_path)

    engine = GB_Crawler()

    categories_data = dict()

    errors_ids = list()

    for _, row in df.iterrows():
        book_id = row['book_id']

        try:
            time.sleep(randint(5, 7))
            title = row['original_title']
            categories = engine.get_book_categories(title)
        except:
            try:
                time.sleep(randint(5, 7))
                title = row['title']
                categories = engine.get_book_categories(title)
            except:
                print(f'{book_id}| Error!')
                errors_ids.append(book_id)
                continue

        print(f'{book_id}| {title.strip()} | {categories}')

        for c in categories:
            try:
                categories_data[c].append(book_id)
            except:
                categories_data[c] = list()
                categories_data[c].append(book_id)

    df_dict = dict()
    df_dict['book_id'] = [ id for id in range(1, book_id + 1) ]

    for c in categories_data:
        df_dict[c] = list()
        for id in range(1, book_id + 1):
            df_dict[c].append(0 if categories_data[c].count(id) == 0 else 1)

    pd.DataFrame(df_dict).to_csv('goodbooks_categories.csv', index=False)

    with open('errors.json', 'w') as errors_file:
        json_dict = { 'errors_ids' : errors_ids}
        json.dump(json_dict, fp=errors_file)

if __name__ == '__main__':
    main()