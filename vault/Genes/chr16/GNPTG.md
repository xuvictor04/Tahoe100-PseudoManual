---
symbol: "GNPTG"
type: "gene"
col: 1630
ensembl_id: "ENSG00000090581"
name: "N-acetylglucosamine-1-phosphate transferase subunit gamma"
location: "16p13.3"
module: 122
arm: "+"
pooled_cpm: 21.78
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# GNPTG

*N-acetylglucosamine-1-phosphate transferase subunit gamma* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.40× (z +15.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.551× (z -10.3, q 6e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPNS1]] (+0.78, fdr 7e-06), [[CTSD]] (+0.68, fdr 7e-06), [[RAB5C]] (+0.66, fdr 7e-06); moves opposite to [[LACC1]] (-0.57, fdr 4e-05), [[ZNF620]] (-0.57, fdr 1e-05), [[COX18]] (-0.57, fdr 3e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +15.0 | 0e+00 | 47/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +12.2 | 5e-32 | 45/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +11.5 | 3e-28 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +10.4 | 3e-23 | 42/48 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +8.3 | 1e-14 | 27/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.8 | 8e-13 | 29/42 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.6 | 2e-12 | 23/32 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +5.8 | 4e-07 | 27/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +5.8 | 4e-07 | 18/36 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 9e-07 | 24/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 22/48 (LoVo, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +5.2 | 8e-06 | 24/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.5 | 3e-04 | 13/48 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 4e-04 | 22/46 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.002 | 17/45 (Hs 766T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.022 | 9/45 (SNU-423, HCT15, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.022 | 5/46 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.027 | 8/47 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.035 | 4/47 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -10.3 | 6e-22 | 38/47 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -9.2 | 8e-18 | 36/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -8.6 | 2e-15 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -8.4 | 6e-15 | 23/47 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -7.9 | 3e-13 | 37/48 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -6.1 | 8e-08 | 27/48 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -4.1 | 0.004 | 14/48 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.005 | 11/48 (A-427, NCI-H1573, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.033 | 7/48 (SW1417, NCI-H1573, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.033 | 18/46 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.0 | 0.13 | 16/48 (H4, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 43.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +12.2) | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.11× (z +13.1) | — |
| [[SW480 (line)]] | alt | 18.9 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.80× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.6) |
| [[A-427 (line)]] | wt | 24.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -15.8) |
| [[A498 (line)]] | wt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.262× (z -9.0) |
| [[LoVo (line)]] | wt | 15.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.5) |
| [[PANC-1 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.9) |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.4) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPNS1]] | +0.78 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[CTSD]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 | STRING 660 |
| [[RAB5C]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NAGPA]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 | STRING 985 |
| [[ILRUN]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[PTDSS2]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CLPTM1]] | +0.62 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[ATF6B]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ATPAF2]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[COMMD9]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RAB40B]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LACC1]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ZNF620]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[COX18]] | -0.57 | -0.68 / -0.28 | both halves | 3e-04 |  |
| [[SPDL1]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CYREN]] | -0.54 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[SS18]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZC3H12C]] | -0.53 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[C21orf91]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TRIM59]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[C9orf64]] | -0.52 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[RWDD2B]] | -0.52 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.1, -17.6); signed map (-49.8, -9.2). **Vector** length 94.8, 21.0% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +15.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.7 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.9 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylglucosamine-1-phosphate transferase subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,351,931-1,365,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAB56184, c316G12.3; previously GNPTAG, C16orf27 |
| Gene groups (HGNC) | MRH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJJ9](https://www.uniprot.org/uniprotkb/Q9UJJ9) (N-acetylglucosamine-1-phosphotransferase subunit gamma):

> Non-catalytic subunit of the N-acetylglucosamine-1-phosphotransferase complex, an enzyme that catalyzes the formation of mannose 6-phosphate (M6P) markers on high mannose type oligosaccharides in the Golgi apparatus. Binds and presents the high mannose glycans of the acceptor to the catalytic alpha and beta subunits (GNPTAB). Enhances the rate of N-acetylglucosamine-1-phosphate transfer to the oligosaccharides of acid hydrolase acceptors.

**Summary**, from NCBI Gene [84572](https://www.ncbi.nlm.nih.gov/gene/84572):

> This gene encodes the gamma sunbunit of the N-acetylglucosamine-1-phosphotransferase complex. This hexameric complex, composed of alpha, beta and gamma subunits, catalyzes the first step in synthesis of a mannose 6-phosphate lysosomal recognition marker. This enzyme complex is necessary for targeting of lysosomal hydrolases to the lysosome. Mutations in the gene encoding the gamma subunit have been associated with mucolipidosis IIIC, also known as mucolipidosis III gamma.[provided by RefSeq, …

**Accessions** — [HGNC:23026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23026) · Entrez [84572](https://www.ncbi.nlm.nih.gov/gene/84572) · UniProt [Q9UJJ9](https://www.uniprot.org/uniprotkb/Q9UJJ9) · Ensembl [ENSG00000090581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090581)

## Data

Gene col 1630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1630); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1630]; `tensor/DDL_lfc|DDL_z.npy` [1630]; `embed/gene_vectors.npy` [1630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1630 or target_col == 1630). Every well: [[GNPTG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNPTG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
