# Server Specific Configurations
from lidongliang import model
from pecan.hooks import TransactionHook

server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'lidongliang.controllers.user.UserController',
    'modules': ['lidongliang'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/lidongliang/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    },
    'hooks': [
        TransactionHook(
            model.start,
            model.start_read_only,
            model.commit,
            model.rollback,
            model.clear
        )
    ]
}

logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'lidongliang': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'pecan': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
        '__force_dict__': True
        }
    }
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
sqlalchemy_w = {
    'url'           : 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8&use_unicode=0',
    'echo'          : False,
    'echo_pool'     : False,
    'pool_recycle'  : 3600,
    'encoding'      : 'utf-8'
}

sqlalchemy_ro = {
    'url'           : 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8&use_unicode=0',
    'echo'          : False,
    'echo_pool'     : False,
    'pool_recycle'  : 3600,
    'encoding'      : 'utf-8'
}