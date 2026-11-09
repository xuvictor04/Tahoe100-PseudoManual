---
symbol: "ACTG1"
type: "gene"
col: 11482
ensembl_id: "ENSG00000184009"
name: "actin gamma 1"
location: "17q25.3"
module: 46
arm: "-"
pooled_cpm: 716.2
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ACTG1

*actin gamma 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +7.2, q 3e-10, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.96× (z +7.0, q 5e-10, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.548× (z -8.9, q 3e-16, down in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (RKO 0.356×, NCI-H23 0.339×, HEC-1-A 0.393×, LoVo 0.309×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.275×, A-427 0.264×, NCI-H2347 0.354×, C-33 A 0.381×, …; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTB]] (+0.58, fdr 7e-06), [[DLGAP4]] (+0.57, fdr 4e-05), [[SMYD3]] (+0.57, fdr 1e-04); moves opposite to [[PNISR-AS1]] (-0.60, fdr 1e-04), [[HFE]] (-0.57, fdr 7e-05), [[LINC00869-1]] (-0.56, fdr 1e-04).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.11×** | +7.2 | 3e-10 | 44/49 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +7.0 | 5e-10 | 45/48 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +6.1 | 2e-07 | 47/48 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.17×** | +5.8 | 9e-07 | 48/48 (SW 900, LS 180, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.75×** | +5.7 | 2e-06 | 37/44 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.67×** | +5.2 | 2e-05 | 39/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.64×** | +5.0 | 4e-05 | 39/48 (C32, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +5.0 | 4e-05 | 44/48 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.60×** | +5.0 | 4e-05 | 40/47 (SW 900, NCI-H460, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.8 | 7e-05 | 39/48 (HS-578T, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 38/49 (CFPAC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +4.2 | 0.001 | 36/48 (NCI-H460, SW 900, …) | two highest doses |  |
| [[vincristine (drug)]] 5 µM |  | **2.07×** | +4.0 | 0.003 | 44/46 (LS 180, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 36/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.44×** | +3.9 | 0.004 | 40/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.014 | 32/49 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.014 | 39/48 (SHP-77, NCI-H460, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.020 | 33/48 (A-172, CHP-212, …) | all doses, stronger at high dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.024 | 41/48 (LOX-IMVI, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.024 | 39/47 (AN3 CA, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11482.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (RKO 0.356×, NCI-H23 0.339×, HEC-1-A 0.393×, LoVo 0.309×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.275×, A-427 0.264×, NCI-H2347 0.354×, C-33 A 0.381×, …; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -8.9 | 3e-16 | 37/49 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.695×** | -3.7 | 0.069 | 31/47 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.796× | -3.4 | 0.12 | 41/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.799× | -3.3 | 0.12 | 29/48 (SNU-1, BT-474, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.722× | -3.3 | 0.12 | 35/48 (NCI-H23, A-427, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.560× | -3.2 | 0.14 | 30/49 (LOX-IMVI, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.741× | -3.1 | 0.14 | 29/48 (BT-474, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.726× | -3.1 | 0.15 | 31/48 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.815× | -3.0 | 0.16 | 31/48 (NCI-H2030, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 338 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.35× (z +10.0) | — |
| [[C32 (line)]] | wt | 716 | 3 (2 ⚠) | 1 | [[Belumosudil (drug)]] 5 µM 3.15× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.9) |
| [[J82 (line)]] | alt | 625 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 754 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.08× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belumosudil (drug)]] 5 µM 2.76× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.8) |
| [[A498 (line)]] | wt | 330 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.15× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 1,415 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 376 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 251 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 673 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +10.1) | — |
| [[LoVo (line)]] | wt | 799 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -13.2) |
| [[LS 180 (line)]] | wt | 582 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.02× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 236 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SHP-77 (line)]] | alt | 558 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 437 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 820 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 521 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 690 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.8) |
| [[HCT15 (line)]] | alt | 384 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 1,217 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 1,789 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 1,264 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 369 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 452 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 883 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.84× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.524× (z -8.8) |
| [[A-172 (line)]] | wt | 419 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[BT-474 (line)]] | alt | 817 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.9) |
| [[H4 (line)]] | wt | 251 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 856 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -10.1) |
| [[HT-29 (line)]] | alt | 759 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 787 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 1,200 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 796 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 636 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 463 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 809 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 1,244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.5) |
| [[SW480 (line)]] | alt | 659 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.7) |
| [[AN3 CA (line)]] | alt | 610 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 816 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 827 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 446 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 589 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1,054 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 491 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 577 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 635 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 441 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 473 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTB]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |
| [[DLGAP4]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[SMYD3]] | +0.57 | +0.37 / +0.34 | both halves | 1e-04 |  |
| [[MFSD10]] | +0.56 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[TNFAIP8L1]] | +0.54 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[KCTD17]] | +0.54 | +0.34 / +0.36 | both halves | 1e-04 |  |
| [[MAPK8]] | +0.54 | +0.33 / +0.40 | both halves | 1e-04 | pathway: Leishmania infection |
| [[STUB1]] | +0.54 | +0.34 / +0.27 | both halves | 3e-04 |  |
| [[RRAS]] | +0.53 | +0.37 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_APICAL_JUNCTION |
| [[RABGAP1L]] | +0.53 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[RSU1]] | +0.53 | +0.44 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_APICAL_JUNCTION |
| [[RAB11FIP1]] | +0.53 | +0.35 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | -0.60 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[HFE]] | -0.57 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[LINC00869-1]] | -0.56 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[MAIP1]] | -0.56 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.56 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[TIAL1]] | -0.55 | -0.41 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PRR3]] | -0.55 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[C2orf42]] | -0.55 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[HSPA14]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[DHRS4]] | -0.54 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[HOXB7]] | -0.54 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[MED24]] | -0.54 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.0, 12.9); signed map (-18.2, 25.8). **Vector** length 131, 52.7% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.1 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.4 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.5 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.4 | -8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.8 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.4 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -6.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | actin gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,509,413-81,523,847 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ACTG, DFNA20, DFNA26 |
| Gene groups (HGNC) | Actins |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, APICAL_JUNCTION |
| Reactome | 70 pathways, smallest: Formation of annular gap junctions; Gap junction degradation; GBP-mediated host defense |
| Matched by | ensembl_id |

**Function**, from UniProt [P63261](https://www.uniprot.org/uniprotkb/P63261) (Actin, cytoplasmic 2):

> Actins are highly conserved proteins that are involved in various types of cell motility and are ubiquitously expressed in all eukaryotic cells. May play a role in the repair of noise-induced stereocilia gaps thereby maintains hearing sensitivity following loud noise damage (By similarity).

**Summary**, from NCBI Gene [71](https://www.ncbi.nlm.nih.gov/gene/71):

> Actins are highly conserved proteins that are involved in various types of cell motility and in maintenance of the cytoskeleton. Three main groups of actin isoforms have been identified in vertebrate animals: alpha, beta, and gamma. The alpha actins are found in muscle tissues and are a major constituent of the contractile apparatus. The beta and gamma actins co-exist in most cell types as components of the cytoskeleton and as mediators of internal cell motility. Actin gamma 1, encoded by this …

**Accessions** — [HGNC:144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:144) · Entrez [71](https://www.ncbi.nlm.nih.gov/gene/71) · UniProt [P63261](https://www.uniprot.org/uniprotkb/P63261) · Ensembl [ENSG00000184009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184009)

## Data

Gene col 11482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11482); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11482]; `tensor/DDL_lfc|DDL_z.npy` [11482]; `embed/gene_vectors.npy` [11482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11482 or target_col == 11482). Every well: [[ACTG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
