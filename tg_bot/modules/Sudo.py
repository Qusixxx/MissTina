import html

from typing idxal siyahısı

from telegram idxal Update, Bot
from telegram.ext idxal CommandHandler, Filters
from telegram.ext.dispetçer idxal run_async

from tg_bot import dispetçer, SUDO_USERS, OWNER_USERNAME, OWNER_ID
from tg_bot.modullar.helper_funcs.extrac idxal extract_user
from tg_bot.modules.helper_funcs.chat_status bot_admin idxal edin


@bot_admin
@run_async
def addsudo(bot: Bot, yeniləmə: Yeniləmə, args: Siyahı [str]):
    message = update.effective_message
    banner = update.effective_user
    user_id = çıxarış_ istifadəçisi (mesaj, arq)
    
    if not user_id:
        message.reply_text("Əvvəlcə bir istifadəçiyə müraciət edin....")
      qayıt""
        
    if int(user_id) == OWNER_ID:
        message.reply_text("Göstərilən istifadəçi mənim sahibimdir!Onu SUDO_USERS siyahısına əlavə etməyə ehtiyac yoxdur")
        qayıt "
        
    if int(user_id) in SUDO_USERS:
        message.reply_text("Dostum bu istifadəçi artıq sudo istifadəçisidir.")
        qayıt ""
    
    with open(" sudo_users.txt","a") fayl kimi:
        file.write(str(İstifadəçi_adı) + "\n")
   
    SUDO_USERS.əlavə edin(İstifadəçi_adı)
    message.reply_text("Uğurla SUDO siyahısına əlavə edildi!")
        
    qayıt ""

@bot_admin
@run_async
def rsudo(bot: Bot, yeniləmə: Yeniləmə, args: Siyahı [str]):
    message = update.effective_message
    user_id = çıxarış_ istifadəçisi (mesaj, arq)
    
    if not user_id:
        message.reply_text("Əvvəlcə istifadəçiyə müraciət edin....")

    if int(user_id) == OWNER_ID:
        message.reply_text("Göstərilən istifadəçi mənim sahibimdir!Onu SUDO_USERS siyahısından çıxarmayacağam!")
        qayıt ""
    
    if user_id not in SUDO_USERS:
        message.reply_text("{}sudo istifadəçisi deyil".format(user_id))
        qayıt ""

    users = [line.rstrip('\n')açıq xətt üçün("sudo_users.txt")]

    with open("sudo_users.txt","w")fayl kimi:
     istifadəçilərdəki istifadəçi üçün:
           if not int(istifadəçi) ==istifadəçi_adı:
                file.write(str(istifadəçi) + "\n")

    SUDO_USERS.remove(istifadəçi_adı)
    message.reply_text("Yep Uğurla SUDO Siyahısından çıxarıldı!")
    
    qayıt ""


__help__ = """
*Bot owner only:*
 - /addsudo: istifadəçini SUDO USER səviyyəsinə yüksəldir
 - /rsudo: istifadəçini SUDO USER-dən aşağı salır
"""

__mod_name__ = "Sudo"

addsudo_HANDLER = CommandHandler("addsudo", addsudo, pass_args=Doğru, filtrlər=Filters.user(OWNER_ID))
rsudo_HANDLER = CommandHandler("rsudo", rsudo, pass_args=Doğru, filtrlər=Filters.user(OWNER_ID))

dispatcher.add_handler(addsudo_HANDLER)
dispatcher.add_handler(rsudo_HANDLER)
