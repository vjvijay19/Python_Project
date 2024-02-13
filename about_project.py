def about_project(db):

     col = db["about_project"]
     x = col.find_one()

     print(x["content"])