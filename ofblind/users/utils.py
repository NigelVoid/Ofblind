# users/utils.py
import environ
import re
import github
from github import Github

env = environ.Env()


def parse_github_skills(username):
    if not username:
        return "Отсутствуют"
    
    g = Github(env('GITHUB_TOKEN'))

    user = g.get_user(username)
    lang_list = set()
    libraries = set()

    for repo in user.get_repos(type="public"):
        languages = repo.get_languages()
        
        if languages:
            for lang in languages.keys():
                lang_list.add(lang)

        try:
            file_content = repo.get_contents("requirements.txt")
            raw_text = file_content.decoded_content.decode("utf-8")

            found_libraries = []
            for line in raw_text.splitlines():
                line = line.strip()
                
                if not line or line.startswith("#") or line.startswith("-r") or line.startswith("git+"):
                    continue
                    
                clean_lib = re.split(r"==|>=|<=|~=|!=|<|>|@", line)[0].strip()
                
                if clean_lib:
                    found_libraries.append(clean_lib)
            
            if found_libraries:
                for lib in found_libraries:
                    libraries.add(lib)
                
        except github.UnknownObjectException:
            pass
        except Exception as e:
            print(f"Ошибка при чтении библиотек: {e}")
        
    return ', '.join(lang_list) + ', ' + ', '.join(libraries) if lang_list or libraries else "Отсутствуют"

            
        
