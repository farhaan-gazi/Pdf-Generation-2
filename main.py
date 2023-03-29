from jinja2 import Environment, FileSystemLoader
import copy;

from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

def generateTableData(N):
    notAvailable = "/home/farhaangazi/Projects/Increff/PdfGeneration/main2/pdfResources/image-not-available.jpg"
    topSellerStyleLevelPdfRowList = [
        {"style" : "ADFEWRQ120874210",
         "imageUrl" : notAvailable,
         "healthyRos" : 2.2,
         "doh" : 50,
         "mrp" : 1799.00,
         "str" : 100,
         "rawSalesQty" : 100,
         "revenue" : 202.2,
         "avgHealthyDaysLive" : 20,
         "avgRawDaysLive" : 20,
         "closingStock" : 10,
         "averageDiscountPercentage" : 20.5,
         "noOfStores" : 20 }
    ]
    for i in range(N-1):
        sample = copy.deepcopy(topSellerStyleLevelPdfRowList[0])
        sample["style"] = str(i)
        sample["doh"] = sample["doh"]+i
        topSellerStyleLevelPdfRowList.append(sample)

    if(N==0):
        return []
    return topSellerStyleLevelPdfRowList

def generateParams():
    params = {
        "start_date" : "11-01-23",
        "end_date" : "11-20-23",
        "category" : "category1",
        "subcategory" : "subcategory1",
        "channel" : "channel1",
        "attribute1" : "attribute1",
        "attribute2" : "attribute2",
        "season" : "summer-spring",
        "brand" : "",
        "gender" : "male",
        "style_tag" : "",
        "sort_by" : "ros_dec",
        "minLiveDays" : "0",
        "minStrPercentage" : "20.20",
        "maxStrPercentage" : "50.5"
    }
    return params;

def main():
    params = generateParams();
    results = generateTableData(26);
    increffLogoUrl = "/home/farhaangazi/Projects/Increff/PdfGeneration/main2/pdfResources/increff_image.jpg";
    data = {
            "params" : params,
            "results" : results,
            "increffLogo" : increffLogoUrl
    }
    getPdfFromHTMLusingWeasyPrint(data)

def getPdfFromHTMLusingWeasyPrint(data):
    environment = Environment(loader=FileSystemLoader("./"))

    print(">>data", data);

    #content
    template = environment.get_template("./pdfResources/top-seller-report.html")
    content = template.render( data )

    with open("pdf_rendered.html", "w") as file: # for PDF 
        file.write(content)

    font_config = FontConfiguration()
    html = HTML(filename='pdf_rendered.html')
    html.write_pdf( './pdf_rendered.pdf',
                   font_config=font_config,
                    presentational_hints=True) 
main();
