def find_spamer (prased_log):
    if not parsed_log:
        return None
    db = {}
    for log in prased_log:
        if not db.get(log[0]):
            db[log[0]] = {"count":1, "files":set([log[2]])}
        else:
            db[log[0]]["count"] += 1
            db[log[0]]["files"].add(log[2])
    return max(db.items(), key=lambda x: x[1]["count"])
if __name__ == "__main__":
    parsed_log = parse_log("./nginx_logs.txt")
    spamer = find_spamer(parsed_log)
