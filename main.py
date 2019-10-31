from springbot import create_app


app = create_app('production-springbot.cfg')

if __name__ == '__main__':
    app.run()
