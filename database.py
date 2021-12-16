class Database:
    id_to_user_map = {}
    user_to_id_map = {}
    user_favorites = {
        "9999": {}
    }

    def get_num_users():
        # print(f"num of users: {len(Database.id_to_user_map.keys())}")
        return len(Database.id_to_user_map.keys())

    def get_user_to_id_map():
        return Database.user_to_id_map

    def get_id_to_user_map():
        return Database.id_to_user_map