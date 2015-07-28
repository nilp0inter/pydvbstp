import attr


@attr.s
class DVBSTP:
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
