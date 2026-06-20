def logic():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    dict_of_tuples = dict(list_of_tuples)
    dict_of_tuples = { k : int(v) for k, v in dict_of_tuples.items() }
    sorted_countries = dict(sorted(dict_of_tuples.items(), key=lambda item: (-item[1], item[0])))

    for country in sorted_countries:
        print(country)

if __name__ == "__main__":
    try:
        logic()
    except ValueError:
        print("int convert failure")
    except Exception as e:
        print(f"Something went wrong: {e}")