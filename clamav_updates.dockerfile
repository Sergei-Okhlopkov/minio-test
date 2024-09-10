FROM clamav/clamav

COPY clamav_data/update_clamav.sh /opt/update_clamav.sh

RUN chmod +x /opt/update_clamav.sh
RUN /bin/sh /opt/update_clamav.sh

EXPOSE 3310:3310

CMD ["/usr/sbin/clamd", "--foreground=true"]
