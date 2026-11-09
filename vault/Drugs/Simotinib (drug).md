---
drug: "Simotinib"
type: "drug"
salt_base: "Simotinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 339
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Simotinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 21 / 10 / 339; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.10.
> Flags by dose: - / - / toxic. ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D10 | 5 / 16 | — | -0.14 | +0.4/+0.8/+0.5 | — |
| 0.5 µM | [[Plate 08]]:D10 | 9 / 1 | — | -0.64 | +0.7/+0.0/-0.7 | — |
| 5 µM | [[Plate 09]]:D10 | 331 / 8 | — | -1.11 | +1.2/+1.0/+1.0 | ⚠ toxic |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[TPPP]] 1.66× (z +5.3, 13/39 lines), [[MAN1B1]] 1.23× (z +3.4, 9/47 lines), [[ZNF581]] 1.26× (z +3.2, 9/46 lines), [[TMEM79]] 1.28× (z +2.8, 4/39 lines), [[SLC2A8]] 1.26× (z +2.8, 2/38 lines)

**0.5 µM** (9 genes, none with an alert): [[ENSG00000239498]] 1.46× (z +3.9, 8/27 lines), [[SLC25A10]] 1.35× (z +3.5, 7/45 lines), [[CALCRL]] 1.41× (z +3.3, 5/27 lines), [[ST6GALNAC3]] 1.32× (z +3.3, 8/29 lines), [[BEST1]] 1.39× (z +3.2, 13/45 lines), [[CDH8]] 1.36× (z +3.0, 2/17 lines), [[AACSP1]] 1.42× (z +2.9, 0/14 lines), [[ENSG00000284879]] 1.27× (z +2.9, 10/44 lines), [[SGO1-AS1]] 1.24× (z +2.7, 7/46 lines)

**5 µM** (331 genes, 331 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ENSG00000232692]] ⚠ 1.83× (z +4.9, 4/15 lines), [[ENSG00000203635]] ⚠ 2.34× (z +4.7, 2/11 lines), [[ELAPOR1]] ⚠ 1.63× (z +4.6, 3/17 lines), [[GAB3]] ⚠ 1.63× (z +4.5, 2/16 lines), [[HHIPL2]] ⚠ 1.79× (z +4.5, 2/10 lines), [[COL15A1]] ⚠ 1.73× (z +4.5, 3/13 lines), [[ENSG00000255102]] ⚠ 1.70× (z +4.4, 3/17 lines), [[DSC3]] ⚠ 1.54× (z +4.4, 2/14 lines), [[TNK1]] ⚠ 1.54× (z +4.3, 1/18 lines), [[PTCH2]] ⚠ 1.56× (z +4.3, 9/23 lines), [[CHDH]] ⚠ 1.50× (z +4.3, 0/19 lines), [[DCLK1]] ⚠ 1.33× (z +4.3, 4/27 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[BEST1]] 0.492× (z -5.2, 20/43 lines), [[ASMTL-AS1]] 0.567× (z -4.4, 26/46 lines), [[GTF2IP4]] 0.674× (z -4.2, 11/38 lines), [[ENSG00000291228]] 0.702× (z -4.2, 21/45 lines), [[FUT10]] 0.801× (z -3.9, 14/46 lines), [[ENSG00000291283]] 0.702× (z -3.8, 14/35 lines), [[FAM193B]] 0.832× (z -3.6, 22/48 lines), [[CAMSAP1-DT]] 0.732× (z -3.6, 18/44 lines), [[KPNA1]] 0.813× (z -3.3, 22/48 lines), [[POLR2J3-1]] 0.716× (z -3.2, 14/42 lines), [[NSFP1]] 0.787× (z -3.2, 6/38 lines), [[NPIPB14P]] 0.793× (z -3.2, 16/46 lines)

**0.5 µM** (1 gene, none with an alert): [[LINC01019]] 0.774× (z -3.6, 5/46 lines)

**5 µM** (8 genes, 8 with an alert ⚠; the drug-dose carries ⚠ toxic): [[ATP8B3]] ⚠ 0.735× (z -3.5, 10/33 lines), [[GLB1L2]] ⚠ 0.745× (z -3.5, 6/24 lines), [[PMM2]] ⚠ 0.805× (z -3.4, 23/47 lines), [[KCNQ1OT1]] ⚠ 0.813× (z -3.1, 20/41 lines), [[IQANK1]] ⚠ 0.821× (z -2.9, 5/25 lines), [[ALDH18A1]] ⚠ 0.825× (z -2.8, 16/47 lines), [[MOV10]] ⚠ 0.817× (z -2.8, 12/46 lines), [[PARP12]] ⚠ 0.817× (z -2.7, 16/45 lines)

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
| 0.05 µM | — | [[SNU-1 (line)]] (1.93), [[SW1417 (line)]] (1.88), [[HepG2_C3A (line)]] (1.72), [[CFPAC-1 (line)]] (1.54) · weakest: [[SW 1088 (line)]] (-0.580), [[CHP-212 (line)]] (0.319), [[C-33 A (line)]] (0.510) |
| 0.5 µM | [[SW 1088 (line)]] (-3.3) | — |
| 5 µM | — | [[AN3 CA (line)]] (1.82), [[CHP-212 (line)]] (1.60), [[C-33 A (line)]] (1.60), [[HepG2_C3A (line)]] (1.51) · weakest: [[SW480 (line)]] (0.198), [[NCI-H1573 (line)]] (0.243), [[KATO III (line)]] (0.368) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Drospirenone (drug)]] (+0.72, unclear); [[Bendamustine (drug)]] (+0.71, DNA synthesis/repair inhibitor); [[Bicalutamide (drug)]] (+0.65, Androgen receptor antagonist); [[Saquinavir (drug)]] (+0.63, unclear); [[Sunitinib (drug)]] (+0.62, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Vitamin K4 (drug)]] (+0.62, unclear); [[Imiquimod (hydrochloride) (drug)]] (+0.62, unclear, ⚠ vector dose flagged: toxic); [[AZD2858 (drug)]] (+0.62, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Pimozide (drug)]] (+0.62, unclear); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.61, Glucose transporter inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.61, Glucose transporter inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Simotinib"
- `tables/drugdoses.parquet` — dd in 949, 950, 951
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
