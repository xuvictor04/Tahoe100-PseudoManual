---
symbol: "CAVIN1"
type: "gene"
col: 10825
ensembl_id: "ENSG00000177469"
name: "caveolae associated protein 1"
location: "17q21.2"
module: 224
arm: "+"
pooled_cpm: 176.06
n_lines_expressing: 44
n_dd_up: 30
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# CAVIN1

*caveolae associated protein 1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.40× (z +10.3, q 3e-22, up in 38 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.77× (z +7.0, q 6e-10, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.761× (z -4.8, q 8e-04, down in 39 of 42 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.507× (z -4.4, q 0.002, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PICALM]] (+0.59, fdr 3e-05), [[SERTAD2]] (+0.58, fdr 7e-06), [[LMNA]] (+0.52, fdr 3e-05); moves opposite to [[PHB2]] (-0.50, fdr 2e-05), [[SNX13]] (-0.46, fdr 3e-05), [[POLR3E]] (-0.46, fdr 5e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[COL5A3]] → it (grade B ⚠); 5 go from it, the strongest it → [[S100A10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.40×** | +10.3 | 3e-22 | 38/39 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +7.0 | 6e-10 | 35/42 (SW480, SW1417, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.9 | 1e-09 | 37/42 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +6.6 | 7e-09 | 32/42 (A549, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.27×** | +6.4 | 1e-08 | 38/43 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.71×** | +6.1 | 1e-07 | 29/40 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +5.4 | 4e-06 | 24/42 (A549, HOP62, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.1 | 2e-05 | 29/41 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +5.0 | 3e-05 | 30/42 (NCI-H460, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.49×** | +4.9 | 5e-05 | 33/42 (SW 900, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.45×** | +4.6 | 3e-04 | 29/42 (SW480, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 6e-04 | 23/43 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +4.3 | 7e-04 | 32/41 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 30/43 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.87×** | +4.0 | 0.002 | 30/40 (NCI-H1573, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.002 | 26/43 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.81×** | +3.7 | 0.007 | 33/42 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.030 | 18/42 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.033 | 24/41 (MIA PaCa-2, A549, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.041 | 26/42 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.044 | 22/42 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.044 | 21/42 (A-172, A-427, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +2.8 | 0.089 | 19/41 (NCI-H1573, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.761×** | -4.8 | 8e-04 | 39/42 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.670×** | -4.7 | 8e-04 | 28/42 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.507×** | -4.4 | 0.002 | 34/43 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.753×** | -3.5 | 0.061 | 23/42 (H4, HOP62, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.592×** | -3.4 | 0.077 | 28/43 (Hs 766T, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.082 | 33/42 (SW 900, A498, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 112 | 7 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.18× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 74.6 | 5 (2 ⚠) | 0 | [[Daptomycin (drug)]] 0.5 µM 5.54× (z +11.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 5.66× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 115 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.19× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 187 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[A549 (line)]] | wt | 195 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.54× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 559 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Bortezomib (drug)]] 0.05 µM 0.308× (z -11.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.393× (z -9.5) |
| [[H4 (line)]] | wt | 206 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.249× (z -11.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.318× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 152 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.73× (z +9.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 83.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 103 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +11.3) | — |
| [[A-172 (line)]] | wt | 401 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.7) | — |
| [[A498 (line)]] | wt | 329 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 153 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.76× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 305 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.8) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.342× (z -10.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 356 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 297 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 130 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.66× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[RPMI-7951 (line)]] | alt | 278 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 196 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 165 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 84.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 82.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 383 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 70.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 214 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 81.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +11.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 249 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 293 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 387 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PICALM]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SERTAD2]] | +0.58 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LMNA]] | +0.52 | +0.59 / +0.45 | both halves | 3e-05 | STRING 510 |
| [[LIMA1]] | +0.52 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[CAV2]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 | STRING 920 |
| [[KCTD11]] | +0.51 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[COL1A1]] | +0.51 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[DUSP14]] | +0.51 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[CALM2]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[MYL6]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[EHD2]] | +0.49 | +0.36 / +0.47 | both halves | 1e-04 | STRING 893 |
| [[CCDC80]] | +0.48 | +0.40 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB2]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SNX13]] | -0.46 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[POLR3E]] | -0.46 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[LETMD1]] | -0.45 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[UBAC2]] | -0.44 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MRPL37]] | -0.44 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[HERC2P9-1]] | -0.43 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[TRMT2B]] | -0.43 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[NSMAF]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[MRPS15]] | -0.43 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[CDKAL1]] | -0.42 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DRAM2]] | -0.42 | -0.44 / -0.40 | both halves | 5e-05 | pathway: HALLMARK_ADIPOGENESIS |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL5A3]] | B | COL5A3 activity raises CAVIN1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without COL5A3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[PSMB5]] | B | PSMB5 activity raises CAVIN1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FOXD1]] | B | FOXD1 activity raises CAVIN1's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 3.40× lower at baseline in the lines without FOXD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |
| [[EMP3]] | B | EMP3 activity raises CAVIN1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without EMP3 | 0.088 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[AXL]] | B | AXL activity raises CAVIN1's level | lines that do not express AXL (14) vs lines expressing it (36) | 3.66× lower at baseline in the lines without AXL | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A10]] | B | CAVIN1 activity raises S100A10's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without CAVIN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[FSCN1]] | B | CAVIN1 activity raises FSCN1's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 3.24× lower at baseline in the lines without CAVIN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[SYNPO]] | B | CAVIN1 activity raises SYNPO's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without CAVIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[DLGAP4]] | B | CAVIN1 activity raises DLGAP4's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without CAVIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[SMS]] | B | CAVIN1 activity raises SMS's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CAVIN1 | 0.087 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, 8.1); signed map (3.2, 23.3). **Vector** length 112, 37.0% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -6.1 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.5 | -3.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | caveolae associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,402,449-42,423,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cavin-1, CGL4; previously PTRF |
| Gene groups (HGNC) | Cavins |
| Hallmark sets | HYPOXIA, ADIPOGENESIS |
| Reactome | 8 pathways, smallest: RNA Polymerase I Transcription Termination; RNA Polymerase I Transcription; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NZI2](https://www.uniprot.org/uniprotkb/Q6NZI2) (Caveolae-associated protein 1):

> Plays an important role in caveolae formation and organization. Essential for the formation of caveolae in all tissues. Core component of the CAVIN complex which is essential for recruitment of the complex to the caveolae in presence of calveolin-1 (CAV1). Essential for normal oligomerization of CAV1. Promotes ribosomal transcriptional activity in response to metabolic challenges in the adipocytes and plays an important role in the formation of the ribosomal transcriptional loop. Dissociates …

**Summary**, from NCBI Gene [284119](https://www.ncbi.nlm.nih.gov/gene/284119):

> This gene encodes a protein that enables the dissociation of paused ternary polymerase I transcription complexes from the 3' end of pre-rRNA transcripts. This protein regulates rRNA transcription by promoting the dissociation of transcription complexes and the reinitiation of polymerase I on nascent rRNA transcripts. This protein also localizes to caveolae at the plasma membrane and is thought to play a critical role in the formation of caveolae and the stabilization of caveolins. This protein …

**Accessions** — [HGNC:9688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9688) · Entrez [284119](https://www.ncbi.nlm.nih.gov/gene/284119) · UniProt [Q6NZI2](https://www.uniprot.org/uniprotkb/Q6NZI2) · Ensembl [ENSG00000177469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177469)

## Data

Gene col 10825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10825); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10825]; `tensor/DDL_lfc|DDL_z.npy` [10825]; `embed/gene_vectors.npy` [10825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10825 or target_col == 10825). Every well: [[CAVIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAVIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
