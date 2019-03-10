import sqlite3 as lite


class CoinsData:
    """Класс, работающий с БД монет"""

    con = lite.connect('test.db')

    # def __init__(self):
    #     with self.con:
    #         cur = self.con.cursor()
    #         cur.execute("DROP TABLE IF EXISTS coins")
    #         cur.execute("CREATE TABLE coins("   # Таблица для работы с монетами
    #                     "id INT, "              # id монеты - отсчет с 0
    #                     "nominal INT, "         # номинал монеты
    #                     "currency TEXT, "       # Валюта (Р, $, и тд)
    #                     "year INT, "            # Год выпуска
    #                     "country TEXT, "        # Страна выпуска
    #                     "seria TEXT, "          # Серия
    #                     "model TEXT, "          # Название в серии
    #                     "img_path TEXT)"        # Относительный путь до изображения монеты
    #                     )
    #
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (0, 10, 'Р', 2015, 'Россия', 'Города воинской славы', 'Елец', (?))""",
    #             [r'coins_interface\ten_rubles\elec.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (1, 10, 'Р', 2013, 'Россия', 'Города воинской славы', 'Курск', (?))""",
    #             [r'coins_interface\ten_rubles\kursk.png'])
    #         cur.execute(
    #             """INSERT INTO coins VALUES (2, 10, 'Р', 2018, 'Россия', 'Города воинской славы', 'Ржев', (?))""",
    #             [r'coins_interface\ten_rubles\rjev.png'])

    def get_coins_info(self):
        """Метод берет информацию о всех монетах в БД"""

        cur = self.con.cursor()
        cur.execute("SELECT * FROM coins")
        request = cur.fetchall()
        coins_info = []

        for coin in request:
            coins_info.append({'id': coin[0], 'nominal': coin[1], 'currency': coin[2],
                               'year': coin[3], 'country': coin[4],
                               'seria': coin[5], 'model': coin[6],
                               'img_path': coin[7]})

        return coins_info

