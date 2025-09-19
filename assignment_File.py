# Example No 1

name = "ali Akbar"
admission_date = "2025-10-20"
blood_Pressure = 140
hr = 70

separate = admission_date.split(sep='-') 
print(separate)

update_admission_date = separate[2]+ "/" +separate[1]+ "/"+separate[0]
print(update_admission_date)



print(f""
      "Patient Report --> {0}\nupdate_Admission_Date:{1}\nVitals:\n --Blood Pressure:{2}mmHg\n --HR:{3}bpm\n\nDisclaimer: This is confidential Under HIPPA """.format(name.upper(),update_admission_date,blood_Pressure,hr))


# example no 2


raw_url = "https://example-shop.com/products/laptop?category=electronics&price=999.99&sort=price_low&quot"


print("URL is true or False , it's", raw_url.startswith("https://") and raw_url.endswith("price_low&quot"))



scheme, nn, rest = raw_url.partition("://")
print(scheme,nn,rest)
print("this is rest link ",rest)



domain, n, path = rest.partition("/")
print("this is domain",domain,"this is path ",path)


main_url = scheme + nn + domain
print("this is main url ", main_url)


endpoint, n, query = path.partition("?")
print("this is endpoint",endpoint)
print("this is query",query)



category = query.find("category=")  
print("it give us index",category) 

category = query[category+len("category="): query.find("&", category)]
print("this is final category",category)



price = query.find("price=")
print("this is price index",price)

print("this is query",query)

price = query[price+len("price="): query.find("&", price)]

print("Final Price", price)


# output
print(f"""
Main URl -> {main_url} \nEndpoint-> {endpoint}\nCategory-> {category}\nPrice-> {price} """)





# example mo 3
log1 = "ERROR: Database connection failed at 14:32:05"
log2 = "INFO: User login successful"
log3 = "WARNING: High CPU at 14:33:05 - 85%"

all_logs = "\n".join([log1, log2, log3])

print("this is all_logs",all_logs)
log_with_error = (("ERROR" in log1) and log1) or \
                 (("ERROR" in log2) and log2) or \
                 (("ERROR" in log3) and log3)

print("this is All log error ", log_with_error)

message = log_with_error.split(" at ")[0].replace("ERROR: ", "")
print("this is message", message)

timestamp = log_with_error.split(" at ")[1]
print("this is time",timestamp)

final_message = "\n".join(["Message: ".join(["", message]),"Time: ".join(["", timestamp])])

print(final_message)

