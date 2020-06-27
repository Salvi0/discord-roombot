import dataset
import os
from dotenv import load_dotenv
load_dotenv()

db = dataset.connect(os.getenv('DATABASE_URL'))
rooms_db = db.get_table('rooms', primary_id='role_id', primary_type=db.types.bigint)
settings_db = db.get_table('settings', primary_id='guild_id', primary_type=db.types.bigint)
invites_db = db.get_table('invites')