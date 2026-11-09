---
drug: "Pimozide"
type: "drug"
salt_base: "Pimozide"
targets: "DRD2, DRD3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 185
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pimozide

*unclear (inhibitor/antagonist) · targets: DRD2, DRD3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 185 / 141 / 30; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.42 / -0.15.
> Flags by dose: low cells (technical?) / transcription drop / -. ⚠ 0.5 µM: transcription drop (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G5 | 181 / 4 | — | -1.38 | -1.3/-0.6/-0.5 | low cells (technical?) |
| 0.5 µM | [[Plate 11]]:G5 | 132 / 9 | — | -0.72 | -0.9/+0.1/-0.9 | ⚠ transcription drop |
| 5 µM | [[Plate 12]]:G5 | 2 / 28 | — | +0.00 | -0.3/+0.1/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (181 genes, none with an alert; 12 shown): [[ZNF667]] 1.80× (z +5.2, 1/10 lines), [[TSPOAP1]] 1.97× (z +5.1, 3/14 lines), [[ESR1]] 1.61× (z +4.9, 5/29 lines), [[LINC02977]] 1.45× (z +4.6, 5/31 lines), [[ENSG00000289145]] 1.71× (z +4.4, 7/28 lines), [[ENSG00000222042]] 1.73× (z +4.4, 1/10 lines), [[ENSG00000250271]] 1.89× (z +4.4, 0/15 lines), [[SUCNR1]] 2.33× (z +4.3, 2/4 lines), [[NIM1K]] 1.38× (z +4.3, 5/34 lines), [[GPX2]] 1.67× (z +4.2, 2/12 lines), [[LINC03040]] 1.76× (z +4.2, 1/14 lines), [[CHRDL1]] 1.87× (z +4.2, 0/4 lines)

**0.5 µM** (132 genes, 132 with an alert ⚠; the drug-dose carries ⚠ transcription drop; 12 shown): [[STAG3]] ⚠ 1.52× (z +5.3, 2/17 lines), [[PHF21B]] ⚠ 1.30× (z +4.8, 5/24 lines), [[SPG7]] ⚠ 1.20× (z +4.5, 22/48 lines), [[ZNF8-DT]] ⚠ 1.28× (z +4.4, 8/43 lines), [[SNORC]] ⚠ 1.32× (z +4.3, 16/46 lines), [[FAM95A]] ⚠ 1.89× (z +4.3, 0/8 lines), [[THAP4]] ⚠ 1.22× (z +4.2, 12/47 lines), [[TRPV2]] ⚠ 1.58× (z +4.1, 0/15 lines), [[PADI2]] ⚠ 1.52× (z +4.0, 1/19 lines), [[ENSG00000258101]] ⚠ 1.43× (z +4.0, 5/34 lines), [[ENSG00000287460]] ⚠ 1.71× (z +4.0, 0/10 lines), [[RUBCNL]] ⚠ 1.57× (z +4.0, 1/11 lines)

**5 µM** (2 genes, none with an alert): [[U2AF1]] 1.35× (z +3.4, 15/47 lines), [[DDX3X]] 1.21× (z +3.0, 21/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[IL4I1]] 0.783× (z -4.5, 14/45 lines), [[WDR5]] 0.818× (z -4.0, 14/46 lines), [[LRRC14]] 0.701× (z -3.7, 12/35 lines), [[SLC1A3]] 0.779× (z -3.3, 7/25 lines)

**0.5 µM** (9 genes, 9 with an alert ⚠; the drug-dose carries ⚠ transcription drop): [[ZNF35]] ⚠ 0.748× (z -4.7, 14/44 lines), [[ENSG00000273149]] ⚠ 0.539× (z -4.5, 14/30 lines), [[RAB33B]] ⚠ 0.826× (z -3.8, 16/47 lines), [[TMED7]] ⚠ 0.781× (z -3.6, 30/48 lines), [[TMOD2]] ⚠ 0.773× (z -3.5, 8/36 lines), [[HNRNPA1L3]] ⚠ 0.751× (z -3.3, 8/41 lines), [[GOPC]] ⚠ 0.822× (z -3.3, 17/48 lines), [[SSBP2]] ⚠ 0.831× (z -3.1, 18/44 lines), [[PGAP3]] ⚠ 0.760× (z -2.9, 8/37 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[PLBD2]] 0.773× (z -5.0, 21/48 lines), [[MT-CO1]] 0.653× (z -5.0, 47/48 lines), [[MUC17]] 0.509× (z -4.7, 0/4 lines), [[LINC02327]] 0.587× (z -4.3, 0/5 lines), [[KIF5C]] 0.771× (z -4.2, 13/48 lines), [[NUMBL]] 0.805× (z -4.2, 11/48 lines), [[ENSG00000258028]] 0.614× (z -4.0, 1/8 lines), [[SCEL]] 0.672× (z -3.8, 0/13 lines), [[CD68]] 0.736× (z -3.7, 19/42 lines), [[GRHL2]] 0.781× (z -3.6, 0/14 lines), [[ENSG00000100101]] 0.792× (z -3.6, 11/48 lines), [[LMLN]] 0.773× (z -3.6, 12/46 lines)

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
| 0.05 µM | — | [[SW 1271 (line)]] (2.29), [[AN3 CA (line)]] (1.91), [[CHP-212 (line)]] (1.89), [[HepG2_C3A (line)]] (1.48) · weakest: [[SW480 (line)]] (0.143), [[NCI-H2347 (line)]] (0.238), [[NCI-H460 (line)]] (0.252) |
| 0.5 µM | [[RKO (line)]] (-3.6) | [[SW 1088 (line)]] (2.35), [[CHP-212 (line)]] (2.14), [[AN3 CA (line)]] (1.89), [[SW 1271 (line)]] (1.62) · weakest: [[NCI-H2347 (line)]] (0.0816), [[A498 (line)]] (0.105), [[PANC-1 (line)]] (0.139) |
| 5 µM | — | [[C32 (line)]] (2.08), [[RKO (line)]] (1.67), [[HCT15 (line)]] (1.54), [[NCI-H23 (line)]] (1.49) · weakest: [[SW 1088 (line)]] (0.444), [[LS 180 (line)]] (0.475), [[NCI-H1573 (line)]] (0.583) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Canagliflozin (hemihydrate) (drug)]] (+0.72, Glucose transporter inhibitor); [[Valdecoxib (drug)]] (+0.68, Cyclooxygenase inhibitor); [[Drospirenone (drug)]] (+0.66, unclear); [[AZD2858 (drug)]] (+0.64, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Pioglitazone (drug)]] (+0.63, unclear); [[Vemurafenib (drug)]] (+0.62, RAF inhibitor, ⚠ only 1 significant gene); [[Simotinib (drug)]] (+0.62, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Vitamin K4 (drug)]] (+0.58, unclear); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.58, Glucose transporter inhibitor); [[Bendamustine (drug)]] (+0.58, DNA synthesis/repair inhibitor); [[Hydroxyfasudil (drug)]] (+0.58, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 9, C 21. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BATF]] | 0.05 µM | B | BATF activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express BATF (33) vs lines expressing it (15) | the lines without BATF: 0.86× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[PIP5K1B]] | 0.05 µM | B | PIP5K1B activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.83× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[HUNK]] | 0.5 µM | B | HUNK activity lowers the cells' numbers under Pimozide 0.5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| [[ENSG00000287292]] | 0.05 µM | B | ENSG00000287292 activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express ENSG00000287292 (13) vs lines expressing it (35) | the lines without ENSG00000287292: 0.93× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: NR3C2, ENSG00000249631, SATB1; maybe low, not absent |
| [[HPGD]] | 0.05 µM | B | HPGD activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express HPGD (30) vs lines expressing it (18) | the lines without HPGD: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[FGD6]] | 0.5 µM | B | FGD6 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express FGD6 (12) vs lines expressing it (36) | the lines without FGD6: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[SLC7A2]] | 0.5 µM | B | SLC7A2 activity lowers the cells' numbers under Pimozide 0.5 µM (makes them more sensitive) | lines that do not express SLC7A2 (30) vs lines expressing it (18) | the lines without SLC7A2: 1.15× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[CACNG7]] | 0.05 µM | B | CACNG7 activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[MGC32805]] | 0.05 µM | B | MGC32805 activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 0.89× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[FIGN]] | 0.05 µM | C | FIGN activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.17× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ENSG00000285458]] | 0.5 µM | C | ENSG00000285458 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.72× the cells of the other lines | 0.009 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[ENSG00000286964]] | 0.05 µM | C | ENSG00000286964 activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.19× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[DDR1]] | 0.5 µM | C | DDR1 activity raises the cells' numbers under Pimozide 0.5 µM (protects the cells) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 0.70× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[ITPK1]] | 0.05 µM | C | ITPK1 activity raises the cells' numbers under Pimozide 0.05 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.79× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 0.05 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.16× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pimozide"
- `tables/drugdoses.parquet` — dd in 815, 816, 817
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
