import csv
import os


class PolicyMapStatement:

    def open(self):
        return open(os.path.join(os.path.expanduser("~"), "Documents\\vpolicyMapStatement.csv"), 'w', newline='')

    def column_name(self, writer):
        vmap_headers = ["className", "policeCir", "policeBc", "policeBe", "bandwidth", "randomDetect", "fairQueue",
                        "bandwidthPercent", "shape", "shapeAverage", "policyMap", "priorityPercent",
                        "priorityPercentBurst", "priority", "compressHeaderIpRtp", "setExpTopMost", "setExpImposition",
                        "shapePeak", "priorityBurst", "setDSCP", "policerPir", "shapeAverageBc", "shapeAverageBe",
                        "gsrPriority", "cirPercentage", "bcbeInMs", "setPrec", "device", "policyMapName",
                        "policeConformAction", "policeConformTransformValue", "policeConformTransformType",
                        "policeExceedAction", "policeExceedTransformValue", "policeExceedTransformType",
                        "policeViolateAction", "policeViolateTransformValue", "policeViolateTransformType"]
        writer.writerow(vmap_headers)
