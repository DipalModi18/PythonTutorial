import requests
import json
import datetime

str2 = "aaa"
print(str2.split("::")[0])

session = requests.session()

response = session.post(
			"https://so-lab-ent1-sevone-metered-trial.silverpeak.cloud/gms/rest/authentication/login",
			data=json.dumps({"user": "dmohan@sevone.com", "password": "Silverpeak123!@#"}),
			headers={'Content-type': 'application/json'}, timeout=10)

print(str(response.headers))


str1='dipalamodi123'
print(str1[:10])


from random import randint

def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("What number did we guess (0-100)?"))

        if user_guess == random_int:
            print("You found the number ({random_int}). Congrats!")
            break

        if user_guess < random_int:
            print("Your number is less than the number we guessed.")
            continue

        if user_guess > random_int:
            print("Your number is more than the number we guessed.")
            continue


def to_human_readable_time(date_str):
    """
    Converts timestamp(in milliseconds) into date time(DD-<Short-Name-of-the-Month>-YYYY hh:mm:ss) string
    :param timestamp: integer to be converted to date time (DD-<Short-Name-of-the-Month>-YYYY hh:mm:ss) format
    :return: string date time of above format
    """
    supported_formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y/%m/%d %H:%M:%S']
    date_time_obj = None
    for date_time_format in supported_formats:
        try:
            date_time_obj = datetime.datetime.strptime(date_str,
                                                       date_time_format)  # Exit the loop if got the date obj without exception
            break
        except ValueError as e:
            pass
        except Exception as e:
            print(
                "An exception occured while converting date {} to human readable time".format(date_str))
            print(e)

    if date_time_obj is not None:
        return date_time_obj.strftime('%d-%b-%Y %H:%M:%S')
    else:
        print(
            "Date {} is not in one of the supported formats. Cannot convert to human readable time".format(
                date_str))


if __name__ == '__main__':
    print(to_human_readable_time(date_str="2018/07/17 10:25:18"))
    play()

