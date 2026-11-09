---
symbol: "CSRNP2"
type: "gene"
col: 3181
ensembl_id: "ENSG00000110925"
name: "cysteine and serine rich nuclear protein 2"
location: "12q13.12"
module: 148
arm: "+"
pooled_cpm: 25.27
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# CSRNP2

*cysteine and serine rich nuclear protein 2* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +22.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.725× (z -4.5, q 0.003, down in 23 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.814× (z -4.1, q 0.008, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.165×, A498 0.185×, C32 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0615×, AN3 CA 0.0886×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.139×, Hs 766T 0.170×; ⚠ toxic; transcription drop); [[Vilanterol (drug)]] 0.5 µM in 1 line (H4 0.0808×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.122×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEPCE]] (+0.68, fdr 1e-05), [[ATXN1L]] (+0.67, fdr 8e-05), [[EIF5]] (+0.65, fdr 4e-05); moves opposite to [[MNAT1]] (-0.63, fdr 1e-05), [[HMGN3]] (-0.62, fdr 4e-05), [[RFC1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +22.4 | 0e+00 | 45/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +17.7 | 0e+00 | 41/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +14.7 | 0e+00 | 45/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +13.6 | 6e-40 | 40/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +10.4 | 3e-23 | 42/46 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +8.5 | 2e-15 | 35/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +8.2 | 2e-14 | 37/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +7.0 | 1e-10 | 31/48 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +6.4 | 8e-09 | 39/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 1e-08 | 25/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +6.1 | 7e-08 | 29/47 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.7 | 6e-07 | 1/48 (NCI-H460) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.2 | 8e-06 | 27/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.28×** | +4.9 | 4e-05 | 27/48 (SW480, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 24/48 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 1e-04 | 25/48 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 18/47 (A498, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.046 | 17/47 (H4, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3181.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H460 0.165×, A498 0.185×, C32 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0615×, AN3 CA 0.0886×); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.139×, Hs 766T 0.170×; ⚠ toxic; transcription drop); [[Vilanterol (drug)]] 0.5 µM in 1 line (H4 0.0808×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.122×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.725×** | -4.5 | 0.003 | 23/47 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.729×** | -4.4 | 0.003 | 24/43 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.814×** | -4.1 | 0.008 | 21/48 (C32, AsPC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.609×** | -3.6 | 0.041 | 14/31 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.773×** | -3.5 | 0.057 | 15/35 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.626×** | -3.4 | 0.057 | 17/47 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.3 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +15.7) | [[Lonafarnib (drug)]] 5 µM 0.0761× (z -12.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 19.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +16.1) | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 19.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 16.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 24.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 20.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 25.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +15.0) | — |
| [[C32 (line)]] | wt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 18.7 | 0 | 2 | — | [[Vilanterol (drug)]] 0.5 µM 0.0808× (z -11.1) |
| [[HCT15 (line)]] | alt | 20.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +8.7) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.122× (z -9.2) |
| [[Hs 766T (line)]] | wt | 16.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +13.1) | — |
| [[LoVo (line)]] | wt | 30.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 25.1 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 31.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.5) | — |
| [[SW48 (line)]] | wt | 17.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.153× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 33.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.7) | — |
| [[A549 (line)]] | wt | 19.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +13.6) | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0886× (z -9.4) |
| [[BT-474 (line)]] | alt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0615× (z -14.8) |
| [[HT-29 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.3) | — |
| [[KATO III (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.9) | — |
| [[RKO (line)]] | wt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.2) | — |
| [[A-427 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEPCE]] | +0.68 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.67 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[EIF5]] | +0.65 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[KRBOX5]] | +0.65 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[NXF1]] | +0.63 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CEP164]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[LINC01004]] | +0.62 | +0.66 / +0.32 | both halves | 1e-04 |  |
| [[C6orf62]] | +0.62 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[POLR2A]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[LINC00910]] | +0.61 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[HEXIM1]] | +0.61 | +0.67 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CABYR]] | +0.61 | +0.66 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNAT1]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.62 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[RFC1]] | -0.57 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SMYD3]] | -0.57 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[SPATA6]] | -0.56 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[GUSBP18]] | -0.56 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[SKIC3]] | -0.56 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SBF2]] | -0.55 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[NDUFB6]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[LRBA]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[C1QTNF3-AMACR]] | -0.53 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[RPP30]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSRNP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (20.7, -9.8); signed map (21.3, -7.9). **Vector** length 97.3, 24.0% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.0 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +22.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +13.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.0 | -0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.5 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | cysteine and serine rich nuclear protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:51,061,205-51,083,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C12ORF2, TAIP-12, PPP1R72; previously C12orf22, FAM130A1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H175](https://www.uniprot.org/uniprotkb/Q9H175) (Cysteine/serine-rich nuclear protein 2):

> Binds to the consensus sequence 5'-AGAGTG-3' and has transcriptional activator activity (By similarity). May play a role in apoptosis.

**Summary**, from NCBI Gene [81566](https://www.ncbi.nlm.nih.gov/gene/81566):

> The protein encoded by this gene belongs to the CSRNP family of nuclear proteins that share conserved regions, including cysteine- and serine- rich regions, a basic domain, a transcriptional activation domain, and bind the sequence 'AGAGTG', thus have the hallmark of transcription factors. Studies in mice suggest that these genes may have redundant functions. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:16006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16006) · Entrez [81566](https://www.ncbi.nlm.nih.gov/gene/81566) · UniProt [Q9H175](https://www.uniprot.org/uniprotkb/Q9H175) · Ensembl [ENSG00000110925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110925)

## Data

Gene col 3181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3181); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3181]; `tensor/DDL_lfc|DDL_z.npy` [3181]; `embed/gene_vectors.npy` [3181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3181 or target_col == 3181). Every well: [[CSRNP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRNP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
