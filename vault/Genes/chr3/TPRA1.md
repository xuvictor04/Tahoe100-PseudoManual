---
symbol: "TPRA1"
type: "gene"
col: 8796
ensembl_id: "ENSG00000163870"
name: "transmembrane protein adipocyte associated 1"
location: "3q21.3"
module: 130
arm: "+"
pooled_cpm: 22.14
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# TPRA1

*transmembrane protein adipocyte associated 1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +20.7, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.691× (z -5.9, q 2e-06, down in 21 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.131×, SW1417 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.111×, PANC-1 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.276×, A-172 0.293×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.0894×); [[Silodosin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0820×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRC5C]] (+0.55, fdr 6e-05), [[JADE2]] (+0.55, fdr 3e-05), [[CCDC115]] (+0.53, fdr 1e-05); moves opposite to [[HARS1]] (-0.48, fdr 8e-05), [[KCTD20]] (-0.46, fdr 8e-05), [[DYNC1I1]] (-0.46, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +20.7 | 0e+00 | 44/46 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +13.8 | 5e-41 | 37/47 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.40×** | +7.2 | 9e-11 | 26/48 (A498, J82, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.1 | 2e-10 | 29/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.8 | 1e-09 | 26/46 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.6 | 3e-06 | 21/48 (HEC-1-A, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +5.3 | 1e-05 | 25/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 7e-04 | 17/45 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Menadione (drug)]] 5 µM |  | **1.33×** | +4.4 | 7e-04 | 22/47 (J82, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +4.4 | 7e-04 | 20/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 11/48 (J82, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.004 | 14/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +3.8 | 0.006 | 19/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.008 | 20/47 (KATO III, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-7648 (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.010 | 10/45 (NCI-H1573, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.023 | 12/48 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.030 | 19/47 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.131×, SW1417 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.111×, PANC-1 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.276×, A-172 0.293×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.0894×); [[Silodosin (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0820×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -5.9 | 2e-06 | 21/41 (A-427, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -4.6 | 0.001 | 14/31 (A-172, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +17.5) | — |
| [[SW1417 (line)]] | alt | 27.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 42.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 23.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.5) | — |
| [[J82 (line)]] | alt | 63.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.56× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.4) | — |
| [[A549 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0894× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 9.86 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0820× (z -9.4) |
| [[HOP62 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.2) | — |
| [[LoVo (line)]] | wt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 9.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[RKO (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +8.8) | — |
| [[SW480 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5C]] | +0.55 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[JADE2]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CCDC115]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TP53]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LNX2]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CHASERR]] | +0.50 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[GATA2]] | +0.50 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[WTAP]] | +0.50 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[TAPT1]] | +0.49 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CCNG2]] | +0.48 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[SUPV3L1]] | +0.48 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[CDIPT]] | +0.48 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HARS1]] | -0.48 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[KCTD20]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[DYNC1I1]] | -0.46 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[PCNX2]] | -0.46 | -0.13 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[EEFSEC]] | -0.44 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[MIR31HG]] | -0.43 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NAV3]] | -0.43 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[INTS7]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[PKIA]] | -0.42 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[CREB5]] | -0.42 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[TMTC3]] | -0.42 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[LINC01589]] | -0.42 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[HIF1AN]] | -0.42 | -0.26 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.7, -26.7); signed map (31.8, -24.3). **Vector** length 76.4, 13.3% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +20.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.9 | +3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein adipocyte associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,571,232-127,598,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TPRA40, FLJ32197, TMEM227; previously GPR175 |
| Gene groups (HGNC) | 7TM uncharacterized proteins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q86W33](https://www.uniprot.org/uniprotkb/Q86W33) carries no function annotation.

**Summary**, from NCBI Gene [131601](https://www.ncbi.nlm.nih.gov/gene/131601):

> Predicted to enable G protein-coupled receptor activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Predicted to act upstream of or within embryonic cleavage and negative regulation of mitotic cell cycle phase transition. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30413) · Entrez [131601](https://www.ncbi.nlm.nih.gov/gene/131601) · UniProt [Q86W33](https://www.uniprot.org/uniprotkb/Q86W33) · Ensembl [ENSG00000163870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163870)

## Data

Gene col 8796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8796); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8796]; `tensor/DDL_lfc|DDL_z.npy` [8796]; `embed/gene_vectors.npy` [8796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8796 or target_col == 8796). Every well: [[TPRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
