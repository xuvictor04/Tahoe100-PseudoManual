---
symbol: "KNSTRN"
type: "gene"
col: 4935
ensembl_id: "ENSG00000128944"
name: "kinetochore localized astrin (SPAG5) binding protein"
location: "15q15.1"
module: 22
arm: "+"
pooled_cpm: 17.89
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KNSTRN

*kinetochore localized astrin (SPAG5) binding protein* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.86× (z +10.0, q 5e-21, up in 34 of 42 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +7.3, q 2e-11, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Cytarabine (drug)]] 5 µM: 0.629× (z -7.2, q 3e-10, down in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Ciclopirox (drug)]] 5 µM: 0.780× (z -5.7, q 2e-06, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB1]] (+0.91, fdr 7e-06), [[PLK1]] (+0.90, fdr 7e-06), [[AURKA]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.86×** | +10.0 | 5e-21 | 34/42 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.82×** | +9.3 | 5e-18 | 17/29 (A-172, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.50×** | +9.2 | 6e-18 | 26/47 (NCI-H2030, RKO, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.70×** | +8.6 | 2e-15 | 27/41 (HT-29, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.71×** | +8.3 | 1e-14 | 30/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.3 | 2e-11 | 25/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.36×** | +7.0 | 2e-10 | 28/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.11×** | +6.3 | 2e-08 | 24/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.43×** | +5.8 | 4e-07 | 22/47 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +5.7 | 8e-07 | 21/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.28×** | +5.6 | 1e-06 | 24/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.45×** | +5.5 | 2e-06 | 16/36 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 4e-06 | 21/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +5.1 | 1e-05 | 21/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.1 | 2e-05 | 20/46 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 1e-03 | 12/47 (HT-29, NCI-H23, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.001 | 14/46 (HOP62, NCI-H460, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.003 | 18/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.004 | 11/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.005 | 13/48 (HT-29, SW 900, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 12/47 (NCI-H460, LoVo, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 15/48 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.014 | 11/46 (HOP62, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[OTS514 (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.019 | 6/42 (SW480, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.020 | 14/48 (HOP62, SW1417, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.020 | 10/48 (HT-29, LoVo, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.629×** | -7.2 | 3e-10 | 29/47 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.689×** | -6.0 | 4e-07 | 27/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.780×** | -5.7 | 2e-06 | 21/48 (RPMI-7951, HOP62, …) | top dose only | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.704×** | -5.7 | 2e-06 | 23/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.717×** | -5.4 | 7e-06 | 21/48 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.791×** | -5.4 | 7e-06 | 21/48 (LS 180, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.533×** | -5.3 | 8e-06 | 20/47 (SHP-77, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.730×** | -5.1 | 2e-05 | 18/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.791×** | -5.1 | 2e-05 | 14/48 (NCI-H661, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.734×** | -5.0 | 3e-05 | 14/47 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.557×** | -4.9 | 4e-05 | 16/46 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.812×** | -4.8 | 8e-05 | 23/48 (HOP62, A-427, …) | all doses, flat | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -4.6 | 2e-04 | 16/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.761×** | -4.4 | 4e-04 | 13/47 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.835× | -4.1 | 0.001 | 17/48 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.774×** | -3.8 | 0.004 | 11/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.790×** | -3.6 | 0.009 | 12/47 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.801×** | -3.6 | 0.009 | 5/48 (C-33 A, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.040 | 7/47 (PANC-1, HOP62, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.778×** | -2.9 | 0.091 | 4/47 (KATO III, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Naproxen (drug)]] 0.05 µM 0.0473× (z -14.5) |
| [[A-172 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.305× (z -10.6) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0750× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0947× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.211× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0757× (z -11.2) |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB1]] | +0.91 | +0.89 / +0.93 | both halves | 7e-06 | STRING 609 |
| [[PLK1]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 660 |
| [[AURKA]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | STRING 541 |
| [[CCNB2]] | +0.87 | +0.85 / +0.90 | both halves | 7e-06 | STRING 437 |
| [[BUB1]] | +0.87 | +0.85 / +0.88 | both halves | 7e-06 | STRING 638 |
| [[TROAP]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 |  |
| [[DEPDC1]] | +0.86 | +0.88 / +0.88 | both halves | 7e-06 | STRING 411 |
| [[ASPM]] | +0.86 | +0.84 / +0.88 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.85 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[CDKN3]] | +0.84 | +0.88 / +0.87 | both halves | 7e-06 | STRING 452 |
| [[DLGAP5]] | +0.84 | +0.84 / +0.89 | both halves | 7e-06 | STRING 628 |
| [[CDC20]] | +0.84 | +0.86 / +0.85 | both halves | 7e-06 | STRING 562 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KNSTRN's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without PIMREG | 0.031 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KNSTRN's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without NDC80 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises KNSTRN's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without PBK | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KNSTRN's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without AURKB | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises KNSTRN's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KNSTRN's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.3, -57.4); signed map (-51.4, -43.6). **Vector** length 115, 30.1% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.69 to 60); *DREAM G2/M down* (control, mean cos +0.80 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.65 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | +6.4 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +5.0 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +9.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.9 | +6.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.9 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.5 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +1.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.9 | +3.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -6.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.4 | -7.2 |
|  | [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.0 | -5.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.0 | -3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -3.8 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -3.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.0 | -5.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | kinetochore localized astrin (SPAG5) binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,382,721-40,394,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14502, SKAP, kinastrin, TRAF4AF1; previously C15orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y448](https://www.uniprot.org/uniprotkb/Q9Y448) (Small kinetochore-associated protein):

> Essential component of the mitotic spindle required for faithful chromosome segregation and progression into anaphase. Promotes the metaphase-to-anaphase transition and is required for chromosome alignment, normal timing of sister chromatid segregation, and maintenance of spindle pole architecture. The astrin (SPAG5)-kinastrin (SKAP) complex promotes stable microtubule-kinetochore attachments. Required for kinetochore oscillations and dynamics of microtubule plus-ends during live cell mitosis, …

**Summary**, from NCBI Gene [90417](https://www.ncbi.nlm.nih.gov/gene/90417):

> Enables microtubule plus-end binding activity and protein homodimerization activity. Involved in several processes, including cellular response to epidermal growth factor stimulus; mitotic sister chromatid segregation; and regulation of attachment of spindle microtubules to kinetochore. Located in kinetochore; microtubule cytoskeleton; and ruffle. Implicated in actinic keratosis and skin squamous cell carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30767) · Entrez [90417](https://www.ncbi.nlm.nih.gov/gene/90417) · UniProt [Q9Y448](https://www.uniprot.org/uniprotkb/Q9Y448) · Ensembl [ENSG00000128944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128944)

## Data

Gene col 4935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4935); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4935]; `tensor/DDL_lfc|DDL_z.npy` [4935]; `embed/gene_vectors.npy` [4935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4935 or target_col == 4935). Every well: [[KNSTRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KNSTRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
