def uniqueemail(emails):

    unique_emails = set()

    for email in emails:
        local_name, domain_name = email.split('@')

        #Applying Rule #1 and #2 to
        local_rule = local_name.split('+')[0].replace('.','')
        unique_emails.add(local_rule+'@'+domain_name)

    return len(unique_emails)

emails = ['sree.kanth@gmail.com','sreekanthM+ok@gmail.com','mutthoju.sree+kanth@gmail.com']
count = uniqueemail(emails)
print("The count of unique emails is :",count)




