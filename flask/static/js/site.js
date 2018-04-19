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

var initializeCheckboxes = function() {
  var filterCheckboxes = $('#frm_filter').find('input:checkbox');
  // Inefficient!!
  var url = new URL(location.href);
  for(var param of url.searchParams.entries()) {
    filterCheckboxes.each(function(i) {
      var cb = filterCheckboxes[i];
      console.log(cb);
      if(cb.name === param[0] && cb.value === param[1]) {
        cb.checked = true;
      }
    });
  }
}

$(document).ready(function() {
  initializeCheckboxes();
  $('#btn_filter').on('click', filter);
});