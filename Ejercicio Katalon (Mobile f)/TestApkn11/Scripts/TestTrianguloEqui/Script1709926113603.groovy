import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

Mobile.startApplication('C:\\Users\\Usuario\\Desktop\\Curso Testing Master QA\\UTN QA profesional\\Modulo 2\\Unidad 1\\TestingAvanzadoApp11.apk', 
    true)

Mobile.tap(findTestObject('Object Repository/ObjTestTriangulo/android.widget.Button - Triangulo'), 0)

Mobile.setText(findTestObject('Object Repository/ObjTestTriangulo/android.widget.EditText'), ladoA, 0)

Mobile.setText(findTestObject('Object Repository/ObjTestTriangulo/android.widget.EditText (1)'), ladoB, 0)

Mobile.setText(findTestObject('Object Repository/ObjTestTriangulo/android.widget.EditText (2)'), ladoC, 0)

Mobile.tap(findTestObject('Object Repository/ObjTestTriangulo/android.widget.Button - Calcular'), 0)

Mobile.verifyElementText(findTestObject('Object Repository/ObjTestTriangulo/android.widget.EditText - S, es un tringulo'), 
    'Sí, es un triángulo')

Mobile.closeApplication()

