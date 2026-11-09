---
symbol: "SGTA"
type: "gene"
col: 2533
ensembl_id: "ENSG00000104969"
name: "small glutamine rich tetratricopeptide repeat co-chaperone alpha"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 27.46
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SGTA

*small glutamine rich tetratricopeptide repeat co-chaperone alpha* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.98× (z +12.0, q 1e-30, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW48 0.129×); [[Pemetrexed (drug)]] 5 µM in 1 line (hTERT-HPNE 0.199×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED16]] (+0.68, fdr 1e-05), [[MIER2]] (+0.64, fdr 7e-06), [[E2F4]] (+0.63, fdr 1e-05); moves opposite to [[CDC14A]] (-0.49, fdr 2e-05), [[ACVR2A]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +12.0 | 1e-30 | 41/47 (SW480, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +10.6 | 1e-23 | 38/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +9.9 | 8e-21 | 33/47 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +9.2 | 8e-18 | 34/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +8.3 | 2e-14 | 40/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.2 | 2e-14 | 31/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.60×** | +7.9 | 2e-13 | 20/37 (A-172, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.8 | 4e-13 | 32/47 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.53×** | +7.5 | 4e-12 | 27/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.4 | 9e-12 | 29/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +7.3 | 2e-11 | 37/47 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +7.2 | 3e-11 | 31/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +6.3 | 1e-08 | 31/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +6.1 | 4e-08 | 28/48 (SW480, RKO, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.41×** | +6.1 | 5e-08 | 25/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +5.9 | 1e-07 | 29/48 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 3e-07 | 29/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 3e-07 | 24/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.4 | 2e-06 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 3e-06 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 2e-04 | 21/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2533.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.113×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW48 0.129×); [[Pemetrexed (drug)]] 5 µM in 1 line (hTERT-HPNE 0.199×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.2 | 0.018 | 2/48 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.859× | -3.8 | 0.039 | 8/48 (A-172, SW480, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.832× | -3.3 | 0.21 | 14/47 (KATO III, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.821× | -3.1 | 0.26 | 13/48 (CHP-212, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.6 | 10 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.95× (z +15.7) | — |
| [[SW1417 (line)]] | alt | 37.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 28.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.0) | — |
| [[A-172 (line)]] | wt | 43.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.2) | — |
| [[A549 (line)]] | wt | 19.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 34.4 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.129× (z -11.6) |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.121× (z -8.8) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 21.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.48× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 21.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.29× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.199× (z -9.1) |
| [[LoVo (line)]] | wt | 26.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED16]] | +0.68 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[MIER2]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[E2F4]] | +0.63 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[BAP1]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.61 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[TBL3]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MFN2]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ANAPC2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CHFR]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NCDN]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[IPO13]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14A]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ACVR2A]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.8, -26.7); signed map (-11.9, -31.0). **Vector** length 69.4, 12.7% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.4 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.3 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | small glutamine rich tetratricopeptide repeat co-chaperone alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,754,715-2,783,362 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBP, SGT1, Vpu, hSGT, alphaSGT; previously SGT |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; GET4-GET5 transmembrane domain recognition complex subunits; Small glutamine rich tetratricopeptide repeat co-chaperone family |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43765](https://www.uniprot.org/uniprotkb/O43765) (Small glutamine-rich tetratricopeptide repeat-containing protein alpha):

> Co-chaperone that binds misfolded and hydrophobic patches-containing client proteins in the cytosol. Mediates their targeting to the endoplasmic reticulum but also regulates their sorting to the proteasome when targeting fails. Functions in tail-anchored/type II transmembrane proteins membrane insertion constituting with ASNA1 and the BAG6 complex a targeting module. Functions upstream of the BAG6 complex and ASNA1, binding more rapidly the transmembrane domain of newly synthesized proteins. It …

**Summary**, from NCBI Gene [6449](https://www.ncbi.nlm.nih.gov/gene/6449):

> This gene encodes a protein which is capable of interacting with the major nonstructural protein of parvovirus H-1 and 70-kDa heat shock cognate protein; however, its function is not known. Since this transcript is expressed ubiquitously in various tissues, this protein may serve a housekeeping function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10819) · Entrez [6449](https://www.ncbi.nlm.nih.gov/gene/6449) · UniProt [O43765](https://www.uniprot.org/uniprotkb/O43765) · Ensembl [ENSG00000104969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104969)

## Data

Gene col 2533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2533); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2533]; `tensor/DDL_lfc|DDL_z.npy` [2533]; `embed/gene_vectors.npy` [2533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2533 or target_col == 2533). Every well: [[SGTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
