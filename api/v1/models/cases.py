from api.db import db
from typing import List
from sqlalchemy import func


class CaseModel(db.Model):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    continent = db.Column(db.String(80), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)
    confirmed = db.Column(db.Integer, nullable=False)
    life_expectancy = db.Column(db.Float(precision=2), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, country, city, continent, population, deaths, confirmed, life_expectancy):
        self.country = country
        self.city = city
        self.continent = continent
        self.population = population
        self.deaths = deaths
        self.confirmed = confirmed
        self.life_expectancy = life_expectancy

    def __repr__(self):
        return 'CaseModel(country=%s, city=%s, continent=%s, population=%s, deaths=%s, confirmed=%s, life_expectancy=%s )'\
             % (self.country, self.city, self.continent, self.population, self.deaths, self.confirmed, self.life_expectancy)

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
    def summary(cls) -> dict:
        return cls.query(
            CaseModel.continent, 
            func.sum(CaseModel.deaths).label('deaths'),
            func.sum(CaseModel.confirmed).label('confirmed')).group_by(CaseModel.continent).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()