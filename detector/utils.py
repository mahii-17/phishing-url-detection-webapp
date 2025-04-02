# detector/utils.py

def extract_features(url):
    return [[
        len(url),                      # URL Length
        1 if '@' in url else 0,        # Has @ symbol
        url.count('.'),                # Number of dots
        1 if url.startswith("https") else 0  # Uses HTTPS
    ]]
