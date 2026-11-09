---
symbol: "SLC2A13"
type: "gene"
col: 7496
ensembl_id: "ENSG00000151229"
name: "solute carrier family 2 member 13"
location: "12q12"
module: 88
arm: "-"
pooled_cpm: 156.3
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# SLC2A13

*solute carrier family 2 member 13* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.51× (z +8.8, q 1e-15, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.497× (z -14.9, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA6]] (+0.56, fdr 2e-04), [[SNX25]] (+0.55, fdr 1e-04), [[CHD1L]] (+0.55, fdr 3e-05); moves opposite to [[FAIM]] (-0.59, fdr 1e-04), [[MR1]] (-0.56, fdr 7e-05), [[LRRC37A3]] (-0.56, fdr 0.002, ⚠ not reproduced), [[ARMCX4]] (-0.56, fdr 6e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PMP22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +8.8 | 1e-15 | 31/46 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +8.3 | 3e-14 | 29/46 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.9 | 4e-13 | 33/46 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +5.2 | 3e-05 | 25/47 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 5e-05 | 23/46 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 23/46 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.0 | 0.006 | 17/46 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.37×** | +3.5 | 0.030 | 19/43 (A498, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.14 | 6/47 (BT-474, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -14.9 | 0e+00 | 38/46 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.632×** | -13.8 | 6e-41 | 32/46 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -11.6 | 1e-28 | 35/46 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -11.1 | 3e-26 | 38/45 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -11.0 | 4e-26 | 31/47 (LoVo, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -10.1 | 3e-22 | 32/46 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -9.6 | 5e-20 | 29/42 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -8.5 | 1e-15 | 36/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -8.1 | 4e-14 | 35/46 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -8.0 | 7e-14 | 31/46 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -7.6 | 1e-12 | 29/46 (C32, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -6.9 | 3e-10 | 32/46 (AsPC-1, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -6.5 | 4e-09 | 30/46 (HOP62, PANC-1, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.756×** | -5.9 | 1e-07 | 32/46 (KATO III, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.774×** | -5.4 | 2e-06 | 26/46 (HOP62, LoVo, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.777×** | -5.3 | 3e-06 | 30/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.777×** | -5.3 | 3e-06 | 26/46 (SNU-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -5.2 | 7e-06 | 23/46 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -4.7 | 9e-05 | 17/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -4.4 | 3e-04 | 21/46 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -4.1 | 8e-04 | 21/45 (HT-29, LS 180, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.9 | 0.002 | 20/46 (NCI-H1792, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.886× | -3.6 | 0.006 | 4/47 (AsPC-1, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 371 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.249× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 247 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -11.8) |
| [[HOP62 (line)]] | alt | 143 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -18.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -13.1) |
| [[LoVo (line)]] | wt | 333 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -22.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -19.4) |
| [[C32 (line)]] | wt | 235 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.356× (z -12.8) |
| [[SNU-1 (line)]] | wt | 189 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -15.4) |
| [[A498 (line)]] | wt | 117 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.434× (z -10.5) |
| [[A549 (line)]] | wt | 138 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -26.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.141× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 93.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.35× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -20.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 147 | 2 | 5 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.23× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 197 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 206 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -24.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -13.6) |
| [[PANC-1 (line)]] | alt | 94.2 | 2 | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.85× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -14.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.367× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 805 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 54.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -10.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 67.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +11.6) | — |
| [[J82 (line)]] | alt | 172 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 145 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -8.9) |
| [[SNU-423 (line)]] | alt | 126 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -12.7) |
| [[CHP-212 (line)]] | wt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -11.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 223 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 57.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 93.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.4) | — |
| [[A-172 (line)]] | wt | 81.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.428× (z -8.7) |
| [[BT-474 (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -11.2) |
| [[H4 (line)]] | wt | 156 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.282× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 56.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.93× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -12.9) |
| [[SHP-77 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 1.99× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 81.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -9.4) |
| [[RKO (line)]] | wt | 133 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.314× (z -11.3) |
| [[SW48 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 35.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | +0.56 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[SNX25]] | +0.55 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[CHD1L]] | +0.55 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[LANCL3]] | +0.54 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[C1orf21]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[FLNB]] | +0.54 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[PAG1]] | +0.54 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[PSD3]] | +0.53 | +0.58 / +0.32 | both halves | 2e-04 |  |
| [[GLG1]] | +0.53 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[MLXIP]] | +0.53 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[NPHP4]] | +0.53 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[KIAA1328]] | +0.53 | +0.44 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.59 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[MR1]] | -0.56 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[LRRC37A3]] | -0.56 | -0.49 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[ARMCX4]] | -0.56 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[RNF146]] | -0.55 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[TXNRD2]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[DCUN1D1]] | -0.55 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[TBCEL]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[THNSL2]] | -0.54 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[CCNT2]] | -0.54 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[MARVELD2]] | -0.54 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[IQCH-AS1]] | -0.53 | -0.52 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[C1RL]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ACCS]] | -0.53 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | PMP22 activity raises SLC2A13's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without PMP22 | 0.054 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SLC2A13's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PMP22]] | B | PMP22 activity strengthens SLC2A13's drug response | lines that do not express PMP22 (10) vs lines expressing it (37) | the lines without PMP22 respond 0.58× as strongly (z diff +2.34); strongest at Homoharringtonine 5 µM: 1.02x vs 0.54x (z diff +6.6) | 0.089 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (0.5, 11.5); signed map (-5.6, 53.5). **Vector** length 108, 30.2% of its response variance represented; |z| ≥ 3 in 1,460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.1 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.3 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +0.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -14.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:39,755,025-40,106,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HMIT |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 3 pathways, smallest: Inositol transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QE2](https://www.uniprot.org/uniprotkb/Q96QE2) (Proton myo-inositol cotransporter):

> H(+)-myo-inositol cotransporter. Can also transport related stereoisomers.

**Summary**, from NCBI Gene [114134](https://www.ncbi.nlm.nih.gov/gene/114134):

> Enables ATPase binding activity; myo-inositol:proton symporter activity; and protease binding activity. Involved in myo-inositol transport and positive regulation of amyloid-beta formation. Located in cell body and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15956) · Entrez [114134](https://www.ncbi.nlm.nih.gov/gene/114134) · UniProt [Q96QE2](https://www.uniprot.org/uniprotkb/Q96QE2) · Ensembl [ENSG00000151229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151229)

## Data

Gene col 7496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7496); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7496]; `tensor/DDL_lfc|DDL_z.npy` [7496]; `embed/gene_vectors.npy` [7496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7496 or target_col == 7496). Every well: [[SLC2A13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
