#!/usr/bin/env python
# coding=utf-8

from crispy_forms.helper import FormHelper
from threadedcomments.forms import ThreadedCommentForm as base_class

class MyCommentForm(base_class):


    helper = FormHelper()
    helper.form_tag = False