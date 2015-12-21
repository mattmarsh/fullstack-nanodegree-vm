#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Database connection
conn = psycopg2.connect("dbname=forum")
cur = conn.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    cur.execute("SELECT time, content FROM posts ORDER BY time DESC;")
    posts = [{'content': str(bleach.clean(row[1])), 'time': str(row[0])} for row in cur.fetchall()]
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))
    cur.execute("INSERT INTO posts (content) VALUES (%s);", (content,));
    conn.commit();
    