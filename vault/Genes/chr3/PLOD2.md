---
symbol: "PLOD2"
type: "gene"
col: 7673
ensembl_id: "ENSG00000152952"
name: "procollagen-lysine,2-oxoglutarate 5-dioxygenase 2"
location: "3q24"
module: 99
arm: "+"
pooled_cpm: 549.57
n_lines_expressing: 35
n_dd_up: 11
n_dd_down: 35
n_dd_up_clean: 9
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 11
direction_downstream: 28
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PLOD2

*procollagen-lysine,2-oxoglutarate 5-dioxygenase 2* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[PF-06260933 (drug)]] 5 µM: 2.31× (z +6.7, q 1e-08, up in 24 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.232× (z -31.5, q 0e+00, down in 31 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLLT3]] (+0.66, fdr 7e-06), [[PGK1]] (+0.62, fdr 7e-06), [[ENO1]] (+0.60, fdr 7e-06); moves opposite to [[IKBKB]] (-0.44, fdr 8e-05), [[ENTPD6]] (-0.42, fdr 4e-04), [[CCDC66]] (-0.41, fdr 9e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MLLT3]] → it (grade B ⚠); 28 go from it, the strongest it → [[VEGFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **2.31×** | +6.7 | 1e-08 | 24/33 (RPMI-7951, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +6.1 | 2e-07 | 27/32 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.34×** | +4.4 | 0.002 | 26/33 (A549, H4, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.003 | 21/32 (HOP62, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +4.2 | 0.003 | 20/34 (NCI-H460, RPMI-7951, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.005 | 19/33 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.005 | 23/34 (NCI-H2030, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 23/34 (A-172, NCI-H1792, …) | rises with dose | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.059 | 17/33 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.1 | 0.084 | 14/28 (HOP62, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.1 | 0.084 | 13/33 (NCI-H460, SNU-423, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.084 | 16/34 (HOP62, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.45× | +3.0 | 0.11 | 16/33 (HOP62, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.232×** | -31.5 | 0e+00 | 31/33 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.266×** | -19.4 | 0e+00 | 31/33 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.304×** | -17.4 | 0e+00 | 32/32 (SW 900, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -17.4 | 0e+00 | 33/33 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.329×** | -16.3 | 0e+00 | 31/32 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -15.8 | 0e+00 | 32/33 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -12.2 | 2e-32 | 29/33 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -12.2 | 3e-32 | 29/33 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.538×** | -9.4 | 2e-19 | 32/33 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.679×** | -8.3 | 5e-15 | 22/34 (A549, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.609×** | -7.5 | 2e-12 | 24/34 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.602×** | -7.4 | 6e-12 | 21/30 (SW 900, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.656×** | -6.4 | 6e-09 | 26/33 (H4, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.751×** | -6.1 | 4e-08 | 24/33 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.667×** | -5.6 | 8e-07 | 23/33 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -5.2 | 6e-06 | 22/33 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.740×** | -4.6 | 2e-04 | 21/33 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.814×** | -4.4 | 3e-04 | 16/33 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.812×** | -4.2 | 8e-04 | 20/33 (HT-29, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.746×** | -4.1 | 0.001 | 26/32 (LOX-IMVI, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.690×** | -4.0 | 0.002 | 26/33 (hTERT-HPNE, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 897 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -30.6) |
| [[LOX-IMVI (line)]] | wt | 1,267 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -36.7) |
| [[J82 (line)]] | alt | 2,018 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.5) |
| [[C32 (line)]] | wt | 680 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -35.1) |
| [[HepG2_C3A (line)]] | wt | 1,578 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -39.0) |
| [[SK-MEL-2 (line)]] | alt | 351 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -28.0) |
| [[NCI-H1792 (line)]] | alt | 648 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -16.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 660 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -28.3) |
| [[A549 (line)]] | wt | 865 | 2 (1 ⚠) | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.37× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -21.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.157× (z -19.4) |
| [[COLO 205 (line)]] | alt | 382 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -27.3) |
| [[HOP62 (line)]] | alt | 1,663 | 3 | 6 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.39× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.277× (z -14.5) |
| [[HS-578T (line)]] | alt | 1,498 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.2) |
| [[HT-29 (line)]] | alt | 488 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -22.6) |
| [[NCI-H460 (line)]] | wt | 231 | 1 (1 ⚠) | 8 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.42× (z +9.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -25.2) |
| [[RPMI-7951 (line)]] | alt | 1,200 | 1 | 8 (4 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.32× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -22.1) |
| [[SNU-423 (line)]] | alt | 1,004 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -22.0) |
| [[HCT15 (line)]] | alt | 702 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -25.1) |
| [[LoVo (line)]] | wt | 214 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.4) |
| [[SHP-77 (line)]] | alt | 589 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -22.5) |
| [[A-172 (line)]] | wt | 692 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -32.3) |
| [[CFPAC-1 (line)]] | alt | 501 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.1) |
| [[H4 (line)]] | wt | 1,009 | 2 | 4 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.57× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.6) |
| [[hTERT-HPNE (line)]] | wt | 1,208 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -15.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.7) |
| [[LS 180 (line)]] | wt | 138 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 1,240 | 3 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.55× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 366 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -12.0) |
| [[PANC-1 (line)]] | alt | 686 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -17.7) |
| [[CHP-212 (line)]] | wt | 241 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0506× (z -26.0) |
| [[SW 1271 (line)]] | alt | 637 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 241 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.6) |
| [[A498 (line)]] | wt | 535 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.317× (z -9.0) |
| [[AN3 CA (line)]] | alt | 248 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.6) |
| [[SW 1088 (line)]] | alt | 865 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.4) |
| [[A-427 (line)]] | wt | 106 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 41.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 106 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 46.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 36.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 47.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 578 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 124 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 556 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 38.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 42.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 36.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 47.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 54.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT3]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PGK1]] | +0.62 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ENO1]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[TPI1]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[TMEM45A]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[IGFBP3]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[BNIP3]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[IPMK]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HIF1A-AS3]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FAM162A]] | +0.53 | +0.63 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[GBE1]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CRYBG3]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBKB]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[ENTPD6]] | -0.42 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[CCDC66]] | -0.41 | -0.37 / -0.45 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | MLLT3 activity raises PLOD2's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 4.00× lower at baseline in the lines without MLLT3 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[VLDLR]] | B | VLDLR activity raises PLOD2's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 5.40× lower at baseline in the lines without VLDLR | 0.049 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[SYTL2]] | B | SYTL2 activity raises PLOD2's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 5.23× lower at baseline in the lines without SYTL2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[LINC03047]] | B | LINC03047 activity raises PLOD2's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 3.83× lower at baseline in the lines without LINC03047 | 0.058 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[LIMCH1]] | B | LIMCH1 activity raises PLOD2's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.54× lower at baseline in the lines without LIMCH1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[FBN1]] | B | FBN1 activity raises PLOD2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without FBN1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[NREP]] | B | NREP activity raises PLOD2's level | lines that do not express NREP (13) vs lines expressing it (37) | 5.20× lower at baseline in the lines without NREP | 0.072 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16 |
| [[EYA1]] | B | EYA1 activity raises PLOD2's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without EYA1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[RARB]] | B | RARB activity raises PLOD2's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.32× lower at baseline in the lines without RARB | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[ADAM12]] | C | ADAM12 activity raises PLOD2's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 5.35× lower at baseline in the lines without ADAM12 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[SLC2A1]] | C | SLC2A1 activity raises PLOD2's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 5.03× lower at baseline in the lines without SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 26, C 2. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFA]] | B | PLOD2 activity raises VEGFA's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without PLOD2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[MLLT3]] | B | PLOD2 activity raises MLLT3's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.95× lower at baseline in the lines without PLOD2 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[GALNT2]] | B | PLOD2 activity raises GALNT2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without PLOD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[RNF24]] | B | PLOD2 activity raises RNF24's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without PLOD2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[PKM]] | B | PLOD2 activity raises PKM's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PLOD2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[NDRG1]] | B | PLOD2 activity raises NDRG1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.58× lower at baseline in the lines without PLOD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[DIRC3]] | B | PLOD2 activity raises DIRC3's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without PLOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[LIMCH1]] | B | PLOD2 activity raises LIMCH1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.51× lower at baseline in the lines without PLOD2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[PGRMC2]] | B | PLOD2 activity raises PGRMC2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PLOD2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[HILPDA]] | B | PLOD2 activity raises HILPDA's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.10× lower at baseline in the lines without PLOD2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[EXT1]] | B | PLOD2 activity raises EXT1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without PLOD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[TENT5A]] | B | PLOD2 activity raises TENT5A's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.30× lower at baseline in the lines without PLOD2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, -16.0); signed map (-37.0, 29.5). **Vector** length 130, 44.3% of its response variance represented; |z| ≥ 3 in 1,423 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycolysis* (reactome, mean cos +0.51 to 10); *Glucose metabolism* (reactome, mean cos +0.51 to 10); *Metabolism of carbohydrates and carbohydrate derivatives* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.8 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +0.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.9 | +4.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.0 | -16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -17.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -19.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.5 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.3 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | procollagen-lysine,2-oxoglutarate 5-dioxygenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:146,035,139-146,163,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LH2, TLH |
| Gene groups (HGNC) | Procollagen-lysine,2-oxoglutarate 5-dioxygenase family |
| Hallmark sets | GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O00469](https://www.uniprot.org/uniprotkb/O00469) (Procollagen-lysine,2-oxoglutarate 5-dioxygenase 2):

> Forms hydroxylysine residues in -Xaa-Lys-Gly- sequences in collagens. These hydroxylysines serve as sites of attachment for carbohydrate units and are essential for the stability of the intermolecular collagen cross-links.

**Summary**, from NCBI Gene [5352](https://www.ncbi.nlm.nih.gov/gene/5352):

> The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular crosslinks. Some patients with Ehlers-Danlos syndrome type VIB have deficiencies in lysyl …

**Accessions** — [HGNC:9082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9082) · Entrez [5352](https://www.ncbi.nlm.nih.gov/gene/5352) · UniProt [O00469](https://www.uniprot.org/uniprotkb/O00469) · Ensembl [ENSG00000152952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152952)

## Data

Gene col 7673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7673); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7673]; `tensor/DDL_lfc|DDL_z.npy` [7673]; `embed/gene_vectors.npy` [7673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7673 or target_col == 7673). Every well: [[PLOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
