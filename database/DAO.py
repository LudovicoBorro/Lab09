from database.DB_connect import DBConnect
from model.airport import Airport

class DAO:

    def __init__(self):
        raise RuntimeError("Non creare un'istanza di questa classe, usa i metodi per eseguire le query!")

    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []

        query = """
                select LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as a1, GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as a2, AVG(f.DISTANCE) as distanza_media
                from flights f
                group by a1, a2
        """

        cursor.execute(query)

        for row in cursor:
            res.append((row["a1"], row["a2"], row["distanza_media"]))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []

        query = """
                select *
                from airports a 
        """

        cursor.execute(query)

        for row in cursor:
            res.append(Airport(**row))

        cursor.close()
        conn.close()
        return res