$(() => {
  const user_type = $("#id_user_type");
  const validation_code = $("#id_validation_code");
  const department_number = $("#id_department_number");

  if (user_type.val() === "Habitant") {
    validation_code.parent().toggleClass('d-none');
    validation_code.parent().parent().toggleClass('d-none');
    validation_code.prop('required', false);
  } else {
    department_number.parent().toggleClass('d-none');
    department_number.parent().parent().toggleClass('d-none');
    department_number.prop('required', false);
  }

  user_type.on("change", () => {
    validation_code.prop('required', !validation_code.prop('required'));
    validation_code.parent().parent().toggleClass('d-none');
    validation_code.parent().toggleClass('d-none');

    department_number.prop('required', !validation_code.prop('required'));
    department_number.parent().parent().toggleClass('d-none');
    department_number.parent().toggleClass('d-none');
  });

  $(document).ready( function() {
      var datetime = new Date();
      year = datetime.getFullYear();
      month = datetime.getMonth() + 1;
      month = ("0" + month).slice(-2);
      day = datetime.getDate();
      day = ("0" + day).slice(-2);
      hours = datetime.getHours();
      hours = ("0" + hours).slice(-2);
      minutes = datetime.getMinutes();
      minutes = ("0" + minutes).slice(-2);
      $('.dateinput').val(`${year}-${month}-${day}`);
      $('.timeinput').val(`${hours}:${minutes}`);
  });
});

