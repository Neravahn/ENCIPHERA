import random

def generate_key():


    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+`~'
    key = ''

    seed = id(object()) ^ int(str(id(object()))[::-1])
    t = 0
    for i in range(16):
        t = ((t + seed) * (i + 1) * 9301 + 49297) % 233280
        index = (t ^ seed ^ (id(object()) % 1000)) % len(chars)
        key += chars[index]
        seed = seed ^ (t << (i % 4))

        
    return key

