---
drug: "Selinexor"
type: "drug"
salt_base: "Selinexor"
targets: "XPO1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6067
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Selinexor

*unclear (inhibitor/antagonist) · targets: XPO1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 932 / 2568 / 6067; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.78 / 0.82.
> Flags by dose: cell-cycle shift / cell-cycle shift / low cells (technical?); cell-cycle shift. ⚠ 0.05 µM: cell-cycle shift; 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H3 | 623 / 309 | — | +0.64 | -4.6/-5.5/-2.1 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 05]]:H3 | 1,516 / 1,052 | — | -0.11 | -7.1/-10.0/-0.9 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:H3 | 4,232 / 1,835 | 0.983 | -1.11 | -6.5/-12.2/+0.2 | ⚠ cell-cycle shift · low cells (technical?) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (623 genes, 284 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[PCLO]] 7.78× (z +32.9, 34/34 lines; cell-cycle shift (explains ~4% here)), [[RNF150]] 4.93× (z +21.1, 32/32 lines; cell-cycle shift (explains ~5% here)), [[STK32A]] 6.90× (z +20.6, 25/25 lines; cell-cycle shift (explains ~7% here)), [[NGFR]] 11.2× (z +20.1, 29/29 lines; cell-cycle shift (explains ~0% here)), [[SLC43A2]] 4.12× (z +19.7, 44/44 lines; cell-cycle shift (explains ~4% here)), [[TRPM4]] 2.93× (z +18.6, 47/48 lines; cell-cycle shift (explains ~7% here)), [[SLC44A2]] 3.22× (z +18.3, 39/44 lines; cell-cycle shift (explains ~5% here)), [[HSPA4L]] 2.86× (z +17.5, 46/46 lines; cell-cycle shift (explains ~0% here)), [[GNG2]] 3.34× (z +17.2, 25/26 lines; cell-cycle shift (explains ~0% here)), [[XPO1]] 2.19× (z +15.7, 48/49 lines; cell-cycle shift (explains ~0% here)), [[CAPN5]] 3.09× (z +15.5, 41/44 lines; cell-cycle shift (explains ~11% here)), [[DIXDC1]] 2.15× (z +15.5, 43/48 lines; cell-cycle shift (explains ~2% here))

**0.5 µM** (1516 genes, 816 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[PCLO]] 6.60× (z +30.3, 32/33 lines; cell-cycle shift (explains ~7% here)), [[RNF150]] 4.84× (z +20.9, 32/32 lines; cell-cycle shift (explains ~9% here)), [[NGFR]] 11.7× (z +20.5, 28/29 lines; cell-cycle shift (explains ~0% here)), [[HSPA4L]] 3.17× (z +19.3, 45/46 lines; cell-cycle shift (explains ~0% here)), [[SLC44A2]] 3.23× (z +18.3, 39/44 lines; cell-cycle shift (explains ~8% here)), [[SLC43A2]] 3.43× (z +17.1, 39/44 lines; cell-cycle shift (explains ~9% here)), [[STK32A]] 4.46× (z +15.9, 23/24 lines; cell-cycle shift (explains ~16% here)), [[NUDT16]] 2.64× (z +15.7, 42/47 lines; cell-cycle shift (explains ~7% here)), [[TRPM4]] 2.44× (z +15.4, 44/48 lines; cell-cycle shift (explains ~16% here)), [[XPO1]] 2.14× (z +15.2, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PRTG]] 2.17× (z +14.3, 30/34 lines; cell-cycle shift (explains ~15% here)), [[ZNF433]] 2.98× (z +14.2, 32/37 lines; cell-cycle shift (explains ~0% here))

**5 µM** (4232 genes, 1,570 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[PCLO]] 5.39× (z +38.2, 32/33 lines; cell-cycle shift (explains ~7% here)), [[SLC44A2]] 3.78× (z +29.3, 39/44 lines; cell-cycle shift (explains ~5% here)), [[RNF150]] 4.65× (z +28.8, 30/32 lines; cell-cycle shift (explains ~8% here)), [[HSPA4L]] 3.01× (z +26.0, 46/46 lines; cell-cycle shift (explains ~0% here)), [[NGFR]] 11.3× (z +25.9, 29/29 lines; cell-cycle shift (explains ~1% here)), [[STK32A]] 4.50× (z +22.7, 23/24 lines; cell-cycle shift (explains ~13% here)), [[ZNF441]] 3.04× (z +22.0, 37/41 lines; cell-cycle shift (explains ~3% here)), [[GNG2]] 2.97× (z +22.0, 26/26 lines; cell-cycle shift (explains ~0% here)), [[SLC16A14]] 3.71× (z +21.7, 30/31 lines; cell-cycle shift (explains ~0% here)), [[XPO1]] 2.12× (z +21.2, 47/48 lines; cell-cycle shift (explains ~0% here)), [[NUDT16]] 2.57× (z +21.1, 43/48 lines; cell-cycle shift (explains ~7% here)), [[SLC43A2]] 2.92× (z +21.1, 39/44 lines; cell-cycle shift (explains ~10% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (309 genes, 273 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[NDC80]] ⚠ 0.597× (z -8.0, 38/45 lines; cell-cycle shift, explains ~62% of this change), [[KIF4A]] ⚠ 0.634× (z -8.0, 38/47 lines; cell-cycle shift, explains ~63% of this change), [[CCNF]] ⚠ 0.620× (z -7.8, 31/48 lines; cell-cycle shift, explains ~54% of this change), [[CKAP2L]] ⚠ 0.593× (z -7.6, 40/48 lines; cell-cycle shift, explains ~59% of this change), [[WDR62]] ⚠ 0.600× (z -7.5, 35/46 lines; cell-cycle shift, explains ~48% of this change), [[ENSG00000284906]] ⚠ 0.708× (z -7.5, 37/49 lines; cell-cycle shift, explains ~43% of this change), [[NCAPH]] ⚠ 0.616× (z -7.5, 40/47 lines; cell-cycle shift, explains ~67% of this change), [[KIF18B]] ⚠ 0.552× (z -7.5, 42/46 lines; cell-cycle shift, explains ~57% of this change), [[SGO2]] ⚠ 0.627× (z -7.4, 40/48 lines; cell-cycle shift, explains ~64% of this change), [[KNL1]] ⚠ 0.645× (z -7.4, 40/47 lines; cell-cycle shift, explains ~66% of this change), [[TACC3]] ⚠ 0.657× (z -7.3, 37/48 lines; cell-cycle shift, explains ~69% of this change), [[KIF23]] ⚠ 0.635× (z -7.1, 38/47 lines; cell-cycle shift, explains ~69% of this change), [[TUBGCP5]] 0.748× (z -6.4, 31/48 lines; cell-cycle shift (explains ~0% here)), [[KIAA0232]] 0.770× (z -6.0, 38/49 lines; cell-cycle shift (explains ~0% here)), [[FOXK2]] 0.772× (z -5.2, 30/49 lines; cell-cycle shift (explains ~4% here)), [[URB2]] 0.688× (z -5.0, 20/48 lines; cell-cycle shift (explains ~21% here)), [[MARS1]] 0.747× (z -5.0, 32/49 lines; cell-cycle shift (explains ~9% here)), [[PLXNA2]] 0.660× (z -4.8, 14/33 lines; cell-cycle shift (explains ~0% here)), [[PPM1B]] 0.791× (z -4.8, 27/49 lines; cell-cycle shift (explains ~7% here)), [[GCLM]] 0.717× (z -4.7, 30/47 lines; cell-cycle shift (explains ~19% here)), [[ATP6V0A2]] 0.783× (z -4.6, 15/48 lines; cell-cycle shift (explains ~9% here)), [[TRAPPC13]] 0.791× (z -4.6, 16/48 lines; cell-cycle shift (explains ~0% here)), [[PHF12]] 0.822× (z -4.3, 15/49 lines; cell-cycle shift (explains ~0% here)), [[TSEN15]] 0.763× (z -4.2, 18/48 lines; cell-cycle shift (explains ~0% here))

**0.5 µM** (1052 genes, 557 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[ENSG00000284906]] ⚠ 0.476× (z -16.2, 47/48 lines; cell-cycle shift, explains ~36% of this change), [[KIF4A]] ⚠ 0.432× (z -14.7, 46/47 lines; cell-cycle shift, explains ~63% of this change), [[SGO2]] ⚠ 0.406× (z -14.3, 47/48 lines; cell-cycle shift, explains ~60% of this change), [[NCAPH]] ⚠ 0.398× (z -14.3, 40/47 lines; cell-cycle shift, explains ~61% of this change), [[KIF18B]] ⚠ 0.336× (z -13.8, 45/46 lines; cell-cycle shift, explains ~56% of this change), [[TACC3]] ⚠ 0.461× (z -13.5, 41/48 lines; cell-cycle shift, explains ~67% of this change), [[KIF14]] ⚠ 0.460× (z -13.2, 45/47 lines; cell-cycle shift, explains ~60% of this change), [[CCNF]] ⚠ 0.450× (z -13.1, 36/48 lines; cell-cycle shift, explains ~59% of this change), [[WDR62]] ⚠ 0.417× (z -12.9, 39/45 lines; cell-cycle shift, explains ~44% of this change), [[DIAPH3]] ⚠ 0.548× (z -12.8, 39/45 lines; cell-cycle shift, explains ~56% of this change), [[NSD2]] ⚠ 0.637× (z -12.8, 45/48 lines; cell-cycle shift, explains ~28% of this change), [[NDC80]] ⚠ 0.444× (z -12.6, 39/45 lines; cell-cycle shift, explains ~72% of this change), [[POC1A]] 0.480× (z -12.5, 36/47 lines; cell-cycle shift (explains ~16% here)), [[IQGAP3]] 0.394× (z -11.1, 42/46 lines; cell-cycle shift (explains ~24% here)), [[MAPKAPK2]] 0.651× (z -9.8, 41/48 lines; cell-cycle shift (explains ~18% here)), [[EHD4]] 0.609× (z -9.6, 40/48 lines; cell-cycle shift (explains ~7% here)), [[KIAA0232]] 0.668× (z -9.2, 43/48 lines; cell-cycle shift (explains ~0% here)), [[TJP1]] 0.736× (z -9.2, 36/48 lines; cell-cycle shift (explains ~13% here)), [[DLEU2]] 0.721× (z -9.1, 37/48 lines; cell-cycle shift (explains ~12% here)), [[GPT2]] 0.571× (z -8.8, 36/46 lines; cell-cycle shift (explains ~0% here)), [[MLXIP]] 0.722× (z -8.7, 35/48 lines; cell-cycle shift (explains ~5% here)), [[MAP3K3]] 0.697× (z -8.1, 30/48 lines; cell-cycle shift (explains ~0% here)), [[MTHFD1L]] 0.719× (z -8.1, 33/45 lines; cell-cycle shift (explains ~0% here)), [[PLXNA2]] 0.507× (z -7.8, 25/31 lines; cell-cycle shift (explains ~0% here))

**5 µM** (1835 genes, 677 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 19 shown): [[ENSG00000284906]] ⚠ 0.460× (z -22.1, 45/48 lines; cell-cycle shift, explains ~31% of this change), [[NCAPH]] ⚠ 0.369× (z -21.9, 42/47 lines; cell-cycle shift, explains ~46% of this change), [[EHD4]] 0.484× (z -21.7, 46/48 lines; cell-cycle shift (explains ~2% here)), [[NSD2]] 0.592× (z -21.0, 47/48 lines; cell-cycle shift (explains ~20% here)), [[NDE1]] 0.564× (z -19.0, 44/48 lines; cell-cycle shift (explains ~17% here)), [[ZCCHC2]] 0.535× (z -18.6, 45/48 lines; cell-cycle shift (explains ~1% here)), [[KIF18B]] ⚠ 0.360× (z -17.9, 43/46 lines; cell-cycle shift, explains ~52% of this change), [[MTHFD1L]] 0.595× (z -17.9, 42/45 lines; cell-cycle shift (explains ~0% here)), [[KIF4A]] ⚠ 0.476× (z -17.8, 44/47 lines; cell-cycle shift, explains ~62% of this change), [[WDR62]] ⚠ 0.430× (z -17.6, 41/46 lines; cell-cycle shift, explains ~32% of this change), [[CKAP2L]] ⚠ 0.422× (z -17.2, 47/48 lines; cell-cycle shift, explains ~56% of this change), [[KIFC1]] ⚠ 0.354× (z -17.0, 43/47 lines; cell-cycle shift, explains ~39% of this change), [[POC1A]] 0.499× (z -16.7, 41/48 lines; cell-cycle shift (explains ~11% here)), [[IQGAP3]] 0.381× (z -16.3, 42/46 lines; cell-cycle shift (explains ~21% here)), [[TJP1]] 0.688× (z -16.3, 41/48 lines; cell-cycle shift (explains ~13% here)), [[TEAD4]] 0.549× (z -16.2, 41/45 lines; cell-cycle shift (explains ~0% here)), [[DLEU2]] 0.672× (z -15.8, 38/48 lines; cell-cycle shift (explains ~8% here)), [[DNM2]] 0.719× (z -15.6, 43/48 lines; cell-cycle shift (explains ~7% here)), [[PNPT1]] 0.452× (z -15.5, 38/47 lines; cell-cycle shift (explains ~6% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 094]] (+9.3), [[Module 059]] (+2.9), [[Module 122]] (+2.5) | [[Module 006]] (-3.6), [[Module 022]] (-3.4), [[Module 194]] (-2.8) |
| 0.5 µM | [[Module 094]] (+9.3), [[Module 064]] (+4.6), [[Module 122]] (+4.0) | [[Module 006]] (-6.6), [[Module 022]] (-5.6), [[Module 067]] (-5.0) |
| 5 µM | [[Module 094]] (+13.7), [[Module 182]] (+8.1), [[Module 135]] (+8.0) | [[Module 006]] (-7.4), [[Module 160]] (-7.4), [[Module 052]] (-6.9) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[LS 180 (line)]] (1.40), [[RPMI-7951 (line)]] (1.36), [[HT-29 (line)]] (1.34), [[NCI-H460 (line)]] (1.31) · weakest: [[NCI-H661 (line)]] (0.557), [[AN3 CA (line)]] (0.674), [[A-427 (line)]] (0.696) |
| 0.5 µM | — | [[H4 (line)]] (1.50), [[LS 180 (line)]] (1.45), [[SNU-1 (line)]] (1.31), [[LOX-IMVI (line)]] (1.30) · weakest: [[NCI-H661 (line)]] (0.527), [[SHP-77 (line)]] (0.553), [[AN3 CA (line)]] (0.644) |
| 5 µM | [[SK-MEL-2 (line)]] (-5.8), [[A-427 (line)]] (-4.8), [[J82 (line)]] (-4.5), [[A549 (line)]] (-4.5), [[Panc 03.27 (line)]] (-4.0) | [[A498 (line)]] (1.24), [[J82 (line)]] (1.23), [[SNU-1 (line)]] (1.20), [[A549 (line)]] (1.19) · weakest: [[NCI-H661 (line)]] (0.420), [[SHP-77 (line)]] (0.563), [[HEC-1-A (line)]] (0.592) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Osimertinib (mesylate) (drug)]] (+0.64, EGFR/ERBB inhibitor); [[IQ 1 (drug)]] (+0.50, unclear); [[Ixazomib (drug)]] (+0.45, Proteasome inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.43, Multi-TK inhibitor); [[Ponatinib (drug)]] (+0.42, Multi-TK inhibitor); [[Topotecan (hydrochloride) (drug)]] (+0.41, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Amsacrine (drug)]] (+0.39, DNA synthesis/repair inhibitor); [[Belzutifan (drug)]] (+0.35, unclear); [[AZD-8055 (drug)]] (+0.35, MTOR inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ZNF404]] | 5 µM | B | ZNF404 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express ZNF404 (14) vs lines expressing it (34) | the lines without ZNF404: 1.32× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[LINC01579]] | 5 µM | B | LINC01579 activity raises the cells' numbers under Selinexor 5 µM (protects the cells) | lines that do not express LINC01579 (13) vs lines expressing it (35) | the lines without LINC01579: 0.80× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |
| [[MSRB3-AS1]] | 0.5 µM | B | MSRB3-AS1 activity lowers the cells' numbers under Selinexor 0.5 µM (makes them more sensitive) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 1.23× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[THEM4]] | 5 µM | B | THEM4 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express THEM4 (5) vs lines expressing it (43) | the lines without THEM4: 1.41× the cells of the other lines | 0.087 | ⚠ across organs; also absent: PIP4P2, CBR1 |
| [[ENSG00000268119]] | 0.5 µM | B | ENSG00000268119 activity lowers the cells' numbers under Selinexor 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000268119 (31) vs lines expressing it (17) | the lines without ENSG00000268119: 1.16× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ANOS1, ZNF732, ENSG00000291130 |
| [[NPR3]] | 0.5 µM | B | NPR3 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express NPR3 (7) vs lines expressing it (41) | the lines without NPR3: 0.90× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ENSG00000267174]] | 0.5 µM | C | ENSG00000267174 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express ENSG00000267174 (3) vs lines expressing it (45) | the lines without ENSG00000267174: 0.72× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: FSCN2, ENSG00000229848, ZFP36; maybe low, not absent |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.29× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[STX1A]] | 0.5 µM | C | STX1A activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.72× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[LITAF]] | 0.5 µM | C | LITAF activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.74× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| [[ENSG00000259539]] | 0.5 µM | C | ENSG00000259539 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express ENSG00000259539 (3) vs lines expressing it (45) | the lines without ENSG00000259539: 0.75× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: PNCK, MAPK11, ENSG00000267174; maybe low, not absent |
| [[LGI4]] | 5 µM | C | LGI4 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.41× the cells of the other lines | 0.088 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| [[TMEM216]] | 0.5 µM | C | TMEM216 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.80× the cells of the other lines | 0.093 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| [[H1-0]] | 0.5 µM | C | H1-0 activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express H1-0 (5) vs lines expressing it (43) | the lines without H1-0: 0.79× the cells of the other lines | 0.094 | ⚠ tissue-confounded; across organs; also absent: TMEM216, TACC2, FER1L4 |
| [[NOMO2]] | 0.5 µM | C | NOMO2's natural level raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | NOMO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Selinexor"
- `tables/drugdoses.parquet` — dd in 940, 941, 942
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
