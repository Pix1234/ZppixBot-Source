""" Some commands for just goofing around and having fun """

from sopel import module


@module.example('.coffee MirahezeBot')
@module.commands('coffee')
def coffee(bot, trigger):
    """
    Makes me give the specified nick a coffee.
    """
    if trigger.group(2) == '':
        bot.reply("To whom should I give this cup of coffee?")
    bot.action("gives %s a nice warm cup of coffee" % (trigger.group(2)), trigger.sender)


@module.example('.hug MirahezeBot')
@module.commands('hug')
def hug(bot, trigger):
    """
    Makes me give the specified nick a hug.
    """
    if trigger.group(2) == '':
        bot.reply("To whom should I give this hug?")
    bot.action("gives %s a great big bear hug" % (trigger.group(2)), trigger.sender)


@module.example('.burger MirahezeBot')
@module.commands('burger')
def burger(bot, trigger):
    """
    Makes me give the specified nick a burger.
    """
    if trigger.group(2) == '':
        bot.reply("To whom should I give this cheeseburger?")
    bot.action("gives %s a freshly cooked cheeseburger" % (trigger.group(2)), trigger.sender)


@module.example('.present MirahezeBot')
@module.commands('present')
def present(bot, trigger):
    """
    Makes me give the specified nick a present.
    """
    if trigger.group(2) == '':
        bot.reply("To whom should I give this present?")
    bot.action("gives %s a present" % (trigger.group(2)), trigger.sender)
