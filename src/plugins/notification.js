export default {
  install(Vue, options) {

    const placeholder_id = 'v-notifications-container';

    let notifier = function (type, message) {

      let settings = {
        prepend: false,
        dismissable: true,
        animate: true,
        attachTo: $('#' + placeholder_id),
        typeClasses: {
          success: 'alert-success',
          info: 'alert-info',
          warning: 'alert-warning',
          error: 'alert-danger'
        }
      };

      let notice = $('<div/>').addClass('alert ' + settings.typeClasses[type]);

      if (settings.dismissable) {

        notice.addClass('alert-dismissable');

        $('<button/>').addClass('close ml-2')
          .attr({
            type: 'button',
            'aria-label': 'close',
            'data-dismiss': 'alert'
          })
          .html('<span aria-hidden="true">&times;</span>')
          .appendTo(notice);

        if (settings.animate) {
          notice.addClass('fade show');
        }
      }

      notice.append(message);

      if (settings.prepend) {
        notice.prependTo(settings.attachTo);
      } else {
        notice.appendTo(settings.attachTo);
      }
      notice.fadeOut(10000);

      return this;

    };

    Vue.component('notifications', {
      template: `<div id="${placeholder_id}"></div>`
    });

    Vue.prototype.$notify = {
      error: function (message) {
        return notifier('error', message);
      },
      warning: function (message) {
        return notifier('warning', message);
      },
      info: function (message) {
        return notifier('info', message);
      },
      success: function (message) {
        return notifier('success', message);
      }
    }
  }
};