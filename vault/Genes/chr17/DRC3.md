---
symbol: "DRC3"
type: "gene"
col: 10191
ensembl_id: "ENSG00000171962"
name: "dynein regulatory complex subunit 3"
location: "17p11.2"
module: 205
arm: "+"
pooled_cpm: 3.36
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# DRC3

*dynein regulatory complex subunit 3* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.42× (z +18.4, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.517× (z -7.0, q 2e-09, down in 19 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.667× (z -6.1, q 4e-07, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSCP1]] (+0.75, fdr 7e-06), [[CCDC157]] (+0.74, fdr 7e-06), [[RFX1]] (+0.70, fdr 7e-06); moves opposite to [[GPR180]] (-0.57, fdr 2e-05), [[USB1]] (-0.54, fdr 2e-05), [[PACC1]] (-0.53, fdr 6e-05).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.42×** | +18.4 | 0e+00 | 30/34 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +12.0 | 9e-31 | 24/31 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.06×** | +11.8 | 7e-30 | 36/45 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +9.4 | 8e-19 | 4/5 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +8.7 | 6e-16 | 16/32 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +8.4 | 5e-15 | 26/44 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.20×** | +8.3 | 6e-15 | 22/43 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 3e-09 | 5/14 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 6e-06 | 1/4 (PANC-1) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.2 | 9e-06 | 4/15 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.0 | 3e-05 | 15/42 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 10/28 (A498, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.007 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.009 | 7/44 (NCI-H23, A-172, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.018 | 4/43 (KATO III, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.019 | 6/35 (A549, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.020 | 7/36 (NCI-H2030, KATO III, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.027 | 2/40 (A-427, A549) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.056 | 3/38 (SW480, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.517×** | -7.0 | 2e-09 | 19/45 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.667×** | -6.1 | 4e-07 | 20/42 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -5.5 | 6e-06 | 14/45 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.638×** | -4.8 | 3e-04 | 12/45 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.436×** | -4.6 | 5e-04 | 9/32 (HT-29, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.614×** | -4.4 | 9e-04 | 11/39 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.660×** | -4.4 | 9e-04 | 12/36 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.573×** | -4.2 | 0.002 | 10/45 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.680×** | -4.1 | 0.003 | 11/38 (RPMI-7951, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.697×** | -3.8 | 0.008 | 16/40 (J82, SHP-77, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.702×** | -3.7 | 0.010 | 10/31 (HT-29, PANC-1, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.719×** | -3.5 | 0.022 | 6/41 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.710×** | -3.5 | 0.022 | 10/37 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.712×** | -3.4 | 0.029 | 3/37 (NCI-H1792, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.97 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.102× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 6.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 2.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 3.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 5.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 9.74 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0741× (z -10.9) |
| [[SW480 (line)]] | alt | 5.32 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.171× (z -8.9) |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSCP1]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[CCDC157]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[RFX1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[AK8]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MORN2]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[LRRC51]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CFAP69]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 | same gene group; STRING 461 |
| [[EFCAB6]] | +0.62 | +0.66 / +0.63 | both halves | 7e-06 | STRING 493 |
| [[KAT6B]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DNAJC27]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KIF9]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 | STRING 482 |
| [[MOK]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR180]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[USB1]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[PACC1]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[MCOLN2]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EEF1E1]] | -0.50 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[MTFR1]] | -0.50 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[TXN]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[KLHL8]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[POLR3G]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[GNPNAT1]] | -0.48 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[RUSC2]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PRRG1]] | -0.48 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.1, 20.2); signed map (-1.8, 7.1). **Vector** length 57.3, 8.26% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +18.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,972,813-18,016,889 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586M1120, CFAP134; previously LRRC48 |
| Gene groups (HGNC) | Dynein regulatory complex; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H069](https://www.uniprot.org/uniprotkb/Q9H069) (Dynein regulatory complex subunit 3):

> Component of the nexin-dynein regulatory complex (N-DRC) a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes.

**Summary**, from NCBI Gene [83450](https://www.ncbi.nlm.nih.gov/gene/83450):

> Predicted to be involved in flagellated sperm motility. Located in axoneme. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25384) · Entrez [83450](https://www.ncbi.nlm.nih.gov/gene/83450) · UniProt [Q9H069](https://www.uniprot.org/uniprotkb/Q9H069) · Ensembl [ENSG00000171962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171962)

## Data

Gene col 10191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10191); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10191]; `tensor/DDL_lfc|DDL_z.npy` [10191]; `embed/gene_vectors.npy` [10191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10191 or target_col == 10191). Every well: [[DRC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
