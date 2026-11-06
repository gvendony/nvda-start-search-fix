# NVDA app module override for the Windows 11 Start menu search (SearchHost.exe).
#
# Problem: since the October 2026 Windows update the search web page fires
# EVENT_OBJECT_SELECTION on the "All" filter tab every time the results are
# re-rendered, right after the selection of the top result. NVDA's
# NVDAObject.event_selection cancels speech and reports any selected object
# inside the results document, so the tab interrupts the result and the
# navigator object moves to the tab.
#
# Fix: ignore selection events on filter tabs inside the results document.
# Real keyboard focus on a tab arrives as gainFocus and is not affected.

import controlTypes
from logHandler import log
from nvdaBuiltin.appModules.searchui import *  # noqa: F403
from nvdaBuiltin.appModules.searchui import AppModule as _BuiltinAppModule
from nvdaBuiltin.appModules.searchui import StartChromiumObj

log.info("Start Search Fix add-on loaded: ignoring selection events on search filter tabs")


class AppModule(_BuiltinAppModule):
	def event_selection(self, obj, nextHandler):
		if isinstance(obj, StartChromiumObj) and obj.role == controlTypes.Role.TAB:
			return
		nextHandler()
