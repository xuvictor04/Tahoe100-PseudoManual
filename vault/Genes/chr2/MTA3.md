---
symbol: "MTA3"
type: "gene"
col: 653
ensembl_id: "ENSG00000057935"
name: "metastasis associated 1 family member 3"
location: "2p21"
module: 64
arm: "+"
pooled_cpm: 71.53
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# MTA3

*metastasis associated 1 family member 3* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.24× (z +4.1, q 0.016, up in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 2.54×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.279× (z -24.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUL5]] (+0.73, fdr 7e-06), [[PEX14]] (+0.68, fdr 7e-06), [[TYW3]] (+0.68, fdr 7e-06); moves opposite to [[CDK2AP2]] (-0.58, fdr 6e-05), [[B3GAT3]] (-0.56, fdr 5e-05), [[DNAAF3]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCDHA6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ULK-101 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 653.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 2.54×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.016 | 22/47 (KATO III, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.9 | 0.016 | 19/48 (AsPC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.016 | 22/48 (NCI-H23, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.25×** | +3.6 | 0.042 | 22/50 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.052 | 20/50 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.052 | 17/47 (SW 900, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.14 | 11/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 15/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.14 | 12/48 (HepG2/C3A, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.279×** | -24.8 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.301×** | -23.4 | 0e+00 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.338×** | -21.1 | 0e+00 | 48/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.499×** | -19.1 | 0e+00 | 45/49 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.553×** | -11.5 | 1e-28 | 41/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -11.2 | 6e-27 | 42/50 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.572×** | -10.9 | 1e-25 | 41/48 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.683×** | -10.5 | 6e-24 | 36/48 (COLO 205, LOX-IMVI, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.576×** | -10.3 | 4e-23 | 38/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -8.8 | 9e-17 | 44/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -8.6 | 6e-16 | 36/48 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.650×** | -8.4 | 2e-15 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.668×** | -7.9 | 2e-13 | 38/48 (SW48, SNU-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -7.7 | 4e-13 | 36/48 (HOP62, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.544×** | -6.2 | 2e-08 | 37/49 (MIA PaCa-2, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.580×** | -5.5 | 1e-06 | 32/48 (HOP62, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.687×** | -3.8 | 0.003 | 24/49 (HEC-1-A, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.828×** | -3.7 | 0.006 | 19/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.884× | -3.4 | 0.015 | 14/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.024 | 15/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.037 | 7/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.037 | 20/48 (SNU-1, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 63.0 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 74.4 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.168× (z -18.2) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 10 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0479× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.246× (z -12.8) |
| [[SW480 (line)]] | alt | 56.4 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -24.2) |
| [[BT-474 (line)]] | alt | 70.0 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 96.5 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -22.5) |
| [[HEC-1-A (line)]] | alt | 90.3 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.25× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -19.4) |
| [[LS 180 (line)]] | wt | 65.6 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -18.8) |
| [[C32 (line)]] | wt | 75.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -15.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 68.8 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -20.9) |
| [[COLO 205 (line)]] | alt | 63.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.3) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.135× (z -18.0) |
| [[NCI-H1792 (line)]] | alt | 95.4 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -16.8) |
| [[LoVo (line)]] | wt | 59.4 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -21.4) |
| [[HCT15 (line)]] | alt | 92.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -11.8) |
| [[HT-29 (line)]] | alt | 55.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -16.6) |
| [[KATO III (line)]] | alt | 52.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 85.2 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 68.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -18.8) |
| [[RKO (line)]] | wt | 53.6 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.191× (z -15.1) |
| [[SW48 (line)]] | wt | 75.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -13.7) |
| [[A-172 (line)]] | wt | 81.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -13.3) |
| [[A-427 (line)]] | wt | 151 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -13.5) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.143× (z -13.0) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 32.4 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.237× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 88.8 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 48.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.279× (z -11.5) |
| [[PANC-1 (line)]] | alt | 86.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -13.3) |
| [[SNU-423 (line)]] | alt | 52.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.151× (z -19.0) |
| [[SW1417 (line)]] | alt | 51.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -14.5) |
| [[A549 (line)]] | wt | 69.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -17.0) |
| [[C-33 A (line)]] | alt | 118 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -14.4) |
| [[Hs 766T (line)]] | wt | 28.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -13.1) |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.8) |
| [[J82 (line)]] | alt | 45.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.1) |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 81.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -14.8) |
| [[A498 (line)]] | wt | 62.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.408× (z -9.2) |
| [[H4 (line)]] | wt | 62.3 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.307× (z -8.6) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 63.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.312× (z -10.6) |
| [[SW 900 (line)]] | alt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.4) |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUL5]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[PEX14]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TYW3]] | +0.68 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZMYM4]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[AFG1L]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DLG5]] | +0.61 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[SPR]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[GTF3C6]] | +0.60 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PSMC3]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP2]] | -0.58 | -0.38 / -0.60 | both halves | 6e-05 | pathway: ATP-dependent chromatin remodelers; STRING 445 |
| [[B3GAT3]] | -0.56 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[DNAAF3]] | -0.56 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[EPOR]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MTMR14]] | -0.55 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TRPT1]] | -0.55 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ING1]] | -0.55 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.55 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[CCNYL1]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[BET1L]] | -0.54 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[NARF]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[RELL1]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | PCDHA6 activity raises MTA3's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PCDHA6 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MTA3's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ULK-101 (drug)]] 5 µM | C | MTA3's natural level raises the cells' numbers under ULK-101 5 µM (protects the cells) | MTA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.2, 10.2); signed map (8.2, -32.0). **Vector** length 85.6, 24.1% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +8.1 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.4 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | -2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +1.5 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -21.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -23.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -19.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -5.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | metastasis associated 1 family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:42,494,569-42,756,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1266 |
| Gene groups (HGNC) | GATA zinc finger domain containing; Myb/SANT domain containing; NuRD complex subunits |
| Reactome | 28 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTC8](https://www.uniprot.org/uniprotkb/Q9BTC8) (Metastasis-associated protein MTA3):

> Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Plays a role in maintenance of the normal epithelial architecture through the repression of SNAI1 transcription in a histone deacetylase-dependent manner, and thus the regulation of E-cadherin levels. Contributes to transcriptional repression by BCL6.

**Summary**, from NCBI Gene [57504](https://www.ncbi.nlm.nih.gov/gene/57504):

> Predicted to enable histone deacetylase binding activity; transcription coactivator activity; and transcription corepressor activity. Involved in chromatin remodeling and negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of NuRD complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23784) · Entrez [57504](https://www.ncbi.nlm.nih.gov/gene/57504) · UniProt [Q9BTC8](https://www.uniprot.org/uniprotkb/Q9BTC8) · Ensembl [ENSG00000057935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057935)

## Data

Gene col 653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 653); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 653]; `tensor/DDL_lfc|DDL_z.npy` [653]; `embed/gene_vectors.npy` [653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 653 or target_col == 653). Every well: [[MTA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
