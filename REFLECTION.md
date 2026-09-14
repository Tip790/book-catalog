# 0.5 .FAILED (errors=1) 'ERROR: False is not true : Couldn't find 'The Pale Writer' in the following response


## This is the failed test message I got from breaking the 'views.py' for the Books. It couldn't find the right book on the book_list as the books no longer displayed, thus giving an error as it could not find the specific book 'The Pale Writer'.

# 1. Your models use two foreign keys. Pick one of them. Name which model carries the ForeignKey and which model it points at, and explain why you arranged it that way. What would be different about the data you entered if you had reversed it?

## I selected The "book" Foreign key connected the Reviews model to the Book model because many reviews could be about one book. If this was swapped, (which I had tried to do earlier) by having the books model hold the foreign key to reviews, it just broke as it could not define the Review model as it came after the Book model in the code. Making it impossible to be a child for a Model that was created after it. 

# 2. You added one field of your own to Book. Which field type did you choose, and why that type rather than another? What would you lose if you had stored the same fact as a CharField?

## The field I added was orginally another 'CharField' but seeing as it says something different in the reflection, I went back quickly and changed it to a 'DecimalField' to caclulate the price of the book. I picked it as it was one of the few on the reference sheet that seemed like a quick fix for accidentaly messing up and doing another 'CharField'. If I stored price as a 'Charfield' there would be the possibilty that someone would put a letter instead of a digit into the code, or without the decimals there would be no change, making gauging the price much more difficult in the database.


