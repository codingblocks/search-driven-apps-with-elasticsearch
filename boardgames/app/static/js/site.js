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
  var initializeRadios = function() {
    var filterInputs = $('#frm_filter').find('input:radio');
    // Inefficient!!
    var url = new URL(location.href);
    for(var param of url.searchParams.entries()) {
      filterInputs.each(function(i) {
        var cb = filterInputs[i];
        if(cb.name === param[0] && cb.value === param[1]) {
          cb.checked = true;
        }
      });
    }
  }

  var initializeTitle = function() {
    $("#title").autocomplete({
      source: getSuggestions,
      select: selectItem,
      minLength: 2,
      change: function() {
        $("#title").val("").css("display", 2);
      }
    });
  }

  var initializeInputs = function() {
    initializeCheckboxes();
    initializeRadios();
    initializeTitle();
  }

  var showFilters = function() {
    $('#mdl_filter').modal('show');
  }

  var filter = function(event) {
    event.preventDefault();

    var checked = $('#frm_filter').find('input:checked');
    var params = [];
    checked.each(function(i) {
      var cb = checked[i];
      if(cb.name && cb.value) {
        params.push({ name: cb.name, value: cb.value });
      }
    });
    
    if($('#title').val()) {
      params.push({ name: 'title', value: $('#title').val() })
    }
    if(params.length) {
      location.href = '/?' + $.param(params);
    }
  }

  var clearFilters = function() {
    if(confirm('Clear filters?')) {
      location.href='/';
    }
  }

  var reset = function() {
    if(confirm('Reset all data??')) {
      location.href='/reset';
    } else {
      return false;
    }
    return true;
  }

  var getSuggestions = function (request, response) {
    $.getJSON(
      "/suggest?title=" + request.term,
      function (data) {
        var formatted = data.hits.hits.map(function(g) {
          return g._source.title;
        });
        response(formatted);
      }
    );
  }

  var selectItem = function (event, ui) {
    $("#title").val(ui.item.value);
    return false;
  }


  $(document).ready(function() {
    initializeInputs();
    $('input').change(filter);
    $('.action_clear').on('click', clearFilters);
    $('.action_showFilters').on('click', showFilters);
    $('.action_reset').on('click', reset);
  });
})();