---
symbol: "USP25"
type: "gene"
col: 7886
ensembl_id: "ENSG00000155313"
name: "ubiquitin specific peptidase 25"
location: "21q21.1"
module: 216
arm: "+"
pooled_cpm: 176.45
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# USP25

*ubiquitin specific peptidase 25* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +7.6, q 2e-11, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.509× (z -11.9, q 4e-30, down in 37 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -11.2, q 1e-26, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENAH]] (+0.59, fdr 1e-05), [[SGMS1]] (+0.56, fdr 1e-05), [[MIPOL1]] (+0.55, fdr 1e-05); moves opposite to [[ZNF275]] (-0.54, fdr 3e-05), [[ARAP1]] (-0.52, fdr 1e-05), [[PPIL3]] (-0.52, fdr 2e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.6 | 2e-11 | 33/45 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.7 | 7e-04 | 32/44 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +4.4 | 0.002 | 25/46 (HT-29, HOP62, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.009 | 29/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +4.0 | 0.009 | 27/47 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.019 | 13/45 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.021 | 23/44 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.021 | 15/45 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.047 | 23/45 (Hs 766T, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.049 | 24/47 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.055 | 19/45 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.055 | 21/45 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.055 | 21/45 (SW 900, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.11 | 20/45 (SW 900, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.509×** | -11.9 | 4e-30 | 37/41 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.544×** | -11.2 | 1e-26 | 40/46 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -11.2 | 1e-26 | 39/46 (A549, BT-474, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.569×** | -8.9 | 1e-16 | 36/42 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.622×** | -8.8 | 2e-16 | 39/45 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -5.7 | 9e-07 | 30/44 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.556×** | -5.3 | 1e-05 | 27/46 (RKO, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.754×** | -5.2 | 1e-05 | 32/45 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.793×** | -4.3 | 0.001 | 26/45 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.636×** | -4.1 | 0.003 | 28/42 (RKO, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.796×** | -4.0 | 0.003 | 24/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.009 | 26/45 (SW1417, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.821×** | -3.6 | 0.012 | 22/45 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.024 | 22/45 (A549, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.838× | -3.3 | 0.041 | 20/45 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.041 | 20/45 (SW1417, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 152 | 13 (1 ⚠) | 2 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.65× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 290 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 297 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 242 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 177 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0617× (z -34.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.7) |
| [[SNU-423 (line)]] | alt | 159 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.1) |
| [[SW480 (line)]] | alt | 176 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -13.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -10.5) |
| [[A-172 (line)]] | wt | 189 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -12.7) |
| [[A-427 (line)]] | wt | 248 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.516× (z -9.0) |
| [[A549 (line)]] | wt | 257 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -27.6) |
| [[BT-474 (line)]] | alt | 187 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -17.6) |
| [[RKO (line)]] | wt | 166 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -14.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -11.1) |
| [[A498 (line)]] | wt | 197 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -8.9) |
| [[C-33 A (line)]] | alt | 282 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 337 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.5) |
| [[PANC-1 (line)]] | alt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.6) |
| [[SW1417 (line)]] | alt | 243 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.8) |
| [[HT-29 (line)]] | alt | 153 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.419× (z -10.0) |
| [[LoVo (line)]] | wt | 154 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 231 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.494× (z -9.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -8.9) |
| [[SNU-1 (line)]] | wt | 168 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -9.9) |
| [[SW48 (line)]] | wt | 226 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 222 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.295× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 98.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.5) |
| [[HS-578T (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.7) |
| [[KATO III (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.390× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 205 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.7) |
| [[SW 1088 (line)]] | alt | 119 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0921× (z -8.5) |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.164× (z -9.0) |
| [[AN3 CA (line)]] | alt | 34.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 163 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 453 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 99.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENAH]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SGMS1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SNX24]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[CHN1]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[EFR3A]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SHTN1]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[DTNB]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[STK3]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PTPN21]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[MYCBP2]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[YWHAH]] | +0.50 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF275]] | -0.54 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ARAP1]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PPIL3]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RCN3]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CCNK]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ADAM8]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ECD]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP1]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[KLHL3]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ISY1]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RPL34-DT]] | -0.49 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[WDR37]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -25.0); signed map (9.4, -3.7). **Vector** length 114, 38.0% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.3 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -6.1 | -8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.3 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.9 | -11.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:15,729,982-15,880,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | USP21 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHP3](https://www.uniprot.org/uniprotkb/Q9UHP3) (Ubiquitin carboxyl-terminal hydrolase 25):

> Deubiquitinating enzyme that hydrolyzes ubiquitin moieties conjugated to substrates and thus, functions in various biological processes including inflammation and immune response. Modulates the Wnt/beta-catenin pathway by deubiquitinating and stabilizing tankyrases TNKS1 and TNKS2. Regulates KEAP1-NRF2 axis in the defense against oxidative assaults by deubiquitinating KEAP1 and protecting it from degradation leading to degradation of the NRF2 transcription factor that is responsible for …

**Summary**, from NCBI Gene [29761](https://www.ncbi.nlm.nih.gov/gene/29761):

> Ubiquitin (MIM 191339) is a highly conserved 76-amino acid protein involved in regulation of intracellular protein breakdown, cell cycle regulation, and stress response. Ubiquitin is released from degraded proteins by disassembly of the polyubiquitin chains, which is mediated by ubiquitin-specific proteases (USPs), such as USP25 (Valero et al., 1999 [PubMed 10644437]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:12624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12624) · Entrez [29761](https://www.ncbi.nlm.nih.gov/gene/29761) · UniProt [Q9UHP3](https://www.uniprot.org/uniprotkb/Q9UHP3) · Ensembl [ENSG00000155313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155313)

## Data

Gene col 7886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7886); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7886]; `tensor/DDL_lfc|DDL_z.npy` [7886]; `embed/gene_vectors.npy` [7886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7886 or target_col == 7886). Every well: [[USP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
