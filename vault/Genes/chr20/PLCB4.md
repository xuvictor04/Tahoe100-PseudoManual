---
symbol: "PLCB4"
type: "gene"
col: 2115
ensembl_id: "ENSG00000101333"
name: "phospholipase C beta 4"
location: "20p12.3-p12.2"
module: 197
arm: "+"
pooled_cpm: 117.93
n_lines_expressing: 37
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# PLCB4

*phospholipase C beta 4* — 20p12.3-p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +13.4, q 3e-38, up in 24 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.753× (z -8.1, q 3e-13, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK6]] (+0.69, fdr 7e-06), [[ALCAM]] (+0.68, fdr 7e-06), [[CDH2]] (+0.66, fdr 7e-06); moves opposite to [[IL17RA]] (-0.61, fdr 1e-05), [[CCDC32]] (-0.60, fdr 1e-05), [[GLE1]] (-0.57, fdr 3e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TENM3]] → it (grade B ⚠); 5 go from it, the strongest it → [[TENM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +13.4 | 3e-38 | 24/35 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +11.1 | 4e-26 | 24/35 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +9.9 | 1e-20 | 24/35 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +9.1 | 1e-17 | 21/36 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +6.7 | 3e-09 | 21/36 (NCI-H460, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 4e-08 | 21/35 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.5 | 4e-06 | 17/34 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 20/34 (HEC-1-A, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 8e-04 | 14/35 (CFPAC-1, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 1e-03 | 17/34 (A549, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.004 | 15/36 (HEC-1-A, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.004 | 10/35 (HEC-1-A, A549, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.8 | 0.006 | 10/35 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.006 | 11/28 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.037 | 13/32 (NCI-H460, HOP62, …) | inconsistent across doses | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.039 | 13/35 (HEC-1-A, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 1.12× | +3.2 | 0.050 | 2/35 (H4, A-172) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.050 | 9/35 (HEC-1-A, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -8.1 | 3e-13 | 25/36 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -7.1 | 3e-10 | 25/34 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -7.0 | 4e-10 | 22/35 (A498, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -6.7 | 3e-09 | 22/35 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.739×** | -6.1 | 1e-07 | 23/35 (NCI-H2030, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.817×** | -5.8 | 8e-07 | 16/35 (J82, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -5.4 | 4e-06 | 20/35 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -5.4 | 5e-06 | 20/35 (A498, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -4.7 | 2e-04 | 16/35 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.796×** | -4.6 | 2e-04 | 19/35 (HEC-1-A, A498, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.808×** | -4.3 | 9e-04 | 18/35 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.679×** | -4.1 | 0.002 | 14/34 (NCI-H23, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.003 | 15/35 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.694×** | -3.9 | 0.005 | 12/35 (HEC-1-A, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.829×** | -3.8 | 0.006 | 16/35 (HEC-1-A, J82, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.036 | 9/35 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.851× | -3.2 | 0.036 | 12/35 (LoVo, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.899× | -3.0 | 0.063 | 8/36 (LoVo, CHP-212, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.819×** | -2.9 | 0.098 | 10/35 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 346 | 13 (5 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +32.7) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 397 | 4 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -16.3) |
| [[A549 (line)]] | wt | 275 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +29.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -13.5) |
| [[A498 (line)]] | wt | 195 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -15.8) |
| [[J82 (line)]] | alt | 500 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.273× (z -18.2) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 271 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +37.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -14.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 30.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +22.2) | — |
| [[KATO III (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -17.1) |
| [[LoVo (line)]] | wt | 116 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.70× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.420× (z -9.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.8) |
| [[A-172 (line)]] | wt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 179 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.0) | [[Selinexor (drug)]] 5 µM 0.456× (z -13.1) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.401× (z -10.8) |
| [[CHP-212 (line)]] | wt | 233 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -8.7) |
| [[LS 180 (line)]] | wt | 177 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -10.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.1) | — |
| [[RKO (line)]] | wt | 36.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.82× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -8.8) |
| [[BT-474 (line)]] | alt | 252 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.0) | — |
| [[hTERT-HPNE (line)]] | wt | 78.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 66.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.6) |
| [[SW 1271 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.5) | — |
| [[A-427 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 26.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.92 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK6]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ALCAM]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CDH2]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PARD3B]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[NFIB]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[FAT1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | same gene group; pathway: Inositol phosphate metabolism; STRING 688 |
| [[TPM1]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[TBL1XR1]] | +0.58 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[TSPAN2]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SPTLC3]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[GLE1]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SS18L1]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[VRK3]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SDF2]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TAF11]] | -0.53 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[GPR89B]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3]] | B | TENM3 activity raises PLCB4's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without TENM3 | 0.038 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[HLF]] | B | HLF activity raises PLCB4's level | lines that do not express HLF (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without HLF | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM230C, CHST8, GPR158; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3]] | B | PLCB4 activity raises TENM3's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.91× lower at baseline in the lines without PLCB4 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[ALCAM]] | B | PLCB4 activity raises ALCAM's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without PLCB4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[COL12A1]] | B | PLCB4 activity raises COL12A1's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 4.61× lower at baseline in the lines without PLCB4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[SLC4A4]] | B | PLCB4 activity raises SLC4A4's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without PLCB4 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[PGM5P2-1]] | B | PLCB4 activity raises PGM5P2-1's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without PLCB4 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 14.9); signed map (46.5, 18.4). **Vector** length 113, 29.3% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.1 | -5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -6.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.3 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3-p12.2 — chr20:9,067,825-9,504,593 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 9 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; PLC beta mediated events; G-protein mediated events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15147](https://www.uniprot.org/uniprotkb/Q15147) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase beta-4):

> Activated phosphatidylinositol-specific phospholipase C enzymes catalyze the production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3) involved in G protein-coupled receptor signaling pathways. PLCB4 is a direct effector of the endothelin receptor signaling pathway that plays an essential role in lower jaw and middle ear structures development.

**Summary**, from NCBI Gene [5332](https://www.ncbi.nlm.nih.gov/gene/5332):

> The protein encoded by this gene catalyzes the formation of inositol 1,4,5-trisphosphate and diacylglycerol from phosphatidylinositol 4,5-bisphosphate. This reaction uses calcium as a cofactor and plays an important role in the intracellular transduction of many extracellular signals in the retina. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:9059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9059) · Entrez [5332](https://www.ncbi.nlm.nih.gov/gene/5332) · UniProt [Q15147](https://www.uniprot.org/uniprotkb/Q15147) · Ensembl [ENSG00000101333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101333)

## Data

Gene col 2115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2115); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2115]; `tensor/DDL_lfc|DDL_z.npy` [2115]; `embed/gene_vectors.npy` [2115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2115 or target_col == 2115). Every well: [[PLCB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
