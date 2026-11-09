---
symbol: "METTL8"
type: "gene"
col: 4447
ensembl_id: "ENSG00000123600"
name: "methyltransferase 8, tRNA N3-cytidine"
location: "2q31.1"
module: 5
arm: "+"
pooled_cpm: 41.41
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# METTL8

*methyltransferase 8, tRNA N3-cytidine* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.71× (z +9.8, q 5e-20, up in 40 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.58× (z +8.4, q 1e-14, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.342× (z -10.2, q 9e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRMT3]] (+0.75, fdr 7e-06), [[GNL3L]] (+0.72, fdr 7e-06), [[ITPA]] (+0.72, fdr 7e-06); moves opposite to [[PJA2]] (-0.65, fdr 1e-05), [[CASP9]] (-0.62, fdr 1e-05), [[FBXO33]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PJA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +9.8 | 5e-20 | 40/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 1e-14 | 36/47 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.8 | 2e-09 | 25/45 (NCI-H1792, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.7 | 3e-09 | 28/46 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.3 | 5e-08 | 22/40 (RPMI-7951, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.27×** | +6.2 | 6e-08 | 21/48 (C32, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.1 | 9e-08 | 23/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 29/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.38×** | +5.8 | 3e-07 | 26/47 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 2e-04 | 21/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 20/48 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 16/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.005 | 11/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.007 | 13/48 (A549, A-172, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.010 | 16/47 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.012 | 10/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.014 | 15/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.014 | 21/47 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.019 | 17/47 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.20× | +3.3 | 0.025 | 12/48 (HOP62, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.342×** | -10.2 | 9e-22 | 41/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.673×** | -7.2 | 1e-10 | 28/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -5.9 | 7e-07 | 27/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.741×** | -5.5 | 7e-06 | 26/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.760×** | -5.0 | 7e-05 | 24/47 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.782×** | -4.3 | 0.002 | 19/48 (PANC-1, A-427, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.661×** | -3.9 | 0.006 | 18/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.826×** | -3.5 | 0.035 | 21/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.065 | 11/46 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.838× | -3.1 | 0.11 | 11/48 (SW 1088, NCI-H2030, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 83.2 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.294× (z -10.5) |
| [[PANC-1 (line)]] | alt | 58.6 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.189× (z -11.8) |
| [[LS 180 (line)]] | wt | 42.6 | 3 (1 ⚠) | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.7) | [[Ixazomib citrate (drug)]] 0.5 µM 0.284× (z -10.1) |
| [[A-427 (line)]] | wt | 59.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.283× (z -14.0) |
| [[SW480 (line)]] | alt | 55.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 56.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.430× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 69.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.254× (z -9.8) |
| [[A549 (line)]] | wt | 54.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 15.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.56× (z +10.2) | — |
| [[LoVo (line)]] | wt | 33.3 | 1 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.418× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 86.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 44.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.88× (z +9.7) ⚠ toxic | — |
| [[A498 (line)]] | wt | 43.1 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0907× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 41.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -9.4) |
| [[HT-29 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 58.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -8.8) |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT3]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ITPA]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[UTP20]] | +0.71 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ATR]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[WDR4]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PUS1]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[CASP9]] | -0.62 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[FBXO33]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[RNASE4]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ANG]] | -0.60 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[MXD1]] | -0.59 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises METTL8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PCSK6]] | B | PCSK6 activity raises METTL8's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without PCSK6 | 0.086 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[TCN2]] | B | TCN2 activity lowers METTL8's level | lines that do not express TCN2 (12) vs lines expressing it (38) | 1.53× higher at baseline in the lines without TCN2 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRSS23, TMSB4X, ARHGAP23; maybe low, not absent |
| [[MVB12B]] | B | MVB12B activity raises METTL8's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without MVB12B | 0.098 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises METTL8's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.41× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PJA2]] | C | METTL8's natural level weakens PJA2's drug response | METTL8's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.11; direction not clear | 0.088 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.3, -33.8); signed map (0.3, -49.2). **Vector** length 127, 35.9% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 13); *ribosome biogenesis* (control, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.6 | +8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.1 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.0 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Pimitespib (drug)]] 5 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 8, tRNA N3-cytidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,315,746-171,434,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13984, TIP |
| Gene groups (HGNC) | 7BS N3-cytosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H825](https://www.uniprot.org/uniprotkb/Q9H825) (tRNA N(3)-cytidine methyltransferase METTL8, mitochondrial):

> Mitochondrial S-adenosyl-L-methionine-dependent methyltransferase that mediates N(3)-methylcytidine modification of residue 32 of the tRNA anticodon loop of mitochondrial tRNA(Ser)(UCN) and tRNA(Thr). N(3)-methylcytidine methylation modification regulates mitochondrial translation efficiency and is required for activity of the respiratory chain. N(3)-methylcytidine methylation of mitochondrial tRNA(Ser)(UCN) requires the formation of N(6)-dimethylallyladenosine(37) (i6A37) by TRIT1 as …

**Summary**, from NCBI Gene [79828](https://www.ncbi.nlm.nih.gov/gene/79828):

> Enables mRNA methyltransferase activity and tRNA (cytidine-N3)-methyltransferase activity. Involved in RNA metabolic process and positive regulation of mitochondrial translation. Is active in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25856) · Entrez [79828](https://www.ncbi.nlm.nih.gov/gene/79828) · UniProt [Q9H825](https://www.uniprot.org/uniprotkb/Q9H825) · Ensembl [ENSG00000123600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123600)

## Data

Gene col 4447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4447); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4447]; `tensor/DDL_lfc|DDL_z.npy` [4447]; `embed/gene_vectors.npy` [4447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4447 or target_col == 4447). Every well: [[METTL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
