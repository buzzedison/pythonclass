def main(): 
    

    movies = [
    {
        "name": "Black Panther",
        "Score": 6.0,
        "Category": "Action"
    },

    {
        "name": "Acriomony",
        "Score": 7.5,
        "Category": "Romance"
    },

    {
        "name": "Star Trek Discovery",
        "Score": 7.0,
        "Category": "Fiction"
        
    },

    {
        "name": "Queer Eye",
        "Score": 5.0,
        "Category": "Romance",
        
    },

    {
        "name": "Fast and Furious",
        "Score": 8.0,
        "Category": "Action",
        
    },

    {
        "name": "You, Me, Her",
        "Score": 5.0,
        "Category": "Romance",
        
    }

    
]
    

    for mov in movies:
        if mov("name") == "moviemain" and mov("Score") > 5.5:
            the_score = True
        elif mov("name") == "moviemain" and mov("Score") < 5.5:
            the_score = "Sorry, movie score is less than 5.5"
        return the_score
    main()