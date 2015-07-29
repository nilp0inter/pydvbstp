from collections import defaultdict

import binascii

from .message import Segment


class Collector:
    def __init__(self):
        self.sections = defaultdict(dict)
        self.segments = set()

    def add_section(self, section):
        sections = self.sections[section.payload_id]
        sections[section.section_number] = section

        have_all_sections = len(sections) == section.last_section_number + 1

        if section.is_last and have_all_sections:
            raw = b''.join(s.payload
                           for _, s in
                           sorted(sections.items(),
                                  key=lambda x: x[0]))
            if section.has_crc:
                crc_match = section.crc == binascii.crc32(raw)
            else:
                crc_match = None

            del self.sections[section.payload_id]

            if crc_match is not False:
                segment = Segment(payload_id=section.payload_id,
                                  segment_id=section.segment_id,
                                  segment_version=section.segment_version,
                                  text=raw)
                if not segment in self.segments:
                    self.segments.add(segment)
                    return segment
