class UserClient:
    def __init__(self, request):
        self.__request = request

    @property
    def ip_address(self) -> str:
        x_forwarded_for = self.__request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[-1].strip()
        elif self.__request.META.get("HTTP_X_REAL_IP"):
            ip = self.__request.META.get("HTTP_X_REAL_IP")
        else:
            ip = self.__request.META.get("REMOTE_ADDR")
        return ip

    @property
    def agent_type(self) -> str:
        if self.__request.user_agent.is_mobile:
            return "Mobile"
        elif self.__request.user_agent.is_tablet:
            return "Tablet"
        elif self.__request.user_agent.is_touch_capable:
            return "Touch Capable"
        elif self.__request.user_agent.is_pc:
            return "PC"
        elif self.__request.user_agent.is_bot:
            return "Bot"
        else:
            return "Unknown"

    @property
    def agent_browser(self) -> str:
        return self.__request.user_agent.browser

    @property
    def agent_browser_family(self) -> str:
        return self.__request.user_agent.browser.family

    @property
    def agent_browser_version(self) -> str:
        return f"{self.__request.user_agent.browser.version}"

    @property
    def agent_browser_version_string(self) -> str:
        return self.__request.user_agent.browser.version_string

    @property
    def agent_os(self) -> str:
        return self.__request.user_agent.os

    @property
    def agent_os_family(self) -> str:
        return self.__request.user_agent.os.family

    @property
    def agent_os_version(self) -> str:
        return f"{self.__request.user_agent.os.version}"

    @property
    def agent_os_version_string(self) -> str:
        return self.__request.user_agent.os.version_string

    @property
    def agent_device(self) -> str:
        return self.__request.user_agent.device

    @property
    def agent_device_family(self) -> str:
        return self.__request.user_agent.device.family
