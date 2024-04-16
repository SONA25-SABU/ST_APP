import streamlit as st

def main():
    st.title("About Page")
   

    st.header("Women’s Clothing E-Commerce dataset")
    st.write(
        """
       This is a Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Its
nine supportive features offer a great environment to parse out the text through its multiple dimensions.
Because this is real commercial data, it has been anonymized, and references to the company in the
review text and body have been replaced with “retailer”.
        """
    )

    st.header("Content")
    st.write(
        """
        This dataset includes 23486 rows and 10 feature variables. Each row corresponds to a customer review,
and includes the variables:

● Age: Positive Integer variable of the reviewers' age.
● Title: String variable for the title of the review.
● Review Text: String variable for the review body.
● Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1
Worst to 5 Best.
● Recommended IND: Binary variable stating where the customer recommends the product
where 1 is recommended, and 0 is not recommended.
● Positive Feedback Count: Positive Integer documenting the number of other customers who
found this review positive.
● Division Name: Categorical name of the product high-level division.
● Department Name: Categorical name of the product department name.
● Class Name: Categorical name of the product class name.
        """
    )

if __name__ == "__main__":
    main()
# git init
# git add .
# git commit -m "Your commit message here"
# git push --set-upstream origin master
# git push