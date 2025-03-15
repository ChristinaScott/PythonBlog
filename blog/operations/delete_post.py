from blog.database import connect_db

def delete_post():
    """Delete a blog post by ID."""
    #in this function, we will take function that returns the connection object (conn1) and assign it to a variable to use here (conn2).
    
    conn2 = connect_db()
    #now we can use the conn variable to interact with our db
    #a "cursor", in databases is an object that allows you to execute SQL commands and fetch results. 
    #in the next line, we create a cursor object from the connection object.
    cursor = conn2.cursor()
    # now we have an object (cursor) we can use to send SQL queries to DB

    
    post_id = input("Enter the ID of the post to delete: ")
    
    cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn2.commit()
    conn2.close()
    print("Post deleted successfully!")


