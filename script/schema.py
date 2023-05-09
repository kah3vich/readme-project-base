def schema_readme(url, title, subtitle, description, links, stacks, developers):
    result = f'<div align="center"><img width="200" height="200" src="{url}"><br /><h1>{title}</h1><p>{subtitle}</p><br /></div><div align="center"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/tableOfContents.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div>'

    result += '\n\n### 1. <a href="#script">Script</a>'

    result += '\n\n### 2. <a href="#description">Description</a>'

    result += '\n\n### 3. <a href="#link">Link</a>'

    result += '\n\n### 4. <a href="#stack">Stack</a>'

    result += '\n\n### 5. <a href="#team">Team</a>'

    result += '\n\n### 6. <a href="#license">License</a>'

    result += '\n\n<div align="center" id="script"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/script.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div>'

    result += '\n\n### Install dependencies: \n\n```bash\nyarn\n```\n\n### Start dev mode:\n\n```bash\nyarn start\n```\n\n'

    result += f'<br /><a href="https://github.com/kah3vich/Gulp-RS/blob/set/readme.md#script" target="_blank"><b>More scripts.</b></a><br /><div align="center" id="description"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/description.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div><div align="center"><p>{description}</p></div><div align="center" id="link"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/link.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div>'

    for i in links:
        id = i['id']
        link = i['link']
        title = i['title']

        result += f'\n\n### {id}. <a href="{link}">{title}</a>'
    
    result += '\n\n<div align="center" id="stack"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/stack.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div><table align="center"><tr>'

    for i in stacks:
        url = i['url']
        title = i['title']

        result += f'<td align="center" width="96"><a href="#"><img src="{url}" width="48" height="48" alt="{title}" /></a><br /><p>{title}</p></td>\n'

    result += '</tr></table>\n\n<div align="center" id="team"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/team.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div><table align="center"><tr>'

    for i in developers:
        name = i['name']
        url = i['url']
        link = i['link']
        status = i['status']

        result += f'<td align="center" valign="top"><img width="96" height="96" src="{url}"><br /><a href="{link}">{name}</a><p>{status}</p></td>\n'

    result += '</tr></table><div align="center" id="license"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/license.svg" alt="" width="100%" height="29px"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/gif/line.gif" alt="" width="100%" height="20px"><br /></div><a href="https://github.com/kah3vich/readme-project-base/blob/main/LICENSE"><br /><img src="https://raw.githubusercontent.com/kah3vich/readme-project-base/main/assets/svg/licenseContent.svg" alt="" width="100%" height="29px"><br /></a>\n\n<!-- ! by kah3vich -->'

    return result 

def schema_command(reps): 
    result = 'cd ./cache/reps/; rm -rf ./* \n\n'

    title = reps['title']
    result += f'git clone git@github.com:kah3vich/{title}.git; '
    result += f'cd {title}; '
    result += f'mv ../../readme/{title}.md .; '
    result += f'mv {title}.md readme.md; '
    result += 'git add .; git commit -m "feat: readme update"; git push; '
    result += 'cd ../; \n\n'

    result += 'cd ../..;'

    return result 
