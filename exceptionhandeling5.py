try:
    try:
        raise ValueError
    except ValueError:
        print('Error')
except:
    print('outer block')
