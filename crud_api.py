from main import Users, Address, Company, Comments, posts, db, app
from sqlalchemy import select
from flask import request

conn = db.engine.connect()

################# USERS ####################
@app.route("/users", methods=['GET'])
def user_with_args():
    args = request.args.to_dict()

    return user_by_id(args['id'])

@app.route("/users",methods=['POST'])
def users(): 

    stmt = select(Users)

    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:
        address_stmt = select(Address).where(Address.users_id == item[0])
        address = conn.execute(address_stmt).fetchall()[0]

        company_stmt = select(Company).where(Company.users_id == item[0])
        company = conn.execute(company_stmt).fetchall()[0]

        child_dict = {
            item[0] : {
                "name" : item[1],
                "username" : item[2],
                "email" : item[3],
                "phone" : item[4], 
                "website" : item[5],
                "address" : {
                    "street" : address[2],
                    "suite" : address[3],
                    "zipcode" : address[4],
                    "geo" : {
                        "lat" : address[5],
                        "lng" : address[6],
                        }
                    },
                "company": {
                    "name" : company[2],
                    "catch_phrase" : company[3],
                    "bs" : company[4],
                }
            }
        }


        parent.update(child_dict)

    return parent

@app.route("/users/<int:id>", methods=['PUT'])
def user_by_id(id:int):
    stmt = select(Users).where(Users.id_users == id)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:
        address_stmt = select(Address).where(Address.users_id == item[0])
        address = conn.execute(address_stmt).fetchall()[0]

        company_stmt = select(Company).where(Company.users_id == item[0])
        company = conn.execute(company_stmt).fetchall()[0]

        child_dict = {
            item[0] : {
                "name" : item[1],
                "username" : item[2],
                "email" : item[3],
                "phone" : item[4], 
                "website" : item[5],
                "address" : {
                    "street" : address[2],
                    "suite" : address[3],
                    "zipcode" : address[4],
                    "geo" : {
                        "lat" : address[5],
                        "lng" : address[6],
                        }
                    },
                "company": {
                    "name" : company[2],
                    "catch_phrase" : company[3],
                    "bs" : company[4],
                }
            }
        }


        parent.update(child_dict)

    return parent

@app.route("/users/<string:username>", methods=['PUT'])
def user_by_username(username:str):
    stmt = select(Users).where(Users.username == username)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:
        address_stmt = select(Address).where(Address.users_id == item[0])
        address = conn.execute(address_stmt).fetchall()[0]

        company_stmt = select(Company).where(Company.users_id == item[0])
        company = conn.execute(company_stmt).fetchall()[0]

        child_dict = {
            item[0] : {
                "name" : item[1],
                "username" : item[2],
                "email" : item[3],
                "phone" : item[4], 
                "website" : item[5],
                "address" : {
                    "street" : address[2],
                    "suite" : address[3],
                    "zipcode" : address[4],
                    "geo" : {
                        "lat" : address[5],
                        "lng" : address[6],
                        }
                    },
                "company": {
                    "name" : company[2],
                    "catch_phrase" : company[3],
                    "bs" : company[4],
                }
            }
        }


        parent.update(child_dict)

    return parent



################# COMMENTS ####################

@app.route('/comments', methods=['GET'])
def comments():
    stmt = select(Comments)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}
    for item in result_list:
        
        child_dict = {
            item[0] : {
                "postId" : item[1],
                "name" : item[2],
                "email" : item[3],
                "body" : item[4], 
            }
        }

        parent.update(child_dict)


    return parent

@app.route('/comments', methods=['POST'])
def comments_with_args():
    args = request.args.to_dict()

    return comments_by_post_id(args['postId'])

@app.route('/comments/<int:post_id>', methods=['PUT'])
def comments_by_post_id(post_id):
    stmt = select(Comments).where(Comments.post_id == post_id)

    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}
    for item in result_list:
        
        child_dict = {
            item[0] : {
                "postId" : item[1],
                "name" : item[2],
                "email" : item[3],
                "body" : item[4], 
            }
        }

        parent.update(child_dict)


    return parent

@app.route('/comments/<string:email>', methods=['PUT'])
def comments_by_email(email):
    stmt = select(Comments).where(Comments.email_address == email)

    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}
    for item in result_list:
        
        child_dict = {
            item[0] : {
                "postId" : item[1],
                "name" : item[2],
                "email" : item[3],
                "body" : item[4], 
            }
        }

        parent.update(child_dict)


    return parent

################# POSTS ####################

@app.route('/posts', methods=['GET'])
def posts_function():
    stmt = select(posts)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:

        child_dict = {
            item[0] : {
                "userId" : item[1],
                "title" : item[2],
                "body" : item[3],
            }
        }

        parent.update(child_dict)

    return parent

@app.route('/posts', methods=['POST'])
def posts_with_args():
    args = request.args.to_dict()

    return posts_by_id_user_id(args['post_id'], args['user_id'])

@app.route('/posts/<int:post_id>',methods=['POST'])
def posts_by_id(post_id):
    stmt = select(posts).where(posts.id_posts == post_id)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:

        child_dict = {
            item[0] : {
                "userId" : item[1],
                "title" : item[2],
                "body" : item[3],
            }
        }

        parent.update(child_dict)

    return parent


def posts_by_id_user_id(post_id, user_id):
    stmt = select(posts).where(posts.id_posts == post_id, posts.users_id == user_id)
    result = conn.execute(stmt)
    result_list = result.fetchall()

    parent = {}

    for item in result_list:

        child_dict = {
            item[0] : {
                "userId" : item[1],
                "title" : item[2],
                "body" : item[3],
            }
        }

        parent.update(child_dict)

    return parent
@app.route('/')
def Welcome():
    return 'Welcome'
    


if __name__ == '__main__':
    app.run(debug=True)
