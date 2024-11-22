from . import db

# Category Table
class FoodCategory(db.Model):
    __tablename__ = 'food_category'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    foods = db.relationship('Food', back_populates='category')

# Food Table
class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    fdc_id = db.Column(db.Integer, unique=True, nullable=False)  # USDA unique ID
    description = db.Column(db.String, nullable=False)
    data_type = db.Column(db.String, nullable=False)  # Branded, SR Legacy, etc.
    publication_date = db.Column(db.DateTime, nullable=False)
    food_category_id = db.Column(db.Integer, db.ForeignKey('food_category.id'))

    category = db.relationship('FoodCategory', back_populates='foods')
    nutrients = db.relationship('FoodNutrient', back_populates='food')

# Nutrient Table
class Nutrient(db.Model):
    __tablename__ = 'nutrient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    unit_name = db.Column(db.String, nullable=False)  # e.g., "g", "mg", etc.
    nutrient_number = db.Column(db.String, nullable=True)  # e.g., "203" for Protein

    foods = db.relationship('FoodNutrient', back_populates='nutrient')

# FoodNutrient Table (Association Table)
class FoodNutrient(db.Model):
    __tablename__ = 'food_nutrient'
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    nutrient_id = db.Column(db.Integer, db.ForeignKey('nutrient.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    food = db.relationship('Food', back_populates='nutrients')
    nutrient = db.relationship('Nutrient', back_populates='foods')

# MeasureUnit Table
class MeasureUnit(db.Model):
    __tablename__ = 'measure_unit'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    abbreviation = db.Column(db.String, nullable=False)

# DataSource Table
class DataSource(db.Model):
    __tablename__ = 'data_source'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    foods = db.relationship('FoodDataSource', back_populates='data_source')

# Food Data Source Association
class FoodDataSource(db.Model):
    __tablename__ = 'food_data_source'
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    data_source_id = db.Column(db.Integer, db.ForeignKey('data_source.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint('food_id', 'data_source_id', name='_food_data_source_uc'),)
