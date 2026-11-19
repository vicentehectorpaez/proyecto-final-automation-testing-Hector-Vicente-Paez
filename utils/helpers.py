import logging
import pathlib

#1)carpeta donde se almacenaran los logs
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

#2)Configuracion global 
logging.basicConfig(
    filename=str(audit_dir / 'suite.log'), #ruta del archivo del log
    level=logging.INFO, #INFO Y SUPERIORES 
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%H:%M:%S',
    force=True
)

#3) Logger especificos que usaran los test 
logger = logging.getLogger('talentolab')

