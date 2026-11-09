---
symbol: "FAM204A"
type: "gene"
col: 9161
ensembl_id: "ENSG00000165669"
name: "family with sequence similarity 204 member A"
location: "10q26.11"
module: 28
arm: "+"
pooled_cpm: 66.34
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# FAM204A

*family with sequence similarity 204 member A* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.57× (z +15.5, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.779× (z -8.6, q 4e-15, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMPCB]] (+0.77, fdr 7e-06), [[CUL5]] (+0.76, fdr 7e-06), [[PGGT1B]] (+0.70, fdr 7e-06); moves opposite to [[PAQR4]] (-0.61, fdr 1e-05), [[RCOR1]] (-0.58, fdr 1e-05), [[FRMD8]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NDUFS4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +15.5 | 0e+00 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +14.8 | 0e+00 | 46/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +12.0 | 1e-30 | 34/49 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +10.3 | 2e-22 | 42/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +10.0 | 1e-21 | 34/43 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +10.0 | 2e-21 | 41/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +9.4 | 5e-19 | 35/48 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +9.1 | 9e-18 | 30/45 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +8.3 | 5e-15 | 41/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +8.2 | 1e-14 | 37/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +7.9 | 2e-13 | 30/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +7.0 | 2e-10 | 30/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.0 | 9e-08 | 20/48 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +5.5 | 2e-06 | 31/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.4 | 2e-06 | 23/37 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.3 | 6e-04 | 14/48 (AsPC-1, RKO, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.003 | 14/48 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.003 | 20/49 (A-427, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.008 | 14/48 (SW1417, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.5 | 0.011 | 14/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.035 | 9/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9161.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -8.6 | 4e-15 | 33/48 (SNU-423, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -7.3 | 6e-11 | 31/48 (AN3 CA, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -6.4 | 3e-08 | 23/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.819×** | -4.9 | 1e-04 | 25/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -4.9 | 1e-04 | 21/49 (RKO, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -4.0 | 0.006 | 20/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.031 | 16/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.5 | 0.033 | 20/48 (SW 1088, SW480, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.874× | -3.3 | 0.062 | 12/48 (HCT15, SW 1271, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.082 | 13/48 (SW 1088, SNU-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.882× | -3.1 | 0.11 | 5/48 (AsPC-1, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 79.6 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.37× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 82.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.5) | — |
| [[A498 (line)]] | wt | 48.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.5) | — |
| [[LoVo (line)]] | wt | 59.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +11.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.62× (z +10.7) | — |
| [[A-172 (line)]] | wt | 67.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 55.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 78.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.09× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.9) | — |
| [[A-427 (line)]] | wt | 50.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 71.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 58.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) | — |
| [[RKO (line)]] | wt | 87.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.6) | — |
| [[A549 (line)]] | wt | 70.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.5) | — |
| [[H4 (line)]] | wt | 52.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 97.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.7) | — |
| [[KATO III (line)]] | alt | 63.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 1 | — | [[Entrectinib (drug)]] 0.05 µM 0.0769× (z -8.5) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMPCB]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[CUL5]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PGGT1B]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[COPS5]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZFR]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RBM41]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ATP6V1H]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ZDHHC17]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SCRN3]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR4]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RCOR1]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[FRMD8]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.56 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[KLF13]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TMEM104]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[EHD4]] | -0.55 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RELL1]] | -0.54 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[KLHL29]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZBED4]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[LINC01128]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CMIP]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FAM204A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFS4]] | C | FAM204A's natural level strengthens NDUFS4's drug response | FAM204A's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.11; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.5, 3.7); signed map (9.2, -32.2). **Vector** length 102, 26.9% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +10.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 204 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:118,297,925-118,342,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13188, bA319I23.1; previously C10orf84 |
| Matched by | ensembl_id |

UniProt [Q9H8W3](https://www.uniprot.org/uniprotkb/Q9H8W3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25794) · Entrez [63877](https://www.ncbi.nlm.nih.gov/gene/63877) · UniProt [Q9H8W3](https://www.uniprot.org/uniprotkb/Q9H8W3) · Ensembl [ENSG00000165669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165669)

## Data

Gene col 9161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9161); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9161]; `tensor/DDL_lfc|DDL_z.npy` [9161]; `embed/gene_vectors.npy` [9161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9161 or target_col == 9161). Every well: [[FAM204A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM204A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
