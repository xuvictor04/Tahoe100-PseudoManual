---
symbol: "FXN"
type: "gene"
col: 9059
ensembl_id: "ENSG00000165060"
name: "frataxin"
location: "9q21.11"
module: 33
arm: "+"
pooled_cpm: 10.29
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# FXN

*frataxin* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +10.9, q 6e-25, up in 18 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +10.0, q 4e-21, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.539× (z -14.3, q 2e-43, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB13]] (+0.79, fdr 7e-06), [[TMEM177]] (+0.77, fdr 7e-06), [[HEATR3]] (+0.77, fdr 7e-06); moves opposite to [[ATXN1L]] (-0.62, fdr 1e-05), [[ZCWPW2]] (-0.61, fdr 2e-05), [[SYNRG]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[OTUD5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +10.9 | 6e-25 | 18/32 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +10.4 | 5e-23 | 11/17 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +10.0 | 4e-21 | 33/45 (A498, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +8.7 | 5e-16 | 21/35 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +7.7 | 2e-12 | 19/45 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.0 | 3e-10 | 18/45 (SNU-423, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.57×** | +6.8 | 8e-10 | 12/23 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 1e-08 | 17/43 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +6.1 | 5e-08 | 18/45 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.7 | 5e-07 | 17/45 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +5.1 | 1e-05 | 14/44 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +5.1 | 2e-05 | 17/45 (NCI-H2347, SNU-423, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.7 | 9e-05 | 5/19 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +4.6 | 2e-04 | 8/45 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +4.4 | 4e-04 | 10/39 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.66×** | +4.3 | 5e-04 | 6/35 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.002 | 12/44 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.003 | 9/42 (HEC-1-A, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.009 | 9/45 (SK-MEL-2, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.031 | 5/37 (NCI-H460, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.040 | 5/40 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.072 | 4/45 (NCI-H1792, HepG2/C3A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.074 | 2/36 (HEC-1-A, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.090 | 7/39 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -14.3 | 2e-43 | 31/41 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -13.5 | 6e-39 | 27/43 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -5.8 | 1e-06 | 20/40 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -5.3 | 2e-05 | 20/46 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 0.002 | 10/45 (SW 900, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.753×** | -4.3 | 0.002 | 11/43 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.0 | 0.006 | 17/43 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.7 | 0.014 | 8/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.090 | 6/44 (J82, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.878× | -3.0 | 0.14 | 6/45 (RPMI-7951, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -9.9) |
| [[RKO (line)]] | wt | 26.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -12.2) |
| [[HOP62 (line)]] | alt | 6.19 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.2) |
| [[LoVo (line)]] | wt | 13.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.82× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.8) |
| [[PANC-1 (line)]] | alt | 9.55 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.1) |
| [[SW480 (line)]] | alt | 14.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.5) |
| [[A-172 (line)]] | wt | 4.22 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0671× (z -9.5) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -8.5) |
| [[A498 (line)]] | wt | 8.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.113× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -15.6) |
| [[SNU-1 (line)]] | wt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.0) |
| [[SW48 (line)]] | wt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -9.9) |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB13]] | +0.79 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.77 | +0.60 / +0.80 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[HEATR3]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[NLE1]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 438 |
| [[UCK2]] | +0.70 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.70 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SCAP]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MCOLN2]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CHST10]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZCWPW2]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FXN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises FXN's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without MCOLN2 | 0.008 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[FAM78B]] | B | FAM78B activity raises FXN's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without FAM78B | 0.023 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[MVB12B]] | B | MVB12B activity raises FXN's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without MVB12B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises FXN's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TSEN2]] | C | TSEN2 activity raises FXN's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; co-absent with the target; its own permutation p |
| [[USP31]] | C | USP31 activity raises FXN's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[GARNL3]] | C | GARNL3 activity raises FXN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.39× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OTUD5]] | C | FXN's natural level weakens OTUD5's drug response | FXN's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.07; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.1, -40.4); signed map (-8.4, -53.4). **Vector** length 88.8, 18.2% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +4.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -13.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | frataxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:69,035,751-69,079,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FA, FARR, X25, CyaY; previously FRDA |
| Gene groups (HGNC) | Mitochondrial iron-sulfur assembly components |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: Mitochondrial iron-sulfur cluster biogenesis; Maturation of TCA enzymes and regulation of TCA cycle; Complex III assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16595](https://www.uniprot.org/uniprotkb/Q16595) (Frataxin, mitochondrial):

> [Frataxin mature form]: Functions as an activator of persulfide transfer to the scaffoding protein ISCU as component of the core iron-sulfur cluster (ISC) assembly complex and participates to the [2Fe-2S] cluster assembly. Accelerates sulfur transfer from NFS1 persulfide intermediate to ISCU and to small thiols such as L-cysteine and glutathione leading to persulfuration of these thiols and ultimately sulfide release. Binds ferrous ion and is released from FXN upon the addition of both …

**Summary**, from NCBI Gene [2395](https://www.ncbi.nlm.nih.gov/gene/2395):

> This nuclear gene encodes a mitochondrial protein which belongs to the FRATAXIN family. The protein functions in regulating mitochondrial iron transport and respiration. The expansion of intronic trinucleotide repeat GAA from 8-33 repeats to >90 repeats results in Friedreich ataxia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:3951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3951) · Entrez [2395](https://www.ncbi.nlm.nih.gov/gene/2395) · UniProt [Q16595](https://www.uniprot.org/uniprotkb/Q16595) · Ensembl [ENSG00000165060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165060)

## Data

Gene col 9059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9059); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9059]; `tensor/DDL_lfc|DDL_z.npy` [9059]; `embed/gene_vectors.npy` [9059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9059 or target_col == 9059). Every well: [[FXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
