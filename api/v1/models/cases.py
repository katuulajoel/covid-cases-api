from api.db import db
from typing import List
from sqlalchemy import BIGINT, INTEGER, func


class CaseModel(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    continent = db.Column(db.String(80), nullable=True)
    population = db.Column(db.BigInteger, nullable=True)
    deaths = db.Column(db.BigInteger, nullable=True)
    confirmed = db.Column(db.BigInteger, nullable=True)
    life_expectancy = db.Column(db.Float(precision=2), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, country, city, continent, population, deaths, confirmed, life_expectancy, updated_at):
        self.country = country
        self.city = city
        self.continent = continent
        self.population = population
        self.deaths = deaths
        self.confirmed = confirmed
        self.life_expectancy = life_expectancy
        self.updated_at = updated_at

    def __repr__(self):
        return 'CaseModel(country=%s, city=%s, continent=%s, population=%s, deaths=%s, confirmed=%s, life_expectancy=%s, updated_at=%s )'\
             % (self.country, self.city, self.continent, self.population, self.deaths, self.confirmed, self.life_expectancy, self.updated_at)

    def json(self):
        return {'country': self.country, 'city': self.city, 'continent': self.continent, 'population': self.population,}

    @classmethod
    def find_by_country(cls, country) -> "CaseModel":
        return cls.query.filter_by(country=country).first()

    @classmethod
    def find_by_id(cls, id) -> "CaseModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_continent(cls, continent) -> List["CaseModel"]:
        return cls.query.filter_by(continent=continent)

    @classmethod
    def find_all(cls) -> List["CaseModel"]:
        return cls.query.all()

    @classmethod
    def summary(cls):
        return db.session.query(
            CaseModel.continent, 
            db.func.sum(CaseModel.deaths).label('deaths'),
            db.func.sum(CaseModel.confirmed).label('confirmed')).group_by(CaseModel.continent).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()