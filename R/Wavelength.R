Wavelength <- function()
{
  library(data.table)
  library(ggplot2)
  FileList <- list.files(pattern = "SSM$")
  for (i in 1:length(FileList))
  {
    File <- FileList[i]
    Data <- fread(File, header = FALSE)
    DataFrame <- data.frame(spectrum = Data[, 1], intensity = Data[, 2])
    colnames(DataFrame) <- c("Wavelength", "Counts")
    FileName <- substr(File, start = 1, stop = (nchar(File) - 4))
    MaxCounts <- max(Data[, 2])
    Max <- DataFrame[DataFrame$Counts == MaxCounts, ]
    MaxWavelength <- paste("Main Wavelength =", Max[, 1], "nm")
    yRoof <- MaxCounts * 1.1
    graph <- ggplot(DataFrame, aes(x = Wavelength, y = Counts)) +
             geom_line() +
             xlab("Wavelength in Nanometers") +
             ylab("Counts") +
             ggtitle(FileName) +
             theme(plot.title = element_text(hjust=0.5)) +
             theme(plot.title = element_text(size = 20),
                   axis.title = element_text(size = 15),
                   axis.text = element_text(size = 12)) +
             annotate("text", x = 900, y = yRoof,
                      label = MaxWavelength, fontface = "italic", size = 5)
    graph
    ggsave(file = paste0(FileName, ".png"), dpi = 200, width = 8, height = 5)
  }
}
