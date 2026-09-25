# post = "sujan is a good boy, sujan is amazing, sujan always wakes up early and he is excellent"

post = input("Enter your post: ")

# You can take post input aswell 


# Lower function can detect sujan in lowercase also and post.lower can detect lower case anywhere 

if ("sujan".lower() in post.lower()):
    print("This post is about sujan")
else:
    print("This post is not about sujan")