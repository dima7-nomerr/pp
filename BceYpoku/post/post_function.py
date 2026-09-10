from post import Post


def input_post_date()->Post:
    posting_datetime = input("введите дату выхода поств в формате hh:mm:ss dd.MM.YYYY ")
    media_url = input("введите url или картинки вставленые в пост ")
    description = input("введитек текст к медиофайлу ")

    return Post(
        posting_datetime=posting_datetime,
        madia_url=media_furl,
        description=description
    )



def add_new_post_to_end_of_list(posts:list[Post],   new_post:Post):
    posts.append(new_post)
def print_post_header():
    print(f"{'ИД':<5}{'Дата публикации':<25}{'Медиа URL':<25}{'Описание':<25}")

def print_one_post(post: Post):
    print(
        f"{post.id:<5}{post.posting_datetime:<25}{post.media_url:<25}{post.description:<25}"
    )


def print_posts(posts:list[Post]):
    print_post_header()

    for post in posts:
        print_one_post(post)

