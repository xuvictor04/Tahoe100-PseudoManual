---
symbol: "MAN1A2"
type: "gene"
col: 12543
ensembl_id: "ENSG00000198162"
name: "mannosidase alpha class 1A member 2"
location: "1p12"
module: 143
arm: "+"
pooled_cpm: 134.41
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# MAN1A2

*mannosidase alpha class 1A member 2* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +17.8, q 0e+00, up in 36 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.578×, J82 0.582×, NCI-H1792 0.573×, AN3 CA 0.444×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.603×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RKO 0.484×; ⚠ toxic; cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STAU2]] (+0.56, fdr 3e-05), [[GNAQ]] (+0.55, fdr 2e-05), [[TCF12]] (+0.51, fdr 3e-05); moves opposite to [[CCDC127]] (-0.52, fdr 4e-05), [[KLHL26]] (-0.50, fdr 6e-05), [[MRPL2]] (-0.49, fdr 4e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +17.8 | 0e+00 | 36/49 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +15.4 | 0e+00 | 35/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.53×** | +14.5 | 3e-45 | 37/49 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +13.2 | 2e-37 | 41/48 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.49×** | +13.1 | 6e-37 | 29/44 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +12.9 | 6e-36 | 40/48 (CFPAC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +12.2 | 3e-32 | 35/45 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +11.3 | 2e-27 | 35/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +10.0 | 1e-21 | 26/48 (A-172, A498, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +9.6 | 3e-20 | 34/50 (A-172, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +9.6 | 3e-20 | 26/48 (A-172, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +8.4 | 1e-15 | 28/48 (SW480, SHP-77, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +8.3 | 5e-15 | 28/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +8.0 | 7e-14 | 35/49 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +7.6 | 2e-12 | 25/48 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +6.7 | 7e-10 | 23/48 (MIA PaCa-2, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +6.3 | 7e-09 | 13/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +6.1 | 2e-08 | 23/49 (SW480, NCI-H23, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +4.5 | 2e-04 | 13/48 (NCI-H1792, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +4.1 | 9e-04 | 5/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.10× | +3.2 | 0.032 | 9/47 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (C32 0.578×, J82 0.582×, NCI-H1792 0.573×, AN3 CA 0.444×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.603×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RKO 0.484×; ⚠ toxic; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.863× | -5.0 | 1e-04 | 9/49 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.853× | -5.0 | 1e-04 | 17/47 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -4.9 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.915× | -4.2 | 0.003 | 4/48 (RKO, SW 1088, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.925× | -3.7 | 0.022 | 4/48 (SNU-1, hTERT-HPNE, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.904× | -3.4 | 0.062 | 4/48 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.902× | -3.4 | 0.063 | 6/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.911× | -3.1 | 0.12 | 11/48 (PANC-1, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 80.0 | 10 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 139 | 10 (6 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 83.0 | 10 (6 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.51× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 90.8 | 9 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +15.8) | — |
| [[A498 (line)]] | wt | 98.4 | 7 (5 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.49× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 103 | 7 (5 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.93× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +19.9) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 4 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.21× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 95.8 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.6) | — |
| [[A-427 (line)]] | wt | 112 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 56.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 74.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 123 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.1) | — |
| [[SW480 (line)]] | alt | 154 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 118 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 93.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 280 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +15.9) | — |
| [[A549 (line)]] | wt | 85.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 87.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.8) | — |
| [[J82 (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.76× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 176 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.65× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 141 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 102 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 131 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 226 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 96.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.62× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.484× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 345 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.603× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 182 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 203 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 234 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAU2]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[GNAQ]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TCF12]] | +0.51 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GOLM2]] | +0.51 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[EXT2]] | +0.50 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HIGD1A]] | +0.50 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[TMEM131]] | +0.49 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[TULP4]] | +0.49 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TMX3]] | +0.49 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[RBFOX2]] | +0.48 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[COP1]] | +0.48 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[IDE]] | +0.48 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC127]] | -0.52 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[KLHL26]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[MRPL2]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[AFMID]] | -0.49 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[TARS2]] | -0.45 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[ZNF766]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[VPS37C]] | -0.43 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ZNF550]] | -0.43 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[HAUS3]] | -0.43 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[NFKBIL1]] | -0.42 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[NAGK]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 | pathway: Asparagine N-linked glycosylation |
| [[CRTC1]] | -0.42 | -0.47 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAN1A2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.1, 10.3); signed map (7.9, -1.5). **Vector** length 108, 29.7% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +8.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +8.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.2 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.0 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.9 | +10.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.5 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 1A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:117,367,449-117,528,872 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAN1B |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Reactome | 8 pathways, smallest: Progressive trimming of alpha-1,2-linked mannose residues from Man9/8/7GlcNAc2 to produce Man5GlcNAc2; N-glycan trimming and elongation in the cis-Golgi; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O60476](https://www.uniprot.org/uniprotkb/O60476) (Mannosyl-oligosaccharide 1,2-alpha-mannosidase IB):

> Involved in the maturation of Asn-linked oligosaccharides. Progressively trim alpha-1,2-linked mannose residues from Man(9)GlcNAc(2) to produce Man(5)GlcNAc(2).

**Summary**, from NCBI Gene [10905](https://www.ncbi.nlm.nih.gov/gene/10905):

> Alpha-mannosidases function at different stages of N-glycan maturation in mammalian cells. See MAN2A1 (MIM 154582) for general information.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:6822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6822) · Entrez [10905](https://www.ncbi.nlm.nih.gov/gene/10905) · UniProt [O60476](https://www.uniprot.org/uniprotkb/O60476) · Ensembl [ENSG00000198162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198162)

## Data

Gene col 12543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12543); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12543]; `tensor/DDL_lfc|DDL_z.npy` [12543]; `embed/gene_vectors.npy` [12543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12543 or target_col == 12543). Every well: [[MAN1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
