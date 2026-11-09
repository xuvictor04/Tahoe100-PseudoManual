---
symbol: "SMCO2"
type: "gene"
col: 9212
ensembl_id: "ENSG00000165935"
name: "single-pass membrane protein with coiled-coil domains 2"
location: "12p11.23"
module: 39
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 41
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SMCO2

*single-pass membrane protein with coiled-coil domains 2* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +9.8, q 4e-20, up in 19 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.565× (z -5.3, q 7e-05, down in 20 of 36 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.582× (z -5.0, q 2e-04, down in 13 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSUH2]] (+0.71, fdr 7e-06), [[BMAL2-AS1]] (+0.70, fdr 7e-06, ⚠ same locus), [[ITPR2-AS1]] (+0.69, fdr 7e-06), [[LINC02516]] (+0.67, fdr 7e-06); moves opposite to [[EFNA4]] (-0.61, fdr 1e-05), [[EFNA3]] (-0.61, fdr 1e-05), [[KANTR]] (-0.58, fdr 3e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC00707]] → it (grade B ⚠); 17 go from it, the strongest it → [[BMAL2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +9.8 | 4e-20 | 19/33 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.2 | 7e-14 | 10/22 (HOP62, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +6.9 | 8e-10 | 5/15 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +6.2 | 6e-08 | 17/32 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +5.3 | 1e-05 | 4/8 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.75×** | +5.0 | 7e-05 | 14/36 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.5 | 6e-04 | 10/34 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.65×** | +4.4 | 9e-04 | 18/36 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 9/36 (BT-474, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +3.9 | 0.005 | 14/36 (LS 180, HEC-1-A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +3.9 | 0.006 | 12/36 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.011 | 10/36 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.015 | 10/36 (COLO 205, LoVo, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.015 | 13/35 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.027 | 11/38 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.038 | 7/29 (SW 900, LoVo, …) | two highest doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.044 | 7/30 (SW 900, NCI-H460, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.066 | 4/37 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.071 | 9/36 (HS-578T, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.565×** | -5.3 | 7e-05 | 20/36 (NCI-H1573, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -5.0 | 2e-04 | 13/35 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.602×** | -4.7 | 5e-04 | 17/37 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.399×** | -4.4 | 0.001 | 15/28 (NCI-H23, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.656×** | -3.9 | 0.011 | 19/37 (SW480, NCI-H1573, …) | two highest doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.672×** | -3.7 | 0.022 | 9/36 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.680×** | -3.6 | 0.026 | 7/37 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.682×** | -3.5 | 0.026 | 16/36 (SW 900, A549, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.683×** | -3.5 | 0.026 | 3/36 (LS 180, C-33 A, …) | two highest doses |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.670×** | -3.4 | 0.034 | 8/35 (RKO, SW48, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.693×** | -3.4 | 0.036 | 14/38 (SW480, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.707×** | -3.2 | 0.061 | 9/35 (NCI-H1573, A549, …) | two highest doses |  |
| [[Tirabrutinib (drug)]] 5 µM |  | **0.705×** | -3.1 | 0.080 | 2/36 (COLO 205, RKO) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.084 | 11/36 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.720×** | -3.0 | 0.086 | 9/36 (A-172, NCI-H1792, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.086 | 7/36 (BT-474, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.4 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0970× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0406× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.3) |
| [[A-172 (line)]] | wt | 3.28 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +12.7) | [[Loperamide (hydrochloride) (drug)]] 0.5 µM 0.0607× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0733× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 7.19 | 0 | 2 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0823× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0929× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 4.50 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0880× (z -9.0) |
| [[HOP62 (line)]] | alt | 5.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 5.34 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0763× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0861× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSUH2]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[BMAL2-AS1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ITPR2-AS1]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[LINC02516]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TBILA]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[BMAL2]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 | STRING 656; ⚠ same locus (21.4 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM236]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NEK10]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TIAM2]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CEACAM19]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA4]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[EFNA3]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[KANTR]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[BAG4]] | -0.58 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.57 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[IFT172]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PRKRA]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SNAPC3]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MED23]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.55 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[L2HGDH]] | -0.55 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LIX1L]] | -0.55 | -0.60 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00707]] | B | LINC00707 activity raises SMCO2's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 1.77× lower at baseline in the lines without LINC00707 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[LTBP2]] | B | LTBP2 activity raises SMCO2's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without LTBP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[GCAWKR]] | B | GCAWKR activity raises SMCO2's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without GCAWKR | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[GPR39]] | C | GPR39 activity raises SMCO2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without GPR39 | 0.062 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3; co-absent with the target |
| [[BMAL2]] | C | BMAL2 activity raises SMCO2's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMAL2-AS1]] | B | SMCO2 activity raises BMAL2-AS1's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.006 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[CDKL4]] | B | SMCO2 activity raises CDKL4's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.006 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[LINC01191]] | B | SMCO2 activity raises LINC01191's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.46× lower at baseline in the lines without SMCO2 | 0.010 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[ABHD12]] | B | SMCO2 activity lowers ABHD12's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without SMCO2 | 0.012 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[KANTR]] | B | SMCO2 activity lowers KANTR's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.78× higher at baseline in the lines without SMCO2 | 0.040 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[L2HGDH]] | B | SMCO2 activity lowers L2HGDH's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.17× higher at baseline in the lines without SMCO2 | 0.048 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[RIPK2-DT]] | B | SMCO2 activity raises RIPK2-DT's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without SMCO2 | 0.060 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[OIT3]] | B | SMCO2 activity raises OIT3's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without SMCO2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[ZDHHC14]] | B | SMCO2 activity lowers ZDHHC14's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.88× higher at baseline in the lines without SMCO2 | 0.070 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[MYOCOS]] | B | SMCO2 activity raises MYOCOS's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.074 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[PGM5P2-1]] | B | SMCO2 activity raises PGM5P2-1's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without SMCO2 | 0.078 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[TMEM236]] | B | SMCO2 activity raises TMEM236's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without SMCO2 | 0.081 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, -10.1); signed map (22.5, 5.7). **Vector** length 82.8, 16.8% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.9 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.7 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | single-pass membrane protein with coiled-coil domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:27,446,736-27,502,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC341346; previously C12orf70 |
| Matched by | ensembl_id |

UniProt [A6NFE2](https://www.uniprot.org/uniprotkb/A6NFE2) carries no function annotation.

**Summary**, from NCBI Gene [341346](https://www.ncbi.nlm.nih.gov/gene/341346):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34448) · Entrez [341346](https://www.ncbi.nlm.nih.gov/gene/341346) · UniProt [A6NFE2](https://www.uniprot.org/uniprotkb/A6NFE2) · Ensembl [ENSG00000165935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165935)

## Data

Gene col 9212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9212); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9212]; `tensor/DDL_lfc|DDL_z.npy` [9212]; `embed/gene_vectors.npy` [9212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9212 or target_col == 9212). Every well: [[SMCO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMCO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
