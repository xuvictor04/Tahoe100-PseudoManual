---
symbol: "HBEGF"
type: "gene"
col: 3429
ensembl_id: "ENSG00000113070"
name: "heparin binding EGF like growth factor"
location: "5q31.3"
module: 81
arm: "+"
pooled_cpm: 38.5
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 32
n_dd_up_clean: 8
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 10
direction_downstream: 15
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# HBEGF

*heparin binding EGF like growth factor* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +9.7, q 2e-19, up in 30 of 44 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.05× (z +6.4, q 2e-08, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.425× (z -7.2, q 3e-10, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD1]] (+0.73, fdr 7e-06), [[PTHLH]] (+0.73, fdr 7e-06), [[LINC01204]] (+0.69, fdr 7e-06); moves opposite to [[KCTD3]] (-0.56, fdr 1e-05), [[CHPT1]] (-0.55, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CSF2]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.17×** | +9.7 | 2e-19 | 30/44 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +8.2 | 6e-14 | 34/43 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.22×** | +6.8 | 2e-09 | 29/44 (A498, HOP62, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +6.4 | 2e-08 | 30/45 (HEC-1-A, HCT15, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +5.6 | 3e-06 | 23/43 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 4e-06 | 28/43 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 26/44 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.69×** | +4.7 | 2e-04 | 25/45 (A498, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.67×** | +4.6 | 3e-04 | 23/45 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.63×** | +4.3 | 8e-04 | 23/45 (NCI-H460, A-427, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.60×** | +4.2 | 0.001 | 27/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.56×** | +4.0 | 0.003 | 24/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.010 | 20/44 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.010 | 21/45 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.017 | 19/45 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.024 | 20/45 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.072 | 21/45 (A-172, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.425×** | -7.2 | 3e-10 | 31/43 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.424×** | -7.0 | 6e-10 | 36/45 (MIA PaCa-2, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.582×** | -6.6 | 9e-09 | 37/45 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.487×** | -6.3 | 4e-08 | 32/44 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.504×** | -5.5 | 4e-06 | 30/45 (MIA PaCa-2, NCI-H1792, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.544×** | -5.4 | 6e-06 | 26/45 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.539×** | -5.4 | 6e-06 | 32/45 (PANC-1, J82, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.836× | -5.4 | 6e-06 | 20/46 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.529×** | -5.2 | 1e-05 | 27/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.607×** | -5.2 | 1e-05 | 31/45 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.557×** | -5.1 | 2e-05 | 28/46 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.620×** | -5.0 | 3e-05 | 27/45 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.561×** | -4.9 | 5e-05 | 26/44 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.594×** | -4.5 | 2e-04 | 24/45 (HS-578T, A-172, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.596×** | -4.5 | 3e-04 | 24/45 (A-172, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.349×** | -4.5 | 3e-04 | 29/44 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 76.2 | 0 | 16 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.133× (z -38.5) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0895× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 10.2 | 6 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.60× (z +14.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A498 (line)]] | wt | 13.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +17.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 20.6× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 31.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +15.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.00× (z +11.4) | [[Adagrasib (drug)]] 0.05 µM 0.515× (z -12.1) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 53.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.0) ⚠ cell-cycle shift, explains ~43% of this change | [[Cobimetinib (drug)]] 5 µM 0.179× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 19.0 | 2 (2 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 14.2× (z +10.2) ⚠ toxic | [[Verteporfin (drug)]] 5 µM 0.105× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 39.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Adagrasib (drug)]] 0.05 µM 0.488× (z -11.2) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.126× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 32.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.08× (z +8.5) | [[Cobimetinib (drug)]] 5 µM 0.181× (z -8.6) |
| [[A-172 (line)]] | wt | 35.9 | 0 | 2 | — | [[Budesonide (drug)]] 5 µM 0.179× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 65.2 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.68× (z +9.8) ⚠ cell-cycle shift, explains ~74% of this change | [[Trametinib (drug)]] 5 µM 0.229× (z -8.8) |
| [[C32 (line)]] | wt | 17.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +12.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.8× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +12.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.31× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.166× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 52.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.69× (z +9.4) ⚠ toxic | [[Adagrasib (drug)]] 0.05 µM 0.533× (z -13.3) ⚠ position not correctable |
| [[HCT15 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 49.7 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.180× (z -8.8) |
| [[LoVo (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 33.4 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.170× (z -8.6) |
| [[SW1417 (line)]] | alt | 98.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD1]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PTHLH]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NIPAL1]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Bacterial Infection Pathways; STRING 429 |
| [[C3orf52]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PHLDA2]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PRDM8]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ITGA2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[STK10]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF2]] | B | CSF2 activity raises HBEGF's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without CSF2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[NR3C1]] | B | NR3C1 activity lowers HBEGF's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[RASGRF2]] | B | RASGRF2 activity lowers HBEGF's level | lines that do not express RASGRF2 (21) vs lines expressing it (29) | 1.36× higher at baseline in the lines without RASGRF2 | 0.055 | ⚠ within organs, on part of the lines; also absent: SFRP1, MT1A, RGCC |
| [[PLAUR]] | B | PLAUR activity raises HBEGF's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.64× lower at baseline in the lines without PLAUR | 0.059 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[CALB2]] | B | CALB2 activity raises HBEGF's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without CALB2 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[SEMA7A]] | B | SEMA7A activity raises HBEGF's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without SEMA7A | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LUCAT1]] | B | LUCAT1 activity raises HBEGF's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without LUCAT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[CXCL8]] | B | CXCL8 activity raises HBEGF's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without CXCL8 | 0.077 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[MAP2K1]] | B | MAP2K1 activity raises HBEGF's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCF7]] | C | TCF7 activity raises HBEGF's level | lines that do not express TCF7 (3) vs lines expressing it (47) | 3.42× lower at baseline in the lines without TCF7 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: FHL3, SKAP2, IGF2BP2; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ouabain (Octahydrate) (drug)]] 0.05 µM | C | HBEGF activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.66× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[S100A16]] | C | HBEGF activity raises S100A16's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 7.60× lower at baseline in the lines without HBEGF | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | HBEGF activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.30× the cells of the other lines | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[C3orf52]] | C | HBEGF activity raises C3orf52's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 4.02× lower at baseline in the lines without HBEGF | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| cells under [[Auranofin (drug)]] 5 µM | C | HBEGF activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.59× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[STK17A]] | C | HBEGF activity raises STK17A's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without HBEGF | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | HBEGF activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 1.35× the cells of the other lines | 0.037 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[GRB10]] | C | HBEGF activity raises GRB10's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 6.35× lower at baseline in the lines without HBEGF | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[FOSL1]] | C | HBEGF activity raises FOSL1's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 3.75× lower at baseline in the lines without HBEGF | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| cells under [[Adagrasib (drug)]] 5 µM | C | HBEGF activity raises the cells' numbers under Adagrasib 5 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.68× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | HBEGF activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 1.35× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[MYO10]] | C | HBEGF activity raises MYO10's level | lines that do not express HBEGF (3) vs lines expressing it (47) | 4.32× lower at baseline in the lines without HBEGF | 0.061 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 1.1); signed map (4.1, 45.8). **Vector** length 135, 44.3% of its response variance represented; |z| ≥ 3 in 1,525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.4 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.1 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.0 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.7 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | heparin binding EGF like growth factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,332,843-140,346,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HB-EGF; previously HEGFL, DTS, DTR |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | INFLAMMATORY_RESPONSE, MYOGENESIS, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 53 pathways, smallest: Uptake and function of diphtheria toxin; PTK6 promotes HIF1A stabilization; EGFR Transactivation by Gastrin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99075](https://www.uniprot.org/uniprotkb/Q99075) (Proheparin-binding EGF-like growth factor):

> Growth factor that mediates its effects via EGFR, ERBB2 and ERBB4. Required for normal cardiac valve formation and normal heart function. Promotes smooth muscle cell proliferation. May be involved in macrophage-mediated cellular proliferation. It is mitogenic for fibroblasts, but not endothelial cells. It is able to bind EGF receptor/EGFR with higher affinity than EGF itself and is a far more potent mitogen for smooth muscle cells than EGF. Also acts as a diphtheria toxin receptor.

**Summary**, from NCBI Gene [1839](https://www.ncbi.nlm.nih.gov/gene/1839):

> Enables growth factor activity; heparin binding activity; and transmembrane receptor protein tyrosine kinase activator activity. Involved in several processes, including cell chemotaxis; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and positive regulation of wound healing. Acts upstream of or within epidermal growth factor receptor signaling pathway. Located in cell surface. Is active in obsolete extracellular space. Implicated in congestive heart …

**Accessions** — [HGNC:3059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3059) · Entrez [1839](https://www.ncbi.nlm.nih.gov/gene/1839) · UniProt [Q99075](https://www.uniprot.org/uniprotkb/Q99075) · Ensembl [ENSG00000113070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113070)

## Data

Gene col 3429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3429); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3429]; `tensor/DDL_lfc|DDL_z.npy` [3429]; `embed/gene_vectors.npy` [3429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3429 or target_col == 3429). Every well: [[HBEGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HBEGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
