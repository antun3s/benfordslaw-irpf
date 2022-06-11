This tool use [Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law) to analise IRPF files (Brazilian Personal Income Tax)

I got to know Benford's Law in a documentary, and I found it curious how it works. There are several applications, such as analyzing fraud in the Personal Income Tax.
After wasting some time to calculate my Personal Income Tax, I decided to do an analysis applying Bendord's Law on it.

Benford's Law works for naturally occurring collections, and the larger the database the better. In the IRPF files it can vary, but as the intention was to execute the programming with something fun.

The tool's output displays in text format the frequency of the first digits, the number of analyzed values and how many of these are valid numbers (which do not start with zero). Then a PNG graphic is generated.

## How to use
### Preparation
This tool read de data in file `irpf.xml` , so the first step  is copy one or more IRPF XML to this file.
To see them use:

`find ~/ProgramasRFB/ -regextype sed -regex '.*/IRPF.*[0-9]\{11\}.*xml'`

If you you want to analyze one file, just copy to irpf.xml:

`cp /home/antunes/ProgramasRFB/IRPF2022/aplicacao/dados/YOUR-CPF/*.xml`

But, if you want to analyze all XML, joint all in same file:

`find ~/ProgramasRFB/ -regextype sed -regex '.*/IRPF.*[0-9]\{11\}.*xml' | awk '{print "cat " $1 " >> irpf.xml"}' | sh`

### Run ~~Forrest, Run!~~
`python3 benfordslaw-irpf.py`

### The output
**Chart**

This is example outup saved titled: `BenfordsLaw-analysis-on-IRPF.png`

![output chart BenfordsLaw analysis on IRPF ](https://github.com/antun3s/benfordslaw-irpf/blob/master/imgs/output-chart.png?raw=true)


**Text**

![output text BenfordsLaw analysis on IRPF ](https://github.com/antun3s/benfordslaw-irpf/blob/master/imgs/output-text.png?raw=true)