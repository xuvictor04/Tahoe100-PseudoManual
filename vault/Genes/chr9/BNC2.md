---
symbol: "BNC2"
type: "gene"
col: 10336
ensembl_id: "ENSG00000173068"
name: "basonuclin zinc finger protein 2"
location: "9p22.3-p22.2"
module: 121
arm: "+"
pooled_cpm: 79.89
n_lines_expressing: 29
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 30
direction_downstream: 57
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# BNC2

*basonuclin zinc finger protein 2* — 9p22.3-p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Retinoic acid (drug)]] 0.05 µM: 1.29× (z +4.0, q 0.042, up in 15 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 4.53×, A-427 3.21×, NCI-H661 6.89×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 5.29×, NCI-H661 4.55×; ⚠ cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.299× (z -19.0, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03041]] (+0.70, fdr 7e-06, ⚠ read-through risk), [[DOCK10]] (+0.56, fdr 4e-05), [[TTC28]] (+0.54, fdr 2e-05), [[ZFHX4]] (+0.54, fdr 3e-05); moves opposite to [[ESRP1]] (-0.50, fdr 5e-05), [[RAB33B-AS1]] (-0.47, fdr 4e-05), [[FUT3]] (-0.47, fdr 1e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[ESRP1]] → it (grade B ⚠); 57 go from it, the strongest it → [[SNHG26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10336.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 4.53×, A-427 3.21×, NCI-H661 6.89×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 5.29×, NCI-H661 4.55×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.042 | 15/27 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.067 | 10/26 (A-172, C32, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.22 | 5/27 (NCI-H460, C-33 A, …) | rises with dose | position effect removed |
| [[Bentamapimod (drug)]] 5 µM |  | 1.46× | +3.1 | 0.22 | 10/27 (HOP62, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.22 | 4/27 (A549, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10336.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.299×** | -19.0 | 0e+00 | 26/27 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.327×** | -17.6 | 0e+00 | 24/27 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -16.3 | 0e+00 | 25/27 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.539×** | -9.3 | 1e-18 | 19/24 (LOX-IMVI, J82, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.530×** | -9.2 | 3e-18 | 20/25 (SNU-423, J82, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.571×** | -8.8 | 1e-16 | 23/27 (HOP62, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -8.7 | 2e-16 | 16/25 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.369×** | -8.2 | 2e-14 | 22/27 (RKO, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.524×** | -7.6 | 2e-12 | 20/28 (A-427, J82, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.612×** | -7.4 | 7e-12 | 19/27 (RKO, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.653×** | -6.5 | 6e-09 | 20/29 (RKO, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.664×** | -6.1 | 6e-08 | 17/27 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.698×** | -5.7 | 7e-07 | 19/27 (hTERT-HPNE, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.775×** | -5.5 | 2e-06 | 14/27 (NCI-H1792, RKO, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -5.4 | 2e-06 | 12/27 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -5.2 | 6e-06 | 19/27 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -5.1 | 1e-05 | 16/27 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.733×** | -4.9 | 3e-05 | 14/27 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.752×** | -4.5 | 2e-04 | 13/27 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.753×** | -4.5 | 2e-04 | 17/27 (LOX-IMVI, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.770×** | -4.1 | 0.001 | 10/27 (MIA PaCa-2, A549, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.624×** | -3.9 | 0.003 | 12/26 (Hs 766T, C-33 A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.003 | 14/27 (RKO, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10336. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 506 | 0 | 24 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0205× (z -37.1) |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.167× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.218× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -35.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.203× (z -14.3) |
| [[SNU-423 (line)]] | alt | 271 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -17.9) |
| [[A498 (line)]] | wt | 273 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -19.6) |
| [[A549 (line)]] | wt | 82.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -17.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -12.2) |
| [[C32 (line)]] | wt | 169 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -14.5) |
| [[HS-578T (line)]] | alt | 279 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -17.4) |
| [[J82 (line)]] | alt | 133 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -13.0) |
| [[C-33 A (line)]] | alt | 434 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -17.1) |
| [[A-427 (line)]] | wt | 115 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0625× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.332× (z -9.3) |
| [[A-172 (line)]] | wt | 79.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.53× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -10.7) |
| [[Hs 766T (line)]] | wt | 47.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -13.4) |
| [[NCI-H661 (line)]] | alt | 157 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +10.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.89× (z +9.6) | — |
| [[H4 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HOP62 (line)]] | alt | 54.2 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.259× (z -9.4) |
| [[AN3 CA (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10336), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03041]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 | ⚠ **readthrough risk**: LINC03041 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[DOCK10]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TTC28]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZFHX4]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 | same gene group |
| [[DSE]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[PHACTR1]] | +0.53 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[KIRREL1]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC01776]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[ADAMTS12]] | +0.52 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[NR2F1-AS1]] | +0.52 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[EVC]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[VEGFC]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CDK17]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESRP1]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[RAB33B-AS1]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[FUT3]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TMEM45B]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[TMC4]] | -0.47 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[EPS8L3]] | -0.46 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[MPZL2]] | -0.44 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[DNM2]] | -0.43 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[GPR35]] | -0.43 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[TMEM125]] | -0.43 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[RORC]] | -0.43 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[INAVA]] | -0.42 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 14, C 16. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP1]] | B | ESRP1 activity lowers BNC2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 6.60× higher at baseline in the lines without ESRP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TMEM125]] | B | TMEM125 activity lowers BNC2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 7.00× higher at baseline in the lines without TMEM125 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[GPR35]] | B | GPR35 activity lowers BNC2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 7.03× higher at baseline in the lines without GPR35 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[INAVA]] | B | INAVA activity lowers BNC2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 4.88× higher at baseline in the lines without INAVA | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[RORC]] | B | RORC activity lowers BNC2's level | lines that do not express RORC (30) vs lines expressing it (20) | 5.00× higher at baseline in the lines without RORC | 0.006 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[TMEM45B]] | B | TMEM45B activity lowers BNC2's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 6.86× higher at baseline in the lines without TMEM45B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[GALNT3]] | B | GALNT3 activity lowers BNC2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 5.05× higher at baseline in the lines without GALNT3 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[MPZL2]] | B | MPZL2 activity lowers BNC2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 6.85× higher at baseline in the lines without MPZL2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[FUT3]] | B | FUT3 activity lowers BNC2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.83× higher at baseline in the lines without FUT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[TMC4]] | B | TMC4 activity lowers BNC2's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 4.83× higher at baseline in the lines without TMC4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[EPS8L3]] | B | EPS8L3 activity lowers BNC2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 6.61× higher at baseline in the lines without EPS8L3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[ARHGAP31]] | B | ARHGAP31 activity raises BNC2's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.93× lower at baseline in the lines without ARHGAP31 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 37, C 20. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG26]] | B | BNC2 activity raises SNHG26's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without BNC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[TMEM45B]] | B | BNC2 activity lowers TMEM45B's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 8.02× higher at baseline in the lines without BNC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[SCHIP1]] | B | BNC2 activity raises SCHIP1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.99× lower at baseline in the lines without BNC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[MPZL2]] | B | BNC2 activity lowers MPZL2's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 5.85× higher at baseline in the lines without BNC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[GPR35]] | B | BNC2 activity lowers GPR35's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.84× higher at baseline in the lines without BNC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[FRMD6]] | B | BNC2 activity raises FRMD6's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.53× lower at baseline in the lines without BNC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[INAVA]] | B | BNC2 activity lowers INAVA's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 4.66× higher at baseline in the lines without BNC2 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[DDAH1]] | B | BNC2 activity raises DDAH1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 1.22× lower at baseline in the lines without BNC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | B | BNC2 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.16× the cells of the other lines | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| cells under [[5-Azacytidine (drug)]] 5 µM | B | BNC2 activity lowers the cells' numbers under 5-Azacytidine 5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.30× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | BNC2 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 0.88× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[DSE]] | B | BNC2 activity raises DSE's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without BNC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.3, 24.4); signed map (29.1, 32.9). **Vector** length 93.8, 26.0% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -8.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -8.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | basonuclin zinc finger protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3-p22.2 — chr9:16,409,503-16,870,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BSN2, FLJ20043, bn2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Basonuclin zinc finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN30](https://www.uniprot.org/uniprotkb/Q6ZN30) (Zinc finger protein basonuclin-2):

> Probable transcription factor specific for skin keratinocytes. May play a role in the differentiation of spermatozoa and oocytes. May also play an important role in early urinary-tract development.

**Summary**, from NCBI Gene [54796](https://www.ncbi.nlm.nih.gov/gene/54796):

> This gene encodes a conserved zinc finger protein. The encoded protein functions in skin color saturation. Mutations in this gene are associated with facial pigmented spots. This gene is also associated with susceptibility to adolescent idiopathic scoliosis. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:30988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30988) · Entrez [54796](https://www.ncbi.nlm.nih.gov/gene/54796) · UniProt [Q6ZN30](https://www.uniprot.org/uniprotkb/Q6ZN30) · Ensembl [ENSG00000173068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173068)

## Data

Gene col 10336: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10336); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10336, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10336]; `tensor/DDL_lfc|DDL_z.npy` [10336]; `embed/gene_vectors.npy` [10336]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10336 or target_col == 10336). Every well: [[BNC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
