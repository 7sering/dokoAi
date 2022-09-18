import os
import openai
from django.conf import settings

# Load your API key from an environment variable or secret management service
openai.api_key = settings.OPENAI_API_KEY

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







# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n1. The fastest way to lose weight \u2013 and keep it off\n2. The best exercises to help you lose weight quickly\n3. How to make sure you stick to your weight loss goals\n4. The best ways to cut calories and lose weight\n5. How to make weight loss a sustainable lifestyle change"
#     }
#   ],
#   "created": 1663470322,
#   "id": "cmpl-5reuQ56nddhfXQ115wVPzXnll17vE",
#   "model": "text-davinci-002",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 64,
#     "prompt_tokens": 41,
#     "total_tokens": 105
#   }
# }