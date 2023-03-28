import os
import unittest
from flask import current_app
from flask_testing import TestCase
from flasky import app
from app.main import create_app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
    
class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config['DEBUG'])