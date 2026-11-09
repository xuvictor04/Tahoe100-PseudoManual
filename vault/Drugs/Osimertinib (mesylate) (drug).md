---
drug: "Osimertinib (mesylate)"
type: "drug"
salt_base: "Osimertinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 551
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Osimertinib (mesylate)

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 15 / 551; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.47.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C10 | 2 / 0 | — | -0.21 | +0.2/-0.3/+0.0 | — |
| 0.5 µM | [[Plate 11]]:C10 | 15 / 0 | — | +0.34 | +0.4/+0.2/+0.4 | — |
| 5 µM | [[Plate 12]]:C10 | 456 / 95 | — | -0.62 | -2.1/-1.9/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[LRRC34]] 1.39× (z +3.5, 2/23 lines), [[LHFPL3]] 1.27× (z +3.1, 5/46 lines)

**0.5 µM** (15 genes, none with an alert; 12 shown): [[PCLO]] 1.46× (z +6.0, 27/33 lines), [[SLC43A2]] 1.39× (z +4.6, 12/44 lines), [[XPO1]] 1.26× (z +4.6, 31/48 lines), [[GNG2]] 1.33× (z +4.1, 8/26 lines), [[SLC16A14]] 1.41× (z +4.0, 9/31 lines), [[TRPM4]] 1.24× (z +3.8, 11/48 lines), [[SLC16A9]] 1.29× (z +3.7, 5/29 lines), [[DUSP15]] 1.65× (z +3.3, 6/26 lines), [[ZNF433]] 1.28× (z +3.2, 4/39 lines), [[HSPA4L]] 1.21× (z +3.2, 9/46 lines), [[RNF150]] 1.29× (z +3.1, 8/32 lines), [[STK32A]] 1.34× (z +3.1, 9/25 lines)

**5 µM** (456 genes, none with an alert; 12 shown): [[PCLO]] 4.01× (z +20.2, 32/33 lines), [[SLC43A2]] 3.50× (z +17.4, 43/44 lines), [[STK32A]] 3.94× (z +14.6, 24/24 lines), [[RNF150]] 2.88× (z +14.0, 30/32 lines), [[GNG2]] 2.66× (z +14.0, 25/26 lines), [[SLC44A2]] 2.37× (z +13.5, 36/44 lines), [[TRPM4]] 2.17× (z +13.4, 45/47 lines), [[NGFR]] 4.85× (z +13.2, 27/29 lines), [[ANO10]] 1.65× (z +12.5, 46/48 lines), [[XPO1]] 1.85× (z +12.3, 48/48 lines), [[HSPA4L]] 2.06× (z +12.1, 44/45 lines), [[CAPN5]] 2.36× (z +11.8, 38/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (95 genes, none with an alert; 12 shown): [[TJP1]] 0.831× (z -5.7, 24/48 lines), [[MTHFD1L]] 0.810× (z -5.1, 21/45 lines), [[CREB5]] 0.749× (z -5.1, 21/33 lines), [[KIAA0232]] 0.807× (z -4.9, 26/48 lines), [[ANAPC7]] 0.786× (z -4.6, 19/47 lines), [[SCLT1]] 0.798× (z -4.5, 28/48 lines), [[CTPS1]] 0.721× (z -4.5, 22/47 lines), [[NLK]] 0.813× (z -4.5, 26/48 lines), [[DBF4B]] 0.793× (z -4.4, 14/47 lines), [[WDR62]] 0.741× (z -4.4, 18/45 lines), [[PKP4]] 0.826× (z -4.4, 23/48 lines), [[FANCA]] 0.750× (z -4.3, 15/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 094]] (+6.8), [[Module 059]] (+3.9), [[Module 086]] (+3.2) | [[Module 194]] (-2.7), [[Module 006]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.41), [[C-33 A (line)]] (1.36), [[NCI-H460 (line)]] (1.26), [[SNU-423 (line)]] (1.22) · weakest: [[NCI-H661 (line)]] (0.454), [[NCI-H2030 (line)]] (0.614), [[NCI-H1573 (line)]] (0.657) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Almonertinib (hydrochloride) (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Selinexor (drug)]] (+0.64, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Docetaxel (Trihydrate) (drug)]] (+0.61, Microtubule inhibitor); [[Bicalutamide (drug)]] (+0.60, Androgen receptor antagonist); [[Almonertinib (mesylate) (drug)]] (+0.59, EGFR/ERBB inhibitor); [[Fingolimod (hydrochloride) (drug)]] (+0.56, unclear, ⚠ vector dose flagged: toxic); [[Sunitinib (drug)]] (+0.56, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Darolutamide (drug)]] (+0.55, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Entrectinib (drug)]] (+0.55, Other TK inhibitor); [[Saquinavir (drug)]] (+0.55, unclear); [[Methylprednisolone succinate (drug)]] (+0.51, Glucocorticoid receptor agonist); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.51, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BMPER]] | 5 µM | B | BMPER activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.11× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[HUNK]] | 5 µM | B | HUNK activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.14× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| [[HS3ST3B1]] | 5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.14× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ODF3B]] | 5 µM | B | ODF3B activity raises the cells' numbers under Osimertinib (mesylate) 5 µM (protects the cells) | lines that do not express ODF3B (13) vs lines expressing it (35) | the lines without ODF3B: 0.87× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity lowers the cells' numbers under Osimertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.09× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Osimertinib (mesylate)"
- `tables/drugdoses.parquet` — dd in 750, 751, 752
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
