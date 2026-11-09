---
symbol: "COQ6"
type: "gene"
col: 4112
ensembl_id: "ENSG00000119723"
name: "coenzyme Q6, monooxygenase"
location: "14q24.3"
module: 28
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# COQ6

*coenzyme Q6, monooxygenase* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +15.8, q 0e+00, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.787× (z -6.0, q 1e-06, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[palbociclib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0692×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.103×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H1573 0.146×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO8]] (+0.68, fdr 1e-05), [[TMEM128]] (+0.67, fdr 1e-05), [[XRCC1]] (+0.65, fdr 1e-05); moves opposite to [[TXN]] (-0.58, fdr 1e-05), [[PIP4K2A]] (-0.58, fdr 7e-05), [[LMBR1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +15.8 | 0e+00 | 35/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +12.6 | 1e-33 | 4/11 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +11.3 | 1e-27 | 27/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +9.4 | 9e-19 | 24/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.70×** | +9.3 | 2e-18 | 19/33 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.2 | 4e-18 | 24/43 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +8.8 | 9e-17 | 10/21 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.3 | 2e-11 | 17/35 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +5.9 | 3e-07 | 18/46 (KATO III, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.9 | 4e-05 | 13/47 (NCI-H2347, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 1e-04 | 12/47 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +3.9 | 0.005 | 9/46 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +3.8 | 0.006 | 2/47 (A-427, LoVo) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.008 | 5/44 (A549, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.4 | 0.027 | 1/14 (NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.059 | 3/47 (SW480, Panc 03.27, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.064 | 7/41 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.077 | 9/42 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.090 | 2/36 (NCI-H1573, KATO III) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[palbociclib (drug)]] 0.05 µM in 1 line (Hs 766T 0.0692×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.103×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (NCI-H1573 0.146×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -6.0 | 1e-06 | 18/48 (LS 180, SW1417, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.765×** | -4.7 | 6e-04 | 9/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.824× | -3.4 | 0.11 | 10/46 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Erythromycin (drug)]] 0.05 µM |  | 0.826× | -3.4 | 0.11 | 7/47 (A498, A-427, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.882× | -3.1 | 0.19 | 9/48 (NCI-H661, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.837× | -3.0 | 0.21 | 13/46 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.837× | -3.0 | 0.21 | 11/38 (NCI-H23, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.46 | 0 | 3 | — | [[palbociclib (drug)]] 0.05 µM 0.0692× (z -11.2) |
| [[HCT15 (line)]] | alt | 7.66 | 0 | 2 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0687× (z -8.6) |
| [[A498 (line)]] | wt | 6.22 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.233× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 7.22 | 0 | 1 | — | [[Niclosamide (olamine) (drug)]] 0.05 µM 0.0679× (z -8.6) |
| [[LoVo (line)]] | wt | 4.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 7.84 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.146× (z -9.5) |
| [[PANC-1 (line)]] | alt | 6.97 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 9.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.5) | — |
| [[A-172 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO8]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[XRCC1]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PPIE]] | +0.64 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[MKS1]] | +0.63 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SUPT20H]] | +0.62 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[GIN1]] | +0.60 | +0.74 / +0.29 | both halves | 3e-04 |  |
| [[IFT74]] | +0.60 | +0.65 / +0.43 | both halves | 4e-05 |  |
| [[HIRIP3]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[COPS5]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[COQ5]] | +0.59 | +0.69 / +0.39 | both halves | 6e-05 | pathway: Metabolism of cofactors; STRING 997 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.58 | -0.67 / -0.38 | both halves | 7e-05 |  |
| [[LMBR1]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[TMEM241]] | -0.54 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[NME2]] | -0.54 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[TPST2]] | -0.54 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[CMTM8]] | -0.53 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[ARHGAP8]] | -0.53 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[GARNL3]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[EDA]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.5, 5.6); signed map (7.1, -24.2). **Vector** length 54.2, 6.74% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.1 | +9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.1 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q6, monooxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,949,926-73,963,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-10 |
| Gene groups (HGNC) | Flavoproteins; Oxygenases |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Z9](https://www.uniprot.org/uniprotkb/Q9Y2Z9) (Ubiquinone biosynthesis monooxygenase COQ6, mitochondrial):

> FAD-dependent monooxygenase required for two non-consecutive steps during ubiquinone biosynthesis. Required for the C5-ring hydroxylation during ubiquinone biosynthesis by catalyzing the hydroxylation of 4-hydroxy-3-(all-trans-decaprenyl)benzoic acid to 3,4-dihydroxy-5-(all-trans-decaprenyl)benzoic acid. Also acts downstream of COQ4, for the C1-hydroxylation during ubiquinone biosynthesis by catalyzing the hydroxylation of 2-methoxy-6-(all-trans-decaprenyl)phenol to …

**Summary**, from NCBI Gene [51004](https://www.ncbi.nlm.nih.gov/gene/51004):

> The protein encoded by this gene belongs to the ubiH/COQ6 family. It is an evolutionarily conserved monooxygenase required for the biosynthesis of coenzyme Q10 (or ubiquinone), which is an essential component of the mitochondrial electron transport chain, and one of the most potent lipophilic antioxidants implicated in the protection of cell damage by reactive oxygen species. Knockdown of this gene in mouse and zebrafish results in decreased growth due to increased apoptosis. Mutations in this …

**Accessions** — [HGNC:20233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20233) · Entrez [51004](https://www.ncbi.nlm.nih.gov/gene/51004) · UniProt [Q9Y2Z9](https://www.uniprot.org/uniprotkb/Q9Y2Z9) · Ensembl [ENSG00000119723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119723)

## Data

Gene col 4112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4112); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4112]; `tensor/DDL_lfc|DDL_z.npy` [4112]; `embed/gene_vectors.npy` [4112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4112 or target_col == 4112). Every well: [[COQ6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
