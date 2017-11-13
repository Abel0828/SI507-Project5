def create_request_identifier(url, params_diction):
    sorted_params = sorted(params_diction.items(),key=lambda x:x[0])
    params_str = "_".join([str(e) for l in sorted_params for e in l]) # Make the list of tuples into a flat list using a complex list comprehension
    total_ident = url + "?" + params_str
    return total_ident.upper() # Creating the identifier
tumblr_search_baseurl = "https://api.tumblr.com/v2/blog"
tumblr_search_params = {'q':"University of Michigan", "count":4}
print(create_request_identifier(tumblr_search_baseurl,tumblr_search_params))
