function factory(form_obj) {
    function callback(position) {
        $(form_obj).find('#id_latitude').val(position.coords.latitude);
        $(form_obj).find('#id_longitude').val(position.coords.longitude);
        form_obj.submit();
    }
    return callback
}

function initGeolocation(form_obj) {
    if (navigator && navigator.geolocation) {
        success = factory(form_obj);
        navigator.geolocation.getCurrentPosition(
            success, error, {enableHighAccuracy: true});
    } else {
        console.warn('Geolocation is not supported');
    }
}

function error() {
    console.warn('ERROR(' + err.code + '): ' + err.message);
}

$("#add form").submit(function(event) {
    event.preventDefault();
    initGeolocation(this)
});

$("#around_you form").submit(function(event) {
    event.preventDefault();
    initGeolocation(this)
});
