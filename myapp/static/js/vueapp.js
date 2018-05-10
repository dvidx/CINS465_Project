var events = new Vue({
  el: '#load-events',
  data: {
    events: [],
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchEventList();
        this.timer = setInterval(this.fetchEventList, 3000);
  },
  methods: {
    fetchEventList: function() {
        $.get('/events/', function(event_list) {
            this.events = event_list.events;
            console.log(event_list);
        }.bind(this));
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
})


var chats = new Vue({
  el: '#load-chat',
  data: {
    chats: [],
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchChatList();
        this.timer = setInterval(this.fetchChatList, 3000);
  },
  methods: {
    fetchChatList: function() {
        $.get('/chats/', function(chat_list) {
            this.chats = chat_list.chats;
            console.log(chat_list);
        }.bind(this));
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
})
