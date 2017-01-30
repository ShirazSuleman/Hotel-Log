import sys, os
sys.path.append(os.path.join(os.getcwd(), "site-packages"))

import price_checker

items = [ {'spreadsheet_id': '[some spreadsheet id]', 'url': '[some booking.com url]'}]

price_checker.execute(items)
