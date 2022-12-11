"""
ეს არის მთავარი ფაილი საიდანაც ყველაფერი ეშვება

გამოყენებული ბიბლიოთეკები:
pip install pandas
pip install numpy
pip install openpyxl
pip install matplotlib
pip install scikit-learn
"""
import Omega
import Read
import Draw
import Regression
import Kmean

if __name__ == '__main__':
    # ჩვეულებრივი შედარება
    # data = Read.ReadCsv()  # აბრუნებს -> [(S, b)]
    # Draw.DrawErrors(data)



    # წავიკითხოთ მონაცემები ფაილებიდან და მივიღოთ წრფივი სისტემები
    # linearSystems = Read.GetData()

    # # ამოვხსნათ სისტემები
    # solutions = Omega.Solve(linearSystems)
    #
    # print(solutions.CO)
    # # # დავხაზოთ მიღებული შედეგები
    # Draw.PlotSolutions(solutions.CO, "CO Coefficients")
    # Draw.PlotSolutions(solutions.NO, "NO solutions")
    # Draw.PlotSolutions(solutions.NO2, "NO2 solutions")
    # Draw.PlotSolutions(solutions.O3, "O3 solutions")
    # Draw.PlotSolutions(solutions.O3NO2, "O3NO2 solutions")
    #
    # # # წრფივი რეგრესია ცდომილობა
    # coError = Regression.Predict(solutions.CO)
    # noError = Regression.Predict(solutions.NO)
    # no2Error = Regression.Predict(solutions.NO2)
    # o3Error = Regression.Predict(solutions.O3)
    # o3no2Error = Regression.Predict(solutions.O3NO2)
    # #
    # x = [i[0] for i in solutions.CO]
    # y = [i[1] for i in solutions.CO]
    # z = [i[2] for i in solutions.CO]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "CO clustering")
    #
    # x = [i[0] for i in solutions.NO]
    # y = [i[1] for i in solutions.NO]
    # z = [i[2] for i in solutions.NO]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "NO clustering")
    #
    # x = [i[0] for i in solutions.NO2]
    # y = [i[1] for i in solutions.NO2]
    # z = [i[2] for i in solutions.NO2]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "NO2 clustering")
    #
    # x = [i[0] for i in solutions.O3]
    # y = [i[1] for i in solutions.O3]
    # z = [i[2] for i in solutions.O3]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "O3 clustering")
    #
    # x = [i[0] for i in solutions.O3NO2]
    # y = [i[1] for i in solutions.O3NO2]
    # z = [i[2] for i in solutions.O3NO2]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "O3NO2 clustering")
    # #
    # # ეს მხოლოდ წერტილებს დასვავს წრფეებს აღარ გაავლებს
    # Draw.ScatterSolutions(solutions.CO, "CO Coefficients (9K)")
    # Draw.ScatterSolutions(solutions.NO, "NO Coefficients (9K)")
    # Draw.ScatterSolutions(solutions.NO2, "NO2 solutions")
    # Draw.ScatterSolutions(solutions.O3, "O3 solutions")
    # Draw.ScatterSolutions(solutions.O3NO2, "O3NO2 solutions")
    #
    # # დავხაზოთ ცდომილობა
    # Draw.ErrorGraph(coError, "CO coefficients deviation from line (9K)")
    # Draw.ErrorGraph(noError, "NO coefficients deviation from line (9K)")
    # Draw.ErrorGraph(no2Error, "NO2 error")
    # Draw.ErrorGraph(o3Error, "O3 error")
    # Draw.ErrorGraph(o3no2Error, "O3NO2 error")
    # #
    #
    # """ეტაპი 2 ვასაშუალოებთ 15-15-15-15 წამებით"""
    #
    # წავიკითხოთ მონაცემები ფაილებიდან და მივიღოთ წრფივი სისტემები
    # linearSystems = Read.GetDataMinMax()
    #
    # for vector in linearSystems:
    #     b = vector[4].CO
    #     ma = max(vector[0].CO, vector[2].CO)
    #     mi = min(vector[1].CO, vector[3].CO)
    #     print("CO ->  MAX: " + str(ma) + "| MIN: " + str(mi) + "| NEA: " + str(b))
    # # ამოვხსნათ სისტემები
    # solutions = Omega.Solve15(linearSystems)
    #
    #
    # # წრფივი რეგრესია ცდომილობა
    # coError, x1, y1 = Regression.Predict2d(solutions.CO)
    noError, x2, y2 = Regression.Predict2d(solutions.NO)
    # no2Error, x3, y3 = Regression.Predict2d(solutions.NO2)
    # o3Error, x4, y4 = Regression.Predict2d(solutions.O3)
    # o3no2Error, x5, y5 = Regression.Predict2d(solutions.O3NO2)
    #
    # # ეს მხოლოდ წერტილებს დასვავს წრფეებს აღარ გაავლებს
    # Draw.ScatterSolutions2d(solutions.CO, "CO Coefficients (MIN-MAX)", x1, y1)
    # Draw.ScatterSolutions2d(solutions.NO, "NO Coefficients (MIN-MAX)", x2, y2)
    # Draw.ScatterSolutions2d(solutions.NO2, "NO2 solutions", x3, y3)
    # Draw.ScatterSolutions2d(solutions.O3, "O3 solutions", x4, y4)
    # Draw.ScatterSolutions2d(solutions.O3NO2, "O3NO2 solutions", x5, y5)
    #
    # # დავხაზოთ ცდომილობა
    # Draw.ErrorGraph(coError, "CO coefficients deviation from line (MIN-MAX)")
    # Draw.ErrorGraph(noError, "NO coefficients deviation from line (MIN-MAX)")
    # Draw.ErrorGraph(no2Error, "NO2 error")
    # Draw.ErrorGraph(o3Error, "O3 error")
    # Draw.ErrorGraph(o3no2Error, "O3NO2 error")


    # x = [i[0] for i in solutions.CO]
    # y = [i[1] for i in solutions.CO]
    # clusters = Kmean.UniqueClustering2D(x, y, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections2D(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters2D(UniqueClusters, 2, 2)
    # result = Kmean.Clean2D(lastStep)
    # Draw.ScatterClusters2D(result, "CO clusters")
    #
    # x = [i[0] for i in solutions.NO]
    # y = [i[1] for i in solutions.NO]
    # clusters = Kmean.UniqueClustering2D(x, y, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections2D(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters2D(UniqueClusters, 2, 2)
    # result = Kmean.Clean2D(lastStep)
    # Draw.ScatterClusters2D(result, "NO clusters")
    #
    # x = [i[0] for i in solutions.NO2]
    # y = [i[1] for i in solutions.NO2]
    # clusters = Kmean.UniqueClustering2D(x, y, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections2D(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters2D(UniqueClusters, 2, 2)
    # result = Kmean.Clean2D(lastStep)
    # Draw.ScatterClusters2D(result, "NO2 clusters")
    #
    # x = [i[0] for i in solutions.O3]
    # y = [i[1] for i in solutions.O3]
    # clusters = Kmean.UniqueClustering2D(x, y, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections2D(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters2D(UniqueClusters, 2, 2)
    # result = Kmean.Clean2D(lastStep)
    # Draw.ScatterClusters2D(result, "O3 clusters")
    #
    # x = [i[0] for i in solutions.O3NO2]
    # y = [i[1] for i in solutions.O3NO2]
    # clusters = Kmean.UniqueClustering2D(x, y, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections2D(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters2D(UniqueClusters, 2, 2)
    # result = Kmean.Clean2D(lastStep)
    # Draw.ScatterClusters2D(result, "O3NO2 clusters")

    #
    # """ეტაპი 3 ვასაშუალოებთ 7-7 წამის ინტერვალებით"""
    #
    # # წავიკითხოთ მონაცემები ფაილებიდან და მივიღოთ წრფივი სისტემები
    linearSystems = Read.GetData9()

    # ამოვხსნათ სისტემები
    solutions = Omega.Solve(linearSystems)

    # ეს მხოლოდ წერტილებს დასვავს წრფეებს აღარ გაავლებს
    # Draw.ScatterSolutions(solutions.CO, "CO Coefficients (7-7)")
    Draw.ScatterSolutions(solutions.NO, "NO Coefficients (7-7)")
    # Draw.ScatterSolutions(solutions.NO2, "NO2 solutions")
    # Draw.ScatterSolutions(solutions.O3, "O3 solutions")
    # Draw.ScatterSolutions(solutions.O3NO2, "O3NO2 solutions")

    # x = [i[0] for i in solutions.CO]
    # y = [i[1] for i in solutions.CO]
    # z = [i[2] for i in solutions.CO]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "CO clustering")
    #
    # x = [i[0] for i in solutions.NO]
    # y = [i[1] for i in solutions.NO]
    # z = [i[2] for i in solutions.NO]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "NO clustering")
    #
    # x = [i[0] for i in solutions.NO2]
    # y = [i[1] for i in solutions.NO2]
    # z = [i[2] for i in solutions.NO2]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "NO2 clustering")
    #
    # x = [i[0] for i in solutions.O3]
    # y = [i[1] for i in solutions.O3]
    # z = [i[2] for i in solutions.O3]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "O3 clustering")
    #
    # x = [i[0] for i in solutions.O3NO2]
    # y = [i[1] for i in solutions.O3NO2]
    # z = [i[2] for i in solutions.O3NO2]
    # clusters = Kmean.UniqueClustering(x, y, z, 14, 2)
    # UniqueClusters = Kmean.ClusterIntersections(clusters, 2, 2)
    # lastStep = Kmean.ShrinkClusters(UniqueClusters, 2, 2)
    # result = Kmean.Clean(lastStep)
    # Draw.ScatterClusters3D(result, "O3NO2 clustering")

    # წრფივი რეგრესია ცდომილობა
    # coError = Regression.Predict(solutions.CO)
    noError = Regression.Predict(solutions.NO)
    # no2Error = Regression.Predict(solutions.NO2)
    # o3Error = Regression.Predict(solutions.O3)
    # o3no2Error = Regression.Predict(solutions.O3NO2)

    # დავხაზოთ ცდომილობა
    # Draw.ErrorGraph(coError, "CO coefficients deviation from line (7-7)")
    Draw.ErrorGraph(noError, "NO coefficients deviation from line (7-7)")
    # Draw.ErrorGraph(no2Error, "NO2 error")
    # Draw.ErrorGraph(o3Error, "O3 error")
    # Draw.ErrorGraph(o3no2Error, "O3NO2 error")


"""
2 wutiani intervali avigo da davyo 4S da shemdeg S1 S2 S3 S4 da b1 da b2  da vnaxo ra gamova 

S1 maximumi  da minimumi
S2 minimumi da maximumi

----  1) 
pirdapir rom gavasashualo sensori ra cdomileba mijdeba am shemtxvevashi davtvalo da NEA s monacems gamovaklo 
ramden wertilshi aris 5% naklebi cdomileba ramdenshia 5-10% , 10-20% , 20-50%  50 - 75% , 75 % da zemot.


da calke cxrilad amovigo excelshi shevinaxo wertilebi 

---- 2) 
imis nacvlad rom gavaketot prediction pirdapir 1 wutiani intervalis ert wutiani intervalis koreqcia gavaketot
w1, w2 meqneba isev da eseni iqneba koreqciistvis ra unda iyos koreqcia 

s1 - Ssashualo , s2 - S_sashualo, s3 - S_sashualo, s4 - Ssashualo, b1, b2,  koreqcia rom iyos sensoris sashualo unda avigo  axla meqneba (b - Ssashualo) 

"""


"""

მისადაგება პირდაპირ წრფივი ფუნქციით. 
1) ზოგადი პროგრამის დაწერა თუ ჩვენ გვაქვს ერთ წუთიანი ინტერვალი, ერთ წუთიანი გავასაშუალოთ ნახევარზე და 2 ვეთი გვინდა რომ 
რაღაც საშუალო მივიღო 
S1' 1 | a = NEA  
S2' 1 | b = NEA

ეს გავაკეთო 2 წუთიანზე 4 წუთიანზე 16 იანზე ,32 იანზე და 60 იანზე


"""
