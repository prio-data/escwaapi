# db_url should NEVER point to a real ViEWS database
# but rather to one created using escwatransfer!

db_url = 'postgresql+asyncpg://xiaolong@localhost:5432/views_api'
# db_url = 'postgresql://xiaolong@localhost:5432/views_api'

schema = 'pipeline'
allowed_loas = ('pgm','cm')
codebook_location = 'codebooks'