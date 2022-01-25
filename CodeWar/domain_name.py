'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    if 'www' in url:
      start_point=url.index('.')+1
      end_point=url[start_point:].index('.')+start_point
      return url[start_point:end_point]
    elif '//' in url:
      start_point=url.index('/')+2
      end_point=url.index('.')
      return url[start_point:end_point]
    else:
      end_point=url.index('.')
      return url[:end_point]
