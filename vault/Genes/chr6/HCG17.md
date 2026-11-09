---
symbol: "HCG17"
type: "gene"
col: 15665
ensembl_id: "ENSG00000270604"
name: ""
location: ""
module: 26
arm: "+"
pooled_cpm: 13.79
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# HCG17

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.73× (z +21.7, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.594× (z -6.1, q 6e-07, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01191]] (+0.76, fdr 1e-05), [[LINC02955]] (+0.76, fdr 1e-05), [[LIX1-AS1]] (+0.76, fdr 7e-06); moves opposite to [[WRAP73]] (-0.71, fdr 2e-05), [[TTC38]] (-0.67, fdr 1e-05), [[MAST3]] (-0.67, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +21.7 | 0e+00 | 45/46 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +13.8 | 1e-40 | 41/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +13.6 | 1e-39 | 38/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +11.2 | 3e-27 | 23/28 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +9.9 | 6e-21 | 29/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.6 | 8e-16 | 33/47 (HOP62, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +7.5 | 5e-12 | 24/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +6.7 | 1e-09 | 29/46 (C32, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.4 | 1e-08 | 30/47 (NCI-H460, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-06 | 21/44 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 3e-05 | 22/44 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 18/45 (NCI-H23, COLO 205, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.86×** | +3.8 | 0.007 | 9/43 (LoVo, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.014 | 11/47 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.015 | 16/47 (SNU-423, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.024 | 15/47 (LoVo, KATO III, …) | top dose only |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.079 | 5/47 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.079 | 10/47 (LoVo, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -6.1 | 6e-07 | 29/47 (KATO III, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -5.0 | 2e-04 | 24/46 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -4.8 | 4e-04 | 23/47 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -4.7 | 4e-04 | 21/45 (KATO III, SHP-77, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.010 | 18/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.530×** | -3.9 | 0.010 | 15/44 (hTERT-HPNE, SW48, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -3.7 | 0.017 | 14/46 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.3 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +14.0) | — |
| [[LoVo (line)]] | wt | 22.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[NCI-H460 (line)]] | wt | 7.80 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +12.4) | — |
| [[C32 (line)]] | wt | 15.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 18.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.16 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +10.8) | — |
| [[RKO (line)]] | wt | 19.3 | 2 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.6) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.121× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 7.63 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +10.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0964× (z -9.4) |
| [[SW480 (line)]] | alt | 17.4 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.99× (z +14.1) | — |
| [[A-172 (line)]] | wt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 14.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.4) | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.115× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 8.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 7.21 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.7) | [[Imiquimod (maleate) (drug)]] 5 µM 0.0749× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 28.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 24.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[SNU-423 (line)]] | alt | 13.1 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 16.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 8.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.108× (z -9.2) |
| [[Hs 766T (line)]] | wt | 13.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.122× (z -9.5) |
| [[J82 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 8.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 5.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 6.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +10.5) | — |
| [[A-427 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01191]] | +0.76 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.76 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[LIX1-AS1]] | +0.76 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.76 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.75 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.74 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[ST8SIA5]] | +0.74 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[LINC00571]] | +0.73 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[PSMD7-DT]] | +0.73 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | +0.72 | +0.74 / +0.39 | both halves | 6e-05 |  |
| [[ARRDC3-AS1]] | +0.72 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | +0.72 | +0.70 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.71 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TTC38]] | -0.67 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[MAST3]] | -0.67 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[CAMK2G]] | -0.65 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[DPY30]] | -0.64 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[NBPF3]] | -0.64 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[FAM118A]] | -0.63 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[SLC9A6]] | -0.63 | -0.68 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises HCG17's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without NEK10 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises HCG17's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.60× lower at baseline in the lines without LINC02641 | 0.022 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HCG17's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises HCG17's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DDR2]] | B | DDR2 activity raises HCG17's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without DDR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.6, 14.9); signed map (24.0, -2.4). **Vector** length 97.6, 22.4% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +21.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +13.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

> [!warning] No registry record
> HCG17 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15665); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15665]; `tensor/DDL_lfc|DDL_z.npy` [15665]; `embed/gene_vectors.npy` [15665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15665 or target_col == 15665). Every well: [[HCG17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
