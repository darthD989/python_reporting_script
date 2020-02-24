from jira_lib import Jira
import re
import os

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    key_cert_data = 'key_cert_data'
    projects = 'ntqa_projects'
    issueTypes = 'ntqa_issue_types'
    
    with open(key_cert_data, 'r') as key_cert_file:
        rsa_private_key = key_cert_file.read()

    with open(projects, 'r') as projects_file:
        projects = eval(projects_file.read())

    with open(issueTypes, 'r') as issue_type_file:
        issueTypes = eval(issue_type_file.read())

    options = {
            'server': os.environ['environment_url'],
        }

    oauth_dict = {
        'access_token': os.environ['access_token'],
        'access_token_secret': os.environ['access_token_secret'],
        'consumer_key': os.environ['consumer_key'],
        'key_cert': rsa_private_key
        }
    jira = Jira(options,oauth_dict)

    for project in projects:
        try:
            jqlQry = f"project in ({project[0]}) ORDER BY updated DESC"
            issueCount = len(jira.runJql(jqlQry))
            comment = [f"Project = {project[0]}\nTotal Number of Issues = {issueCount}\n"]
            for issueType in issueTypes:
                try:
                  jqlQry = f"project in ({project[0]}) AND issuetype in (\"{issueType}\") ORDER BY updated DESC"
                  storyCount = len(jira.runJql(jqlQry))
                  comment.append(f"Total Number of \"{issueType}\" = {storyCount}\n")
                except:
                  comment.append(f"{issueType} does not exist in {project[0]}!\n")
        except:
                  comment.append(f"{project[0]} does not exist!\n")

        jira.addComment(os.environ['issue'],''.join(comment))    
