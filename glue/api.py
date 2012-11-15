import logging

from glue.misc import Epoxy

logger = logging.getLogger(__name__)

def index(request):
	# logger.info("Welcome to GLUEBOX api")
	return Epoxy( request ).json()