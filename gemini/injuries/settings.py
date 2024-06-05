from models.ModelOptions import ModelOptions

__session_key = 'INJURY_ADVISOR'
__system_instruction = ("User will provide injuries with whom he is struggling. Try to present advices before "
                        "consulting to doctor to faster recover from them. If possible, you can present a "
                        "chronological list of steps. Do not generate information that you cannot give advice as a "
                        "doctor i will provide it by myself in my application. Name each section with desired title "
                        "when writing.")

injury_model_options = ModelOptions(__session_key, __system_instruction)
