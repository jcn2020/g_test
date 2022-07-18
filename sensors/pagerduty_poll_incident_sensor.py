# See ./requirements.txt for requirements.
import os
import pypd
import logging
import json

from st2reactor.sensor.base import PollingSensor


class PagerDutyPollIncidentSensor(PollingSensor):
    '''
    Sensor will monitor for any new projects created in JIRA and
    emit trigger instance when one is created.
    '''
    def __init__(self, sensor_service, config=None, poll_interval=5):
        super(PagerDutyPollIncidentSensor, self).__init__(sensor_service=sensor_service,
                                                 config=config,
                                                 poll_interval=poll_interval)

        self._pagerduty_api_key = None
        self._pagerduty_team_id = None

        self._logger = self._sensor_service.get_logger(__name__)
        self._trigger_name = 'pagerduty_incident_trigger_event'
        self._trigger_pack = '{{ref}}'
        self._trigger_ref = '.'.join([self._trigger_pack, self._trigger_name])

    def setup(self):
        self.pd = self._init_client()

    def _init_client(self):
        """ init_client method, run at class creation
        """
        self._pagerduty_api_key = self._config.get('pagerduty_api_key', None) or None
        self._pagerduty_team_id = self._config.get('pagerduty_team_id', None) or None
        pypd.api_key = self._pagerduty_api_key

        return pypd

    def poll(self):
        self._detect_new_incidents()

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def _detect_new_incidents(self):
        
        incidents = self.pd.Incident.find(statuses=['triggered', ], maximum=5, team_ids=[self._pagerduty_team_id, ])
        incidentsarr = []
        for f in incidents:
            incidentsarr.append(f.json)

        for incident in incidentsarr:
            self._dispatch_incidents_trigger(incident)

    def _dispatch_incidents_trigger(self, incident):
        trigger = self._trigger_ref
        incident_dict = json.loads(json.dumps(incident))
        
        # extracting log entry id from incident payload
        log_entry_id = incident_dict['first_trigger_log_entry']['id']

        # extracting log entry
        log_entry = self.pd.LogEntry.fetch(include=['channels', ], id=log_entry_id )

        log_entry_dict = json.dumps(log_entry.json)
        log_entry_dict_entry = json.loads(log_entry_dict)
        
        incident_id = log_entry_dict_entry['incident']['id']
        incident_channel = log_entry_dict_entry['channel']['type']
        logging.info('incident dispatch trigger called for incident with id: %s, channel: %s', incident_id, incident_channel)

        payload = {}
        payload['pdteam'] = log_entry_dict_entry['teams'][0]['summary']
        payload['pdservice'] = log_entry_dict_entry['service']['summary']
        payload['pdincidentid'] = incident_id
        payload['channeltype'] = incident_channel

        payload['incidentdetails'] = log_entry_dict_entry['channel']
        self._sensor_service.dispatch(trigger, payload)