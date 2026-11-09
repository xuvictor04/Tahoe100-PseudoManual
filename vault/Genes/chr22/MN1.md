---
symbol: "MN1"
type: "gene"
col: 9767
ensembl_id: "ENSG00000169184"
name: "MN1 proto-oncogene, transcriptional regulator"
location: "22q12.1"
module: 19
arm: "+"
pooled_cpm: 17.34
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 12
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# MN1

*MN1 proto-oncogene, transcriptional regulator* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +12.6, q 1e-33, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.552× (z -7.8, q 3e-12, down in 17 of 26 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -7.3, q 9e-11, down in 17 of 27 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLP2R]] (+0.60, fdr 2e-05), [[PAX7]] (+0.57, fdr 1e-05), [[COL4A6]] (+0.54, fdr 2e-05); moves opposite to [[SUCLG2]] (-0.43, fdr 1e-04), [[CCDC171]] (-0.40, fdr 2e-04), [[ZC3H12B]] (-0.38, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PAX7]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF385A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +12.6 | 1e-33 | 13/24 (A549, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.9 | 9e-13 | 3/13 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.00×** | +7.5 | 1e-11 | 12/27 (SNU-1, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.90×** | +7.3 | 5e-11 | 10/22 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +6.3 | 3e-08 | 3/16 (NCI-H1792, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.59×** | +5.8 | 7e-07 | 14/25 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 2/27 (SW480, NCI-H2030) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 2e-04 | 3/22 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +4.5 | 3e-04 | 4/27 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.0 | 0.004 | 1/12 (A498) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.026 | 12/26 (NCI-H460, H4, …) | rises with dose | low cells (technical?) |
| [[AZD-7648 (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.11 | 2/26 (SW1417, CHP-212) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.552×** | -7.8 | 3e-12 | 17/26 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -7.3 | 9e-11 | 17/27 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -6.8 | 2e-09 | 16/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.643×** | -5.8 | 8e-07 | 12/26 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.666×** | -5.2 | 3e-05 | 13/25 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -4.8 | 1e-04 | 17/24 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.715×** | -4.4 | 8e-04 | 12/26 (CHP-212, hTERT-HPNE, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -4.2 | 0.002 | 16/26 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.718×** | -4.2 | 0.002 | 7/26 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.6 | 0.015 | 8/25 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.591×** | -3.6 | 0.015 | 8/21 (SW1417, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.754×** | -3.6 | 0.016 | 9/27 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -3.4 | 0.026 | 12/25 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.794×** | -3.0 | 0.093 | 8/24 (Panc 03.27, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 134 | 0 | 18 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0658× (z -27.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -16.6) |
| [[Hs 766T (line)]] | wt | 167 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -27.8) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 29.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.182× (z -9.1) |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0620× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.0) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.228× (z -8.8) |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -11.1) |
| [[SW480 (line)]] | alt | 6.70 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.181× (z -9.9) |
| [[A-172 (line)]] | wt | 8.36 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -8.5) |
| [[A549 (line)]] | wt | 8.08 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0816× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[NCI-H2030 (line)]] | alt | 5.10 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0671× (z -9.5) |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLP2R]] | +0.60 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[PAX7]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[COL4A6]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CDH11]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SOX7]] | +0.52 | +0.53 / +0.42 | both halves | 4e-05 | **novel candidate** |
| [[LINC01035]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SULF1]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LINC03000]] | +0.51 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[TBXT]] ⚠ | +0.50 | +0.38 / +0.59 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C5orf46]] | +0.50 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[SCARA5]] | +0.50 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CTNND2]] | +0.49 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[PAK3]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCLG2]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[CCDC171]] | -0.40 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[ZC3H12B]] | -0.38 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[NT5DC1]] | -0.37 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[WWOX]] | -0.37 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX7]] | B | PAX7 activity raises MN1's level | lines that do not express PAX7 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without PAX7 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00408, ENSG00000289605, SLC15A5; maybe low, not absent |
| [[GTF2I-AS1]] | B | GTF2I-AS1 activity raises MN1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.94× lower at baseline in the lines without GTF2I-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[GSG1L2]] | B | GSG1L2 activity raises MN1's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 3.70× lower at baseline in the lines without GSG1L2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[GLP2R]] | B | GLP2R activity raises MN1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.00× lower at baseline in the lines without GLP2R | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |
| [[SIM1]] | B | SIM1 activity raises MN1's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.50× lower at baseline in the lines without SIM1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[LINC03000]] | B | LINC03000 activity raises MN1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.26× lower at baseline in the lines without LINC03000 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[CTNND2]] | B | CTNND2 activity raises MN1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.47× lower at baseline in the lines without CTNND2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[SOX7]] | B | SOX7 activity raises MN1's level | lines that do not express SOX7 (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without SOX7 | 0.097 | ⚠ within organs, on part of the lines; also absent: COL4A6, MMRN1, PTGIS |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises MN1's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without TNFRSF11B | 0.020 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[COL4A6]] | C | COL4A6 activity raises MN1's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without COL4A6 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises MN1's level | lines that do not express TBXT (47) vs lines expressing it (3) | 5.15× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |
| [[C5orf46]] | C | C5orf46 activity raises MN1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without C5orf46 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385A]] | B | MN1 activity raises ZNF385A's level | lines that do not express MN1 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without MN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: FHL1, COL7A1, ABI3BP |
| [[LINC00922]] | B | MN1 activity raises LINC00922's level | lines that do not express MN1 (21) vs lines expressing it (29) | 1.58× lower at baseline in the lines without MN1 | 0.040 | ⚠ within organs, on part of the lines; also absent: FHL1, COL7A1, ABI3BP |
| [[PRICKLE1]] | C | MN1 activity raises PRICKLE1's level | lines that do not express MN1 (21) vs lines expressing it (29) | 3.04× lower at baseline in the lines without MN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: FHL1, COL7A1, ABI3BP; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 35.0); signed map (43.2, 46.6). **Vector** length 61.4, 13.0% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | +4.2 | +0.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MN1 proto-oncogene, transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:27,748,277-27,801,756 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGCR1-PEN, MGCR1; previously MGCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10571](https://www.uniprot.org/uniprotkb/Q10571) (Transcriptional activator MN1):

> Transcriptional activator which specifically regulates expression of TBX22 in the posterior region of the developing palate. Required during later stages of palate development for growth and medial fusion of the palatal shelves. Promotes maturation and normal function of calvarial osteoblasts, including expression of the osteoclastogenic cytokine TNFSF11/RANKL. Necessary for normal development of the membranous bones of the skull (By similarity). May play a role in tumor suppression (Probable).

**Summary**, from NCBI Gene [4330](https://www.ncbi.nlm.nih.gov/gene/4330):

> Meningioma 1 (MN1) contains two sets of CAG repeats. It is disrupted by a balanced translocation (4;22) in a meningioma, and its inactivation may contribute to meningioma 32 pathogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7180) · Entrez [4330](https://www.ncbi.nlm.nih.gov/gene/4330) · UniProt [Q10571](https://www.uniprot.org/uniprotkb/Q10571) · Ensembl [ENSG00000169184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169184)

## Data

Gene col 9767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9767); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9767]; `tensor/DDL_lfc|DDL_z.npy` [9767]; `embed/gene_vectors.npy` [9767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9767 or target_col == 9767). Every well: [[MN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
