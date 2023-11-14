# apis/auth.py
from flask_restx import Namespace, Resource
from flask import request

from db_config import db



auth_api = Namespace(
    name='login',
    description='Authentication API'
)


users = db.users


@auth_api.route('/register', methods=['POST'])
class Register(Resource):
    def post(self): 
        params = request.get_json()
        id_ = params['id']
        nickname = params['nickname']
        email = params['email']
        gender = params['gender']
        ageRange = params['ageRange']
        print(id_)
        print(nickname)
        print(email)
        print(gender)
        print(ageRange)
        try: 
            user = users.find_one({'id': id_})

            if user is None: 
                try: 
                    users.insert_one({'id': id_, 'nickname': nickname, 'email': email, 'gender': gender, 'ageRange': ageRange})

                    return "success"
                
                except Exception as e:
                    print(e)

                    return "오류"
            else: 

                return "success"
        except Exception as e:

            return "오류"


@auth_api.route('/pincheck', methods=['POST'])
class Register(Resource):
    def post(self): 
        params = request.get_json()
        id_ = params['id']
        if id_ == '123456789':
            return "success"
        else: 
            return "PIN 틀림"
    
        # nickname = params['nickname']
        # email = params['email']
        # gender = params['gender']
        # ageRange = params['ageRange']
        # print(id_)
        # print(nickname)
        # print(email)
        # print(gender)
        # print(ageRange)
        # try: 
        #     user = users.find_one({'id': id_})

        #     if user is None: 
        #         try: 
        #             users.insert_one({'id': id_, 'nickname': nickname, 'email': email, 'gender': gender, 'ageRange': ageRange})

        #             return "success"
                
        #         except Exception as e:
        #             print(e)

        #             return "오류"
        #     else: 

        #         return "success"
        # except Exception as e:

        #     return "오류"