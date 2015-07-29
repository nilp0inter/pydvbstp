import attr


@attr.s
class Segment:
    payload_id = attr.ib()
    segment_id = attr.ib()
    segment_version = attr.ib()
    text = attr.ib(hash=False, cmp=False)


@attr.s
class Section:
    version = attr.ib()
    reserved = attr.ib()
    encryption = attr.ib()
    has_crc = attr.ib()
    total_segment_size = attr.ib()
    payload_id = attr.ib()
    segment_id = attr.ib()
    segment_version = attr.ib()
    section_number = attr.ib()
    last_section_number = attr.ib()
    compression = attr.ib()
    has_provider_id = attr.ib()
    private_header_length = attr.ib()
    provider_id = attr.ib()
    private_header_data = attr.ib()
    payload = attr.ib()
    crc = attr.ib()

    @property
    def is_last(self):
        return self.last_section_number == self.section_number
