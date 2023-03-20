from domain.fit.models.physical_data import PhysicalData

def create_physical_data(data, user_id):
    physical_data = PhysicalData(
        data['steps'], 
        data['calories'], 
        data['cardio_points'], 
        data['heart_rate'], 
        data['breathing_rate'],
        data['kilometers_traveled']
    )
    physical_data.user_id = user_id
    return physical_data


def get_physical_data_user(user_id):
    physical_data = PhysicalData.simple_filter(**{'user_id': user_id})
    return physical_data
