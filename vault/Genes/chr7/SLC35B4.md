---
symbol: "SLC35B4"
type: "gene"
col: 12944
ensembl_id: "ENSG00000205060"
name: "solute carrier family 35 member B4"
location: "7q33"
module: 4
arm: "+"
pooled_cpm: 13.08
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC35B4

*solute carrier family 35 member B4* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +10.9, q 5e-25, up in 14 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.41× (z +6.8, q 2e-09, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -13.3, q 2e-37, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL1]] (+0.72, fdr 7e-06), [[WDR77]] (+0.70, fdr 7e-06), [[TMEM33]] (+0.70, fdr 7e-06); moves opposite to [[GPX4]] (-0.66, fdr 1e-05), [[TTC21A]] (-0.65, fdr 8e-06), [[RNASE4]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM154]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +10.9 | 5e-25 | 14/22 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.73×** | +7.7 | 4e-12 | 27/38 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.8 | 2e-09 | 27/48 (A549, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +6.4 | 3e-08 | 25/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.3 | 3e-08 | 25/48 (HS-578T, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.58×** | +6.0 | 2e-07 | 16/27 (A549, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 8e-06 | 17/48 (SW480, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +4.7 | 2e-04 | 16/47 (HS-578T, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.41×** | +4.6 | 2e-04 | 18/41 (PANC-1, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.6 | 2e-04 | 18/47 (A498, LOX-IMVI, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.4 | 5e-04 | 17/46 (C32, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.30×** | +3.6 | 0.013 | 13/47 (LS 180, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.4 | 0.025 | 12/38 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +3.4 | 0.025 | 12/45 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.025 | 7/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.025 | 7/48 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.026 | 6/48 (A-172, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.032 | 4/48 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.033 | 4/48 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.043 | 7/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.048 | 8/45 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.051 | 3/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.051 | 5/45 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.051 | 4/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -13.3 | 2e-37 | 36/47 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -5.8 | 1e-06 | 19/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -5.8 | 1e-06 | 23/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.551×** | -4.4 | 0.001 | 14/43 (C32, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -4.4 | 0.001 | 14/48 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.827×** | -3.8 | 0.014 | 11/48 (HCT15, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.031 | 11/47 (NCI-H23, CHP-212, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.660× | -3.1 | 0.14 | 15/44 (SW 900, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 0.805× | -3.1 | 0.14 | 8/47 (HT-29, BT-474, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.665× | -3.0 | 0.14 | 11/45 (SW1417, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.4) |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0671× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Allantoin (drug)]] 0.5 µM 0.0976× (z -8.5) |
| [[A-172 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.91× (z +10.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 7.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0502× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.1) |
| [[J82 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 3.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 7.37 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0952× (z -9.4) |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.4) |
| [[RKO (line)]] | wt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -17.8) |
| [[SNU-423 (line)]] | alt | 8.06 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.107× (z -8.7) |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[WDR77]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[CCT5]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.67 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ATIC]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[GOT2]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[POLR1A]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[CCDC86]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LARS2]] | +0.63 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TMX3]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX4]] | -0.66 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[TTC21A]] | -0.65 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[RNASE4]] | -0.63 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[TESK2]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[HOOK2]] | -0.62 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[KLC4]] | -0.62 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.62 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.60 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[HDAC5]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[WBP1]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM154]] | B | TMEM154 activity lowers SLC35B4's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.49× higher at baseline in the lines without TMEM154 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[CMTM3]] | B | CMTM3 activity raises SLC35B4's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without CMTM3 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |
| [[TOP2A]] | B | TOP2A activity lowers SLC35B4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A2]] | C | SLC26A2 activity raises SLC35B4's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without SLC26A2 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[ALDH1B1]] | C | ALDH1B1 activity raises SLC35B4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.5, -33.0); signed map (-10.5, -45.0). **Vector** length 82.1, 16.1% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +3.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.5 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -13.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.3 | -3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member B4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,289,332-134,316,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14697, YEA4 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 4 pathways, smallest: Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969S0](https://www.uniprot.org/uniprotkb/Q969S0) (Nucleotide sugar transporter SLC35B4):

> Antiporter that transports nucleotide sugars across the endoplasmic reticulum (ER) membrane in exchange for another nucleotide sugar. May couple UDP-alpha-D-glucuronate (UDP-GlcA) or UDP-alpha-D-xylose (UDP-Xyl) efflux to UDP-alpha-D-glucuronate (UDP-GlcA) influx into the ER lumen, which in turn stimulates glucuronidation and excretion of endobiotics and xenobiotics.; [Isoform 1]: Has UDP-GlcA:UDP-GlcNAc antiporter activity.; [Isoform 2]: Has UDP-GlcA:UDP-GlcNAc antiporter activity.

**Summary**, from NCBI Gene [84912](https://www.ncbi.nlm.nih.gov/gene/84912):

> Glycosyltransferases, such as SLC35B4, transport nucleotide sugars from the cytoplasm where they are synthesized, to the Golgi apparatus where they are utilized in the synthesis of glycoproteins, glycolipids, and proteoglycans (Ashikov et al., 2005 [PubMed 15911612]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20584) · Entrez [84912](https://www.ncbi.nlm.nih.gov/gene/84912) · UniProt [Q969S0](https://www.uniprot.org/uniprotkb/Q969S0) · Ensembl [ENSG00000205060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205060)

## Data

Gene col 12944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12944); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12944]; `tensor/DDL_lfc|DDL_z.npy` [12944]; `embed/gene_vectors.npy` [12944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12944 or target_col == 12944). Every well: [[SLC35B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
