---
symbol: "ATP6V1B2"
type: "gene"
col: 7180
ensembl_id: "ENSG00000147416"
name: "ATPase H+ transporting V1 subunit B2"
location: "8p21.3"
module: 45
arm: "+"
pooled_cpm: 29.87
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ATP6V1B2

*ATPase H+ transporting V1 subunit B2* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.42× (z +17.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.746× (z -4.2, q 0.016, down in 18 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.177×, RKO 0.261×, H4 0.135×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.129×, Panc 03.27 0.199×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.170×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FIG4]] (+0.65, fdr 7e-06), [[LTA4H]] (+0.63, fdr 1e-05), [[ARL8B]] (+0.61, fdr 1e-05); moves opposite to [[CRK]] (-0.55, fdr 2e-05), [[AGAP6]] (-0.55, fdr 2e-04), [[TASOR2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPNMB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.42×** | +17.3 | 0e+00 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +16.0 | 0e+00 | 41/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +13.2 | 3e-37 | 43/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +12.3 | 1e-32 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +10.6 | 2e-24 | 43/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +10.2 | 2e-22 | 43/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +10.0 | 2e-21 | 42/49 (RPMI-7951, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.04×** | +9.1 | 9e-18 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +8.7 | 3e-16 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.5 | 1e-15 | 36/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +8.2 | 2e-14 | 36/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +7.0 | 1e-10 | 30/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.7 | 9e-10 | 28/46 (NCI-H23, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +6.7 | 9e-10 | 32/47 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.7 | 1e-09 | 34/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.9 | 1e-07 | 31/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 9e-07 | 29/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7180.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-427 0.177×, RKO 0.261×, H4 0.135×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (KATO III 0.129×, Panc 03.27 0.199×; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SNU-1 0.170×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.746×** | -4.2 | 0.016 | 18/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.736×** | -4.0 | 0.016 | 17/41 (KATO III, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.799× | -3.2 | 0.24 | 10/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.803× | -3.1 | 0.24 | 12/48 (HT-29, HS-578T, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.806× | -3.1 | 0.24 | 15/48 (A498, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.6 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.50× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.51× (z +14.0) | — |
| [[KATO III (line)]] | alt | 30.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.04× (z +17.1) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -14.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 21.4 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.97× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 40.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +14.3) | — |
| [[RKO (line)]] | wt | 45.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +13.3) | — |
| [[A-172 (line)]] | wt | 43.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.9) | — |
| [[A-427 (line)]] | wt | 30.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +13.1) | — |
| [[A549 (line)]] | wt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.6) | — |
| [[J82 (line)]] | alt | 20.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.59× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.63× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.17× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.7 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 23.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +9.8) | — |
| [[H4 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.72× (z +9.4) | — |
| [[LoVo (line)]] | wt | 15.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.91× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 23.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 43.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 62.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.7× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.170× (z -10.1) |
| [[SNU-423 (line)]] | alt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 45.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIG4]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[LTA4H]] | +0.63 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[ARL8B]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PREPL]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GLMP]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[GM2A]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[OAZ2]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[VPS41]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SNX2]] | +0.56 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 | pathway: MITF-M-dependent gene expression |
| [[PSAP]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CREG1]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRK]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.55 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[TASOR2]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.54 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PPRC1]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[LRR1]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CDK11B]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[HAUS7]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MYO19]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PCSK7]] | -0.50 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[METTL2B]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPNMB]] | B | GPNMB activity raises ATP6V1B2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without GPNMB | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.1, -10.3); signed map (-33.1, -14.5). **Vector** length 65.3, 14.0% of its response variance represented; |z| ≥ 3 in 1,199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.3 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | -1.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | +7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:20,197,381-20,226,819 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VATB, Vma2, HO57; previously VPP3, ATP6B2 |
| Gene groups (HGNC) | V-type ATPase subunits; ATPase F1/V1 alpha/A and beta/B subunit family |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [P21281](https://www.uniprot.org/uniprotkb/P21281) (V-type proton ATPase subunit B, brain isoform):

> Non-catalytic subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [526](https://www.ncbi.nlm.nih.gov/gene/526):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A, three B, and two G …

**Accessions** — [HGNC:854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:854) · Entrez [526](https://www.ncbi.nlm.nih.gov/gene/526) · UniProt [P21281](https://www.uniprot.org/uniprotkb/P21281) · Ensembl [ENSG00000147416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147416)

## Data

Gene col 7180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7180); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7180]; `tensor/DDL_lfc|DDL_z.npy` [7180]; `embed/gene_vectors.npy` [7180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7180 or target_col == 7180). Every well: [[ATP6V1B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
