from sqlalchemy import create_engine
from database import Base

engine = create_engine("mssql+pyodbc://LectSIP:LectSIP@srv-bddomtech/IOT_Combustible?driver=ODBC+Driver+17+for+SQL+Server")
Base.metadata.create_all(bind=engine)


