import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
import django

django.setup()
from MainApp.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()
# entries = topics.entry_set.all()

t = Topic.objects.get(id=1)
print(t)
entry = t.entry_set.all()
print(entry)

for t in topics:
    print(f"Topid ID: {t.id} and Topic Name: {t}")
    # id will return whatever is in the string method
    print(f"Date added: {t.date_added}")

for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
