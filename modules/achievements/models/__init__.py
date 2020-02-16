from modules.achievements.models.achievement import Achievement
from modules.achievements.models.user_achievement import UserAchievement

from modules.achievements.models.item_done import ItemDoneAchievement
from modules.achievements.models.login_count import LoginCountAchievement
from modules.achievements.models.progress import ProgressAchievement
from modules.achievements.models.assign_profile import AssignProfileAchievement
from modules.achievements.models.unlock_mission_after_task import UnlockMissionAfterTaskAchievement
from modules.achievements.models.assign_spacecalc_group import AssignSpaceCalcGroupAchievement

from funcrowd.settings import events_manager

events_manager.register_achievements(ItemDoneAchievement)
events_manager.register_achievements(LoginCountAchievement)
events_manager.register_achievements(ProgressAchievement)
events_manager.register_achievements(AssignProfileAchievement)
events_manager.register_achievements(UnlockMissionAfterTaskAchievement)
events_manager.register_achievements(AssignSpaceCalcGroupAchievement)
