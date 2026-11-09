---
symbol: "KRT8"
type: "gene"
col: 9950
ensembl_id: "ENSG00000170421"
name: "keratin 8"
location: "12q13.13"
module: 31
arm: "+"
pooled_cpm: 229.52
n_lines_expressing: 37
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 47
direction_downstream: 7
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KRT8

*keratin 8* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.49× (z +24.2, q 0e+00, up in 36 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.22× (z +4.6, q 4e-04, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.605× (z -7.6, q 2e-11, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT18]] (+0.84, fdr 7e-06, ⚠ same locus), [[CAPN8]] (+0.71, fdr 7e-06), [[LAD1]] (+0.65, fdr 7e-06), [[CEACAM6]] (+0.63, fdr 9e-06); moves opposite to [[FAM193B]] (-0.51, fdr 2e-05), [[TOM1]] (-0.51, fdr 4e-05), [[TMEM258]] (-0.51, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 7 go from it, the strongest it → [[EPHA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +24.2 | 0e+00 | 36/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.60×** | +19.8 | 0e+00 | 33/33 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +15.9 | 0e+00 | 33/34 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.9 | 6e-10 | 6/37 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +4.8 | 2e-04 | 23/35 (PANC-1, A-427, …) | two highest doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.35×** | +4.6 | 4e-04 | 18/35 (A549, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.6 | 4e-04 | 18/35 (A-172, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.33×** | +4.5 | 4e-04 | 18/35 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 15/36 (A-172, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.002 | 16/35 (A-172, HCT15, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 19/35 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.021 | 20/35 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.023 | 15/35 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.4 | 0.026 | 11/35 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +3.4 | 0.026 | 13/37 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.041 | 12/35 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.060 | 15/35 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.073 | 16/35 (PANC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.605×** | -7.6 | 2e-11 | 25/37 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.712×** | -5.2 | 5e-05 | 22/35 (SW48, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -4.3 | 0.004 | 19/35 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.772×** | -4.1 | 0.005 | 16/35 (BT-474, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.830×** | -4.1 | 0.005 | 16/35 (SW480, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.779×** | -4.0 | 0.005 | 19/35 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.005 | 14/35 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.587×** | -3.8 | 0.012 | 20/37 (SW48, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.785×** | -3.7 | 0.012 | 17/35 (A-427, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.025 | 13/35 (SW480, SW48, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.810×** | -3.4 | 0.039 | 18/35 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.048 | 16/36 (SW48, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -3.2 | 0.062 | 14/35 (SW48, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 120 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.95× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.73× (z +11.5) | — |
| [[SW480 (line)]] | alt | 553 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +13.3) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.307× (z -10.9) |
| [[HT-29 (line)]] | alt | 786 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[PANC-1 (line)]] | alt | 147 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +21.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 107 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +16.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 94.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 3.15× (z +9.1) | — |
| [[A-427 (line)]] | wt | 73.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +15.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +19.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 183 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +20.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 316 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +12.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 288 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 98.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +15.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 166 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +13.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 241 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 632 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 509 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H23 (line)]] | alt | 153 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +17.0) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 5 µM 0.394× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 82.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +16.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 433 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +16.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 733 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 477 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H1573 (line)]] | alt | 279 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +16.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 69.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +12.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 334 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 62.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +10.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 340 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 609 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 309 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 87.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 222 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.200× (z -11.0) |
| [[AN3 CA (line)]] | alt | 32.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 51.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 40.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 46.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT18]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CAPN8]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LAD1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CEACAM6]] | +0.63 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[NAB1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[HR]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ACTB]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 | STRING 670 |
| [[ACSL5]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CTSE]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | STRING 407 |
| [[MUC2]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM193B]] | -0.51 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TOM1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[TMEM258]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NUDT2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LRRC37B]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MZT2A]] | -0.50 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[LSM8]] | -0.49 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[ELMOD3]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CHKB]] | -0.48 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[COA6]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[VEGFB]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SETDB1]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 41, C 6. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises KRT8's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.49× lower at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[C1orf116]] | B | C1orf116 activity raises KRT8's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.02× lower at baseline in the lines without C1orf116 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LAD1]] | B | LAD1 activity raises KRT8's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.70× lower at baseline in the lines without LAD1 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[SH2D3A]] | B | SH2D3A activity raises KRT8's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 4.13× lower at baseline in the lines without SH2D3A | 1e-03 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[PRSS22]] | B | PRSS22 activity raises KRT8's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 5.01× lower at baseline in the lines without PRSS22 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14 |
| [[ITGB4]] | B | ITGB4 activity raises KRT8's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.00× lower at baseline in the lines without ITGB4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TNS4]] | B | TNS4 activity raises KRT8's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 4.12× lower at baseline in the lines without TNS4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises KRT8's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without SEPTIN9-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[F2RL1]] | B | F2RL1 activity raises KRT8's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 3.81× lower at baseline in the lines without F2RL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[MALL]] | B | MALL activity raises KRT8's level | lines that do not express MALL (21) vs lines expressing it (29) | 2.91× lower at baseline in the lines without MALL | 0.004 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[KLK10]] | B | KLK10 activity raises KRT8's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without KLK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[TMEM30B]] | B | TMEM30B activity raises KRT8's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.75× lower at baseline in the lines without TMEM30B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | KRT8 activity raises EPHA2's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 3.51× lower at baseline in the lines without KRT8 | 0.066 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent |
| [[SH2D3A]] | B | KRT8 activity raises SH2D3A's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 3.80× lower at baseline in the lines without KRT8 | 0.094 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent |
| [[KIAA0040]] | B | KRT8 activity raises KIAA0040's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without KRT8 | 0.094 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent |
| [[KRT18]] | C | KRT8 activity raises KRT18's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 5.70× lower at baseline in the lines without KRT8 | 0.006 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent; co-absent with the target |
| [[MISP]] | C | KRT8 activity raises MISP's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 4.31× lower at baseline in the lines without KRT8 | 0.044 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent; co-absent with the target |
| [[EPHA2-AS1]] | C | KRT8 activity raises EPHA2-AS1's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without KRT8 | 0.045 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent; co-absent with the target |
| [[DSG2]] | C | KRT8 activity raises DSG2's level | lines that do not express KRT8 (13) vs lines expressing it (37) | 4.52× lower at baseline in the lines without KRT8 | 0.059 | ⚠ within organs, on part of the lines; also absent: KRT18, PKP2, CHMP4C; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, 50.6); signed map (66.8, 10.4). **Vector** length 108, 32.6% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +24.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[OTS514 (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.0 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Afatinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | keratin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,897,187-52,949,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARD2, K8, CK8, CK-8, CYK8, K2C8, KO |
| Gene groups (HGNC) | Keratins, type II |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P05787](https://www.uniprot.org/uniprotkb/P05787) (Keratin, type II cytoskeletal 8):

> Structural component of intermediate filaments in simple epithelial cells. Together with its obligate type I partner KRT18, contributes to the formation of the keratin intermediate filament network that provides mechanical stability and resilience to epithelial cells. Also involved in maintaining epithelial integrity and protecting cells from non-mechanical stress, such as apoptosis (By similarity). Also required for ARHGEF40-mediated actin stress fiber formation and tensional force-induced …

**Summary**, from NCBI Gene [3856](https://www.ncbi.nlm.nih.gov/gene/3856):

> This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellular structural integrity and also functions in signal transduction and cellular differentiation. …

**Accessions** — [HGNC:6446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6446) · Entrez [3856](https://www.ncbi.nlm.nih.gov/gene/3856) · UniProt [P05787](https://www.uniprot.org/uniprotkb/P05787) · Ensembl [ENSG00000170421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170421)

## Data

Gene col 9950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9950); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9950]; `tensor/DDL_lfc|DDL_z.npy` [9950]; `embed/gene_vectors.npy` [9950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9950 or target_col == 9950). Every well: [[KRT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
