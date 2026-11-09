---
symbol: "QTRT2"
type: "gene"
col: 7538
ensembl_id: "ENSG00000151576"
name: "queuine tRNA-ribosyltransferase accessory subunit 2"
location: "3q13.31"
module: 1
arm: "+"
pooled_cpm: 34.95
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# QTRT2

*queuine tRNA-ribosyltransferase accessory subunit 2* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +19.7, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.716× (z -10.2, q 1e-21, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRTO4]] (+0.77, fdr 7e-06), [[UTP15]] (+0.77, fdr 7e-06), [[DDX31]] (+0.76, fdr 7e-06); moves opposite to [[SPAG9]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +19.7 | 0e+00 | 44/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.26×** | +18.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +17.5 | 0e+00 | 43/47 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.47×** | +16.8 | 0e+00 | 42/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +14.0 | 2e-42 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +12.5 | 6e-34 | 39/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +11.1 | 1e-26 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +11.1 | 1e-26 | 37/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +10.8 | 2e-25 | 37/48 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +10.7 | 4e-25 | 40/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +10.0 | 7e-22 | 32/46 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +9.9 | 1e-21 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +9.6 | 4e-20 | 37/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +8.3 | 3e-15 | 31/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.9 | 7e-14 | 24/48 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +7.7 | 3e-13 | 32/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +7.1 | 4e-11 | 25/48 (NCI-H2347, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.8 | 4e-10 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.4 | 1e-06 | 20/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -10.2 | 1e-21 | 38/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.699×** | -7.7 | 3e-12 | 28/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.835× | -3.9 | 0.018 | 20/46 (HEC-1-A, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.840× | -3.8 | 0.021 | 12/47 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -3.5 | 0.054 | 16/38 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.870× | -3.4 | 0.058 | 9/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.062 | 14/47 (C32, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.071 | 9/48 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.883× | -3.2 | 0.084 | 6/48 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.10 | 14/48 (A-427, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 53.3 | 8 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.59× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 27.1 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +10.1) | — |
| [[SW480 (line)]] | alt | 47.3 | 5 | 1 | [[TAK-901 (drug)]] 5 µM 7.00× (z +14.1) | [[Tucidinostat (drug)]] 5 µM 0.644× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 52.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 25.6 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.85× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 11.7× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 25.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 28.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 32.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +10.3) | — |
| [[RKO (line)]] | wt | 43.4 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.48× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 60.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.11× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +9.9) | — |
| [[H4 (line)]] | wt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 35.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.3) | [[XRK3F2 (drug)]] 0.5 µM 0.0716× (z -12.0) |
| [[SHP-77 (line)]] | alt | 44.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 45.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.08× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.6) | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.545× (z -9.0) |
| [[A549 (line)]] | wt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 33.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 18.5× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.0) | — |
| [[J82 (line)]] | alt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +8.5) | — |
| [[KATO III (line)]] | alt | 29.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.67× (z +9.2) | — |
| [[LoVo (line)]] | wt | 23.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.98× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 31.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.16× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 33.1 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 10.5× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +9.0) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 46.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.54× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTO4]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[UTP15]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[DDX31]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.74 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[NOL11]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[BYSL]] | +0.72 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[LTV1]] | +0.72 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.71 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[IMP4]] | +0.71 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[FARS2]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[DHX37]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.1, -37.2); signed map (1.9, -40.7). **Vector** length 91.4, 24.1% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +17.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +16.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +10.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | queuine tRNA-ribosyltransferase accessory subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:114,005,833-114,088,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12960; previously QTRTD1 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H974](https://www.uniprot.org/uniprotkb/Q9H974) (Queuine tRNA-ribosyltransferase accessory subunit 2):

> Non-catalytic subunit of the queuine tRNA-ribosyltransferase (TGT) that catalyzes the base-exchange of a guanine (G) residue with queuine (Q) at position 34 (anticodon wobble position) in tRNAs with GU(N) anticodons (tRNA-Asp, -Asn, -His and -Tyr), resulting in the hypermodified nucleoside queuosine (7-(((4,5-cis-dihydroxy-2-cyclopenten-1-yl)amino)methyl)-7-deazaguanosine).

**Summary**, from NCBI Gene [79691](https://www.ncbi.nlm.nih.gov/gene/79691):

> This gene encodes a subunit of tRNA-guanine transglycosylase. tRNA-guanine transglycosylase is a heterodimeric enzyme complex that plays a critical role in tRNA modification by synthesizing the 7-deazaguanosine queuosine, which is found in tRNAs that code for asparagine, aspartic acid, histidine, and tyrosine. The encoded protein may play a role in the queuosine 5'-monophosphate salvage pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this …

**Accessions** — [HGNC:25771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25771) · Entrez [79691](https://www.ncbi.nlm.nih.gov/gene/79691) · UniProt [Q9H974](https://www.uniprot.org/uniprotkb/Q9H974) · Ensembl [ENSG00000151576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151576)

## Data

Gene col 7538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7538); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7538]; `tensor/DDL_lfc|DDL_z.npy` [7538]; `embed/gene_vectors.npy` [7538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7538 or target_col == 7538). Every well: [[QTRT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QTRT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
