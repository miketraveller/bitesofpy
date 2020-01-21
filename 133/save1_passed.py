def generate_affiliation_link(url):
    pos = url.find("/dp")
    num = url[pos+4:pos+14]
    return f"http://www.amazon.com/dp/{num}/?tag=pyb0f-20"