from ustc_gym_appointment import USTCGymAppointment

bot = USTCGymAppointment()
# 登录
bot.login('PB19030889', 'zhouchao1023')
# 可通过简单交互程序进行预约
bot.interact()
# 也可通过bot.submit方法自行调用预约,需要自己构造params参数
bot.submit(params)
# 通过bot.cancel方法取消预约,参数reserve_id在预约成功后的返回结果中获取
bot.cancel(reserve_id)
# 使用bot.find_available方法获取四天内的可用场地
available = bot.find_available(gymnasium_id=1)
