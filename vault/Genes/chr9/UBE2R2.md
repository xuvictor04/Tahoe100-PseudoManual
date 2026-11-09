---
symbol: "UBE2R2"
type: "gene"
col: 2846
ensembl_id: "ENSG00000107341"
name: "ubiquitin conjugating enzyme E2 R2"
location: "9p13.3"
module: 3
arm: "+"
pooled_cpm: 192.53
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# UBE2R2

*ubiquitin conjugating enzyme E2 R2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.39× (z +11.5, q 9e-28, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -30.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGEF1P1]] (+0.68, fdr 7e-06), [[UBE2D2]] (+0.67, fdr 7e-06), [[UBE2G1]] (+0.66, fdr 9e-06); moves opposite to [[PRKAR1A]] (-0.63, fdr 1e-05), [[HNRNPK]] (-0.60, fdr 1e-05), [[SLC35A5]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +11.5 | 9e-28 | 43/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.9 | 1e-12 | 37/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +7.8 | 2e-12 | 35/48 (SW480, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +6.2 | 9e-08 | 29/48 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.3 | 1e-05 | 25/48 (SW480, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.003 | 26/49 (A498, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.5 | 0.034 | 20/45 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.15× | +3.5 | 0.034 | 19/47 (HS-578T, HOP62, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.10× | +3.4 | 0.047 | 1/49 (HT-29) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.11 | 8/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.13 | 4/48 (LS 180, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -30.0 | 0e+00 | 47/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -18.8 | 0e+00 | 44/48 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.500×** | -17.5 | 0e+00 | 45/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.549×** | -15.1 | 0e+00 | 44/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -14.4 | 8e-45 | 38/44 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.618×** | -12.1 | 6e-32 | 43/49 (AsPC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.649×** | -10.9 | 1e-25 | 39/48 (AsPC-1, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.740×** | -10.7 | 5e-25 | 35/49 (A-172, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.635×** | -10.6 | 2e-24 | 36/45 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -10.3 | 5e-23 | 32/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -6.3 | 1e-08 | 30/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -6.3 | 1e-08 | 25/48 (A-172, J82, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.788×** | -5.8 | 4e-07 | 27/50 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -4.4 | 5e-04 | 23/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.834× | -4.4 | 5e-04 | 24/48 (HS-578T, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.842× | -4.3 | 6e-04 | 23/48 (SK-MEL-2, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.848× | -4.1 | 0.001 | 18/48 (A-172, SW48, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.878× | -3.3 | 0.030 | 13/48 (AsPC-1, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 242 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -31.8) |
| [[AsPC-1 (line)]] | alt | 460 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -26.3) |
| [[J82 (line)]] | alt | 220 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -30.1) |
| [[PANC-1 (line)]] | alt | 273 | 1 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.69× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 195 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -23.3) |
| [[SW480 (line)]] | alt | 180 | 4 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.33× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -19.4) |
| [[HT-29 (line)]] | alt | 247 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -21.3) |
| [[KATO III (line)]] | alt | 221 | 1 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.455× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 187 | 1 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 2.65× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -21.4) |
| [[SNU-423 (line)]] | alt | 187 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -19.7) |
| [[LS 180 (line)]] | wt | 248 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 178 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -19.4) |
| [[SW 900 (line)]] | alt | 178 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -16.6) |
| [[SW1417 (line)]] | alt | 225 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.53× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.387× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -26.7) |
| [[COLO 205 (line)]] | alt | 260 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 5.10× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -24.3) |
| [[LoVo (line)]] | wt | 247 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -22.1) |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 206 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -30.1) |
| [[Panc 03.27 (line)]] | alt | 198 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -22.6) |
| [[A498 (line)]] | wt | 196 | 1 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.69× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.549× (z -10.6) |
| [[BT-474 (line)]] | alt | 171 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -12.4) |
| [[H4 (line)]] | wt | 309 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 147 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.85× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.406× (z -14.9) |
| [[HOP62 (line)]] | alt | 203 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -27.1) |
| [[HS-578T (line)]] | alt | 148 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -18.8) |
| [[SNU-1 (line)]] | wt | 194 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.9) |
| [[SW48 (line)]] | wt | 237 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.7) |
| [[A-427 (line)]] | wt | 126 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.11× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -10.9) |
| [[A549 (line)]] | wt | 214 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.436× (z -13.8) |
| [[C32 (line)]] | wt | 110 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 4.66× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 159 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 157 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -22.7) |
| [[NCI-H1573 (line)]] | alt | 93.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.5) |
| [[RKO (line)]] | wt | 168 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.58× (z +12.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.452× (z -12.1) |
| [[AN3 CA (line)]] | alt | 207 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.8) |
| [[Hs 766T (line)]] | wt | 183 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.8) |
| [[C-33 A (line)]] | alt | 193 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 175 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.8) |
| [[SW 1271 (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.0) |
| [[CHP-212 (line)]] | wt | 219 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1P1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[UBE2D2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 626 |
| [[UBE2G1]] | +0.66 | +0.70 / +0.57 | both halves | 9e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 431 |
| [[MACO1]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[COX6C]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[RALA]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ATOX1]] | +0.61 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TUBD1]] | +0.61 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MARK4]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR1A]] | -0.63 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SLC35A5]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SCRN1]] | -0.60 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ELK4]] | -0.59 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[UBAP2L]] | -0.59 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[GUF1]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ALG10B]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TAF9]] | -0.57 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[FAM111A]] | -0.57 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[EIF2B5]] | -0.56 | -0.67 / -0.46 | both halves | 2e-05 |  |
| [[SRSF6]] | -0.56 | -0.57 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBE2R2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises UBE2R2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.7, -4.8); signed map (-39.3, 4.3). **Vector** length 113, 36.4% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.9 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +11.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | -2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -18.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -30.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.9 | -10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 R2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,817,160-33,920,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBC3B, CDC34B, FLJ20419, MGC10481 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q712K3](https://www.uniprot.org/uniprotkb/Q712K3) (Ubiquitin-conjugating enzyme E2 R2):

> E2 ubiquitin-conjugating enzyme that accepts ubiquitin from an E1 ubiquitin-activating protein, and catalyzes its covalent attachment to other proteins by an E3 ubiquitin-protein ligase complex. In vitro catalyzes monoubiquitination and 'Lys-48'-linked polyubiquitination. Works in collaboration with various Cul1-RING and Cul2-RING E3 ligase complexes. May be involved in degradation of katenin.

**Summary**, from NCBI Gene [54926](https://www.ncbi.nlm.nih.gov/gene/54926):

> Protein kinase CK2 is a ubiquitous and pleiotropic Ser/Thr protein kinase involved in cell growth and transformation. This gene encodes a protein similar to the E2 ubiquitin conjugating enzyme UBC3/CDC34. Studies suggest that CK2-dependent phosphorylation of this ubiquitin-conjugating enzyme functions by regulating beta-TrCP substrate recognition and induces its interaction with beta-TrCP, enhancing beta-catenin degradation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19907) · Entrez [54926](https://www.ncbi.nlm.nih.gov/gene/54926) · UniProt [Q712K3](https://www.uniprot.org/uniprotkb/Q712K3) · Ensembl [ENSG00000107341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107341)

## Data

Gene col 2846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2846); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2846]; `tensor/DDL_lfc|DDL_z.npy` [2846]; `embed/gene_vectors.npy` [2846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2846 or target_col == 2846). Every well: [[UBE2R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
