import nox

@nox.session
def tests(session):
    session.install('py.test')
    session.run('py.test')

@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8')
