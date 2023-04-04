from src.extractors.txt_extractor import TXTExtractor
from os.path import join
import luigi, os, json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                contenido = txt_file.readlines()
                header = contenido[0].split(",")
                registros = contenido[1].split(";")

                txt_file.close()

                header[0] = "numero da fatura"
                header[7] = "Pais"

                registros.pop()
                
                for registro in registros:
                    entry = dict(zip(header, registro.split(",")))

                    result.append(
                        {
                            "description": entry["Descricao"],
                            "quantity": entry["montante"],
                            "price": entry["preco unitario"],
                            "total": float(entry["montante"]) * float(entry["preco unitario"]),
                            "invoice": entry["numero da fatura"],
                            "provider": entry["ID do Cliente"],
                            "country": entry["Pais"]
                        }    
                    )

        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "txt.json"))