import config, analytics
import sys

if __name__ == '__main__':
        try:        
            research = analytics.Research(config.file_dir + sys.argv[1])
            data = research.file_reader()
            calculations = research.Calculations(data)
            heads_tails = calculations.counts()
            fractions = calculations.fractions(heads_tails)

            analyt = analytics.Analytics(data)
            forecast = analyt.predict_random(config.num_of_steps)
            report = analyt.get_report(config.template, forecast)
            analyt.save_file(report, config.file_name_output, config.file_extension_output)
            print('done', config.file_name_output+'.'+config.file_extension_output)
        except Exception as e:
              print('exception:', e)