---
symbol: "CAV2"
type: "gene"
col: 2695
ensembl_id: "ENSG00000105971"
name: "caveolin 2"
location: "7q31.2"
module: 111
arm: "+"
pooled_cpm: 61.44
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CAV2

*caveolin 2* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.79× (z +22.2, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +5.4, q 9e-06, up in 22 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 3.53×, J82 4.33×, A549 5.08×, CFPAC-1 4.68×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 5.10×, A549 5.79×, PANC-1 3.19×, HEC-1-A 4.91×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.27×, MIA PaCa-2 2.65×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.509× (z -11.2, q 1e-26, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAV1]] (+0.71, fdr 7e-06, ⚠ same locus), [[ADAM9]] (+0.60, fdr 2e-05), [[DR1]] (+0.60, fdr 1e-05), [[CAPNS1]] (+0.60, fdr 1e-05); moves opposite to [[TAF6L]] (-0.58, fdr 1e-05), [[INTS4]] (-0.55, fdr 3e-05), [[CLASRP]] (-0.50, fdr 4e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TRIM58]] → it (grade B ⚠); 9 go from it, the strongest it → [[S100A10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 3.53×, J82 4.33×, A549 5.08×, CFPAC-1 4.68×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (J82 5.10×, A549 5.79×, PANC-1 3.19×, HEC-1-A 4.91×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.27×, MIA PaCa-2 2.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +22.2 | 0e+00 | 39/39 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +18.5 | 0e+00 | 34/34 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +14.6 | 1e-45 | 33/37 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.4 | 9e-06 | 22/40 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +5.2 | 2e-05 | 23/40 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.010 | 19/39 (A549, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.20 | 11/39 (SW480, HT-29, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -11.2 | 1e-26 | 31/40 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.561×** | -9.6 | 2e-19 | 28/40 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.656×** | -7.0 | 4e-10 | 24/40 (PANC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.653×** | -5.7 | 2e-06 | 23/40 (Hs 766T, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.714×** | -5.6 | 2e-06 | 23/40 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.802×** | -5.2 | 2e-05 | 21/40 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.573×** | -4.8 | 1e-04 | 20/37 (NCI-H1573, RPMI-7951, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.621×** | -4.1 | 0.003 | 21/40 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.018 | 17/40 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.800×** | -3.5 | 0.024 | 12/40 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.682×** | -3.3 | 0.047 | 9/41 (NCI-H1573, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.059 | 12/39 (LOX-IMVI, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 320 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -27.2) |
| [[Panc 03.27 (line)]] | alt | 118 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +14.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -14.9) |
| [[PANC-1 (line)]] | alt | 79.4 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +16.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -17.4) |
| [[Hs 766T (line)]] | wt | 236 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -18.1) |
| [[A-427 (line)]] | wt | 43.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 79.8 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.21× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.1) | — |
| [[A549 (line)]] | wt | 46.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +14.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 69.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +15.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.418× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 49.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.1) |
| [[A498 (line)]] | wt | 88.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 45.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.1) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.379× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 60.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 37.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.0) |
| [[SNU-423 (line)]] | alt | 41.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.18× (z +11.1) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.469× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 39.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.2) |
| [[A-172 (line)]] | wt | 68.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 93.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 53.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 47.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 27.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +11.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +12.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 59.6 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0618× (z -10.3) |
| [[SW1417 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 131 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAV1]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 | pathway: ESR-mediated signaling; STRING 999; ⚠ same locus (16.5 kb, same strand: neighbours can correlate without regulation) |
| [[ADAM9]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[DR1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CAPNS1]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TAGLN2]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RBM24]] | +0.57 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[LAMC1]] | +0.56 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[LEPROT]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CFL2]] | +0.55 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[YWHAZ]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[SLC39A10]] | +0.52 | +0.27 / +0.55 | both halves | 3e-04 |  |
| [[CAVIN1]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 | STRING 920 |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF6L]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[INTS4]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CLASRP]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RPP21]] | -0.50 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[GOT1]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[IQCB1]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[RPAIN]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[EPB41L4A-AS1]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SLC30A6]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PHKA2]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[DEPDC5]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[RBBP5]] | -0.46 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM58]] | B | TRIM58 activity raises CAV2's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.36× lower at baseline in the lines without TRIM58 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[SYNPO]] | B | SYNPO activity raises CAV2's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.03× lower at baseline in the lines without SYNPO | 0.072 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ANXA8]] | B | ANXA8 activity strengthens CAV2's drug response | lines that do not express ANXA8 (31) vs lines expressing it (9) | the lines without ANXA8 respond 0.62× as strongly (z diff +1.92); strongest at Panobinostat 5 µM: 0.58x vs 0.36x (z diff +3.9) | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; target measured in part of the lines; artifact flags |
| [[LINC02057]] | B | LINC02057 activity raises CAV2's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.39× lower at baseline in the lines without LINC02057 | 0.090 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[PLS3]] | C | PLS3 activity raises CAV2's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 5.18× lower at baseline in the lines without PLS3 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent; co-absent with the target |
| [[CAV1]] | C | CAV1 activity raises CAV2's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without CAV1 | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |
| [[MYOF]] | C | MYOF activity raises CAV2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.67× lower at baseline in the lines without MYOF | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2; co-absent with the target |
| [[ANXA2]] | C | ANXA2 activity raises CAV2's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 4.72× lower at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A10]] | B | CAV2 activity raises S100A10's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 2.78× lower at baseline in the lines without CAV2 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent |
| [[FH]] | B | CAV2 activity lowers FH's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 1.23× higher at baseline in the lines without CAV2 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent |
| [[TAGLN2]] | B | CAV2 activity raises TAGLN2's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without CAV2 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | B | CAV2, [[ENSG00000237813]] activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express CAV2, ENSG00000237813 (8) vs lines expressing them (40) | the lines without CAV2, ENSG00000237813: 0.62× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | CAV2, [[ENSG00000237813]] activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CAV2, ENSG00000237813 (8) vs lines expressing them (40) | the lines without CAV2, ENSG00000237813: 1.34× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent genes |
| [[PLS3]] | C | CAV2 activity raises PLS3's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without CAV2 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[ANXA2]] | C | CAV2 activity raises ANXA2's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 2.93× lower at baseline in the lines without CAV2 | 0.029 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[CAV1]] | C | CAV2 activity raises CAV1's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 7.52× lower at baseline in the lines without CAV2 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |
| [[MYOF]] | C | CAV2 activity raises MYOF's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 3.17× lower at baseline in the lines without CAV2 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-55.9, 6.3); signed map (12.6, 23.5). **Vector** length 93.8, 25.4% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +22.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +18.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.1 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.6 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -11.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | caveolin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,287,380-116,508,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAV |
| Gene groups (HGNC) | Caveolins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 3 pathways, smallest: Extra-nuclear estrogen signaling; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P51636](https://www.uniprot.org/uniprotkb/P51636) (Caveolin-2):

> May act as a scaffolding protein within caveolar membranes. Interacts directly with G protein alpha subunits and can functionally regulate their activity. Acts as an accessory protein in conjunction with CAV1 in targeting to lipid rafts and driving caveolae formation. The Ser-36 phosphorylated form has a role in modulating mitosis in endothelial cells. Positive regulator of cellular mitogenesis of the MAPK signaling pathway. Required for the insulin-stimulated nuclear translocation and …

**Summary**, from NCBI Gene [858](https://www.ncbi.nlm.nih.gov/gene/858):

> The protein encoded by this gene is a major component of the inner surface of caveolae, small invaginations of the plasma membrane, and is involved in essential cellular functions, including signal transduction, lipid metabolism, cellular growth control and apoptosis. This protein may function as a tumor suppressor. This gene and related family member (CAV1) are located next to each other on chromosome 7, and express colocalizing proteins that form a stable hetero-oligomeric complex. …

**Accessions** — [HGNC:1528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1528) · Entrez [858](https://www.ncbi.nlm.nih.gov/gene/858) · UniProt [P51636](https://www.uniprot.org/uniprotkb/P51636) · Ensembl [ENSG00000105971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105971)

## Data

Gene col 2695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2695); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2695]; `tensor/DDL_lfc|DDL_z.npy` [2695]; `embed/gene_vectors.npy` [2695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2695 or target_col == 2695). Every well: [[CAV2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAV2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
