---
symbol: "DPY19L1"
type: "gene"
col: 10434
ensembl_id: "ENSG00000173852"
name: "dpy-19 like C-mannosyltransferase 1"
location: "7p14.2"
module: 149
arm: "+"
pooled_cpm: 133.31
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# DPY19L1

*dpy-19 like C-mannosyltransferase 1* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.17× (z +5.9, q 2e-06, up in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.15×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 9.91×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.557× (z -21.7, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STT3B]] (+0.61, fdr 7e-06), [[RANBP9]] (+0.58, fdr 1e-05), [[SESTD1]] (+0.57, fdr 4e-05); moves opposite to [[CCDC174]] (-0.65, fdr 7e-06), [[NFKBIL1]] (-0.62, fdr 1e-05), [[GOSR1]] (-0.61, fdr 1e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.15×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 9.91×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.9 | 2e-06 | 14/47 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +5.0 | 2e-04 | 20/46 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +4.2 | 0.004 | 13/48 (NCI-H2030, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.16× | +4.0 | 0.009 | 19/47 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | 1.16× | +3.9 | 0.011 | 20/48 (HOP62, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 1.16× | +3.9 | 0.011 | 19/46 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.10 | 11/47 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.10 | 6/47 (CFPAC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -21.7 | 0e+00 | 39/47 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -16.3 | 0e+00 | 40/47 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.637×** | -11.4 | 1e-27 | 34/47 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -9.5 | 3e-19 | 31/47 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.709×** | -9.0 | 2e-17 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -8.2 | 3e-14 | 2/49 (HOP62, SW 1271) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -8.0 | 1e-13 | 32/46 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.743×** | -7.8 | 5e-13 | 28/47 (AsPC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -7.1 | 7e-11 | 30/47 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.783×** | -6.4 | 9e-09 | 30/47 (AsPC-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -5.7 | 5e-07 | 20/47 (C32, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.828×** | -4.9 | 4e-05 | 24/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -4.1 | 0.002 | 18/48 (A549, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.754×** | -3.9 | 0.005 | 17/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.8 | 0.005 | 19/47 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.874× | -3.5 | 0.016 | 16/46 (Panc 03.27, AsPC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.874× | -3.3 | 0.035 | 18/46 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.894× | -2.9 | 0.093 | 14/47 (PANC-1, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 173 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -22.0) |
| [[NCI-H460 (line)]] | wt | 251 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -14.2) |
| [[A549 (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.3) |
| [[KATO III (line)]] | alt | 254 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.2) |
| [[LS 180 (line)]] | wt | 156 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -17.0) |
| [[SW48 (line)]] | wt | 186 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 309 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -13.5) |
| [[C32 (line)]] | wt | 144 | 1 | 2 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.15× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.564× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -18.3) |
| [[C-33 A (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 91.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -13.1) |
| [[Hs 766T (line)]] | wt | 157 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -20.7) |
| [[HT-29 (line)]] | alt | 109 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 87.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -19.4) |
| [[PANC-1 (line)]] | alt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -15.5) |
| [[SW1417 (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.412× (z -11.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 114 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.579× (z -9.7) |
| [[A-427 (line)]] | wt | 72.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.7) |
| [[BT-474 (line)]] | alt | 54.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.91× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.6) |
| [[COLO 205 (line)]] | alt | 93.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.1) |
| [[H4 (line)]] | wt | 212 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.1) |
| [[HCT15 (line)]] | alt | 62.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.6) |
| [[HOP62 (line)]] | alt | 92.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -10.0) |
| [[HS-578T (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.5) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.6) |
| [[SW 900 (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.6) |
| [[A-172 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*26 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | +0.61 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RANBP9]] | +0.58 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SESTD1]] | +0.57 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[ARHGEF26]] | +0.57 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ADAM15]] | +0.56 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ADD3]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PPP3CA]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 | same gene group |
| [[DIAPH1]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LBR]] | +0.54 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[STIM2]] | +0.54 | +0.27 / +0.51 | both halves | 3e-04 |  |
| [[LAPTM4B]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*74 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | -0.65 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.62 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[GOSR1]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[FCF1]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[MTERF4]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ZNF426]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.59 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ARL14EP]] | -0.59 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[TJAP1]] | -0.59 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[MAU2]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[BRAP]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[UTP23]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity raises DPY19L1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without ADD3 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[DHCR24]] | C | DHCR24 activity lowers DPY19L1's level | lines that do not express DHCR24 (4) vs lines expressing it (46) | 1.25× higher at baseline in the lines without DHCR24 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |
| [[SESTD1]] | C | SESTD1 activity raises DPY19L1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without SESTD1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction -0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.1, 5.0); signed map (-18.3, 19.0). **Vector** length 117, 31.2% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.3 | +2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | +5.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +3.9 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -21.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | dpy-19 like C-mannosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:34,927,292-35,038,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0877 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2PZI1](https://www.uniprot.org/uniprotkb/Q2PZI1) (Protein C-mannosyl-transferase DPY19L1):

> C-mannosyltransferase that mediates the C-mannosylation tryptophan residues on target proteins. The reaction occurs on the luminal side of the endoplasmic reticulum and involves the transfer of a mannose unit from a dolichylphosphate mannose (Dol-P-Man) donor to an acceptor protein containing a WxxW consensus sequence (By similarity). C-mannosylates the first two tryptophans in the WxxWxxWxxC motif in thrombospondin (TSP) type-1 of UNC5A (By similarity). Regulates neurite extension during …

**Summary**, from NCBI Gene [23333](https://www.ncbi.nlm.nih.gov/gene/23333):

> Predicted to enable mannosyltransferase activity. Predicted to be involved in protein C-linked glycosylation. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22205) · Entrez [23333](https://www.ncbi.nlm.nih.gov/gene/23333) · UniProt [Q2PZI1](https://www.uniprot.org/uniprotkb/Q2PZI1) · Ensembl [ENSG00000173852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173852)

## Data

Gene col 10434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10434); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10434]; `tensor/DDL_lfc|DDL_z.npy` [10434]; `embed/gene_vectors.npy` [10434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10434 or target_col == 10434). Every well: [[DPY19L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
