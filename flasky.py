import os 
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    cov = coverage.coverage(branch=True, include='app/*')
    cov.start()
from app.main import create_app
from app import blueprint
import sys
import click

app = create_app(os.getenv('APP_CONFIG') or 'dev')

app.register_blueprint(blueprint)
app.app_context().push()

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, help='Run tests under code coverage.')
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    tests = unittest.TestLoader().discover('app/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
    if coverage:
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        cov.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        cov.erase()

