# from aiogram import types, Dispatcher
# from youtube_search import YoutubeSearch as YT
# import hashlib
#
#
# def finder(text):
#     return YT(text, max_results=10).to_dict()
#
#
# async def inline_wiki_handler(query: types.InlineQuery):
#     text = query.query or "echo"
#     link = f"https://ru.wikipedia.org/wiki/{text}"
#     articles = [types.InlineQueryResultArticle(
#         id=hashlib.md5(text.encode()).hexdigest(),
#         title="WIKI",
#         url=link,
#         input_message_content=types.InputMessageContent(
#             message_text=link
#         )
#     )]
#     await query.answer(articles, cache_time=60)
#
#
# def register_handlers_inline(dp: Dispatcher):
#     dp.register_inline_handler(inline_wiki_handler)