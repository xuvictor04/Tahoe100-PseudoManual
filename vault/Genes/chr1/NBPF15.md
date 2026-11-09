---
symbol: "NBPF15"
type: "gene"
col: 15487
ensembl_id: "ENSG00000266338"
name: "NBPF member 15"
location: "1q21.1"
module: 110
arm: "+"
pooled_cpm: 52.86
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# NBPF15

*NBPF member 15* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +4.6, q 0.002, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -19.1, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.696× (z -6.2, q 8e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF8]] (+0.81, fdr 7e-06), [[NBPF9]] (+0.73, fdr 7e-06), [[NBPF20]] (+0.68, fdr 7e-06); moves opposite to [[EFNA1]] (-0.59, fdr 1e-05), [[CTNND1]] (-0.55, fdr 3e-05), [[C4orf33]] (-0.55, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PARVB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 0.002 | 23/47 (hTERT-HPNE, HOP62, …) | two highest doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.29×** | +4.4 | 0.003 | 23/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.015 | 17/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +3.9 | 0.015 | 23/47 (RPMI-7951, LOX-IMVI, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.028 | 22/48 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.053 | 20/47 (SHP-77, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.072 | 22/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.22×** | +3.2 | 0.083 | 18/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.083 | 15/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.20× | +3.1 | 0.11 | 16/47 (NCI-H1573, SW 900, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 13/47 (NCI-H1573, SNU-1, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 10/48 (C-33 A, LOX-IMVI, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.454×** | -19.1 | 0e+00 | 43/48 (NCI-H460, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.829×** | -10.9 | 3e-25 | 24/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.611×** | -8.1 | 1e-13 | 34/48 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.665×** | -7.0 | 5e-10 | 29/48 (NCI-H460, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -6.2 | 8e-08 | 28/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.702×** | -6.0 | 1e-07 | 27/47 (NCI-H23, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.721×** | -5.6 | 2e-06 | 22/48 (SW48, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.708×** | -5.3 | 8e-06 | 24/45 (NCI-H23, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.576×** | -4.9 | 5e-05 | 30/49 (HOP62, A549, …) | all doses, stronger at high dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.752×** | -4.9 | 7e-05 | 23/48 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.588×** | -4.7 | 1e-04 | 25/42 (NCI-H1792, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.797×** | -4.7 | 1e-04 | 26/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.767×** | -4.5 | 3e-04 | 22/48 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.761×** | -4.5 | 3e-04 | 26/48 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.780×** | -4.2 | 9e-04 | 25/47 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.719×** | -4.0 | 0.002 | 21/47 (Panc 03.27, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.797×** | -3.9 | 0.004 | 19/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -3.7 | 0.006 | 18/48 (HS-578T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.814×** | -3.3 | 0.026 | 20/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.3 | 0.028 | 14/48 (Hs 766T, A498, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.041 | 16/48 (HCT15, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.866× | -2.8 | 0.092 | 13/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.847× | -2.8 | 0.092 | 14/47 (J82, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.832×** | -2.8 | 0.092 | 16/47 (SW48, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **0.729×** | -2.8 | 0.092 | 15/48 (C32, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 0.849× | -2.8 | 0.100 | 14/48 (SW480, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 79.9 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.404× (z -10.6) |
| [[A549 (line)]] | wt | 52.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0686× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[MIA PaCa-2 (line)]] | alt | 83.4 | 0 | 5 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.580× (z -18.0) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.398× (z -8.7) |
| [[HS-578T (line)]] | alt | 50.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 83.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 47.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 53.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 64.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A-172 (line)]] | wt | 85.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 38.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 74.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 55.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[PANC-1 (line)]] | alt | 79.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.195× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF8]] | +0.81 | +0.81 / +0.77 | both halves | 7e-06 | same gene group |
| [[NBPF9]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | same gene group |
| [[NBPF20]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | same gene group |
| [[RUSC2]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[GSTO1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.60 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[DPY19L3]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.59 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | +0.58 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[FAM89A]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[CRYL1]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA1]] | -0.59 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CTNND1]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[C4orf33]] | -0.55 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[GBP2]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TET2]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PBX2]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ARHGAP42]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TEF]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[BCL3]] | -0.54 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ECH1]] | -0.54 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[HNRNPH2]] | -0.53 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[BHLHE41]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVB]] | B | PARVB activity raises NBPF15's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PARVB | 0.009 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[RBM47]] | B | RBM47 activity lowers NBPF15's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 1.66× higher at baseline in the lines without RBM47 | 0.011 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[NT5M]] | B | NT5M activity raises NBPF15's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without NT5M | 0.032 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[NT5M]] | B | NT5M activity strengthens NBPF15's drug response | lines that do not express NT5M (7) vs lines expressing it (42) | the lines without NT5M respond 0.44× as strongly (z diff +2.33); strongest at Homoharringtonine 0.5 µM: 1.11x vs 0.61x (z diff +4.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG; target measured in part of the lines; artifact flags |
| [[GBP2]] | B | GBP2 activity lowers NBPF15's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without GBP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ZEB1]] | B | ZEB1 activity raises NBPF15's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without ZEB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[PALS2]] | C | PALS2 activity raises NBPF15's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without PALS2 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[FSD1L]] | C | FSD1L activity raises NBPF15's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without FSD1L | 0.068 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.9, -25.1); signed map (-17.4, 47.1). **Vector** length 110, 28.5% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.6 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.8 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -8.1 | -19.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.3 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.4 | -7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:144,421,390-144,461,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8902; previously NBPF16 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q8N660](https://www.uniprot.org/uniprotkb/Q8N660) carries no function annotation.

**Summary**, from NCBI Gene [284565](https://www.ncbi.nlm.nih.gov/gene/284565):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:28791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28791) · Entrez [284565](https://www.ncbi.nlm.nih.gov/gene/284565) · UniProt [Q8N660](https://www.uniprot.org/uniprotkb/Q8N660) · Ensembl [ENSG00000266338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266338)

## Data

Gene col 15487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15487); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15487]; `tensor/DDL_lfc|DDL_z.npy` [15487]; `embed/gene_vectors.npy` [15487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15487 or target_col == 15487). Every well: [[NBPF15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
