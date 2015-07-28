from bitstring import ConstBitStream

from .message import DVBSTP


def unpack(raw):
    """Unpack ``raw`` and return an object."""
    packet = ConstBitStream(raw)

    version = packet.read('uint:2')
    reserved = packet.read('uint:3')
    encryption = packet.read('uint:2')
    has_crc = packet.read('uint:1')
    total_segment_size = packet.read('uint:24')
    payload_id = packet.read('uintbe:8')
    segment_id = packet.read('uintbe:16')
    segment_version = packet.read('uintbe:8')
    section_number = packet.read('uint:12')
    last_section_number = packet.read('uint:12')
    compression = packet.read('uint:3')
    has_provider_id = packet.read('uint:1')
    private_header_length = packet.read('uint:4')

    if has_provider_id:
        provider_id = packet.read('uintbe:32')
    else:
        provider_id = None

    private_header_data = packet.read('bytes:' + str(private_header_length))

    if has_crc:
        payload = raw[packet.bytepos:-4]
        crc = raw[-4:]
    else:
        crc = None
        payload = raw[packet.bytepos:]

    del raw
    del packet

    return DVBSTP(**locals())
