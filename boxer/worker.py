import celery, os

app = celery.Celery('example')
app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

@app.task
def add(x, y):
    return x + y

# import datetime
# import sys
# import hashlib

# def process_ended_auctions():
    # current_time = datetime.datetime.now()
    # ended_auctions = AuctionEvent.objects.filter(end_time__lt=current_time, item__status=AUCTION_ITEM_STATUS_RUNNING)
    # for auction_event in ended_auctions:
        # process_ended_auction(auction_event)

# if __name__ == "__main__":
    # process_ended_auctions()
