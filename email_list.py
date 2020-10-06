#!/usr/bin/python3.7
# written by: atholcomb
# email_list.py

def email_list(domains):
    emails = []
    for domains, users in domains.items():
        for user in users:
            emails.append(user+'@'+domains)
    return emails
    

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
