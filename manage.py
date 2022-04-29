from app import create_app
from flask__script import Manager,Server

#Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()   