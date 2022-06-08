import json, requests

from main import Address, Comments, Company, db, Users, posts


def fetch_posts_data():
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url=url)
    
    return_value = json.loads(response.text)

    for i in return_value:
        id = i.get('id')
        users_id = i.get('userId')
        title = i.get('title')
        body = i.get('body')

        post_model = posts(id, users_id, title, body)

        db.session.add(post_model)
        db.session.commit()


def fetch_comments_data():
    url = 'https://jsonplaceholder.typicode.com/comments'

    response = requests.get(url=url)
    
    return_value = json.loads(response.text)

    for i in return_value:
        id = i.get('id')
        post_id = i.get('postId')
        name = i.get('name')
        email = i.get('email')
        body = i.get('body')

        comment_model = Comments(id, post_id, name, email, body)

        db.session.add(comment_model)
        db.session.commit()






def fetch_users_data():
    url = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(url=url)
    
    return_value = json.loads(response.text)

    for i in return_value:
        
        id = i.get('id')
        name = i.get("name")
        username = i.get('username')
        email_address = i.get('email')
        website = i.get('website')
        phone = i.get('phone')

        address = i.get('address')
        street = address['street']
        suite = address['suite']
        zipcode = address['zipcode']
        lat = address['geo']['lat']
        lng = address['geo']['lng']



        company = i.get('company')
        company_name = company['name']
        catch_phrase = company['catchPhrase']
        bs = company['bs']
        
        users = Users(id, name, username, email_address, phone=phone, website=website)
       
        user_address = Address(id, id, street, suite, zipcode, lat, lng)

        user_company = Company(id, id, company_name, catch_phrase, bs)


        db.session.add(user_company)
        db.session.add(users)
        db.session.add(user_address)

        db.session.commit()

        print(company_name)

# fetch_users_data()
# fetch_posts_data()
# fetch_comments_data()