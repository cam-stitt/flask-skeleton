from datetime import datetime, date

import arrow
from flask.json import JSONEncoder as FlaskJSONEncoder

from .models import Base


class JSONEncoder(FlaskJSONEncoder):
    """An extension of the Flask JSONEncoder to handle datetime."""

    def default(self, o):
        """Perform conversions from datetime/date to timestamp"""
        if isinstance(o, Base):
            return o.to_dict()
        if isinstance(o, datetime):
            return arrow.Arrow.fromdatetime(o).timestamp
        if isinstance(o, date):
            return arrow.Arrow.fromdate(o).timestamp
        if isinstance(o, arrow.Arrow):
            return o.timestamp
        return FlaskJSONEncoder.default(self, o)
