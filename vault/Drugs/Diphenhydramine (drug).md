---
drug: "Diphenhydramine"
type: "drug"
salt_base: "Diphenhydramine"
targets: "HRH1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 111
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Diphenhydramine

*unclear (inhibitor/antagonist) · targets: HRH1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 69 / 111 / 40; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.01 / -0.23.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C10 | 1 / 68 | — | +0.53 | +0.0/+0.1/-1.3 | — |
| 0.5 µM | [[Plate 08]]:C10 | 35 / 76 | — | +0.58 | +1.4/+0.7/-1.1 | — |
| 5 µM | [[Plate 09]]:C10 | 22 / 18 | — | +0.19 | +1.2/+0.4/+0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[IPPK]] 1.20× (z +2.8, 2/48 lines)

**0.5 µM** (35 genes, none with an alert; 12 shown): [[EVA1A-AS]] 1.85× (z +4.1, 10/25 lines), [[CD44]] 1.21× (z +3.9, 18/33 lines), [[ENC1]] 1.47× (z +3.8, 25/43 lines), [[ZRANB3]] 1.29× (z +3.8, 21/48 lines), [[IRS1]] 1.33× (z +3.6, 14/42 lines), [[ENSG00000283415]] 1.30× (z +3.5, 11/34 lines), [[SPANXA2-OT1]] 1.39× (z +3.4, 13/26 lines), [[TRIM9]] 1.26× (z +3.4, 11/32 lines), [[SYTL2]] 1.30× (z +3.4, 13/41 lines), [[WFDC3]] 1.37× (z +3.3, 6/32 lines), [[DCBLD2]] 1.24× (z +3.3, 23/39 lines), [[CCN2]] 1.51× (z +3.3, 4/31 lines)

**5 µM** (22 genes, none with an alert; 12 shown): [[UBE2N]] 1.24× (z +4.4, 25/48 lines), [[AZIN1]] 1.24× (z +3.3, 23/48 lines), [[HSPA1B]] 1.48× (z +3.3, 16/48 lines), [[CD83]] 1.50× (z +3.3, 13/44 lines), [[LAMTOR3]] 1.27× (z +3.3, 9/48 lines), [[USP3]] 1.35× (z +3.3, 26/48 lines), [[ENSG00000249328]] 1.35× (z +3.3, 4/44 lines), [[HSPA1A]] 1.64× (z +3.2, 15/34 lines), [[KHDRBS3]] 1.26× (z +3.2, 10/37 lines), [[GGA2]] 1.22× (z +3.2, 18/48 lines), [[FUS]] 1.22× (z +3.1, 22/48 lines), [[GNA13]] 1.25× (z +3.1, 22/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (68 genes, none with an alert; 12 shown): [[ACSS3]] 0.606× (z -4.7, 2/16 lines), [[MAL2]] 0.755× (z -4.7, 0/17 lines), [[PAX3]] 0.593× (z -4.6, 0/10 lines), [[LINC02864]] 0.686× (z -4.5, 0/12 lines), [[CSF2RA]] 0.644× (z -4.5, 2/19 lines), [[MLANA]] 0.536× (z -4.1, 6/39 lines), [[RAMP1]] 0.668× (z -4.1, 2/28 lines), [[FCRLA]] 0.402× (z -4.1, 0/6 lines), [[EDARADD]] 0.735× (z -4.1, 0/21 lines), [[GALNT13]] 0.756× (z -4.1, 0/17 lines), [[LINC00491]] 0.564× (z -4.0, 1/12 lines), [[TOX3]] 0.701× (z -4.0, 0/17 lines)

**0.5 µM** (76 genes, none with an alert; 12 shown): [[PREPL]] 0.762× (z -4.4, 27/48 lines), [[RAB21]] 0.806× (z -4.3, 27/48 lines), [[NDUFV2]] 0.811× (z -4.2, 22/48 lines), [[LRRFIP2]] 0.807× (z -4.2, 27/48 lines), [[ADAM20]] 0.702× (z -4.1, 23/48 lines), [[KLHL24]] 0.774× (z -4.1, 27/48 lines), [[MAX]] 0.783× (z -3.9, 29/48 lines), [[LINC02680]] 0.651× (z -3.9, 22/48 lines), [[SARNP]] 0.830× (z -3.8, 21/48 lines), [[RAB18]] 0.768× (z -3.7, 32/48 lines), [[YPEL2]] 0.802× (z -3.7, 13/45 lines), [[JMY]] 0.793× (z -3.7, 19/47 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[TOX3]] 0.705× (z -4.0, 1/17 lines), [[FTH1]] 0.672× (z -3.9, 41/44 lines), [[IDH1]] 0.763× (z -3.7, 10/48 lines), [[ZNF382]] 0.718× (z -3.6, 4/28 lines), [[TLCD4-RWDD3]] 0.712× (z -3.5, 3/32 lines), [[OLFM1]] 0.674× (z -3.5, 4/19 lines), [[TIGD7]] 0.805× (z -3.5, 3/38 lines), [[OR9Q1]] 0.677× (z -3.5, 7/20 lines), [[ENSG00000248734]] 0.707× (z -3.5, 10/44 lines), [[RAB33B-AS1]] 0.817× (z -3.1, 14/48 lines), [[TBC1D8B]] 0.828× (z -3.1, 10/42 lines), [[TMC4]] 0.758× (z -3.1, 2/20 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 048]] (-2.5), [[Module 024]] (-2.4), [[Module 054]] (-2.4) |
| 0.5 µM | — | [[Module 179]] (-2.6), [[Module 207]] (-2.6), [[Module 182]] (-2.6) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[RKO (line)]] (1.49), [[C-33 A (line)]] (1.43), [[CHP-212 (line)]] (1.40), [[SNU-1 (line)]] (1.37) · weakest: [[NCI-H1573 (line)]] (0.488), [[HOP62 (line)]] (0.555), [[SK-MEL-2 (line)]] (0.617) |
| 0.5 µM | — | [[CHP-212 (line)]] (1.56), [[hTERT-HPNE (line)]] (1.37), [[HOP62 (line)]] (1.31), [[SW 1271 (line)]] (1.28) · weakest: [[BT-474 (line)]] (0.343), [[AN3 CA (line)]] (0.358), [[SHP-77 (line)]] (0.452) |
| 5 µM | — | [[A498 (line)]] (1.60), [[HEC-1-A (line)]] (1.53), [[SNU-1 (line)]] (1.46), [[LOX-IMVI (line)]] (1.43) · weakest: [[AN3 CA (line)]] (0.280), [[KATO III (line)]] (0.295), [[A-427 (line)]] (0.361) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Tirabrutinib (drug)]] (+0.93, Other TK inhibitor); [[Esmolol (hydrochloride) (drug)]] (+0.91, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.88, unclear); [[Busulfan (drug)]] (+0.87, DNA synthesis/repair inhibitor); [[Apalutamide (drug)]] (+0.86, Androgen receptor antagonist); [[Larotrectinib (drug)]] (+0.85, Other TK inhibitor); [[Megestrol (drug)]] (+0.81, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Olanzapine (drug)]] (+0.81, unclear, ⚠ only 5 significant genes); [[Palmatine (chloride) (drug)]] (+0.80, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.79, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Diphenhydramine"
- `tables/drugdoses.parquet` — dd in 365, 366, 367
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
