---
symbol: "ANKRD6"
type: "gene"
col: 5677
ensembl_id: "ENSG00000135299"
name: "ankyrin repeat domain 6"
location: "6q15"
module: 102
arm: "+"
pooled_cpm: 20.48
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 29
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# ANKRD6

*ankyrin repeat domain 6* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.48× (z +7.9, q 1e-12, up in 22 of 32 measured lines) ⚠ cell-cycle shift, explains ~82% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.57× (z +6.5, q 2e-08, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -21.0, q 0e+00, down in 24 of 32 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.286× (z -9.4, q 9e-19, down in 24 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP1B2P]] (+0.62, fdr 1e-05), [[FAM124A]] (+0.61, fdr 1e-05), [[MCF2L2]] (+0.58, fdr 9e-06); moves opposite to [[LINC01170]] (-0.41, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[MCF2L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.48×** | +7.9 | 1e-12 | 22/32 (A-172, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 2e-08 | 19/30 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.1 | 2e-07 | 14/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.6 | 5e-04 | 13/31 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +4.6 | 5e-04 | 14/30 (J82, LoVo, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.25×** | +4.5 | 6e-04 | 12/32 (C-33 A, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +4.0 | 0.005 | 16/31 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.007 | 13/31 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.031 | 9/32 (LoVo, C-33 A, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.033 | 7/32 (AN3 CA, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.25×** | +3.3 | 0.057 | 9/32 (J82, LoVo, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.074 | 7/32 (PANC-1, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.086 | 5/32 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.49× | +3.0 | 0.10 | 7/31 (C-33 A, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.354×** | -21.0 | 0e+00 | 24/32 (NCI-H1792, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.453×** | -11.3 | 3e-27 | 26/31 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.488×** | -10.3 | 2e-22 | 21/27 (C-33 A, AN3 CA, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.490×** | -9.8 | 2e-20 | 22/28 (NCI-H23, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.286×** | -9.4 | 9e-19 | 24/30 (SK-MEL-2, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.555×** | -8.1 | 5e-14 | 18/31 (A498, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.558×** | -7.7 | 1e-12 | 19/26 (NCI-H1792, A-172, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.598×** | -7.3 | 1e-11 | 22/30 (J82, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.615×** | -6.9 | 3e-10 | 17/31 (C32, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.622×** | -6.5 | 4e-09 | 19/23 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -6.4 | 8e-09 | 20/31 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.447×** | -6.0 | 8e-08 | 23/29 (A-172, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.657×** | -6.0 | 9e-08 | 18/31 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.3 | 4e-06 | 18/31 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.691×** | -5.3 | 5e-06 | 16/31 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.743×** | -4.2 | 7e-04 | 13/31 (HOP62, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.577×** | -4.1 | 0.001 | 10/30 (A549, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.9 | 0.002 | 12/32 (HEC-1-A, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.004 | 13/31 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.770×** | -3.6 | 0.009 | 13/31 (SW 1271, SNU-423, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.039 | 11/30 (RPMI-7951, SNU-423, …) | top dose only |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.809×** | -3.0 | 0.056 | 7/31 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.811×** | -3.0 | 0.061 | 9/32 (SNU-423, SW 1088, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.810×** | -2.9 | 0.079 | 9/32 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0687× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.3) |
| [[C32 (line)]] | wt | 51.6 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -22.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.1) |
| [[A-172 (line)]] | wt | 33.6 | 1 (1 ⚠) | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.07× (z +8.6) ⚠ cell-cycle shift, explains ~82% of this change | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.461× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 54.7 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -11.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.6) |
| [[A549 (line)]] | wt | 37.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.102× (z -9.5) |
| [[J82 (line)]] | alt | 19.1 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0970× (z -9.5) |
| [[HOP62 (line)]] | alt | 24.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 53.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 47.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0348× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[PANC-1 (line)]] | alt | 9.95 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 5.36× (z +10.8) | — |
| [[A-427 (line)]] | wt | 55.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.102× (z -9.7) |
| [[A498 (line)]] | wt | 21.0 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0561× (z -20.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AN3 CA (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0906× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.224× (z -8.6) |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0936× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Panc 03.27 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP1B2P]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[FAM124A]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MCF2L2]] | +0.58 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[RASGEF1C]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[STOX2]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MAP6]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC00937]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DOCK3]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[ANKRD29]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 | same gene group |
| [[ULK2]] | +0.51 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[HOMER2]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[LRRN2]] | +0.50 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01170]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ANKRD6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MSI1]] | B | MSI1 activity raises ANKRD6's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without MSI1 | 0.085 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ANKRD6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ADCY1]] | C | ADCY1 activity raises ANKRD6's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 3.39× lower at baseline in the lines without ADCY1 | 0.031 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |
| [[STOX2]] | C | STOX2 activity raises ANKRD6's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 3.18× lower at baseline in the lines without STOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27; co-absent with the target |
| [[ULK2]] | C | ULK2 activity raises ANKRD6's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 4.14× lower at baseline in the lines without ULK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2; co-absent with the target |
| [[LRRN2]] | C | LRRN2 activity raises ANKRD6's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 2.38× lower at baseline in the lines without LRRN2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL; co-absent with the target |
| [[KHDC1-AS1]] | C | KHDC1-AS1 activity raises ANKRD6's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 4.04× lower at baseline in the lines without KHDC1-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[ETNK2]] | C | ETNK2 activity raises ANKRD6's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 3.79× lower at baseline in the lines without ETNK2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent; co-absent with the target |
| [[RAB6B]] | C | RAB6B activity raises ANKRD6's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 3.64× lower at baseline in the lines without RAB6B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L2]] | B | ANKRD6 activity raises MCF2L2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without ANKRD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[ADAP2]] | B | ANKRD6 activity raises ADAP2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without ANKRD6 | 0.062 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[CIB2]] | B | ANKRD6 activity raises CIB2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without ANKRD6 | 0.068 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[LINC00937]] | B | ANKRD6 activity raises LINC00937's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without ANKRD6 | 0.080 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB |
| [[LRRN2]] | C | ANKRD6 activity raises LRRN2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without ANKRD6 | 0.039 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[COL4A4]] | C | ANKRD6 activity raises COL4A4's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without ANKRD6 | 0.055 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[ZNF287]] | C | ANKRD6 activity raises ZNF287's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without ANKRD6 | 0.055 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[ADCY1]] | C | ANKRD6 activity raises ADCY1's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 4.04× lower at baseline in the lines without ANKRD6 | 0.056 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[ETNK2]] | C | ANKRD6 activity raises ETNK2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without ANKRD6 | 0.074 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[RASGEF1C]] | C | ANKRD6 activity raises RASGEF1C's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.21× lower at baseline in the lines without ANKRD6 | 0.075 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[STOX2]] | C | ANKRD6 activity raises STOX2's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 4.38× lower at baseline in the lines without ANKRD6 | 0.084 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |
| [[COL4A3]] | C | ANKRD6 activity raises COL4A3's level | lines that do not express ANKRD6 (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without ANKRD6 | 0.097 | ⚠ within organs, on part of the lines; also absent: MAP9, RIMKLB, TUB; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.0, 40.4); signed map (26.3, 29.6). **Vector** length 84.9, 22.3% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.5 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +4.2 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +3.5 | -10.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.0 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -9.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.7 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,433,152-89,633,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0957 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G4](https://www.uniprot.org/uniprotkb/Q9Y2G4) (Ankyrin repeat domain-containing protein 6):

> Recruits CKI-epsilon to the beta-catenin degradation complex that consists of AXN1 or AXN2 and GSK3-beta and allows efficient phosphorylation of beta-catenin, thereby inhibiting beta-catenin/Tcf signals.

**Summary**, from NCBI Gene [22881](https://www.ncbi.nlm.nih.gov/gene/22881):

> Predicted to be involved in establishment or maintenance of cell polarity and regulation of Wnt signaling pathway. Predicted to act upstream of or within negative regulation of canonical Wnt signaling pathway and positive regulation of Wnt signaling pathway, planar cell polarity pathway. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17280) · Entrez [22881](https://www.ncbi.nlm.nih.gov/gene/22881) · UniProt [Q9Y2G4](https://www.uniprot.org/uniprotkb/Q9Y2G4) · Ensembl [ENSG00000135299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135299)

## Data

Gene col 5677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5677); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5677]; `tensor/DDL_lfc|DDL_z.npy` [5677]; `embed/gene_vectors.npy` [5677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5677 or target_col == 5677). Every well: [[ANKRD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
