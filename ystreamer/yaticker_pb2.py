# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yfin.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nyfin.proto\"\xcb\x08\n\x08yaticker\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x12\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\x12\x10\n\x08\x65xchange\x18\x05 \x01(\t\x12&\n\tquoteType\x18\x06 \x01(\x0e\x32\x13.yaticker.QuoteType\x12.\n\x0bmarketHours\x18\x07 \x01(\x0e\x32\x19.yaticker.MarketHoursType\x12\x15\n\rchangePercent\x18\x08 \x01(\x02\x12\x11\n\tdayVolume\x18\t \x01(\x12\x12\x0f\n\x07\x64\x61yHigh\x18\n \x01(\x02\x12\x0e\n\x06\x64\x61yLow\x18\x0b \x01(\x02\x12\x0e\n\x06\x63hange\x18\x0c \x01(\x02\x12\x11\n\tshortName\x18\r \x01(\t\x12\x12\n\nexpireDate\x18\x0e \x01(\x12\x12\x11\n\topenPrice\x18\x0f \x01(\x02\x12\x15\n\rpreviousClose\x18\x10 \x01(\x02\x12\x13\n\x0bstrikePrice\x18\x11 \x01(\x02\x12\x18\n\x10underlyingSymbol\x18\x12 \x01(\t\x12\x14\n\x0copenInterest\x18\x13 \x01(\x12\x12)\n\x0boptionsType\x18\x14 \x01(\x0e\x32\x14.yaticker.OptionType\x12\x12\n\nminiOption\x18\x15 \x01(\x12\x12\x10\n\x08lastSize\x18\x16 \x01(\x12\x12\x0b\n\x03\x62id\x18\x17 \x01(\x02\x12\x0f\n\x07\x62idSize\x18\x18 \x01(\x12\x12\x0b\n\x03\x61sk\x18\x19 \x01(\x02\x12\x0f\n\x07\x61skSize\x18\x1a \x01(\x12\x12\x11\n\tpriceHint\x18\x1b \x01(\x12\x12\x10\n\x08vol_24hr\x18\x1c \x01(\x12\x12\x18\n\x10volAllCurrencies\x18\x1d \x01(\x12\x12\x14\n\x0c\x66romcurrency\x18\x1e \x01(\t\x12\x12\n\nlastMarket\x18\x1f \x01(\t\x12\x19\n\x11\x63irculatingSupply\x18  \x01(\x01\x12\x11\n\tmarketcap\x18! \x01(\x01\"\x80\x02\n\tQuoteType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tALTSYMBOL\x10\x05\x12\r\n\tHEARTBEAT\x10\x07\x12\n\n\x06\x45QUITY\x10\x08\x12\t\n\x05INDEX\x10\t\x12\x0e\n\nMUTUALFUND\x10\x0b\x12\x0f\n\x0bMONEYMARKET\x10\x0c\x12\n\n\x06OPTION\x10\r\x12\x0c\n\x08\x43URRENCY\x10\x0e\x12\x0b\n\x07WARRANT\x10\x0f\x12\x08\n\x04\x42OND\x10\x11\x12\n\n\x06\x46UTURE\x10\x12\x12\x07\n\x03\x45TF\x10\x14\x12\r\n\tCOMMODITY\x10\x17\x12\x0c\n\x08\x45\x43NQUOTE\x10\x1c\x12\x12\n\x0e\x43RYPTOCURRENCY\x10)\x12\r\n\tINDICATOR\x10*\x12\r\n\x08INDUSTRY\x10\xe8\x07\"\x1f\n\nOptionType\x12\x08\n\x04\x43\x41LL\x10\x00\x12\x07\n\x03PUT\x10\x01\"a\n\x0fMarketHoursType\x12\x0e\n\nPRE_MARKET\x10\x00\x12\x12\n\x0eREGULAR_MARKET\x10\x01\x12\x0f\n\x0bPOST_MARKET\x10\x02\x12\x19\n\x15\x45XTENDED_HOURS_MARKET\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yfin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_YATICKER']._serialized_start=15
  _globals['_YATICKER']._serialized_end=1114
  _globals['_YATICKER_QUOTETYPE']._serialized_start=726
  _globals['_YATICKER_QUOTETYPE']._serialized_end=982
  _globals['_YATICKER_OPTIONTYPE']._serialized_start=984
  _globals['_YATICKER_OPTIONTYPE']._serialized_end=1015
  _globals['_YATICKER_MARKETHOURSTYPE']._serialized_start=1017
  _globals['_YATICKER_MARKETHOURSTYPE']._serialized_end=1114
# @@protoc_insertion_point(module_scope)
