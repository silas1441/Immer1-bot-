const mineflayer = require('mineflayer')


const bot = mineflayer.createBot({
    host: 'lostify.net', //localhost für interne server
    port: '25565',
    username: 'Immer1',
    version: false //mit false auch Versionsübergreifend mit 'Version' spezifieren
});

bot.on('chat', (username, message) => {
    if (username === bot.username)
    return;
    bot.chat(message);
      
    
})
