from springbot import create_app


app = create_app('production-springbot.cfg')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
