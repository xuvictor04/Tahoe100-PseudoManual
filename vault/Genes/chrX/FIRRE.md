---
symbol: "FIRRE"
type: "gene"
col: 13107
ensembl_id: "ENSG00000213468"
name: "firre intergenic repeating RNA element"
location: "Xq26.2"
module: 4
arm: "+"
pooled_cpm: 23.58
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FIRRE

*firre intergenic repeating RNA element* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +9.5, q 1e-18, up in 18 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.71× (z +4.3, q 0.002, up in 15 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -13.0, q 8e-36, down in 26 of 29 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.549× (z -6.0, q 2e-07, down in 18 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA25]] (+0.67, fdr 1e-05), [[METAP1D]] (+0.67, fdr 1e-05), [[VWA8]] (+0.64, fdr 1e-05); moves opposite to [[SHOC2]] (-0.64, fdr 7e-06), [[TMEM50A]] (-0.52, fdr 1e-04), [[ING2]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ROBO2]] → it (grade B ⚠); 2 go from it, the strongest it → [[ROBO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.5 | 1e-18 | 18/26 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.4 | 4e-11 | 10/17 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.2 | 1e-10 | 14/22 (NCI-H2030, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +5.8 | 8e-07 | 21/29 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.71×** | +4.3 | 0.002 | 15/29 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.010 | 14/30 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.012 | 14/29 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.02×** | +3.7 | 0.015 | 14/29 (NCI-H1573, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.022 | 13/29 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.95×** | +3.5 | 0.024 | 13/28 (KATO III, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.91×** | +3.4 | 0.034 | 13/29 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.2 | 0.055 | 3/30 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.065 | 5/30 (NCI-H1573, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.065 | 10/30 (H4, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.401×** | -13.0 | 8e-36 | 26/29 (NCI-H460, H4, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -7.2 | 2e-10 | 22/29 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.538×** | -6.2 | 9e-08 | 16/29 (NCI-H460, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.549×** | -6.0 | 2e-07 | 24/30 (SW480, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -6.0 | 2e-07 | 18/29 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.3 | 9e-06 | 20/30 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.590×** | -5.3 | 9e-06 | 18/29 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.628×** | -4.5 | 5e-04 | 17/29 (RKO, NCI-H460, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.700×** | -3.6 | 0.021 | 14/29 (RKO, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -3.6 | 0.021 | 15/30 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.061 | 9/30 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.061 | 16/30 (SW 1088, A-427, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.738× | -3.0 | 0.10 | 10/30 (NCI-H23, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.808× | -3.0 | 0.10 | 9/30 (KATO III, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 75.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -13.2) |
| [[SW480 (line)]] | alt | 174 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 62.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.1) |
| [[KATO III (line)]] | alt | 26.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.160× (z -11.9) |
| [[H4 (line)]] | wt | 65.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -18.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.234× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 3 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0765× (z -9.7) ⚠ transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0892× (z -9.1) |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -13.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA25]] | +0.67 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[METAP1D]] | +0.67 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[VWA8]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[RABGGTB]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[PUM3]] | +0.63 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[ATIC]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SARS2]] | +0.61 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[MRPL3]] | +0.61 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[TSEN2]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[MDN1]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[L3HYPDH]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[TMEM50A]] | -0.52 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[ING2]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RNASE4]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[PTPRH]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MTHFR]] | -0.50 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[ZFYVE1]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[KATNA1]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TP53INP2]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[GCC2]] | -0.50 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[GARRE1]] | -0.50 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO2]] | B | ROBO2 activity raises FIRRE's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.64× lower at baseline in the lines without ROBO2 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO2]] | B | FIRRE activity raises ROBO2's level | lines that do not express FIRRE (18) vs lines expressing it (32) | 2.62× lower at baseline in the lines without FIRRE | 0.045 | ⚠ within organs, on part of the lines; also absent: HMCN1, GAP43, ENSG00000286033 |
| [[TGFBR1]] | B | FIRRE activity weakens TGFBR1's drug response | lines that do not express FIRRE (18) vs lines expressing it (31) | the lines without FIRRE respond 1.63× as strongly (z diff -1.72); strongest at Dinaciclib 0.05 µM: 0.57x vs 0.77x (z diff -3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: HMCN1, GAP43, ENSG00000286033; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.2, -34.0); signed map (-11.6, -48.6). **Vector** length 74.5, 19.7% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.7 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | -13.0 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | firre intergenic repeating RNA element |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq26.2 — chrX:131,688,779-131,830,862 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LINC01200 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [286467](https://www.ncbi.nlm.nih.gov/gene/286467):

> This gene produces a long RNA containing a repeating sequence. This RNA interacts with heterogeneous nuclear ribonucleoprotein U and coats chromosomes, where it plays an important role in the maintenance of repressive chromatin. This transcript can also act post-transcriptionally to regulate the stability of mRNAs during the innate immune response. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:49627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49627) · Entrez [286467](https://www.ncbi.nlm.nih.gov/gene/286467) · Ensembl [ENSG00000213468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213468)

## Data

Gene col 13107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13107); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13107]; `tensor/DDL_lfc|DDL_z.npy` [13107]; `embed/gene_vectors.npy` [13107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13107 or target_col == 13107). Every well: [[FIRRE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIRRE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
