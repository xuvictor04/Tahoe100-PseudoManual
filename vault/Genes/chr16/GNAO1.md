---
symbol: "GNAO1"
type: "gene"
col: 1493
ensembl_id: "ENSG00000087258"
name: "G protein subunit alpha o1"
location: "16q13"
module: 82
arm: "+"
pooled_cpm: 10.88
n_lines_expressing: 28
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 20
direction_downstream: 25
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# GNAO1

*G protein subunit alpha o1* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.02× (z +21.3, q 0e+00, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.507× (z -9.3, q 1e-17, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOVA2]] (+0.72, fdr 7e-06), [[JAKMIP1]] (+0.71, fdr 7e-06), [[SEPTIN3]] (+0.66, fdr 7e-06); moves opposite to [[AMY2B]] (-0.52, fdr 1e-04), [[NEK11]] (-0.46, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ADAM22]] → it (grade B ⚠); 25 go from it, the strongest it → [[ADAM22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.02×** | +21.3 | 0e+00 | 23/25 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.21×** | +15.9 | 0e+00 | 23/24 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.96×** | +14.8 | 0e+00 | 22/24 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.86×** | +14.3 | 2e-44 | 20/24 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +14.1 | 8e-43 | 19/24 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +12.8 | 9e-36 | 20/24 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +10.5 | 5e-24 | 7/25 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.23×** | +8.4 | 5e-15 | 20/25 (NCI-H460, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +7.7 | 1e-12 | 19/23 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.9 | 2e-10 | 4/19 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.5 | 2e-06 | 1/13 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Brivudine (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 5/24 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.004 | 3/24 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.014 | 12/24 (C32, BT-474, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.015 | 8/24 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.030 | 8/24 (PANC-1, J82, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.033 | 7/24 (SK-MEL-2, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -9.3 | 1e-17 | 20/25 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -7.7 | 4e-12 | 15/24 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.546×** | -7.6 | 5e-12 | 17/24 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -6.8 | 1e-09 | 17/24 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -6.5 | 9e-09 | 17/24 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -5.8 | 6e-07 | 15/24 (C32, RPMI-7951, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.666×** | -5.6 | 2e-06 | 13/24 (SNU-1, PANC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -5.0 | 3e-05 | 15/24 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.711×** | -4.7 | 2e-04 | 12/23 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -4.3 | 9e-04 | 12/22 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.731×** | -4.3 | 0.001 | 11/25 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -3.9 | 0.005 | 14/23 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.757×** | -3.8 | 0.006 | 5/24 (RPMI-7951, BT-474, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.774×** | -3.5 | 0.019 | 7/24 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.783×** | -3.3 | 0.031 | 15/23 (A-427, PANC-1, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.789×** | -3.0 | 0.100 | 1/24 (SW 1271) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.1 | 6 | 8 (4 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.91× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -22.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -15.2) |
| [[A-427 (line)]] | wt | 42.8 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -17.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0539× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 29.1 | 1 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.56× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.130× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 2.75 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 19.1× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0420× (z -10.6) |
| [[C32 (line)]] | wt | 25.0 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0913× (z -12.3) |
| [[SW480 (line)]] | alt | 9.82 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.68× (z +12.0) | [[Harringtonine (drug)]] 5 µM 0.161× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -9.5) |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0724× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 10.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +13.6) | — |
| [[A498 (line)]] | wt | 4.36 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 6.01 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.10× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.68× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.154× (z -8.8) |
| [[SHP-77 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0489× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOVA2]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SEPTIN3]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LPAR3]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LMX1B]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ADCY1]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[STOX2]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TMEM108]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[VASH1]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF536]] | +0.61 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[SYN2]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RAB6B]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMY2B]] | -0.52 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[NEK11]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 8, C 12. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | ADAM22 activity raises GNAO1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without ADAM22 | 0.014 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[SCN8A]] | B | SCN8A activity raises GNAO1's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.44× lower at baseline in the lines without SCN8A | 0.041 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[SEMA6B]] | B | SEMA6B activity raises GNAO1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.30× lower at baseline in the lines without SEMA6B | 0.052 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NRG2]] | B | NRG2 activity raises GNAO1's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 3.23× lower at baseline in the lines without NRG2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B |
| [[TRIM9]] | B | TRIM9 activity raises GNAO1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without TRIM9 | 0.056 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[EBF2]] | B | EBF2 activity raises GNAO1's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without EBF2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises GNAO1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without FAM78B | 0.084 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[MYT1]] | B | MYT1 activity raises GNAO1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without MYT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[FSD1]] | C | FSD1 activity raises GNAO1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 4.09× lower at baseline in the lines without FSD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises GNAO1's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.89× lower at baseline in the lines without SLC6A17 | 0.009 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises GNAO1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without CTNNA2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[SDK2]] | C | SDK2 activity raises GNAO1's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 3.64× lower at baseline in the lines without SDK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 13, C 12. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | GNAO1 activity raises ADAM22's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without GNAO1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[KCNQ2]] | B | GNAO1 activity raises KCNQ2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without GNAO1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[KIF26A]] | B | GNAO1 activity raises KIF26A's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without GNAO1 | 0.033 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[PPM1E]] | B | GNAO1 activity raises PPM1E's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without GNAO1 | 0.042 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[FBXO27]] | B | GNAO1 activity raises FBXO27's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without GNAO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[SCN8A]] | B | GNAO1 activity raises SCN8A's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.86× lower at baseline in the lines without GNAO1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[SNTG2]] | B | GNAO1 activity raises SNTG2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without GNAO1 | 0.074 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[NRG2]] | B | GNAO1 activity raises NRG2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.63× lower at baseline in the lines without GNAO1 | 0.084 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[CACNA1C]] | B | GNAO1 activity raises CACNA1C's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without GNAO1 | 0.086 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[EBF2]] | B | GNAO1 activity raises EBF2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.74× lower at baseline in the lines without GNAO1 | 0.087 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[WASF3]] | B | GNAO1 activity raises WASF3's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without GNAO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[PTPRS]] | B | GNAO1 activity raises PTPRS's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without GNAO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.0, 39.5); signed map (26.9, 28.2). **Vector** length 74.8, 19.2% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +15.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.5 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.1 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.7 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha o1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,189,660-56,357,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | G-ALPHA-o |
| Gene groups (HGNC) | G protein subunits alpha, group i; MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Ca2+ pathway; Beta-catenin independent WNT signaling; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [P09471](https://www.uniprot.org/uniprotkb/P09471) (Guanine nucleotide-binding protein G(o) subunit alpha):

> Guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades, such as regulation of postsynaptic neurotransmitter release. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP …

**Summary**, from NCBI Gene [2775](https://www.ncbi.nlm.nih.gov/gene/2775):

> The protein encoded by this gene represents the alpha subunit of the Go heterotrimeric G-protein signal-transducing complex. Defects in this gene are a cause of early-onset epileptic encephalopathy. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:4389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4389) · Entrez [2775](https://www.ncbi.nlm.nih.gov/gene/2775) · UniProt [P09471](https://www.uniprot.org/uniprotkb/P09471) · Ensembl [ENSG00000087258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087258)

## Data

Gene col 1493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1493); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1493]; `tensor/DDL_lfc|DDL_z.npy` [1493]; `embed/gene_vectors.npy` [1493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1493 or target_col == 1493). Every well: [[GNAO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
