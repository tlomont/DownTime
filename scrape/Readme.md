For each link you want to store, create an Item and then in the item store the URL, the name of page, the URL,
the tags describing it (use the method add_tag for this), the duration of time for which the page provides entertainment, and NOT the Date.
import item from db_connect
import write_items from db_connect
Once you have a list of items with all of these fields filled, then simply call write_items on the list and it will write to the database

Conventions:
1. Use underscores to_seperate_words_when_naming_functions
2. Class names should be capitalized
3. Make sure indentation is set to 4 spaces
