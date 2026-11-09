---
symbol: "ASMTL"
type: "gene"
col: 9751
ensembl_id: "ENSG00000169093"
name: "acetylserotonin O-methyltransferase like"
location: "Xp22.3 and Yp11.3"
module: 161
arm: "+"
pooled_cpm: 32.22
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# ASMTL

*acetylserotonin O-methyltransferase like* — Xp22.3 and Yp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.60× (z +25.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.681× (z -7.5, q 3e-11, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFB1]] (+0.71, fdr 1e-05), [[SLC27A1]] (+0.68, fdr 3e-05), [[SYP]] (+0.68, fdr 2e-05); moves opposite to [[RAB11FIP2]] (-0.68, fdr 2e-05), [[NSD1]] (-0.64, fdr 2e-05), [[FAIM]] (-0.62, fdr 3e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.60×** | +25.1 | 0e+00 | 47/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +24.2 | 0e+00 | 47/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.07×** | +22.0 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +19.9 | 0e+00 | 45/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +15.7 | 0e+00 | 33/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +15.1 | 0e+00 | 46/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +14.4 | 7e-45 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.05×** | +14.1 | 5e-43 | 46/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.3 | 6e-15 | 22/47 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +7.8 | 4e-13 | 35/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.1 | 4e-08 | 22/48 (SNU-423, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 1e-04 | 18/48 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 12/47 (MIA PaCa-2, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.005 | 13/42 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.005 | 14/47 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.009 | 11/48 (SW480, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -7.5 | 3e-11 | 31/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -5.2 | 7e-05 | 24/48 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -4.9 | 2e-04 | 19/48 (A-427, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.773×** | -4.7 | 3e-04 | 22/46 (H4, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.7 | 3e-04 | 15/48 (KATO III, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.781×** | -4.7 | 3e-04 | 23/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.793×** | -4.4 | 1e-03 | 20/38 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.797×** | -4.3 | 0.001 | 15/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.5 | 0.026 | 16/47 (A-427, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.4 | 0.036 | 13/48 (A-427, SNU-423, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.841× | -3.3 | 0.054 | 10/48 (SK-MEL-2, A-427, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.847× | -3.1 | 0.082 | 11/47 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.092 | 10/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 86.2 | 17 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +20.1) | — |
| [[SW480 (line)]] | alt | 26.4 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.63× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.1 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +25.0) | [[Dexamethasone (drug)]] 0.05 µM 0.280× (z -9.4) |
| [[SNU-423 (line)]] | alt | 54.2 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.70× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 32.8 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.35× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 76.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.4) | — |
| [[A-172 (line)]] | wt | 48.0 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.59× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 38.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.3) | — |
| [[KATO III (line)]] | alt | 26.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +13.7) | — |
| [[LoVo (line)]] | wt | 22.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.38× (z +12.1) | — |
| [[A498 (line)]] | wt | 18.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.1) | — |
| [[A549 (line)]] | wt | 30.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.80× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.08× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 27.4 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +10.4) | — |
| [[A-427 (line)]] | wt | 37.5 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 32.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.52× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0806× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 31.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 33.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.8) | — |
| [[H4 (line)]] | wt | 59.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.3) | [[Harringtonine (drug)]] 0.05 µM 0.151× (z -11.5) |
| [[HCT15 (line)]] | alt | 39.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.13× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 15.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 12.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 60.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 21.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 16.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 22.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.81× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 14.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.26× (z +9.6) | — |
| [[RKO (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +13.6) | — |
| [[SNU-1 (line)]] | wt | 48.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.2) | — |
| [[SW48 (line)]] | wt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFB1]] | +0.71 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.68 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[SYP]] | +0.68 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SHF]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NCKAP5L]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BAIAP3]] | +0.64 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SLC66A2]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D10A]] | +0.62 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[NRTN]] | +0.61 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[BCORL1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MAST1]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[LMTK3]] | +0.61 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP2]] | -0.68 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NSD1]] | -0.64 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[FAIM]] | -0.62 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DECR1]] | -0.61 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CRPPA]] | -0.60 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[QRSL1]] | -0.60 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ANGEL2]] | -0.59 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[DERA]] | -0.59 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[KLHL42]] | -0.59 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[FBXW4]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[MYLK-AS1]] | -0.57 | -0.33 / -0.23 | both halves | 5e-04 |  |
| [[TADA2A]] | -0.56 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises ASMTL's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without SEMA6B | 0.054 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SEMA3F]] | B | SEMA3F activity raises ASMTL's level | lines that do not express SEMA3F (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SEMA3F | 0.062 | ⚠ within organs, on part of the lines; also absent: MCM2, PIMREG, GKAP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.3, 0.5); signed map (-22.4, 28.4). **Vector** length 105, 26.5% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +19.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +14.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +15.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +24.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | acetylserotonin O-methyltransferase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.3 and Yp11.3 — chrX:1,403,139-1,453,762 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pseudoautosomal region 1; 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95671](https://www.uniprot.org/uniprotkb/O95671) (Probable bifunctional dTTP/UTP pyrophosphatase/methyltransferase protein):

> Nucleoside triphosphate pyrophosphatase that hydrolyzes dTTP and UTP. Can also hydrolyze CTP and the modified nucleotides pseudo-UTP, 5-methyl-UTP (m(5)UTP) and 5-methyl-CTP (m(5)CTP). Has weak activity with dCTP, 8-oxo-GTP and N(4)-methyl-dCTP. May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids. In addition, the presence of the putative catalytic domain of S-adenosyl-L-methionine binding in the C-terminal region …

**Summary**, from NCBI Gene [8623](https://www.ncbi.nlm.nih.gov/gene/8623):

> The protein encoded by this gene has an N-terminus that is similar to the multicopy associated filamentation (maf) protein of Bacillus subtilis and to orfE of Escherichia coli, while the C-terminus is similar to N-acetylserotonin O-methyltransferase. This gene is located in the pseudoautosomal region 1 (PAR1) of X and Y chromosomes. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:751) · Entrez [8623](https://www.ncbi.nlm.nih.gov/gene/8623) · UniProt [O95671](https://www.uniprot.org/uniprotkb/O95671) · Ensembl [ENSG00000169093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169093)

## Data

Gene col 9751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9751); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9751]; `tensor/DDL_lfc|DDL_z.npy` [9751]; `embed/gene_vectors.npy` [9751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9751 or target_col == 9751). Every well: [[ASMTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASMTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
