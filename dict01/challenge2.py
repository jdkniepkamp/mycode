#!/usr/bin/env python3


char_name = input("Which character do you want to know about? (Flash, Batman, or Superman?): " )
char_stat = input("Which statistic do you want to know about? (Strength, Speed, or Intelligence?): " )
dictionary ={"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}

#print(f"{char_name}'s {char_stat} is:{dictionary[char_name.values][char_stat.values]} ")
print(f"{char_name}'s {char_stat} is:{dictionary[char_name][char_stat]} ")
# You need to populate those two square brackets to get what you need. Almost there!!
