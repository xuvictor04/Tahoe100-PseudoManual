---
symbol: "RBMS3"
type: "gene"
col: 6906
ensembl_id: "ENSG00000144642"
name: "RNA binding motif single stranded interacting protein 3"
location: "3p24.1"
module: 121
arm: "+"
pooled_cpm: 244.42
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 36
n_dd_up_clean: 19
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# RBMS3

*RNA binding motif single stranded interacting protein 3* — 3p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.31× (z +29.5, q 0e+00, up in 25 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.142× (z -33.9, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZEB2]] (+0.72, fdr 7e-06), [[ARHGAP24]] (+0.71, fdr 7e-06), [[MAGI2]] (+0.66, fdr 7e-06); moves opposite to [[CAPN10]] (-0.53, fdr 2e-05), [[KLHL25]] (-0.53, fdr 2e-05), [[NAPG]] (-0.50, fdr 2e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PLAGL1]] → it (grade B ⚠); 11 go from it, the strongest it → [[CNTNAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.31×** | +29.5 | 0e+00 | 25/29 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.12×** | +19.1 | 0e+00 | 26/29 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +16.4 | 0e+00 | 21/29 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +11.3 | 1e-27 | 21/29 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +6.8 | 1e-09 | 19/29 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +6.6 | 4e-09 | 20/30 (HOP62, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +6.4 | 2e-08 | 22/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +5.4 | 5e-06 | 19/29 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 6e-06 | 16/29 (A549, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 7e-06 | 14/29 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 7e-06 | 21/28 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +5.2 | 8e-06 | 19/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.2 | 9e-06 | 19/31 (HEC-1-A, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 1e-05 | 17/29 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +5.1 | 1e-05 | 18/29 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 1e-04 | 17/30 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.142×** | -33.9 | 0e+00 | 29/29 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.169×** | -30.9 | 0e+00 | 29/29 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.232×** | -25.4 | 0e+00 | 27/29 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.366×** | -17.5 | 0e+00 | 27/29 (H4, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.436×** | -14.4 | 4e-45 | 29/29 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.426×** | -14.3 | 3e-44 | 25/28 (LOX-IMVI, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -14.2 | 4e-44 | 24/30 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.469×** | -12.6 | 1e-34 | 21/28 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.484×** | -12.6 | 1e-34 | 27/30 (A-172, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.508×** | -11.3 | 6e-28 | 23/27 (SNU-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.548×** | -10.5 | 8e-24 | 25/30 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.529×** | -10.4 | 8e-24 | 28/29 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.558×** | -10.1 | 2e-22 | 26/29 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.538×** | -10.0 | 9e-22 | 21/27 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.568×** | -9.8 | 3e-21 | 28/29 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -8.9 | 1e-17 | 24/29 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.446×** | -7.3 | 7e-12 | 25/29 (SNU-423, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.688×** | -6.5 | 2e-09 | 22/29 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -6.4 | 3e-09 | 20/29 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.545×** | -5.5 | 8e-07 | 21/30 (SNU-423, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.804×** | -5.3 | 2e-06 | 15/29 (SNU-423, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.58 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 218 | 19 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.186× (z -18.5) |
| [[H4 (line)]] | wt | 282 | 11 | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.0989× (z -22.2) |
| [[SNU-423 (line)]] | alt | 618 | 2 | 18 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.0838× (z -29.8) |
| [[J82 (line)]] | alt | 648 | 1 | 16 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.105× (z -23.1) |
| [[NCI-H1792 (line)]] | alt | 1,078 | 0 | 17 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0605× (z -38.8) |
| [[LOX-IMVI (line)]] | wt | 659 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0750× (z -29.4) |
| [[RPMI-7951 (line)]] | alt | 364 | 5 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -21.1) |
| [[A-172 (line)]] | wt | 303 | 9 (2 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +24.4) | [[Panobinostat (drug)]] 5 µM 0.104× (z -23.9) |
| [[C32 (line)]] | wt | 610 | 0 | 15 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 559 | 3 | 11 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.0713× (z -29.2) |
| [[NCI-H460 (line)]] | wt | 484 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0912× (z -24.9) |
| [[HS-578T (line)]] | alt | 601 | 7 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +24.3) | [[Panobinostat (drug)]] 5 µM 0.128× (z -22.5) |
| [[A498 (line)]] | wt | 172 | 8 | 4 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +30.1) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -18.2) |
| [[PANC-1 (line)]] | alt | 118 | 3 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +23.3) | [[Panobinostat (drug)]] 5 µM 0.213× (z -17.2) |
| [[A549 (line)]] | wt | 167 | 3 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.9) | [[Panobinostat (drug)]] 5 µM 0.100× (z -20.9) |
| [[CHP-212 (line)]] | wt | 855 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0802× (z -19.1) |
| [[hTERT-HPNE (line)]] | wt | 485 | 4 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.0952× (z -23.4) |
| [[HOP62 (line)]] | alt | 298 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +24.6) | [[Panobinostat (drug)]] 5 µM 0.125× (z -16.9) |
| [[SNU-1 (line)]] | wt | 1,720 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.142× (z -22.0) |
| [[SK-MEL-2 (line)]] | alt | 316 | 2 | 6 | [[Harringtonine (drug)]] 5 µM 4.09× (z +13.7) | [[Auranofin (drug)]] 5 µM 0.279× (z -13.0) |
| [[A-427 (line)]] | wt | 202 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +17.7) | [[Ixazomib citrate (drug)]] 5 µM 0.285× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +18.4) | [[Panobinostat (drug)]] 5 µM 0.226× (z -12.2) |
| [[Hs 766T (line)]] | wt | 187 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.136× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 164 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +21.8) | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 118 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +20.9) | — |
| [[SW 1088 (line)]] | alt | 393 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0524× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 223 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 927 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -11.6) |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0657× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 48.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 34.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 33.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 26.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 17.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZEB2]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ARHGAP24]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MAGI2]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[BHLHE41]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[NLGN4Y]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TRPC4]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.60 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[GPR176]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CAV1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[DPY19L2]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[JAM2]] | +0.59 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[KLHL25]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[NAPG]] | -0.50 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[MTFR1]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SS18L1]] | -0.49 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[TESK1]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TMEM41B]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[STARD3]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[NFATC3]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[TPD52L2]] | -0.48 | -0.47 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAGL1]] | B | PLAGL1 activity raises RBMS3's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.94× lower at baseline in the lines without PLAGL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[MAP2K1]] | B | MAP2K1 activity lowers RBMS3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises RBMS3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UTY]] | B | UTY activity raises RBMS3's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without UTY | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY |
| [[PGM5P2]] | B | PGM5P2 activity raises RBMS3's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 3.42× lower at baseline in the lines without PGM5P2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[ZEB2]] | C | ZEB2 activity raises RBMS3's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 7.61× lower at baseline in the lines without ZEB2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises RBMS3's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 5.63× lower at baseline in the lines without BNC2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises RBMS3's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 6.77× lower at baseline in the lines without FAT4 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[COL12A1]] | C | COL12A1 activity raises RBMS3's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 5.83× lower at baseline in the lines without COL12A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[DPY19L2P2-1]] | C | DPY19L2P2-1 activity raises RBMS3's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 4.16× lower at baseline in the lines without DPY19L2P2-1 | 0.032 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2; co-absent with the target |
| [[CNTNAP1]] | C | CNTNAP1 activity raises RBMS3's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 6.53× lower at baseline in the lines without CNTNAP1 | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[CAV1]] | C | CAV1 activity raises RBMS3's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.22× lower at baseline in the lines without CAV1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP1]] | B | RBMS3 activity raises CNTNAP1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without RBMS3 | 0.029 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[DPY19L2P2]] | B | RBMS3 activity raises DPY19L2P2's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without RBMS3 | 0.038 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[CSF1]] | B | RBMS3 activity raises CSF1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 2.96× lower at baseline in the lines without RBMS3 | 0.048 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[KLHL25]] | B | RBMS3 activity lowers KLHL25's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.53× higher at baseline in the lines without RBMS3 | 0.057 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| cells under [[Balsalazide (sodium hydrate) (drug)]] 5 µM | B | RBMS3 activity raises the cells' numbers under Balsalazide (sodium hydrate) 5 µM (protects the cells) | lines that do not express RBMS3 (19) vs lines expressing it (29) | the lines without RBMS3: 0.89× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[STK24]] | B | RBMS3 activity lowers STK24's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.92× higher at baseline in the lines without RBMS3 | 0.091 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[DPY19L2P2-1]] | C | RBMS3 activity raises DPY19L2P2-1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without RBMS3 | 0.013 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |
| [[LINC01776]] | C | RBMS3 activity raises LINC01776's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 3.19× lower at baseline in the lines without RBMS3 | 0.049 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |
| [[COL12A1]] | C | RBMS3 activity raises COL12A1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 6.29× lower at baseline in the lines without RBMS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |
| [[BNC2]] | C | RBMS3 activity raises BNC2's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 5.02× lower at baseline in the lines without RBMS3 | 0.076 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |
| [[ZEB2]] | C | RBMS3 activity raises ZEB2's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 9.08× lower at baseline in the lines without RBMS3 | 0.091 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 24.5); signed map (42.7, 25.5). **Vector** length 137, 45.2% of its response variance represented; |z| ≥ 3 in 1,534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +12.3 | +19.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.8 | +29.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +11.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +4.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.5 | -14.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.1 | -10.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.0 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -17.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif single stranded interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.1 — chr3:28,574,791-30,010,391 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XE24](https://www.uniprot.org/uniprotkb/Q6XE24) (RNA-binding motif, single-stranded-interacting protein 3):

> Binds poly(A) and poly(U) oligoribonucleotides.

**Summary**, from NCBI Gene [27303](https://www.ncbi.nlm.nih.gov/gene/27303):

> This gene encodes an RNA-binding protein that belongs to the c-myc gene single-strand binding protein family. These proteins are characterized by the presence of two sets of ribonucleoprotein consensus sequence (RNP-CS) that contain conserved motifs, RNP1 and RNP2, originally described in RNA binding proteins, and required for DNA binding. These proteins have been implicated in such diverse functions as DNA replication, gene transcription, cell cycle progression and apoptosis. The encoded …

**Accessions** — [HGNC:13427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13427) · Entrez [27303](https://www.ncbi.nlm.nih.gov/gene/27303) · UniProt [Q6XE24](https://www.uniprot.org/uniprotkb/Q6XE24) · Ensembl [ENSG00000144642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144642)

## Data

Gene col 6906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6906); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6906]; `tensor/DDL_lfc|DDL_z.npy` [6906]; `embed/gene_vectors.npy` [6906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6906 or target_col == 6906). Every well: [[RBMS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
