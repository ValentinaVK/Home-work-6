def File_parsing(file_1="./nginx_logs.txt"):

    if file_1:
        with open(file_1, "r", encoding="utf-8") as file:
            for strok in file:
                ip = strok.split(" - - ")[0]
                remote_addr = strok.split('"')[1]
                request_type = remote_addr.split()[0]
                requested_resource = remote_addr.split()[1]
                yield(ip, request_type, requested_resource)


parsed = File_parsing()

for _ in range(10):
    print(next(parsed))
