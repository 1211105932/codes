def domain_name(url):
    return url.removeprefix("http://").removeprefix("https://").removeprefix("www.").split(".")[0]