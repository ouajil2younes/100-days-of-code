# travel_log={
#     "France":["Paris","lille","dijon"],
#     "Germany":["stuttgart","berlin"]
# }
# print(travel_log["France"][1])

# nested_list=['a','b',["c","d"]]
# print(nested_list[2][1])
travel_log={
    "France":{
        "city_visited":["Paris","lille","dijon"],
        "num_time_visit":8
            },
    "Germany":{
        "city_visited":["test","berlin","stuttgart"],
        "num_time_visit":5
            },
}

print(travel_log["Germany"]["city_visited"][2])
