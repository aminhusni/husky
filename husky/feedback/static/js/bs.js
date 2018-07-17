    <script type="text/javascript">
        $(function () {

            var admin_trigger = 0;
            var feedback_rating = 0;
            var feedback_remarks = 0;
            var getQueryString = function (field, url) {
                var href = url ? url : window.location.href;
                var reg = new RegExp('[?&]' + field + '=([^&#]*)', 'i');
                var string = reg.exec(href);
                return string ? string[1] : null;
            };

            $(".vote").on("click", function () {
                feedback_rating = $(this).attr("rel");
                if ($(this).attr("rel") < 3) {
                    $('.first').fadeOut(300).promise().done(function () {
                        $(".second").fadeIn(300);
                        setTimeout(function () {
                            $('.second').fadeOut(300).promise().done(function () {
                                $(".first").fadeIn(300);
                                $(".fault").removeClass("active");
                            });
                        }, 15000);
                    });
                } else {
                    vote(feedback_rating, feedback_remarks);
                    $('.first').fadeOut(300).promise().done(function () {
                        $(".third").fadeIn(300);
                        setTimeout(function () {
                            $('.third').fadeOut(300).promise().done(function () {
                                $(".first").fadeIn(300);
                            });
                        }, 3000);
                    });
                }
            });


            function vote(rating, remarks) {
                command = {};
                command["command"] = "insert_feedback_rating";
                command["device_id"] = getQueryString('did');
                command["rating"] = rating;
                command["remarks"] = remarks;
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });

                if (rating == "1" || rating == "2")
                {
                    command = {};
                    command["Command"] = "send_feedback_rating";
                    command["Device_ID"] = getQueryString('did');
                    command["Rating"] = rating;
                    command["Remarks"] = remarks;
                    $.ajax({
                        type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=send_email', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                        success: function (data) {
                            console.log("Sent Successfully");
                        }
                    });
                }
            }

            function call_supervisor() {
                command = {};
                command["command"] = "insert_call_supervisor";
                command["device_id"] = getQueryString('did');
                command["user_id"] = $("#user_id").val();
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });
            }

            function complete_check() {
                command = {};
                command["command"] = "insert_cleanliness_check";
                command["device_id"] = getQueryString('did');
                command["user_id"] = $("#user_id").val();
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });
            }

            function complete_fault_check() {
                var fault_ids = $('.checking:checked').map(function (i, n) {
                    return $(n).attr("rel");
                }).get().join(',');

                command = {};
                command["command"] = "update_cleanliness_check";
                command["device_id"] = getQueryString('did');
                command["user_id"] = $("#user_id").val();
                command["fault_ids"] = fault_ids;
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });

                command = {};
                command["Command"] = "Update Fault Cleaning Check";
                command["Device_ID"] = getQueryString('did');
                command["Report_IDs"] = fault_ids;
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=send_email', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });
            }

            function complete_report_check() {
                var report_ids = $('.checking:checked').map(function (i, n) {
                    return $(n).attr("rel");
                }).get().join(',');

                command = {};
                command["command"] = "update_supervisor_cleanliness_check";
                command["device_id"] = getQueryString('did');
                command["user_id"] = $("#user_id").val();
                command["report_ids"] = report_ids;
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });

                command = {};
                command["Command"] = "Update Supervisor to Cleaner Check";
                command["Device_ID"] = getQueryString('did');
                command["Report_IDs"] = report_ids;
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=send_email', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 10000,
                    success: function (data) {
                        console.log("Sent Successfully");
                    }
                });
            }



            $("#back").on("click", function () {
                $('.second').fadeOut(300).promise().done(function () {
                    $(".first").fadeIn(300);
                });
            });

            $("#cancel").on("click", function () {
                $(".active").removeClass("active");
                $('.first').fadeIn(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                admin_trigger = 0;
            });

            $("#cancel_supervisor").on("click", function () {
                $(".active").removeClass("active");
                $('.first').fadeIn(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                $('.supervisor-report-status').fadeOut(300);
                admin_trigger = 0;
            });

            $("#back_admin").on("click", function () {
                $(".active").removeClass("active");
                $('.admin-screen').fadeIn(300);
                $('.admin-fault-status').fadeOut(300);
            });

            

            $("#fault-status").on("click", function () {
                $(".active").removeClass("active");
                $('.admin-fault-status').fadeIn(300);
                $("#admin-fault-list").empty();

                //ajax get_fault_status
                command = {};
                command["command"] = "get_fault_list";
                command["device_id"] = getQueryString('did');
                command["user_id"] = $("#user_id").val();
                var message = "";
                $.ajax({
                    type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 15000,
                    success: function (data) {
                        //console.log(data);
                        //loading.hide();
                        $.each(data.results, function (index) {
                            message = "";
                            message += '<div style="display: inline-block;width: 100%;">';
                            message += '<div style="float:left;">';
                            message += '<input rel="' + this["feedback_id"] + '" class="checking" type="checkbox">';
                            message += '</div>'
                            message += '<div style="float:left;font-size: 24px;line-height: 33px;margin-left: 30px;">'
                            message += this["created_on"] + '<br>' + this["feedback_remarks"];
                            message += '</div>';
                            message += '</div>';
                            $("#admin-fault-list").append(message);
                        })
                    },
                    error: function () {
                        message = "No record(s) found.";
                        $("#admin-fault-list").append(message);
                    }
                });
                $('.first').fadeOut(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
            });

            $("#complete_fault_status").on("click", function () {
                if ($('.checking:checked').length > 0) {
                    complete_fault_check();
                }
                $(".active").removeClass("active");
                $('.admin-screen').fadeIn(300);
                $('.admin-fault-status').fadeOut(300);
            });

            $("#complete_supervisor").on("click", function () {
                if ($('.checking:checked').length > 0) {
                    complete_report_check();
                }
                $(".active").removeClass("active");
                $('.first').fadeIn(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                $('.supervisor-report-status').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                admin_trigger = 0;
            });

            

            $("#call-supervisor").on("click", function () {
                call_supervisor();
                $(".active").removeClass("active");
                $('.first').fadeIn(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                admin_trigger = 0;
            });

            $("#complete1").on("click", function () {
                $(".active").removeClass("active");
                complete_check();
                $('.first').fadeIn(300);
                $('.second').fadeOut(300);
                $('.third').fadeOut(300);
                $('.admin').fadeOut(300);
                $('.admin-screen').fadeOut(300);
                admin_trigger = 0;
            });

            $(".fault").on("click", function () {
                $(this).toggleClass("active");
            });

            $(".check-toilet").on("click", function () {
                $(this).toggleClass("active");
            });

            $("#submit").on("click", function () {
                if ($('.active').length > 0) {
                    feedback_remarks = $('.active').map(function (i, n) {
                        return $(n).attr("data-remark");
                    }).get().join(',');
                    console.log(feedback_remarks);
                    vote(feedback_rating, feedback_remarks);
                    $('.second').fadeOut(300).promise().done(function () {
                        $(".third").fadeIn(300);
                        $(".active").removeClass("active");
                        setTimeout(function () {
                            $('.third').fadeOut(300).promise().done(function () {
                                $(".first").fadeIn(300);
                            });
                        }, 3000);
                    });
                } 
            });

            
            $("#login").on("click", function () {
                admin_trigger += 1;
                if (admin_trigger == 3) {
                    $(".active").removeClass("active");
                    $('.first').fadeOut(300);
                    $('.second').fadeOut(300);
                    $('.third').fadeOut(300).promise().done(function () {
                        $(".admin").fadeIn(300);
                    });
                }
            });


            // Disable checkboxes
            $('input.passcode').click(function () {
                return false;
            });

            var pass = '1593',
                temp = '',
                pressed = 0,
                press_max = 4;

            $('.button-num').click(function () {

                pressed++;

                if (pressed <= press_max) {
                    $($('input')[pressed - 1]).prop('checked', true);
                    temp += $(this).attr("id").split('-')[1];
                }

            });
            var timer,
                timerduration = 300,
                shake = 10;

            $('#button-e').click(function () {

                if (pass == temp) {
                    $("#user_id").val('2');
                    $('.admin').fadeOut(300).promise().done(function () {
                        $(".admin-screen").fadeIn(300);
                    });
                }
                else if (temp == '1234') {
                    $("#user_id").val('3');
                    $("#supervisor-report-list").empty();
                    $('.admin').fadeOut(300).promise().done(function () {
                        command = {};
                        command["command"] = "get_report_check_list";
                        command["device_id"] = getQueryString('did');
                        command["user_id"] = $("#user_id").val();
                        var message = "";
                        $.ajax({
                            type: "POST", url: 'http://toiletkiosk.azurewebsites.net/action.ashx?action=json', data: { data: JSON.stringify(command) }, cache: false, async: true, timeout: 15000,
                            success: function (data) {
                                //console.log(data);
                                //loading.hide();
                                $.each(data.results, function (index) {
                                    message = "";
                                    message += '<div style="display: inline-block;width: 100%;">';
                                    message += '<div style="float:left;">';
                                    message += '<input rel="' + this["report_id"] + '" class="checking" type="checkbox">';
                                    message += '</div>'
                                    message += '<div style="float:left;font-size: 24px;line-height: 33px;margin-left: 30px;">'
                                    message += this["created_on"] + '<br>Cleaner: ' + this["cleaned_by"];
                                    message += '</div>';
                                    message += '</div>';
                                    $("#supervisor-report-list").append(message);
                                })
                            },
                            error: function () {
                                message = "No record(s) found.";
                                $("#supervisor-report-list").append(message);
                            }
                        });
                        $(".supervisor-report-status").fadeIn(300);
                    });
                }
                else {

                    $('#numpad')
                      .transition({ x: shake, duration: timerduration / 5 })
                      .transition({ x: -shake, duration: timerduration / 5 })
                      .transition({ x: shake, duration: timerduration / 5 })
                      .transition({ x: -shake, duration: timerduration / 5 })
                      .transition({ x: 0, duration: timerduration / 5 });

                    clearTimeout(timer);
                    $('#notice').html("Wrong Passcode!");

                    timer = setTimeout(function () {
                        pressed = 0;
                        temp = '';
                        $('input').prop('checked', false);
                    }, timerduration);

                }
            });

            $('#button-c').click(function () {

                if (pressed > 0) {
                    $($('input')[pressed - 1]).prop('checked', false);
                    pressed--;
                    temp = temp.slice(0, pressed);
                }

            });


        });
    </script>
