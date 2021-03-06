import os
import pymongo

URL = os.environ.get("OPENSHIFT_MONGODB_DB_URL")
if URL:
    client = pymongo.MongoClient(URL)
else:
    client = pymongo.MongoClient("localhost", 27017)


def post_userinfo(userinfo):
    db = client.backend
    info = {}
    for k, v in userinfo.items():
        info[k] = v
    return db.userinfo.insert_one(info)


def get_userinfo(phonenumber):
    db = client.backend
    row = db.userinfo.find_one({"phonenumber": phonenumber})
    if not row:
        return {}
    info = {}
    for k, v in row.items():
        info[k] = v
    if '_id' in info:
        info.pop('_id', None)
    return info


def add_route(phonenumber, route):
    db = client.backend
    info = {}
    info[phonenumber] = route
    return db.routeinfo.insert_one(info)


def get_students_info(query):
    db = client.backend
    rows = db.userinfo.find(query)
    return rows


def update_student_info(updated_info):
    db = client.backend
    db.userinfo.update({'phonenumber': updated_info['phonenumber']},
                       {'$set': {'status': updated_info['status']}},
                       True)


def update_student_route(updated_info):
    db = client.backend
    db.userinfo.update({'phonenumber': updated_info['phonenumber']},
                       {'$set': {'route': updated_info['route']}},
                       True)


def get_unassigned_students():
    db = client.backend
    rows = db.userinfo.find({"route": {"$exists": False}})
    return rows

def get_assigned_students():
    db = client.backend
    rows = db.userinfo.find({"route": {"$exists": True}})
    return rows


def register_token(phonenumber, token):
    db = client.backend
    data = {'phonenumber': phonenumber,
            'token': token,
            }
    db.gcmtokens.update({'phonenumber': phonenumber},
                        data,
                        upsert=True)


def get_gcm_token(phonenumber):
    db = client.backend
    if phonenumber:
        return db.gcmtokens.find_one({'phonenumber': phonenumber})['token']
    else:
        return [i['token'] for i in db.gcmtokens.find()]


def update_user_location(phonenumber, location):
    db = client.backend
    db.userinfo.update({'phonenumber': phonenumber},
                       {'$set': {'location': location}},
                       True)
    return True


def add_guardian(guardinfo):
	db = client.backend
	info={}
	for k, v in guardinfo.items():
		info[k] = v
	return db.guardian.insert_one(info)
