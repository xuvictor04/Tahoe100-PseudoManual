---
symbol: "HABP4"
type: "gene"
col: 5149
ensembl_id: "ENSG00000130956"
name: "hyaluronan binding protein 4"
location: "9q22.32"
module: 24
arm: "+"
pooled_cpm: 32.46
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# HABP4

*hyaluronan binding protein 4* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.69× (z +24.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.600× (z -5.0, q 3e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMT2]] (+0.59, fdr 2e-05), [[FAM76A]] (+0.58, fdr 2e-05), [[GPX4]] (+0.58, fdr 1e-05); moves opposite to [[PSMD12]] (-0.56, fdr 1e-05), [[RAE1]] (-0.54, fdr 1e-04), [[SMU1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP3K21]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.69×** | +24.7 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.54×** | +23.9 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.22×** | +22.1 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +14.7 | 0e+00 | 34/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +14.0 | 1e-42 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +13.4 | 1e-38 | 38/47 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +11.6 | 5e-29 | 42/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.9 | 2e-21 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.58×** | +9.4 | 4e-19 | 43/48 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +8.8 | 5e-17 | 32/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +7.5 | 3e-12 | 27/45 (KATO III, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.3 | 1e-11 | 32/47 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +7.1 | 5e-11 | 27/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.88×** | +6.3 | 2e-08 | 32/47 (RKO, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +5.6 | 6e-07 | 22/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +5.2 | 7e-06 | 23/48 (KATO III, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.600×** | -5.0 | 3e-04 | 22/48 (RKO, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.7 | 6e-04 | 3/48 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.781×** | -4.4 | 0.002 | 17/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.821×** | -3.7 | 0.027 | 11/48 (SW480, A-172, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.880× | -3.4 | 0.060 | 6/48 (A549, NCI-H1573, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.060 | 8/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.887× | -3.2 | 0.10 | 15/48 (BT-474, Hs 766T, …) | top dose only | low cells (technical?) |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.889× | -3.1 | 0.10 | 5/48 (HT-29, A498, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | 0.729× | -3.1 | 0.10 | 11/43 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.10 | 8/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.11 | 10/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.3 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 5.24× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.435× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 18.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 18.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +9.9) | [[Simotinib (drug)]] 5 µM 0.161× (z -8.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 22.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 21.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.32× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 49.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 25.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 22.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +12.9) | — |
| [[KATO III (line)]] | alt | 26.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.59× (z +14.9) | — |
| [[LoVo (line)]] | wt | 19.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.15× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 31.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +16.2) | — |
| [[PANC-1 (line)]] | alt | 46.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 28.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.70× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.36× (z +10.0) | — |
| [[J82 (line)]] | alt | 47.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +12.8) | — |
| [[RKO (line)]] | wt | 47.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 30.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 40.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 86.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 39.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.211× (z -9.2) |
| [[A-172 (line)]] | wt | 87.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 52.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.2) | — |
| [[C32 (line)]] | wt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 8.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 17.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 47.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.25× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 65.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +8.5) | — |
| [[A-427 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMT2]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FAM76A]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[GPX4]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CAMTA1]] | +0.58 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[DOP1B]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[KIF3A]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[MTM1]] | +0.54 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[EPS15]] | +0.54 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[BCAS4]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PKN1]] | +0.53 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[CDKN2D]] | +0.52 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[MAP3K3]] | +0.52 | +0.39 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD12]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[RAE1]] | -0.54 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SMU1]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[NUBP1]] | -0.51 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[RABL3]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[TAF2]] | -0.51 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[TRMO]] | -0.51 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[YTHDF3]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[SUCLA2]] | -0.50 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[KLHL3]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CARD8]] | -0.50 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[MRPS7]] | -0.49 | -0.44 / -0.37 | both halves | 9e-05 | STRING 720 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K21]] | B | MAP3K21 activity lowers HABP4's level | lines that do not express MAP3K21 (11) vs lines expressing it (39) | 1.68× higher at baseline in the lines without MAP3K21 | 0.073 | ⚠ within organs, on part of the lines; also absent: PRSS16, KRT8, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.336). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.9, -22.0); signed map (-22.2, 13.3). **Vector** length 99.8, 25.8% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +8.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +3.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.5 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronan binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:96,450,169-96,491,336 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IHABP4, SERBP1L |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JVS0](https://www.uniprot.org/uniprotkb/Q5JVS0) (Intracellular hyaluronan-binding protein 4):

> Ribosome-binding protein that promotes ribosome hibernation, a process during which ribosomes are stabilized in an inactive state and preserved from proteasomal degradation (By similarity). Acts via its association with EEF2/eEF2 factor at the A-site of the ribosome, promoting ribosome stabilization in an inactive state compatible with storage (By similarity). Plays a key role in ribosome hibernation in the mature oocyte by promoting ribosome stabilization (By similarity). Ribosomes, which are …

**Summary**, from NCBI Gene [22927](https://www.ncbi.nlm.nih.gov/gene/22927):

> Enables SUMO binding activity. Involved in PML body organization; positive regulation of RNA splicing; and positive regulation of translational initiation. Located in several cellular components, including cytoplasmic stress granule; nuclear lumen; and nuclear membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17062) · Entrez [22927](https://www.ncbi.nlm.nih.gov/gene/22927) · UniProt [Q5JVS0](https://www.uniprot.org/uniprotkb/Q5JVS0) · Ensembl [ENSG00000130956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130956)

## Data

Gene col 5149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5149); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5149]; `tensor/DDL_lfc|DDL_z.npy` [5149]; `embed/gene_vectors.npy` [5149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5149 or target_col == 5149). Every well: [[HABP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HABP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
