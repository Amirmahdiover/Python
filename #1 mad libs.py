def get_input(word_type) -> str:
    result = input(f'Enter a {word_type}: ')
    return str(result)


name1 = get_input('name')
name2 = get_input('name2')
name3 = get_input('name3')
verb = get_input('yes/no')

story = f'''
{name1}: do you wanna enroll to the tennis tournament {name2}?
{name2}: i don't think so i'm not ready for it
{name1}: i saw you were playing with {name3} yesterday morning and you were brilliant
{name2}: hmmmmm actually i'm a little nervous
{name1}: let me tell you something if you lose, you don't lose anything, 
you get the experience of participating in competitions.
so you are gonna enroll for it?
{name2}: {verb}
'''
print(story)
