---
symbol: "SLC5A4-AS1"
type: "gene"
col: 14300
ensembl_id: "ENSG00000242082"
name: "SLC5A4 antisense RNA 1"
location: "22q12.3"
module: 146
arm: "+"
pooled_cpm: 14.08
n_lines_expressing: 35
n_dd_up: 33
n_dd_down: 32
n_dd_up_clean: 28
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 14
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# SLC5A4-AS1

*SLC5A4 antisense RNA 1* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.87× (z +11.5, q 4e-28, up in 29 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.279× (z -16.7, q 0e+00, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A12]] (+0.64, fdr 1e-05), [[LINC00937]] (+0.62, fdr 1e-05), [[KCNK15-AS1]] (+0.59, fdr 2e-05); moves opposite to [[WFDC10B]] (-0.61, fdr 3e-05), [[WFDC3]] (-0.60, fdr 2e-05), [[WDR45]] (-0.53, fdr 4e-04).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PROS1]] → it (grade B ⚠); 14 go from it, the strongest it → [[DTWD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +11.5 | 4e-28 | 29/33 (PANC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +9.5 | 4e-19 | 26/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +8.6 | 1e-15 | 22/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +8.3 | 1e-14 | 24/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +7.4 | 1e-11 | 20/33 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +7.2 | 6e-11 | 23/33 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.71×** | +7.0 | 2e-10 | 24/33 (A498, NCI-H1573, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +6.6 | 4e-09 | 22/33 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +6.1 | 7e-08 | 21/33 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +6.1 | 7e-08 | 20/33 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 12/33 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.28×** | +4.5 | 3e-04 | 13/33 (A-427, C32, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 12/33 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.41×** | +4.3 | 6e-04 | 14/30 (LoVo, A498, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.003 | 11/33 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.004 | 12/33 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 11/33 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.006 | 12/33 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.279×** | -16.7 | 0e+00 | 26/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.299×** | -15.7 | 0e+00 | 30/33 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.359×** | -13.4 | 2e-38 | 28/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.372×** | -12.9 | 7e-36 | 28/32 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.504×** | -12.6 | 2e-34 | 22/30 (RKO, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.386×** | -11.5 | 2e-28 | 16/23 (HEC-1-A, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -9.3 | 1e-18 | 28/33 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -8.8 | 1e-16 | 22/32 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.512×** | -8.4 | 3e-15 | 22/32 (NCI-H460, A498, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.331×** | -7.5 | 3e-12 | 22/32 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -7.2 | 4e-11 | 21/30 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.597×** | -6.7 | 8e-10 | 19/33 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -6.6 | 2e-09 | 17/33 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.605×** | -6.5 | 2e-09 | 21/33 (LoVo, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.598×** | -6.5 | 4e-09 | 19/32 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.704×** | -6.5 | 4e-09 | 21/33 (CHP-212, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.618×** | -6.0 | 6e-08 | 16/33 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.667×** | -5.3 | 4e-06 | 17/33 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.681×** | -4.8 | 4e-05 | 15/33 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.697×** | -4.7 | 7e-05 | 15/31 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -4.7 | 7e-05 | 16/31 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -4.5 | 1e-04 | 16/33 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 24.6 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0626× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0974× (z -19.5) |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0645× (z -18.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -10.8) |
| [[RKO (line)]] | wt | 38.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.9) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 58.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.7) |
| [[SW480 (line)]] | alt | 16.7 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.143× (z -14.2) |
| [[PANC-1 (line)]] | alt | 6.96 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 8.80× (z +11.4) | [[Digitoxin (drug)]] 0.5 µM 0.192× (z -8.7) |
| [[A-427 (line)]] | wt | 36.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -14.3) |
| [[A498 (line)]] | wt | 20.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.7) |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.187× (z -9.9) |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.0) |
| [[A549 (line)]] | wt | 10.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.107× (z -10.5) |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0887× (z -12.1) |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0719× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0526× (z -10.0) |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.8) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0516× (z -13.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 6.21 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0437× (z -12.1) |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 5.75 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0811× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A12]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[KCNK15-AS1]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 | same gene group |
| [[ADAM22]] | +0.58 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[KLHL13]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SLC27A2]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[FXN]] | +0.56 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[MTMR8]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RAVER2]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ASIC1]] | +0.54 | +0.31 / +0.61 | both halves | 2e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WFDC10B]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[WFDC3]] | -0.60 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[WDR45]] | -0.53 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[FANK1]] | -0.53 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[BCL10-AS1]] | -0.52 | -0.29 / -0.58 | both halves | 3e-04 | same gene group |
| [[ERVK13-1]] | -0.52 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[CCNT2-AS1]] | -0.52 | -0.26 / -0.33 | both halves | 4e-04 | same gene group |
| [[ATXN1L]] | -0.52 | -0.20 / -0.59 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DDX5]] | -0.51 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[GPATCH2L]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CPEB2-DT]] | -0.50 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[LINC00310]] | -0.49 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[SLC35F5]] | -0.49 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.49 | -0.23 / -0.50 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROS1]] | B | PROS1 activity raises SLC5A4-AS1's level | lines that do not express PROS1 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without PROS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: WDR35, AGK, ERO1B |
| [[NFIA]] | B | NFIA activity raises SLC5A4-AS1's level | lines that do not express NFIA (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without NFIA | 0.062 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[SULT1A1]] | B | SULT1A1 activity raises SLC5A4-AS1's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without SULT1A1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTWD2]] | B | SLC5A4-AS1 activity raises DTWD2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without SLC5A4-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[RAVER2]] | B | SLC5A4-AS1 activity raises RAVER2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without SLC5A4-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[DTNB]] | B | SLC5A4-AS1 activity raises DTNB's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without SLC5A4-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[STX18-AS1]] | B | SLC5A4-AS1 activity raises STX18-AS1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without SLC5A4-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[GDPD1]] | B | SLC5A4-AS1 activity raises GDPD1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 2.23× lower at baseline in the lines without SLC5A4-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[CDIN1]] | B | SLC5A4-AS1 activity raises CDIN1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without SLC5A4-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[GSTA4]] | B | SLC5A4-AS1 activity raises GSTA4's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without SLC5A4-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[HMGXB3]] | B | SLC5A4-AS1 activity lowers HMGXB3's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.18× higher at baseline in the lines without SLC5A4-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[UBE3D]] | B | SLC5A4-AS1 activity raises UBE3D's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without SLC5A4-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[IRAK1BP1]] | B | SLC5A4-AS1 activity raises IRAK1BP1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SLC5A4-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[FLVCR2]] | B | SLC5A4-AS1 activity lowers FLVCR2's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.75× higher at baseline in the lines without SLC5A4-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[TEP1]] | B | SLC5A4-AS1 activity raises TEP1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without SLC5A4-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.9, 38.7); signed map (42.5, -9.2). **Vector** length 71.3, 14.9% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.4 | +7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | SLC5A4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.3 — chr22:32,205,115-32,278,382 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP1-90G24.10 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53163) · Entrez [110806273](https://www.ncbi.nlm.nih.gov/gene/110806273) · Ensembl [ENSG00000242082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242082)

## Data

Gene col 14300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14300); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14300]; `tensor/DDL_lfc|DDL_z.npy` [14300]; `embed/gene_vectors.npy` [14300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14300 or target_col == 14300). Every well: [[SLC5A4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC5A4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
