---
symbol: "SGK2"
type: "gene"
col: 2063
ensembl_id: "ENSG00000101049"
name: "serum/glucocorticoid regulated kinase 2"
location: "20q13.12"
module: 26
arm: "+"
pooled_cpm: 7.84
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 15
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SGK2

*serum/glucocorticoid regulated kinase 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.41× (z +18.5, q 0e+00, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.470× (z -9.4, q 2e-18, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.69, fdr 7e-06), [[ALG1L9P]] (+0.68, fdr 7e-06), [[L3MBTL1]] (+0.65, fdr 7e-06, ⚠ same locus), [[ITFG2-AS1]] (+0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); 5 go from it, the strongest it → [[ATF7IP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.41×** | +18.5 | 0e+00 | 34/39 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +17.9 | 0e+00 | 28/34 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.3 | 2e-14 | 4/11 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.0 | 3e-10 | 20/30 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.9 | 6e-10 | 14/43 (HS-578T, SW1417, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.7 | 1e-06 | 16/41 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.29×** | +5.4 | 6e-06 | 12/41 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +5.3 | 9e-06 | 14/39 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.0 | 4e-05 | 13/34 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.0 | 4e-05 | 11/43 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.9 | 4e-05 | 11/39 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.8 | 7e-05 | 2/13 (A498, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.6 | 2e-04 | 11/27 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.37×** | +4.1 | 0.001 | 10/43 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 5/39 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 13/38 (HCT15, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 11/43 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.009 | 8/42 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.010 | 2/37 (CFPAC-1, A-427) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -9.4 | 2e-18 | 24/40 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.378×** | -6.3 | 6e-08 | 17/38 (C-33 A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.613×** | -6.1 | 2e-07 | 20/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.617×** | -6.0 | 2e-07 | 19/34 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -5.5 | 4e-06 | 17/34 (NCI-H23, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.641×** | -5.3 | 9e-06 | 18/39 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -4.8 | 1e-04 | 14/42 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.691×** | -4.6 | 3e-04 | 14/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.706×** | -4.2 | 0.002 | 15/29 (NCI-H23, C-33 A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.545×** | -4.0 | 0.004 | 8/32 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.734×** | -3.9 | 0.006 | 9/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.739×** | -3.8 | 0.007 | 16/39 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.751×** | -3.6 | 0.014 | 9/41 (PANC-1, A-427, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.078 | 13/42 (A498, COLO 205, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.090 | 5/43 (CFPAC-1, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.33 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -13.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.178× (z -10.7) |
| [[COLO 205 (line)]] | alt | 75.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -10.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.191× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 2.34 | 2 | 1 | [[Auranofin (drug)]] 5 µM 13.2× (z +9.6) | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0886× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 11.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.23× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.29 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.112× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 4.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[Panc 03.27 (line)]] | alt | 4.09 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0421× (z -10.0) |
| [[SW480 (line)]] | alt | 7.76 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.68 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[L3MBTL1]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 | STRING 430; ⚠ same locus (8.0 kb, same strand: neighbours can correlate without regulation) |
| [[ITFG2-AS1]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CD72]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[STX17-DT]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MGAM]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[EPCAM-DT]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PPP5D1P-1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CDH26]] | +0.61 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[UPP2]] | +0.61 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[GIPC2]] | +0.60 | +0.60 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises SGK2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ANKRD20A21P | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises SGK2's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without SYT9-AS1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SGK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[L3MBTL1]] | C | L3MBTL1 activity raises SGK2's level | lines that do not express L3MBTL1 (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without L3MBTL1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000277611, DNAJC18, COPZ2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATF7IP2]] | B | SGK2 activity raises ATF7IP2's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without SGK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[ECHDC2]] | B | SGK2 activity raises ECHDC2's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 3.58× lower at baseline in the lines without SGK2 | 0.082 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[ZNF460-AS1]] | B | SGK2 activity raises ZNF460-AS1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 1.21× lower at baseline in the lines without SGK2 | 0.087 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[DDX59-AS1]] | B | SGK2 activity raises DDX59-AS1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without SGK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent |
| [[L3MBTL1]] | C | SGK2 activity raises L3MBTL1's level | lines that do not express SGK2 (5) vs lines expressing it (45) | 3.38× lower at baseline in the lines without SGK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, ADORA2B, ARSD; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.6, 19.7); signed map (30.4, -6.0). **Vector** length 72.0, 12.9% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +17.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | +2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | serum/glucocorticoid regulated kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:43,558,968-43,588,237 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serum/glucocorticoid regulated kinase family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBY8](https://www.uniprot.org/uniprotkb/Q9HBY8) (Serine/threonine-protein kinase Sgk2):

> Serine/threonine-protein kinase which is involved in the regulation of a wide variety of ion channels, membrane transporters, cell growth, survival and proliferation. Up-regulates Na(+) channels: SCNN1A/ENAC, K(+) channels: KCNA3/Kv1.3, KCNE1 and KCNQ1, amino acid transporter: SLC6A19, glutamate transporter: SLC1A6/EAAT4, glutamate receptors: GRIA1/GLUR1 and GRIK2/GLUR6, Na(+)/H(+) exchanger: SLC9A3/NHE3, and the Na(+)/K(+) ATPase.

**Summary**, from NCBI Gene [10110](https://www.ncbi.nlm.nih.gov/gene/10110):

> This gene encodes a serine/threonine protein kinase. Although this gene product is similar to serum- and glucocorticoid-induced protein kinase (SGK), this gene is not induced by serum or glucocorticoids. This gene is induced in response to signals that activate phosphatidylinositol 3-kinase, which is also true for SGK. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:13900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13900) · Entrez [10110](https://www.ncbi.nlm.nih.gov/gene/10110) · UniProt [Q9HBY8](https://www.uniprot.org/uniprotkb/Q9HBY8) · Ensembl [ENSG00000101049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101049)

## Data

Gene col 2063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2063); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2063]; `tensor/DDL_lfc|DDL_z.npy` [2063]; `embed/gene_vectors.npy` [2063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2063 or target_col == 2063). Every well: [[SGK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
