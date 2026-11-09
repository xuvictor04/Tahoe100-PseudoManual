---
drug: "Saquinavir"
type: "drug"
salt_base: "Saquinavir"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 232
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Saquinavir

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 63 / 58 / 232; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.30 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D4 | 60 / 3 | — | -0.70 | -2.2/-1.1/-0.6 | — |
| 0.5 µM | [[Plate 05]]:D4 | 57 / 1 | — | -0.54 | -0.7/-0.5/-0.1 | — |
| 5 µM | [[Plate 14]]:D4 | 226 / 6 | 0.638 | -0.77 | -1.2/-0.7/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (60 genes, none with an alert; 12 shown): [[ECHDC3]] 1.68× (z +4.4, 4/19 lines), [[HAGLR]] 1.47× (z +4.1, 1/19 lines), [[ENSG00000250137]] 1.56× (z +4.0, 1/14 lines), [[LINC01440]] 1.72× (z +3.9, 0/4 lines), [[ENSG00000232754]] 1.40× (z +3.9, 7/38 lines), [[TMEM139]] 1.62× (z +3.8, 1/13 lines), [[LINC02036]] 1.54× (z +3.6, 0/17 lines), [[ENSG00000286010]] 1.96× (z +3.6, 0/2 lines), [[ENSG00000267581]] 1.35× (z +3.5, 1/25 lines), [[VSIR]] 1.29× (z +3.5, 2/28 lines), [[LINC03046]] 1.43× (z +3.5, 1/10 lines), [[HLCS-AS1]] 1.43× (z +3.4, 4/28 lines)

**0.5 µM** (57 genes, none with an alert; 12 shown): [[NLRP2]] 1.56× (z +5.4, 1/15 lines), [[ARHGEF34P]] 1.40× (z +4.6, 10/24 lines), [[FAM219B]] 1.34× (z +4.4, 12/44 lines), [[EXOC8]] 1.22× (z +4.0, 11/46 lines), [[NPIPA1]] 1.41× (z +4.0, 8/39 lines), [[SLC4A11]] 1.61× (z +3.9, 2/16 lines), [[GTPBP3]] 1.29× (z +3.8, 11/44 lines), [[LOXL4]] 1.56× (z +3.8, 6/15 lines), [[UNC80]] 1.69× (z +3.8, 1/7 lines), [[NEURL4]] 1.41× (z +3.6, 7/41 lines), [[PHETA1]] 1.50× (z +3.6, 4/27 lines), [[NFS1]] 1.23× (z +3.6, 6/46 lines)

**5 µM** (226 genes, none with an alert; 12 shown): [[MAGEA10]] 1.91× (z +5.5, 3/6 lines), [[GUCY1B1]] 1.46× (z +4.7, 2/17 lines), [[CCNYL2-1]] 1.58× (z +4.6, 2/11 lines), [[ENSG00000287045]] 1.30× (z +4.6, 6/40 lines), [[MIR4307HG]] 1.58× (z +4.4, 1/11 lines), [[BARX1]] 1.79× (z +4.4, 2/14 lines), [[LRRC4B]] 1.40× (z +4.4, 3/17 lines), [[HSD17B7]] 1.25× (z +4.4, 8/45 lines), [[LINC02967]] 1.67× (z +4.3, 3/11 lines), [[XKR4]] 1.42× (z +4.2, 0/18 lines), [[HS6ST3]] 1.30× (z +4.2, 5/26 lines), [[LARGE2]] 1.47× (z +4.1, 0/14 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[RNF25]] 0.737× (z -3.7, 14/43 lines), [[ARHGAP11A]] 0.812× (z -3.4, 14/46 lines), [[KIF23]] 0.819× (z -3.1, 12/47 lines)

**0.5 µM** (1 gene, none with an alert): [[ZNF815P]] 0.703× (z -3.2, 6/30 lines)

**5 µM** (6 genes, none with an alert): [[TEAD4]] 0.823× (z -5.2, 19/45 lines), [[ENSG00000260658]] 0.796× (z -4.4, 15/22 lines), [[TUBB3]] 0.796× (z -3.8, 14/42 lines), [[CEP72]] 0.820× (z -3.6, 15/48 lines), [[ENSG00000285080]] 0.785× (z -3.5, 13/45 lines), [[H3C12]] 0.780× (z -3.1, 14/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (2.57), [[CHP-212 (line)]] (2.23), [[SW 1271 (line)]] (1.55), [[AN3 CA (line)]] (1.53) · weakest: [[NCI-H2030 (line)]] (0.120), [[SW1417 (line)]] (0.143), [[PANC-1 (line)]] (0.270) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.78), [[COLO 205 (line)]] (1.66), [[SW 1271 (line)]] (1.56), [[CHP-212 (line)]] (1.51) · weakest: [[SW480 (line)]] (0.0794), [[A-427 (line)]] (0.307), [[NCI-H1792 (line)]] (0.313) |
| 5 µM | — | [[SW 1088 (line)]] (2.00), [[SW 1271 (line)]] (1.98), [[CHP-212 (line)]] (1.70), [[SNU-1 (line)]] (1.61) · weakest: [[SW480 (line)]] (0.221), [[PANC-1 (line)]] (0.315), [[NCI-H2347 (line)]] (0.317) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Imiquimod (hydrochloride) (drug)]] (+0.70, unclear, ⚠ vector dose flagged: toxic); [[18β-Glycyrrhetinic acid (drug)]] (+0.67, unclear); [[Sunitinib (drug)]] (+0.67, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Almonertinib (hydrochloride) (drug)]] (+0.66, EGFR/ERBB inhibitor); [[Methylprednisolone succinate (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Tolmetin (drug)]] (+0.66, Cyclooxygenase inhibitor, ⚠ only 4 significant genes); [[Tranilast (drug)]] (+0.65, unclear, ⚠ only 6 significant genes); [[Bendamustine (drug)]] (+0.65, DNA synthesis/repair inhibitor); [[Bicalutamide (drug)]] (+0.65, Androgen receptor antagonist); [[Canagliflozin (hemihydrate) (drug)]] (+0.64, Glucose transporter inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.63, Microtubule inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.61, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Saquinavir"
- `tables/drugdoses.parquet` — dd in 937, 938, 939
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
