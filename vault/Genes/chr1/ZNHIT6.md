---
symbol: "ZNHIT6"
type: "gene"
col: 3883
ensembl_id: "ENSG00000117174"
name: "zinc finger HIT-type containing 6"
location: "1p22.3"
module: 1
arm: "+"
pooled_cpm: 82.52
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZNHIT6

*zinc finger HIT-type containing 6* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +19.5, q 0e+00, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.574× (z -19.5, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIOK1]] (+0.76, fdr 7e-06), [[RBM28]] (+0.73, fdr 7e-06), [[AGK]] (+0.72, fdr 8e-06); moves opposite to [[SWT1]] (-0.63, fdr 1e-05), [[LRP10]] (-0.58, fdr 1e-05), [[MICALL2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +19.5 | 0e+00 | 35/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +15.1 | 0e+00 | 42/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +13.8 | 4e-41 | 38/47 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +10.1 | 9e-22 | 33/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +9.3 | 1e-18 | 37/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +6.5 | 6e-09 | 24/47 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.2 | 6e-08 | 26/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +6.0 | 1e-07 | 22/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.5 | 2e-06 | 22/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +5.3 | 8e-06 | 25/47 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +5.1 | 2e-05 | 24/47 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.1 | 2e-05 | 18/37 (Panc 03.27, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.9 | 4e-05 | 20/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +4.9 | 4e-05 | 19/47 (LoVo, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **1.23×** | +4.9 | 4e-05 | 22/46 (LoVo, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 14/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.007 | 16/47 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.015 | 13/47 (MIA PaCa-2, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.016 | 12/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -19.5 | 0e+00 | 40/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -6.4 | 4e-08 | 24/49 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.785×** | -6.0 | 3e-07 | 28/46 (NCI-H2030, PANC-1, …) | two highest doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -5.7 | 2e-06 | 23/47 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -5.0 | 5e-05 | 23/47 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.833×** | -4.4 | 0.001 | 20/46 (SW48, A498, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.828×** | -3.4 | 0.062 | 17/46 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Capmatinib (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.062 | 15/46 (A-427, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.873× | -3.3 | 0.062 | 20/44 (C-33 A, AsPC-1, …) | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.833×** | -3.3 | 0.062 | 19/47 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.913× | -3.2 | 0.062 | 12/47 (HOP62, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.835× | -3.2 | 0.063 | 12/47 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.886× | -3.0 | 0.11 | 11/47 (A-427, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 207 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +27.6) | — |
| [[CFPAC-1 (line)]] | alt | 59.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +21.8) | — |
| [[SW480 (line)]] | alt | 83.9 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 2.03× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -12.1) |
| [[A-427 (line)]] | wt | 76.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.7) | — |
| [[HEC-1-A (line)]] | alt | 97.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 105 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 88.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.8) | — |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.9) |
| [[A549 (line)]] | wt | 46.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.9) |
| [[HS-578T (line)]] | alt | 91.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.5) |
| [[LoVo (line)]] | wt | 72.0 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.75× (z +12.1) ⚠ toxic; cell-cycle shift, explains ~13% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.42× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 106 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +22.8) | — |
| [[AsPC-1 (line)]] | alt | 71.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.4) |
| [[HT-29 (line)]] | alt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +16.5) | — |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 4.14× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.2) |
| [[J82 (line)]] | alt | 79.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 51.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.14× (z +10.0) | — |
| [[RKO (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -19.8) |
| [[RPMI-7951 (line)]] | alt | 75.6 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 4.17× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.6) |
| [[SHP-77 (line)]] | alt | 67.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.4) |
| [[SNU-1 (line)]] | wt | 207 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.6) |
| [[SNU-423 (line)]] | alt | 44.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.8) |
| [[SW 900 (line)]] | alt | 63.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 95.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.7) |
| [[SW48 (line)]] | wt | 95.4 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -15.6) |
| [[A498 (line)]] | wt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -20.7) |
| [[C-33 A (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 92.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 91.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.7) |
| [[HOP62 (line)]] | alt | 33.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -8.5) |
| [[Hs 766T (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 80.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 57.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -12.2) |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.202× (z -8.5) |
| [[A-172 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIOK1]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RBM28]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[AGK]] | +0.72 | +0.58 / +0.75 | both halves | 8e-06 |  |
| [[MRPL15]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[DCAF17]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[COG2]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ANGEL1]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[RRP15]] | +0.65 | +0.55 / +0.73 | both halves | 1e-05 | STRING 419 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWT1]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[LRP10]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[MICALL2]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[YPEL5]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZNHIT6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.4, -39.4); signed map (-2.4, -41.5). **Vector** length 118, 33.2% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +13.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +15.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.9 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +10.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -19.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.1 | -6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger HIT-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,649,417-85,708,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20729, NY-BR-75, BCD1; previously C1orf181 |
| Gene groups (HGNC) | Zinc fingers HIT-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWK9](https://www.uniprot.org/uniprotkb/Q9NWK9) (Box C/D snoRNA protein 1):

> Required for box C/D snoRNAs accumulation involved in snoRNA processing, snoRNA transport to the nucleolus and ribosome biogenesis.

**Summary**, from NCBI Gene [54680](https://www.ncbi.nlm.nih.gov/gene/54680):

> Enables ATPase binding activity; TFIID-class transcription factor complex binding activity; and identical protein binding activity. Involved in box C/D snoRNP assembly; protein complex oligomerization; and snoRNA localization. Located in extracellular exosome. Part of pre-snoRNP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26089) · Entrez [54680](https://www.ncbi.nlm.nih.gov/gene/54680) · UniProt [Q9NWK9](https://www.uniprot.org/uniprotkb/Q9NWK9) · Ensembl [ENSG00000117174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117174)

## Data

Gene col 3883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3883); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3883]; `tensor/DDL_lfc|DDL_z.npy` [3883]; `embed/gene_vectors.npy` [3883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3883 or target_col == 3883). Every well: [[ZNHIT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNHIT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
