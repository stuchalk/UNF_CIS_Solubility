from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry, ContentType
import json


def index(request):
    """present an overview page about the substance in the sds"""
    usrs = (User.objects.all().filter(last_login__gt='2024-03-01').
            values('id', 'first_name', 'last_name').order_by('last_name'))
    return render(request, "../templates/users/index.html", {'usrs': usrs})


def view(request, usrid=0):
    """ show data about a specific substance"""
    usr = User.objects.get(id=usrid)
    ents = LogEntry.objects.filter(user=usr)
    acts = []
    for ent in ents:
        tmp = model_to_dict(ent)
        ctype = ContentType.objects.get(id=ent.content_type_id)
        tmp.update({'table': ctype.model})
        tmp2 = dict()
        jsn = json.dumps(ent.change_message.strip("[]"))
        tmp2['act'] = json.loads(jsn)
        keys = tmp2['act'].keys()
        tmp.update({'action': keys[0]})  # still a string!  Why?
        acts.append(tmp)
    return render(request, "../templates/users/view.html", {'usr': usr, 'acts': acts})
