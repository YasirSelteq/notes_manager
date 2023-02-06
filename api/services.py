from task_manager import secrets
import json

def getNotes(userId,bookingId):
    print(userId,bookingId)
    # conn = mongo.get_collection(db=secrets.MONGO_DB_1, col=secrets.MONGO_COL_1)
    # conn2 = mongo.get_collection(db=secrets.MONGO_DB_1, col=secrets.MONGO_COL_2)
    # cursor = conn.find({"date":on_date}, {"_id":0})
    # cursor2 = conn2.find({"date":on_date}, {"_id":0})
    # events_data = loads(dumps(cursor))
    # breaks_data = loads(dumps(cursor2))
    # result = events_data+breaks_data
    return {
        # 'events_data': result,
    }
