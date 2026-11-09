---
symbol: "OGFRL1"
type: "gene"
col: 4132
ensembl_id: "ENSG00000119900"
name: "opioid growth factor receptor like 1"
location: "6q13"
module: 14
arm: "+"
pooled_cpm: 44.8
n_lines_expressing: 40
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 10
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# OGFRL1

*opioid growth factor receptor like 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.23× (z +15.2, q 0e+00, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +13.5, q 2e-39, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.460× (z -15.4, q 0e+00, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAM1]] (+0.73, fdr 7e-06), [[LINC02605]] (+0.72, fdr 7e-06), [[LACC1]] (+0.68, fdr 1e-05); moves opposite to [[ATG4B]] (-0.62, fdr 6e-05), [[TECPR1]] (-0.60, fdr 4e-05), [[SPATC1L]] (-0.58, fdr 8e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KLHL5]] → it (grade B ⚠); 10 go from it, the strongest it → [[OXCT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +15.2 | 0e+00 | 25/30 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +15.0 | 0e+00 | 30/36 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +13.5 | 2e-39 | 24/38 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +13.2 | 1e-37 | 26/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +12.7 | 5e-35 | 28/38 (PANC-1, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +10.0 | 2e-21 | 23/38 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.1 | 6e-18 | 27/38 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +7.7 | 9e-13 | 20/38 (J82, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +7.7 | 1e-12 | 21/33 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +7.0 | 1e-10 | 21/38 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.0 | 1e-10 | 24/37 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +6.8 | 4e-10 | 23/37 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +6.8 | 6e-10 | 22/38 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 9e-10 | 20/38 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +6.2 | 2e-08 | 19/38 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 9e-05 | 13/38 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +4.4 | 3e-04 | 16/38 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 7e-04 | 15/38 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.2 | 8e-04 | 12/38 (A549, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.460×** | -15.4 | 0e+00 | 33/38 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.461×** | -15.3 | 0e+00 | 34/38 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.575×** | -10.9 | 1e-25 | 31/38 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -8.1 | 6e-14 | 24/38 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.4 | 9e-06 | 18/38 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -5.3 | 9e-06 | 18/38 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.720×** | -4.6 | 3e-04 | 16/38 (SW 1271, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.785×** | -4.5 | 4e-04 | 20/38 (NCI-H23, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.682×** | -4.0 | 0.005 | 13/33 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.826×** | -3.8 | 0.008 | 17/38 (SW 1088, LoVo, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.814× | -3.1 | 0.10 | 14/38 (NCI-H1573, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | 0.744× | -3.1 | 0.11 | 10/37 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 43.8 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +25.0) | — |
| [[PANC-1 (line)]] | alt | 37.3 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.413× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 80.7 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.367× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 176 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.457× (z -9.5) |
| [[A-172 (line)]] | wt | 40.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +18.4) | — |
| [[Panc 03.27 (line)]] | alt | 63.9 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +20.6) | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -12.7) |
| [[SNU-423 (line)]] | alt | 127 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 90.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.1) |
| [[A549 (line)]] | wt | 57.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +16.9) | — |
| [[J82 (line)]] | alt | 65.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +17.1) | — |
| [[LOX-IMVI (line)]] | wt | 49.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 32.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.8) |
| [[SW 900 (line)]] | alt | 96.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.0) | — |
| [[A-427 (line)]] | wt | 50.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.6) | — |
| [[A498 (line)]] | wt | 96.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 25.4 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.69× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -10.1) |
| [[LoVo (line)]] | wt | 24.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 66.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 121 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.4) |
| [[BT-474 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +13.8) | — |
| [[C32 (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +10.8) | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0730× (z -10.5) |
| [[Hs 766T (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.61× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 28.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0919× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM1]] | +0.73 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[LACC1]] | +0.68 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CFL2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[C1QTNF1-AS1]] | +0.65 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[RWDD2B]] | +0.64 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[CLN5]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TIFA]] | +0.63 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[ERAP1]] | +0.63 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[CSF1]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.62 | +0.61 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4B]] | -0.62 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TECPR1]] | -0.60 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[SPATC1L]] | -0.58 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[RBAK-RBAKDN]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[AP2S1]] | -0.57 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[VRK3]] | -0.56 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SDHAF1]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PPIL2]] | -0.56 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[SIVA1]] | -0.55 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[EIF3K]] | -0.55 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A42]] | -0.55 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[EPS15L1]] | -0.55 | -0.46 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL5]] | B | KLHL5 activity raises OGFRL1's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 4.51× lower at baseline in the lines without KLHL5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[MRAS]] | B | MRAS activity raises OGFRL1's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without MRAS | 0.013 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[DRAM1]] | B | DRAM1 activity raises OGFRL1's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 4.52× lower at baseline in the lines without DRAM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises OGFRL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises OGFRL1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers OGFRL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CFL2]] | C | CFL2 activity raises OGFRL1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 6.39× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OXCT1]] | B | OGFRL1 activity raises OXCT1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.48× lower at baseline in the lines without OGFRL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[AMZ2P1]] | B | OGFRL1 activity raises AMZ2P1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[ADORA2A]] | B | OGFRL1 activity raises ADORA2A's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without OGFRL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[CFL2]] | B | OGFRL1 activity raises CFL2's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without OGFRL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[RC3H2]] | B | OGFRL1 activity raises RC3H2's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[RAB23]] | B | OGFRL1 activity raises RAB23's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without OGFRL1 | 0.067 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[RWDD2B]] | B | OGFRL1 activity raises RWDD2B's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.17× lower at baseline in the lines without OGFRL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[ACADM]] | B | OGFRL1 activity raises ACADM's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without OGFRL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[MR1]] | B | OGFRL1 activity raises MR1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without OGFRL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[LHFPL6]] | C | OGFRL1 activity raises LHFPL6's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 4.42× lower at baseline in the lines without OGFRL1 | 0.061 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 5.3); signed map (24.2, -34.7). **Vector** length 118, 32.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.2 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +6.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +4.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.8 | -15.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -15.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -10.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.6 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | opioid growth factor receptor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:71,288,811-71,309,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ331H24.1 |
| Matched by | ensembl_id |

UniProt [Q5TC84](https://www.uniprot.org/uniprotkb/Q5TC84) carries no function annotation.

**Summary**, from NCBI Gene [79627](https://www.ncbi.nlm.nih.gov/gene/79627):

> Predicted to enable opioid growth factor receptor activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21378) · Entrez [79627](https://www.ncbi.nlm.nih.gov/gene/79627) · UniProt [Q5TC84](https://www.uniprot.org/uniprotkb/Q5TC84) · Ensembl [ENSG00000119900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119900)

## Data

Gene col 4132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4132); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4132]; `tensor/DDL_lfc|DDL_z.npy` [4132]; `embed/gene_vectors.npy` [4132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4132 or target_col == 4132). Every well: [[OGFRL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGFRL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
