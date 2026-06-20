import sys

def to_callcentr(clients : list, recipients : list) -> list:
    return list(set(clients) - set(recipients))

def potential_clients(clients : list, participants: list) -> list:
    return list(set(participants) - set(clients))

def loyalty_program(clients: list, participants: list) -> list:
    return list(set(clients) - set(participants))

def logic():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case "call_center":
                print(to_callcentr(clients, recipients))
            case "potential_clients":
                print(potential_clients(clients=clients, participants=participants))
            case "loyalty_program":
                print(loyalty_program(clients=clients, participants=participants))
            case _:
                raise Exception("unknown command")

if __name__ == "__main__":
    logic()