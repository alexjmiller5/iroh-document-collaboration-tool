import requests
import json
import sys

def get_credentials():
    with open('credentials.txt', 'r') as file:
        api_key = file.readline().strip()
        username = file.readline().strip()
        password = file.readline().strip()
    return api_key, username, password

def get_access_token(api_key, username, password):
    url = "https://api.iroh.network/token"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    print(username, password)
    data = {
        "name_or_email": username,
        "password": password,  # Be cautious with sensitive information
    }
    response = requests.post(url, headers=headers, json=data)  # Using json=data for simplicity
    if response.status_code == 200:
        print("Successfully obtained access token.")
        return response.json()['token']
    else:
        print(f"Error obtaining token: {response.status_code} - {response.text}")
        return None

def get_current_user_details(access_token):
    url = "https://api.iroh.network/user/me"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Successfully retrieved current user details.")
        return response.json()
    else:
        print(f"Failed to get user details: {response.text}")
        return None

def list_projects(access_token):
    url = "https://api.iroh.network/user/me/projects"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Successfully listed projects available to the current user.")
        return response.json()
    else:
        print(f"Failed to list projects: {response.text}")
        return None

def create_document(token, project):
    url = f"https://api.iroh.network/docs/{project}/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "name": "New Collaborative Document"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        doc_id = response.json()['doc_id']
        print(f"Document created with ID: {doc_id}")
        return doc_id
    else:
        print(f"Failed to create document: {response.status_code} - {response.text}")
        return None

def share_document(token, project, doc_id, mode='write'):
    url = f"https://api.iroh.network/docs/{project}/{doc_id}/share"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "mode": mode
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        ticket = response.json()['ticket']
        print(f"Share this ticket to collaborate: {ticket}")
        return ticket
    else:
        print(f"Failed to share document: {response.text}")
        return None

def join_document(token, project, ticket):
    url = f"https://api.iroh.network/docs/{project}/join"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "ticket": ticket
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        doc_id = response.json()['doc_id']
        print(f"Joined document: {doc_id}")
        return doc_id
    else:
        print(f"Failed to join document: {response.text}")
        return None

def edit_document(token, project, doc_id, key, content):
    url = f"https://api.iroh.network/docs/{project}/{doc_id}/set"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "key": key,
        "value": content
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Content saved.")
    else:
        print(f"Failed to save content: {response.text}")

def main():
    api_key, username, password = get_credentials()
    token = get_access_token(api_key, username, password)
    if token:
        projects = list_projects(token)
        if projects:
            for i, project in enumerate(projects, start=1):
                print(f"{i}. {project['name']} (ID: {project['id']})")
            project_choice = int(input("Choose a project number to work with: ")) - 1
            project_id = projects[project_choice]['id']
            
            if len(sys.argv) == 1:
                doc_id = create_document(token, project_id)
                if doc_id:
                    ticket = share_document(token, project_id, doc_id)
                    print(f"Document ticket for sharing: {ticket}")
            elif len(sys.argv) == 2:
                ticket = sys.argv[1]
                doc_id = join_document(token, project_id, ticket)
                if doc_id:
                    while True:
                        command = input("Enter command (edit, view, exit): ")
                        if command == "edit":
                            key = input("Enter the key: ")
                            content = input("Enter the content: ")
                            edit_document(token, project_id, doc_id, key, content)
                        elif command == "view":
                            pass # view_document(token, project_id, doc_id)
                        elif command == "exit":
                            break
                        else:
                            print("Unknown command.")
        else:
            print("No projects available or unable to retrieve projects.")


if __name__ == "__main__":
    main()