import argparse

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import redis

redis_pool, redis_conn = (None, None)


def main():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config-file', help='Config file path.')

    args = parser.parse_args()

    if not args.config_file:
        print('You should specify a config file using --config-file parameter.')
        exit(0)

    config = configparser.ConfigParser()
    config.read(args.config_file)

    redis_pool = redis.ConnectionPool(
        host=config['redis']['host'],
        port=config['redis']['port'],
        db=config['redis']['db']
    )

    redis_conn = redis.Redis(connection_pool=redis_pool)

    print("Executing the server...")

if __name__ == "__main__":
    main()
