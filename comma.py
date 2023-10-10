def comma_code(item_list):
      if len(item_list) == 0:
         return ""
      elif len(item_list) == 1:
         return item_list[0]
      else:
         # Join all items except the last one with a comma and space
         joined_items = ', '.join(item_list[:-1])
         # Add "and" before the last item and combine them all
         result = f"{joined_items}, and {item_list[-1]}"
         return result

# Test cases
spam = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(spam)
print(result)  # Output: 'apples, bananas, tofu, and cats'

empty_list = []
result = comma_code(empty_list)
print(result)  # Output: ''
