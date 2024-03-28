import os

def make_commit(days):
    if days < 1:
        # Push
        return os.system('git push')
    else:
        dates = '{} days ago'.format(days)

        with open('data.txt', 'a') as file:
            file.write('{}\n'.format(dates))

        # Staging
        os.system('git add data.txt')

        # Commit
        os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days * make_commit(days-1)

make_commit(30)