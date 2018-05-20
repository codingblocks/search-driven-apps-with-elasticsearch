(function () {

  var initializeCheckboxes = function() {
    var filterCheckboxes = $('#frm_filter').find('input:checkbox');
    // Inefficient!!
    var url = new URL(location.href);
    for(var param of url.searchParams.entries()) {
      filterCheckboxes.each(function(i) {
        var cb = filterCheckboxes[i];
        if(cb.name === param[0] && cb.value === param[1]) {
          cb.checked = true;
        }
      });
    }
  }

  var showFilters = function() {
    $('#mdl_filter').modal('show');
  }

  var filter = function(event) {
    var checked = $('#frm_filter').find('input:checkbox:checked');
    var params = [];
    checked.each(function(i) {
      var cb = checked[i];
      if(cb.name && cb.value) {
        params.push({ name: cb.name, value: cb.value });
      }
    });

    var search = $('#search').val();
    if(search) {
      params.push({ name: 'search', value: search });
    }

    event.preventDefault();
    if(params.length) {
      location.href = '/?' + $.param(params);
    }
  }

  var clearFilters = function() {
    if(confirm('Clear filters?')) {
      location.href='/' ;
    }
  }

  $(document).ready(function() {
    initializeCheckboxes();
    $('.action_filter').on('click', filter);
    $('.action_clear').on('click', clearFilters);
    $('.action_showFilters').on('click', showFilters);
  });
})();

var Winamp = window.Webamp;
if(!Webamp.browserIsSupported()) {
    alert("Oh no! Webamp does not work!")
    throw new Error("What's the point of anything?")
}

const webamp = new Webamp({
    initialTracks: [],
    initialSkin: {
        // Can be downloaded from https://github.com/captbaritone/webamp/raw/master/skins/base-2.91.wsz
        url: "static/base-2.91.wsz"
    },
});

var winAmpRendered = false;
var queue = function(artist, title) {
    webamp.appendTracks([{
        metaData: {
            artist: artist,
            title: title,
        },
        // Can be downloaded from: https://github.com/captbaritone/webamp/raw/master/mp3/llama-2.91.mp3
        url: "http://media.blubrry.com/codingblocks/s/www.podtrac.com/pts/redirect.mp3/traffic.libsyn.com/codingblocks/codingblocks-episode-080.mp3"
    }]);
    if(!winAmpRendered) {
        winAmpRendered = true;
        webamp.renderWhenReady(document.getElementById('winamp-container'));
    }
}