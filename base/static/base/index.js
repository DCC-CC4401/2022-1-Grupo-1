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
});

