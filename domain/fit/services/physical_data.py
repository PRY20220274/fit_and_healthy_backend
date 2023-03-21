from domain.fit.models.physical_data import PhysicalData

def create_physical_data(data, user_id):
    physical_data = PhysicalData(
        data['steps'], 
        data['calories'], 
        data['cardioPoints'], 
        data['heartRate'], 
        data['breathingRate'],
        data['kilometersTraveled'],
        data['width'],
        data['height']
    )
    physical_data.user_id = user_id
    return physical_data

def get_physical_data_user(user_id):
    physical_data = PhysicalData.query.filter_by(user_id=user_id).order_by(PhysicalData.created_at.desc()).first()
    return physical_data
