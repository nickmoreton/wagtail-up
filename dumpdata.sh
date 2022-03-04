#¡/bin/bash

./manage.py dumpdata --natural-foreign --indent 2 \
-e contenttypes \
-e auth.permission \
-e wagtailcore.groupcollectionpermission \
-e wagtailcore.grouppagepermission \
-e wagtailimages.rendition \
-e sessions \
-e wagtailcore.pagelogentry \
-e wagtailcore.pagesubscription \
-e wagtailcore.groupapprovaltask \
-e wagtailsearch.indexentry \
-e wagtailcore.workflowpage \
-e wagtailcore.workflowtask \
-e wagtailcore.task \
-e wagtailcore.workflow \
-e auth > initial_data/data.json
