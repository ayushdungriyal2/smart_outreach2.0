def check_for_disposable(email):

    url = f"https://disposable.debounce.io/?email={email}"

    response = requests.request("GET", url)

    print(response.text)

    if response.disposable == True:
        return True
    else:
        return False


check_for_disposable('ayush@smartoutreach.net')