---
symbol: "PITX1-AS1"
type: "gene"
col: 13385
ensembl_id: "ENSG00000224186"
name: "PITX1 antisense RNA 1"
location: "5q31.1"
module: 26
arm: "+"
pooled_cpm: 19.86
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PITX1-AS1

*PITX1 antisense RNA 1* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.71× (z +31.8, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.652× (z -7.3, q 1e-10, down in 28 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.690× (z -6.3, q 4e-08, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIBAR1-DT]] (+0.75, fdr 1e-05), [[NEB]] (+0.71, fdr 4e-05), [[PKN2-AS1]] (+0.71, fdr 1e-05); moves opposite to [[DPY30]] (-0.63, fdr 2e-05), [[WRAP73]] (-0.62, fdr 9e-05), [[AP2S1]] (-0.59, fdr 8e-04, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.71×** | +31.8 | 0e+00 | 45/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +18.2 | 0e+00 | 35/47 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +10.3 | 8e-23 | 29/43 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.8 | 1e-20 | 27/45 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.0 | 3e-17 | 31/46 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +8.5 | 1e-15 | 29/46 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.6 | 2e-12 | 26/47 (BT-474, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.29×** | +7.4 | 7e-12 | 28/47 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.6 | 3e-09 | 23/48 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 4e-07 | 24/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 3e-05 | 10/29 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 6e-04 | 16/45 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.002 | 16/47 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 13/46 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.013 | 10/46 (SW480, H4, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.026 | 9/45 (SW 900, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.652×** | -7.3 | 1e-10 | 28/44 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.654×** | -7.3 | 1e-10 | 25/48 (COLO 205, SW480, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -6.3 | 4e-08 | 21/44 (RKO, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.693×** | -6.3 | 5e-08 | 25/47 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -5.4 | 7e-06 | 21/42 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.800×** | -5.4 | 7e-06 | 22/47 (SHP-77, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -5.3 | 1e-05 | 19/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -5.2 | 2e-05 | 20/48 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -5.1 | 2e-05 | 17/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.837× | -4.3 | 0.001 | 11/48 (SW48, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.798×** | -3.8 | 0.006 | 9/48 (H4, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.802×** | -3.8 | 0.008 | 18/47 (SHP-77, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.828×** | -3.2 | 0.056 | 11/45 (SNU-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.086 | 3/48 (J82, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 72.3 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.347× (z -9.6) |
| [[COLO 205 (line)]] | alt | 88.1 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 41.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +20.6) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +19.8) | — |
| [[SHP-77 (line)]] | alt | 57.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.380× (z -8.6) |
| [[A-427 (line)]] | wt | 21.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0823× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +16.8) | — |
| [[A-172 (line)]] | wt | 15.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +15.1) | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.5) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0750× (z -12.0) |
| [[HOP62 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +18.4) | — |
| [[KATO III (line)]] | alt | 17.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -12.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 9.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.73× (z +10.3) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.27× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 30.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.173× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 12.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.8) | [[Cobimetinib (drug)]] 0.05 µM 0.147× (z -10.1) |
| [[SW48 (line)]] | wt | 23.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +15.1) | — |
| [[A498 (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +15.8) | — |
| [[A549 (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 32.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.6) | — |
| [[J82 (line)]] | alt | 8.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 8.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +17.2) | — |
| [[RKO (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0946× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIBAR1-DT]] | +0.75 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[NEB]] | +0.71 | +0.77 / +0.41 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.73 / +0.52 | both halves | 1e-05 | same gene group |
| [[MMADHC-DT]] | +0.69 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | +0.68 | +0.63 / +0.42 | both halves | 4e-05 | same gene group |
| [[LINC01340]] | +0.68 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[FAM174B]] | +0.67 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[LIX1-AS1]] | +0.67 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[DRAIC]] | +0.66 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[CFAP418-AS1]] | +0.66 | +0.63 / +0.50 | both halves | 1e-05 | same gene group |
| [[GRM8]] | +0.66 | +0.70 / +0.49 | both halves | 2e-05 |  |
| [[LINC01933]] | +0.66 | +0.70 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY30]] | -0.63 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[WRAP73]] | -0.62 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[AP2S1]] | -0.59 | -0.62 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MAST3]] | -0.59 | -0.62 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PITX1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CFAP54]] | B | CFAP54 activity lowers PITX1-AS1's level | lines that do not express CFAP54 (6) vs lines expressing it (44) | 2.03× higher at baseline in the lines without CFAP54 | 0.060 | ⚠ within organs, on part of the lines; also absent: LRP12, TMOD2, TBC1D19; maybe low, not absent; its own permutation p |
| [[UGDH]] | C | UGDH activity lowers PITX1-AS1's level | lines that do not express UGDH (3) vs lines expressing it (47) | 1.46× higher at baseline in the lines without UGDH | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, PYGB, TIMP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.0, 16.1); signed map (25.2, -0.4). **Vector** length 95.2, 20.4% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.0 | +31.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.2 | +18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +8.2 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.5 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.1 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PITX1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.1 — chr5:135,033,280-135,358,219 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C5orf66 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48332) · Entrez [100996485](https://www.ncbi.nlm.nih.gov/gene/100996485) · Ensembl [ENSG00000224186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224186)

## Data

Gene col 13385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13385); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13385]; `tensor/DDL_lfc|DDL_z.npy` [13385]; `embed/gene_vectors.npy` [13385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13385 or target_col == 13385). Every well: [[PITX1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITX1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
