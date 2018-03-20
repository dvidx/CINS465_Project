var app = new Vue({
  el: '#load-survey',
  data: {
    surveys: [],
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchSurveyList();
        this.timer = setInterval(this.fetchSurveyList, 3000);
  },
  methods: {
    fetchSurveyList: function() {
        $.get('/surveys/', function(survey_list) {
            this.surveys = survey_list.surveys;
            console.log(survey_list);
        }.bind(this));
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
})

// var app2 = new Vue({
//   el: '#demo',
//   data: {
//     show: false
//   }
// })
