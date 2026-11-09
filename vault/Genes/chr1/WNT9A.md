---
symbol: "WNT9A"
type: "gene"
col: 6810
ensembl_id: "ENSG00000143816"
name: "Wnt family member 9A"
location: "1q42.13"
module: 101
arm: "+"
pooled_cpm: 20.58
n_lines_expressing: 39
n_dd_up: 30
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# WNT9A

*Wnt family member 9A* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.38× (z +11.8, q 2e-29, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.305× (z -8.5, q 2e-14, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNYL1]] (+0.62, fdr 1e-05), [[GBX1]] (+0.61, fdr 1e-05), [[STK10]] (+0.60, fdr 1e-05); moves opposite to [[CAVIN2]] (-0.62, fdr 1e-05), [[CAND1]] (-0.57, fdr 1e-05), [[PUM2]] (-0.53, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GBX1]] → it (grade B ⚠); 3 go from it, the strongest it → [[OSGEPL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +11.8 | 2e-29 | 24/36 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.2 | 5e-14 | 15/35 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.80×** | +7.7 | 2e-12 | 22/35 (NCI-H2030, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +6.9 | 1e-09 | 18/36 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +6.7 | 2e-09 | 17/35 (Hs 766T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.6 | 4e-09 | 20/37 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 1e-07 | 22/36 (NCI-H2030, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.6 | 2e-06 | 12/27 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 2e-06 | 17/36 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.12×** | +5.3 | 5e-06 | 19/33 (SW1417, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 17/35 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.0 | 3e-05 | 11/36 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +4.2 | 0.001 | 11/36 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.005 | 15/34 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.005 | 10/37 (SW48, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 13/36 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.006 | 11/37 (NCI-H2347, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.305×** | -8.5 | 2e-14 | 26/36 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -6.1 | 2e-07 | 18/31 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -6.0 | 3e-07 | 17/32 (A-172, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.433×** | -6.0 | 3e-07 | 20/30 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -4.9 | 1e-04 | 8/38 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.806×** | -4.2 | 0.003 | 11/37 (A549, NCI-H23, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.748×** | -4.0 | 0.006 | 15/32 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.046 | 12/36 (RPMI-7951, Hs 766T, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.064 | 12/36 (Hs 766T, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.794×** | -3.1 | 0.094 | 13/34 (SW 900, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.56 | 13 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.23× (z +14.0) | — |
| [[A-172 (line)]] | wt | 80.4 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 56.6 | 1 | 7 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.12× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.214× (z -11.7) |
| [[SW480 (line)]] | alt | 21.0 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 9.32× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 53.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 49.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +13.8) | [[Selinexor (drug)]] 5 µM 0.345× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 9.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.161× (z -11.9) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.0625× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.513× (z -11.7) ⚠ position not correctable · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 73.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -9.1) |
| [[SW1417 (line)]] | alt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.3) | — |
| [[A498 (line)]] | wt | 9.48 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +9.8) | — |
| [[A549 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 9.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.05× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -9.0) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.3) |
| [[SW 900 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +12.1) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 | same gene group |
| [[GBX1]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[STK10]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TUBB6]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TMEM132B]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CATSPERG]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CELSR1]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ZBTB46]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[JOSD1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ARC]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN2]] | -0.62 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[CAND1]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PUM2]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[WBP11]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[MAP2K6]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[RBM26]] | -0.52 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[OSGEPL1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CSRNP3]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TTC23]] | -0.50 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[HNRNPR]] | -0.49 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ALDH1A1]] | -0.49 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | GBX1 activity raises WNT9A's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without GBX1 | 0.017 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[CELSR1]] | C | CELSR1 activity raises WNT9A's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 4.56× lower at baseline in the lines without CELSR1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSGEPL1]] | B | WNT9A activity raises OSGEPL1's level | lines that do not express WNT9A (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without WNT9A | 0.012 | ⚠ within organs, on part of the lines; also absent: RAB6B, DZIP1L, MRAS |
| [[FAM241A]] | B | WNT9A activity lowers FAM241A's level | lines that do not express WNT9A (11) vs lines expressing it (39) | 2.02× higher at baseline in the lines without WNT9A | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB6B, DZIP1L, MRAS |
| [[ZNF470]] | C | WNT9A activity raises ZNF470's level | lines that do not express WNT9A (11) vs lines expressing it (39) | 4.62× lower at baseline in the lines without WNT9A | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB6B, DZIP1L, MRAS; co-absent with the target |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, 18.3); signed map (-0.7, 33.6). **Vector** length 106, 25.0% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +11.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.6 | +7.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -8.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -6.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 9A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:227,918,656-227,947,932 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WNT14 |
| Gene groups (HGNC) | Wnt family; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: Negative regulation of TCF-dependent signaling by WNT ligand antagonists; WNT ligand biogenesis and trafficking; Class B/2 (Secretin family receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [O14904](https://www.uniprot.org/uniprotkb/O14904) (Protein Wnt-9a):

> Ligand for members of the frizzled family of seven transmembrane receptors. Functions in the canonical Wnt/beta-catenin signaling pathway. Required for normal timing of IHH expression during embryonic bone development, normal chondrocyte maturation and for normal bone mineralization during embryonic bone development. Plays a redundant role in maintaining joint integrity.

**Summary**, from NCBI Gene [7483](https://www.ncbi.nlm.nih.gov/gene/7483):

> The WNT gene family consists of structurally related genes that encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. This gene is a member of the WNT gene family. It is expressed in gastric cancer cell lines. The protein encoded by this gene shows 75% amino acid identity to chicken Wnt14, which has been shown to play a central role in initiating …

**Accessions** — [HGNC:12778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12778) · Entrez [7483](https://www.ncbi.nlm.nih.gov/gene/7483) · UniProt [O14904](https://www.uniprot.org/uniprotkb/O14904) · Ensembl [ENSG00000143816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143816)

## Data

Gene col 6810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6810); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6810]; `tensor/DDL_lfc|DDL_z.npy` [6810]; `embed/gene_vectors.npy` [6810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6810 or target_col == 6810). Every well: [[WNT9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
