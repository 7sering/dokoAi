import os
import openai
from django.conf import settings


openai.api_key = settings.OPENAI_API_KEY


# blog_topics = []

def generateBlogTopicIdea(topic, keywords):
    blog_topics = []

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate Blog Topic Ideas : {}\nKeywords: {}\n".format(topic, keywords),
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            return []
    else:
        return []

    a_list = res.split('*')
    if len(a_list) > 0:
        for blog in a_list:
            blog_topics.append(blog)
    else:
        return []
    return blog_topics


def generateBlogSectionHeadings(topic, keywords):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Generate Blog Section headings  and title.\ntopic: {}\nKeywords: {}\n*".format(topic,keywords),
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            res = None
    else:
        res = None
    return res



