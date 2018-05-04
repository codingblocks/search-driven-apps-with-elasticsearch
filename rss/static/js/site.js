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

  var reset = function() {
    if(confirm('Reset all data??')) {
      location.href='/reset' ;
    } else {
      return false;
    }
    return true;
  }

  $(document).ready(function() {
    initializeCheckboxes();
    $('.action_filter').on('click', filter);
    $('.action_clear').on('click', clearFilters);
    $('.action_showFilters').on('click', showFilters);
    $('.action_reset').on('click', reset);
  });
})();