---
symbol: "TENM3"
type: "gene"
col: 13291
ensembl_id: "ENSG00000218336"
name: "teneurin transmembrane protein 3"
location: "4q34.3-q35.1"
module: 9
arm: "+"
pooled_cpm: 170.69
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TENM3

*teneurin transmembrane protein 3* — 4q34.3-q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +10.8, q 2e-24, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.523× (z -9.9, q 3e-20, down in 24 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENM3-AS1]] (+0.77, fdr 7e-06, ⚠ same locus), [[CACNA2D1]] (+0.67, fdr 1e-05), [[DIO2]] (+0.64, fdr 7e-06), [[MIR99AHG]] (+0.63, fdr 1e-05); moves opposite to [[LCMT1]] (-0.61, fdr 3e-05), [[HEATR5B]] (-0.60, fdr 3e-05), [[WRAP53]] (-0.58, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC02240]] → it (grade B ⚠); 5 go from it, the strongest it → [[FGF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +10.8 | 2e-24 | 19/28 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.3 | 9e-08 | 22/27 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.6 | 4e-06 | 13/28 (HOP62, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +4.6 | 6e-04 | 19/28 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.5 | 6e-04 | 11/28 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.004 | 16/28 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.004 | 16/28 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.004 | 16/29 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +4.0 | 0.004 | 16/30 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.018 | 12/28 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.023 | 15/28 (A-427, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.024 | 17/27 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.024 | 14/28 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.028 | 13/28 (HOP62, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.032 | 16/28 (HCT15, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.047 | 12/28 (A-427, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.523×** | -9.9 | 3e-20 | 24/28 (C-33 A, A-427, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.707×** | -7.5 | 2e-11 | 18/28 (RKO, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -7.2 | 1e-10 | 24/29 (LS 180, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -7.1 | 2e-10 | 22/28 (C-33 A, A-427, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.630×** | -7.0 | 2e-10 | 23/28 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -5.5 | 3e-06 | 20/28 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.696×** | -5.5 | 3e-06 | 24/27 (LS 180, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -4.6 | 3e-04 | 16/27 (RKO, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.768×** | -4.0 | 0.003 | 18/28 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.003 | 15/28 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.013 | 12/28 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.046 | 16/28 (NCI-H460, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.751×** | -3.3 | 0.047 | 15/28 (C-33 A, A-427, …) | inconsistent across doses | composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.865× | -3.1 | 0.071 | 10/29 (CHP-212, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.814×** | -3.0 | 0.095 | 14/27 (C-33 A, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 2,639 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -28.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.115× (z -23.1) |
| [[A-427 (line)]] | wt | 947 | 2 (1 ⚠) | 13 (7 ⚠) | [[Trametinib (drug)]] 5 µM 2.49× (z +10.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 1.95× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.196× (z -18.7) |
| [[HOP62 (line)]] | alt | 181 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +32.4) | — |
| [[HCT15 (line)]] | alt | 617 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -12.5) |
| [[RKO (line)]] | wt | 184 | 0 | 7 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -20.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.165× (z -17.9) |
| [[LoVo (line)]] | wt | 128 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.380× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 272 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -10.3) |
| [[SW48 (line)]] | wt | 273 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 366 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -10.7) |
| [[HT-29 (line)]] | alt | 98.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -15.8) |
| [[J82 (line)]] | alt | 421 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -9.5) |
| [[SW480 (line)]] | alt | 64.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -15.7) |
| [[A-172 (line)]] | wt | 426 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.87× (z +9.7) ⚠ unreliable plate only · without an alert: [[Cobimetinib (drug)]] 5 µM 2.95× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 165 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.200× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 3.17× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +22.3) | — |
| [[SNU-423 (line)]] | alt | 143 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.7) | [[Selinexor (drug)]] 5 µM 0.470× (z -10.3) |
| [[A549 (line)]] | wt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.3) | — |
| [[C32 (line)]] | wt | 162 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +8.7) | — |
| [[H4 (line)]] | wt | 438 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 90.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -8.6) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 1,068 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0523× (z -8.8) |
| [[A498 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 252 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 39.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENM3-AS1]] | +0.77 | +0.83 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CACNA2D1]] | +0.67 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[DIO2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MIR99AHG]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[UNC5C]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CUX1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.59 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[NUTM2B-AS1]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.58 | +0.62 / +0.43 | both halves | 3e-05 | same gene group |
| [[ANKS1B]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NFE2L2]] | +0.57 | +0.55 / +0.46 | both halves | 3e-05 | same gene group |
| [[SEMA6A-AS1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.61 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[HEATR5B]] | -0.60 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[WRAP53]] | -0.58 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.57 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[MINDY3]] | -0.57 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.56 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[MOSPD3]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MTMR14]] | -0.56 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[APAF1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SLC25A14]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MARF1]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 | same gene group |
| [[UHRF2]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02240]] | B | LINC02240 activity raises TENM3's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 2.38× lower at baseline in the lines without LINC02240 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[LINC00470]] | B | LINC00470 activity raises TENM3's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 3.93× lower at baseline in the lines without LINC00470 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA |
| [[PLCB4]] | B | PLCB4 activity raises TENM3's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.91× lower at baseline in the lines without PLCB4 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[LINC02008]] | B | LINC02008 activity raises TENM3's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without LINC02008 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TENM3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PARD3B]] | B | PARD3B activity raises TENM3's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 4.52× lower at baseline in the lines without PARD3B | 0.074 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[FGF2]] | B | FGF2 activity raises TENM3's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without FGF2 | 0.079 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[PCDH7]] | B | PCDH7 activity raises TENM3's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without PCDH7 | 0.095 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4 |
| [[TENM3-AS1]] | C | TENM3-AS1 activity raises TENM3's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 10.02× lower at baseline in the lines without TENM3-AS1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises TENM3's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 5.18× lower at baseline in the lines without MIR99AHG | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF2]] | B | TENM3 activity raises FGF2's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without TENM3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[PLCB4]] | B | TENM3 activity raises PLCB4's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without TENM3 | 0.038 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[IMMP2L]] | B | TENM3 activity raises IMMP2L's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without TENM3 | 0.071 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[TENM3-AS1]] | C | TENM3 activity raises TENM3-AS1's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 3.76× lower at baseline in the lines without TENM3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX; co-absent with the target |
| [[ALPK2]] | C | TENM3 activity raises ALPK2's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.87× lower at baseline in the lines without TENM3 | 0.090 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.5, 24.2); signed map (44.6, 24.7). **Vector** length 100, 30.0% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +3.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -9.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -7.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | teneurin transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.3-q35.1 — chr4:182,143,987-182,803,024 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ten-M3, KIAA1455, TEN3; previously ODZ3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Teneurin transmembrane protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P273](https://www.uniprot.org/uniprotkb/Q9P273) (Teneurin-3):

> Involved in neural development by regulating the establishment of proper connectivity within the nervous system. Acts in both pre- and postsynaptic neurons in the hippocampus to control the assembly of a precise topographic projection: required in both CA1 and subicular neurons for the precise targeting of proximal CA1 axons to distal subiculum, probably by promoting homophilic cell adhesion. Required for proper dendrite morphogenesis and axon targeting in the vertebrate visual system, thereby …

**Summary**, from NCBI Gene [55714](https://www.ncbi.nlm.nih.gov/gene/55714):

> This gene encodes a member of the teneurin transmembrane protein family. The encoded protein may be involved in the regulation of neuronal development including development of the visual pathway. Mutations in this gene have been associated with microphthalmia and developmental dysplasia of the hip. [provided by RefSeq, Jan 2023]

**Accessions** — [HGNC:29944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29944) · Entrez [55714](https://www.ncbi.nlm.nih.gov/gene/55714) · UniProt [Q9P273](https://www.uniprot.org/uniprotkb/Q9P273) · Ensembl [ENSG00000218336](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000218336)

## Data

Gene col 13291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13291); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13291]; `tensor/DDL_lfc|DDL_z.npy` [13291]; `embed/gene_vectors.npy` [13291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13291 or target_col == 13291). Every well: [[TENM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
