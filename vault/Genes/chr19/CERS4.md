---
symbol: "CERS4"
type: "gene"
col: 1634
ensembl_id: "ENSG00000090661"
name: "ceramide synthase 4"
location: "19p13.2"
module: 20
arm: "-"
pooled_cpm: 17.39
n_lines_expressing: 33
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CERS4

*ceramide synthase 4* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +4.9, q 5e-04, up in 14 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 4.48×, PANC-1 4.78×, A498 2.32×, NCI-H2347 3.05×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.33×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.312× (z -16.9, q 0e+00, down in 25 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.576× (z -11.3, q 2e-27, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A11]] (+0.63, fdr 7e-06), [[ZSCAN18]] (+0.60, fdr 1e-05), [[PAOX]] (+0.57, fdr 1e-05); moves opposite to [[DR1]] (-0.51, fdr 3e-05), [[DPAGT1]] (-0.49, fdr 4e-05), [[TM9SF3]] (-0.48, fdr 2e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[EXO5-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1634.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 4.48×, PANC-1 4.78×, A498 2.32×, NCI-H2347 3.05×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 4.33×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.9 | 5e-04 | 14/30 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.3 | 0.27 | 7/31 (H4, NCI-H2030, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.17× | +3.2 | 0.27 | 5/31 (SHP-77, PANC-1, …) | top dose only |  |
| [[MK-3903 (drug)]] 5 µM |  | 1.50× | +3.1 | 0.27 | 1/31 (NCI-H460) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.312×** | -16.9 | 0e+00 | 25/28 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.407×** | -12.5 | 2e-33 | 18/21 (MIA PaCa-2, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.412×** | -11.9 | 3e-30 | 21/26 (A-172, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -11.3 | 2e-27 | 28/31 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.580×** | -7.6 | 4e-12 | 20/31 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.606×** | -7.0 | 3e-10 | 17/30 (HOP62, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.400×** | -6.9 | 3e-10 | 21/31 (HOP62, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.665×** | -5.7 | 1e-06 | 20/30 (NCI-H23, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.4 | 5e-06 | 13/31 (A-172, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -4.5 | 3e-04 | 15/31 (Panc 03.27, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.734×** | -4.5 | 4e-04 | 14/31 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.734×** | -4.5 | 4e-04 | 12/31 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.739×** | -4.4 | 5e-04 | 14/30 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **0.745×** | -4.2 | 9e-04 | 14/30 (NCI-H460, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.746×** | -4.2 | 9e-04 | 14/31 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.9 | 0.003 | 11/31 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.757×** | -3.9 | 0.004 | 10/31 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.1 | 0.044 | 10/31 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.804×** | -3.0 | 0.069 | 7/31 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.069 | 8/31 (NCI-H460, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0393× (z -30.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -14.9) |
| [[A-172 (line)]] | wt | 43.7 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +18.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0501× (z -24.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.195× (z -13.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A498 (line)]] | wt | 53.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -16.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.0) |
| [[C32 (line)]] | wt | 33.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.223× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -11.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.7) |
| [[PANC-1 (line)]] | alt | 10.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0357× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[NCI-H2347 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A11]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZSCAN18]] | +0.60 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PAOX]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PRRX2]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ZNF579]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[LHFPL4]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF316]] | +0.54 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[CROCCP2-1]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[DOCK6]] | +0.53 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[PWWP2B]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MAP2K7]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[DSTYK]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DPAGT1]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[TM9SF3]] | -0.48 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[XRCC5]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ILF2]] | -0.47 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[GPAA1]] | -0.46 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[ARF1]] | -0.46 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[UGGT1]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[TRIP13]] | -0.44 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[TXNDC5]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[FH]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.44 | -0.26 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CERS4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CBFA2T3]] | B | CBFA2T3 activity raises CERS4's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without CBFA2T3 | 0.057 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[DUSP15]] | C | DUSP15 activity raises CERS4's level | lines that do not express DUSP15 (15) vs lines expressing it (35) | 3.62× lower at baseline in the lines without DUSP15 | 0.031 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXO5-DT]] | B | CERS4 activity raises EXO5-DT's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without CERS4 | 0.041 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |
| [[ZNF559]] | B | CERS4 activity raises ZNF559's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without CERS4 | 0.050 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |
| [[PGBD1]] | B | CERS4 activity raises PGBD1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without CERS4 | 0.078 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |
| [[ARF1]] | B | CERS4 activity lowers ARF1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 1.13× higher at baseline in the lines without CERS4 | 0.089 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10 |
| [[KRBA1]] | C | CERS4 activity raises KRBA1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 3.23× lower at baseline in the lines without CERS4 | 0.028 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |
| [[ETNK2]] | C | CERS4 activity raises ETNK2's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without CERS4 | 0.062 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |
| [[FBXO17]] | C | CERS4 activity raises FBXO17's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 4.90× lower at baseline in the lines without CERS4 | 0.097 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, 26.2); signed map (-1.1, -12.7). **Vector** length 72.3, 16.3% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.5 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.0 | -7.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.7 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.4 | -4.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ceramide synthase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,206,736-8,262,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12089, Trh1; previously LASS4 |
| Gene groups (HGNC) | CERS class homeoboxes; Ceramide synthases |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA82](https://www.uniprot.org/uniprotkb/Q9HA82) (Ceramide synthase 4):

> Ceramide synthase that catalyzes formation of ceramide from sphinganine and acyl-CoA substrates, with high selectivity toward long and very-long chains (C18:0-C22:0) as acyl donor.

**Summary**, from NCBI Gene [79603](https://www.ncbi.nlm.nih.gov/gene/79603):

> Enables sphingosine N-acyltransferase activity. Involved in ceramide biosynthetic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23747) · Entrez [79603](https://www.ncbi.nlm.nih.gov/gene/79603) · UniProt [Q9HA82](https://www.uniprot.org/uniprotkb/Q9HA82) · Ensembl [ENSG00000090661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090661)

## Data

Gene col 1634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1634); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1634]; `tensor/DDL_lfc|DDL_z.npy` [1634]; `embed/gene_vectors.npy` [1634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1634 or target_col == 1634). Every well: [[CERS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
