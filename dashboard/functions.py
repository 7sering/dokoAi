import os
import openai
from django.conf import settings


openai.api_key = settings.OPENAI_API_KEY


# blog_topics = []

def generateBlogTopicIdea(topic, keywords):
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
            res = None
    else:
        res = None
    return res


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








# topic = 'How to create blog with ai tools'
# keywords = 'Create Blog with AI tools, AI tools for blogs, best AI tools'

# res = generateBlogTopicIdea(topic, keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#     blog_topics.append(blog)
#     print('\n')
#     print(blog)