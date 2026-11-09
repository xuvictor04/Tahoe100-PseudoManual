---
symbol: "AGO1"
type: "gene"
col: 1709
ensembl_id: "ENSG00000092847"
name: "argonaute RISC component 1"
location: "1p34.3"
module: 25
arm: "+"
pooled_cpm: 42.82
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# AGO1

*argonaute RISC component 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +9.2, q 2e-17, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.63× (z +8.3, q 1e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.496× (z -17.0, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.560× (z -9.9, q 6e-21, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP200]] (+0.76, fdr 7e-06), [[PABIR2]] (+0.74, fdr 7e-06), [[NDRG3]] (+0.73, fdr 8e-06); moves opposite to [[RBX1]] (-0.71, fdr 1e-05), [[TOPORS]] (-0.67, fdr 1e-05), [[SPATC1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.46×** | +9.2 | 2e-17 | 35/48 (A498, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.5 | 8e-15 | 31/47 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +8.3 | 1e-14 | 38/48 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.9 | 3e-13 | 32/41 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +7.7 | 1e-12 | 34/48 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +7.4 | 9e-12 | 3/48 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.5 | 4e-06 | 33/48 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.003 | 21/44 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.26×** | +4.0 | 0.005 | 21/48 (KATO III, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.020 | 20/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.029 | 8/48 (LoVo, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.075 | 17/48 (LoVo, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1709.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.496×** | -17.0 | 0e+00 | 42/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.544×** | -10.0 | 4e-21 | 40/48 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.560×** | -9.9 | 6e-21 | 35/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -7.7 | 2e-12 | 36/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -7.5 | 6e-12 | 36/48 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.664×** | -7.0 | 2e-10 | 35/47 (HT-29, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.668×** | -6.9 | 4e-10 | 33/48 (HT-29, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -6.2 | 4e-08 | 31/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.741×** | -5.1 | 2e-05 | 28/48 (HT-29, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.829×** | -3.2 | 0.074 | 17/48 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.10 | 15/48 (BT-474, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.710× | -3.1 | 0.10 | 17/49 (NCI-H460, HCT15, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.11 | 20/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 77.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 21.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -8.9) |
| [[A498 (line)]] | wt | 24.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.370× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 75.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -9.6) |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -8.7) |
| [[C32 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -8.9) |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -11.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 55.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.213× (z -9.4) ⚠ toxic · without an alert: [[vincristine (drug)]] 5 µM 0.0689× (z -8.5) |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -8.5) |
| [[J82 (line)]] | alt | 29.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.399× (z -9.0) |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.3) |
| [[A-427 (line)]] | wt | 60.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.05 µM 0.0570× (z -9.8) |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0964× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 97.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.0) |
| [[RKO (line)]] | wt | 45.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP200]] | +0.76 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[PABIR2]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.73 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[RPSA]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PPT1]] | +0.68 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.68 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.67 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[CNPY3]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[OPA1]] | +0.67 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[NONO]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Cell-Cell communication |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | -0.71 | -0.50 / -0.71 | both halves | 1e-05 | pathway: Co-inhibition by PD-1 |
| [[TOPORS]] | -0.67 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.66 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[EID2]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[IRX5]] | -0.63 | -0.39 / -0.66 | both halves | 5e-05 |  |
| [[FDX2]] | -0.63 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.63 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[UNK]] | -0.62 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FOXA2]] | -0.61 | -0.38 / -0.68 | both halves | 6e-05 | pathway: Adherens junctions interactions |
| [[ZMYM5]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[MSX1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity raises AGO1's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MSX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers AGO1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.0, -24.0); signed map (-27.0, -35.5). **Vector** length 101, 24.3% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +7.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.7 | +0.2 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.6 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.8 | -17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -9.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.8 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.0 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | argonaute RISC component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,869,808-35,930,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hAGO1; previously EIF2C1 |
| Gene groups (HGNC) | RISC loading complex subunits; Argonaute RISC component family |
| Reactome | 70 pathways, smallest: Post-transcriptional silencing by small RNAs; Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL18](https://www.uniprot.org/uniprotkb/Q9UL18) (Protein argonaute-1):

> Required for RNA-mediated gene silencing (RNAi). Binds to short RNAs such as microRNAs (miRNAs) or short interfering RNAs (siRNAs), and represses the translation of mRNAs which are complementary to them. Lacks endonuclease activity and does not appear to cleave target mRNAs. Also required for transcriptional gene silencing (TGS) of promoter regions which are complementary to bound short antigene RNAs (agRNAs).

**Summary**, from NCBI Gene [26523](https://www.ncbi.nlm.nih.gov/gene/26523):

> This gene encodes a member of the argonaute family of proteins, which associate with small RNAs and have important roles in RNA interference (RNAi) and RNA silencing. This protein binds to microRNAs (miRNAs) or small interfering RNAs (siRNAs) and represses translation of mRNAs that are complementary to them. It is also involved in transcriptional gene silencing (TGS) of promoter regions that are complementary to bound short antigene RNAs (agRNAs), as well as in the degradation of miRNA-bound …

**Accessions** — [HGNC:3262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3262) · Entrez [26523](https://www.ncbi.nlm.nih.gov/gene/26523) · UniProt [Q9UL18](https://www.uniprot.org/uniprotkb/Q9UL18) · Ensembl [ENSG00000092847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092847)

## Data

Gene col 1709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1709); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1709]; `tensor/DDL_lfc|DDL_z.npy` [1709]; `embed/gene_vectors.npy` [1709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1709 or target_col == 1709). Every well: [[AGO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
