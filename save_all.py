import os
import pandas
from connection import PortfolioSession

LOGIN = os.getenv('LOGIN_PORTFOLIO')
PASSWORD = os.getenv('PASSWORD_PORTFOLIO')


def create_dataframe():
    df = pandas.DataFrame(columns=['ФИО', 'Группа', 'Ссылка'])
    return df


def get_all_tables(session: PortfolioSession, length: int, start: int):
    while True:
        data = session.get_table(length, start)
        length_data = len(data)

        yield data
        if length_data < length:
            break
        start += length


def get_portfolios(session: PortfolioSession):
    link = 'https://portfolio.bmstu.ru/portfolio/single/{}'
    generator = get_all_tables(session, 100, 0)
    i = 0
    df = create_dataframe()
    for data in generator:
        for student in data:
            df.loc[i] = {'ФИО': student['fio'],
                         'Группа': student['group'],
                         'Ссылка': link.format(student['student_uuid'])}
            i += 1
    return df


def save_df(df: pandas.DataFrame):
    df.to_excel('base.xlsx', sheet_name='Sheet1')


def main():
    session = PortfolioSession(login=LOGIN, password=PASSWORD)
    session.create_session()
    df = get_portfolios(session)
    save_df(df)


if __name__ == '__main__':
    main()
