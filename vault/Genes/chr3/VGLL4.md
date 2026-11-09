---
symbol: "VGLL4"
type: "gene"
col: 6894
ensembl_id: "ENSG00000144560"
name: "vestigial like family member 4"
location: "3p25.3-p25.2"
module: 186
arm: "+"
pooled_cpm: 149.74
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# VGLL4

*vestigial like family member 4* — 3p25.3-p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.45× (z +4.1, q 0.012, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.518× (z -19.3, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4B]] (+0.63, fdr 1e-05), [[LRP5L]] (+0.63, fdr 1e-05), [[EGLN1]] (+0.61, fdr 1e-05); moves opposite to [[SETX]] (-0.53, fdr 3e-05), [[EXOC8]] (-0.53, fdr 4e-05), [[RP2]] (-0.50, fdr 6e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CREB3]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Ouabain (Octahydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.012 | 25/48 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.012 | 22/49 (HS-578T, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.017 | 25/48 (A-172, HEC-1-A, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.044 | 18/48 (C32, SW48, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.091 | 13/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.518×** | -19.3 | 0e+00 | 43/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -12.9 | 1e-35 | 44/48 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.548×** | -12.3 | 1e-32 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -11.8 | 3e-30 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.564×** | -11.7 | 9e-30 | 38/44 (C32, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.577×** | -11.7 | 1e-29 | 40/49 (C32, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.581×** | -10.7 | 8e-25 | 33/45 (C32, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.631×** | -9.8 | 7e-21 | 40/48 (SW480, SW1417, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.732×** | -6.6 | 2e-09 | 31/48 (A-427, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -6.2 | 4e-08 | 30/47 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.767×** | -5.4 | 3e-06 | 27/47 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.788×** | -5.1 | 2e-05 | 29/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.793×** | -4.9 | 3e-05 | 26/48 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.805×** | -4.6 | 2e-04 | 27/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | 0.835× | -3.8 | 0.005 | 21/48 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.847× | -3.3 | 0.040 | 16/48 (C32, H4, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.1 | 0.061 | 12/48 (SNU-1, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 361 | 2 | 10 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 5.77× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.8) |
| [[PANC-1 (line)]] | alt | 187 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -27.1) |
| [[SW48 (line)]] | wt | 185 | 2 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.29× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.233× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 242 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -14.5) |
| [[SHP-77 (line)]] | alt | 122 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.6) |
| [[SW480 (line)]] | alt | 242 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.474× (z -12.1) |
| [[A-427 (line)]] | wt | 199 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 168 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.497× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -25.9) |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 95.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -25.5) |
| [[SNU-1 (line)]] | wt | 238 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.492× (z -9.9) |
| [[HT-29 (line)]] | alt | 113 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -11.8) |
| [[LoVo (line)]] | wt | 182 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -21.6) |
| [[SW1417 (line)]] | alt | 257 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -20.4) |
| [[NCI-H1573 (line)]] | alt | 74.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -15.0) |
| [[RKO (line)]] | wt | 125 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.9) |
| [[C-33 A (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 143 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -18.2) |
| [[HS-578T (line)]] | alt | 106 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.154× (z -12.7) ⚠ toxic |
| [[J82 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.1) |
| [[KATO III (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.8) |
| [[LS 180 (line)]] | wt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -21.8) |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.555× (z -10.3) |
| [[SW 900 (line)]] | alt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -19.8) |
| [[A-172 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.505× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 89.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.4) |
| [[BT-474 (line)]] | alt | 197 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 71.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -13.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.0) |
| [[SNU-423 (line)]] | alt | 76.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -27.8) |
| [[SW 1088 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.103× (z -8.8) ⚠ toxic |
| [[A498 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4B]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[EGLN1]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[FZD3]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PDK1]] | +0.60 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[NDC1]] | +0.57 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.57 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SMAD5]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[USP3]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RYK]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[EXOC8]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[RP2]] | -0.50 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[GOLGB1]] | -0.50 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[CREB3]] | -0.50 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[TUT7]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.48 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TAF2]] | -0.48 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CYFIP1]] | -0.46 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[RAB3GAP2]] | -0.46 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[ZNF674]] | -0.46 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[SAP30BP]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3]] | C | CREB3's natural level weakens VGLL4's drug response | CREB3's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.04; direction clear | 0.087 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ouabain (Octahydrate) (drug)]] 5 µM | C | VGLL4's natural level raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | VGLL4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, -5.6); signed map (-21.3, 18.0). **Vector** length 105, 30.3% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.3 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -19.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -11.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | vestigial like family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3-p25.2 — chr3:11,556,069-11,771,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0121 |
| Gene groups (HGNC) | Vestigial like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14135](https://www.uniprot.org/uniprotkb/Q14135) (Transcription cofactor vestigial-like protein 4):

> May act as a specific coactivator for the mammalian TEFs.

**Summary**, from NCBI Gene [9686](https://www.ncbi.nlm.nih.gov/gene/9686):

> Predicted to enable transcription coactivator binding activity. Involved in negative regulation of Wnt signaling pathway; negative regulation of cell growth; and negative regulation of hippo signaling. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28966) · Entrez [9686](https://www.ncbi.nlm.nih.gov/gene/9686) · UniProt [Q14135](https://www.uniprot.org/uniprotkb/Q14135) · Ensembl [ENSG00000144560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144560)

## Data

Gene col 6894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6894); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6894]; `tensor/DDL_lfc|DDL_z.npy` [6894]; `embed/gene_vectors.npy` [6894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6894 or target_col == 6894). Every well: [[VGLL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VGLL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
