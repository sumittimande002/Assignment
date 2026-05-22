# # 7. logging frameworks (duck typing + polymorphism)
# # 7. Logging Framework Simulation

# **Concepts Covered:**
# Duck Typing, Polymorphism

# ### Problem Statement

# Logging frameworks are used in applications to record system events. Logs can be written to different outputs such as files, databases, or consoles.

# Create a simple logging framework simulation using Python.

# ### Requirements

# 1. Create multiple logger classes such as:

#    * `FileLogger`
class FileLogger:
    def log(self,msg):
        print(f"[File Log], {msg}")


#    * `ConsoleLogger`
class ConsoleLogger:
    def log(self,msg):
        print(f"[Console Log], {msg}")
# 2. Each class should implement a method called `log(message)`.
# 3. Create a function that accepts a logger object and calls the `log()` method.
def write_log(logger,msg):
    logger.log(msg)
# ### Implementation Guidelines

file_loger = FileLogger()
console_loger = ConsoleLogger()

write_log(file_loger,"File saved successfully.")
write_log(console_loger,"Application Started .")


# * The function should not check the object type explicitly.
# * It should rely on **duck typing** (if the object has a `log()` method, it works).
# * Demonstrate **polymorphism** by passing different logger objects.
# +
# ### Expected Outcome

# The same logging function should work with multiple logger types without modification.

