---
symbol: "RIOK2"
type: "gene"
col: 666
ensembl_id: "ENSG00000058729"
name: "RIO kinase 2"
location: "5q15"
module: 12
arm: "+"
pooled_cpm: 35.67
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RIOK2

*RIO kinase 2* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.10× (z +18.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.486× (z -12.0, q 3e-30, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.604× (z -11.8, q 7e-30, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (AsPC-1 0.227×, LoVo 0.365×, hTERT-HPNE 0.258×, RKO 0.426×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.0846×, A498 0.285×, A-427 0.226×, NCI-H2347 0.325×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.221×, A498 0.257×, NCI-H661 0.0325×, HCT15 0.104×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RP9]] (+0.82, fdr 7e-06), [[VIRMA]] (+0.78, fdr 7e-06), [[KBTBD7]] (+0.76, fdr 7e-06); moves opposite to [[PRDM10]] (-0.61, fdr 1e-05), [[HCFC1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.10×** | +18.9 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +18.4 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.81×** | +15.3 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.20×** | +10.1 | 5e-22 | 37/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.5 | 2e-15 | 40/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 5e-14 | 33/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.6 | 4e-09 | 25/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.4 | 2e-08 | 33/47 (J82, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 3e-08 | 26/48 (SNU-423, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +6.1 | 6e-08 | 25/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +4.0 | 0.003 | 17/48 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.006 | 16/48 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.008 | 18/48 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 19/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.058 | 7/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 666.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (AsPC-1 0.227×, LoVo 0.365×, hTERT-HPNE 0.258×, RKO 0.426×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.0846×, A498 0.285×, A-427 0.226×, NCI-H2347 0.325×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.221×, A498 0.257×, NCI-H661 0.0325×, HCT15 0.104×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.486×** | -12.0 | 3e-30 | 37/47 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -11.8 | 7e-30 | 40/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -11.5 | 3e-28 | 30/38 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.699×** | -5.5 | 6e-06 | 26/45 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -4.8 | 2e-04 | 24/48 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.7 | 0.018 | 20/48 (A498, H4, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.7 | 0.018 | 0/48 | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.826× | -3.2 | 0.11 | 12/48 (SW 1271, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 37.7 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.0) |
| [[SW480 (line)]] | alt | 42.0 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.0 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 69.2 | 1 | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.79× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.5) |
| [[RKO (line)]] | wt | 53.7 | 4 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.2) |
| [[A498 (line)]] | wt | 54.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.8) |
| [[HOP62 (line)]] | alt | 28.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.7) |
| [[Hs 766T (line)]] | wt | 39.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 41.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 48.3 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +12.3) | — |
| [[A549 (line)]] | wt | 29.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -11.9) |
| [[J82 (line)]] | alt | 27.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.29× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 39.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -18.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 32.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 28.5 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 55.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.47× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +10.9) | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0325× (z -13.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 25.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0763× (z -19.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0813× (z -9.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.78 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 924 |
| [[EBAG9]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[PHAX]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[TMEM216]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.73 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM10]] | -0.61 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.6, -7.7); signed map (-15.3, -9.3). **Vector** length 117, 32.6% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +18.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.4 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +18.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +15.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -8.2 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -11.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RIO kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:97,160,867-97,183,247 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11159 |
| Gene groups (HGNC) | Ribosome biogenesis factors; RIO kinase family |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVS4](https://www.uniprot.org/uniprotkb/Q9BVS4) (Serine/threonine-protein kinase RIO2):

> Serine/threonine-protein kinase involved in the final steps of cytoplasmic maturation of the 40S ribosomal subunit. Involved in export of the 40S pre-ribosome particles (pre-40S) from the nucleus to the cytoplasm. Its kinase activity is required for the release of NOB1, PNO1 and LTV1 from the late pre-40S and the processing of 18S-E pre-rRNA to the mature 18S rRNA. Regulates the timing of the metaphase-anaphase transition during mitotic progression, and its phosphorylation, most likely by PLK1, …

**Summary**, from NCBI Gene [55781](https://www.ncbi.nlm.nih.gov/gene/55781):

> Predicted to enable protein kinase activity. Involved in several processes, including positive regulation of rRNA processing; positive regulation of ribosomal small subunit export from nucleus; and regulation of mitotic metaphase/anaphase transition. Located in cytoplasm. Part of preribosome, small subunit precursor. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18999) · Entrez [55781](https://www.ncbi.nlm.nih.gov/gene/55781) · UniProt [Q9BVS4](https://www.uniprot.org/uniprotkb/Q9BVS4) · Ensembl [ENSG00000058729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058729)

## Data

Gene col 666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 666); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 666]; `tensor/DDL_lfc|DDL_z.npy` [666]; `embed/gene_vectors.npy` [666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 666 or target_col == 666). Every well: [[RIOK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIOK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
