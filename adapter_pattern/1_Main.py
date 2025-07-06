from adapter import Logger, LegacyLogger, LegacyLoggerAdapter

def process(logger: Logger):
    logger.log("System started")

legacy = LegacyLogger()
adapter_debug = LegacyLoggerAdapter(legacy)
adapter_info = LegacyLoggerAdapter(legacy, "info")

process(adapter_debug) #Output: [DEBUG] System started
process(adapter_info) #Output: [INFO] System started