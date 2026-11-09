---
symbol: "RIC1"
type: "gene"
col: 2822
ensembl_id: "ENSG00000107036"
name: "RIC1 partner of RAB6A GEF complex"
location: "9p24.1"
module: 48
arm: "+"
pooled_cpm: 118.77
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# RIC1

*RIC1 partner of RAB6A GEF complex* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.33× (z +5.2, q 6e-05, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.302× (z -21.4, q 0e+00, down in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.600× (z -9.1, q 1e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA1]] (+0.61, fdr 1e-05), [[C4orf3]] (+0.60, fdr 4e-05), [[TRAPPC1]] (+0.59, fdr 1e-05); moves opposite to [[CCT6P3]] (-0.59, fdr 1e-05), [[ARMCX4]] (-0.55, fdr 3e-05), [[FBXO30]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.2 | 6e-05 | 31/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.2 | 6e-05 | 26/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +4.7 | 4e-04 | 31/49 (A549, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +4.7 | 4e-04 | 29/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.016 | 24/48 (A-172, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.016 | 27/49 (J82, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.016 | 23/48 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.017 | 22/48 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.6 | 0.017 | 24/49 (J82, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.032 | 23/48 (J82, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.097 | 22/48 (RKO, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.302×** | -21.4 | 0e+00 | 42/43 (KATO III, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.334×** | -20.3 | 0e+00 | 45/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.377×** | -16.7 | 0e+00 | 40/45 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -9.1 | 1e-17 | 37/48 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -7.9 | 2e-13 | 34/48 (HCT15, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.656×** | -7.5 | 5e-12 | 39/47 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -5.9 | 2e-07 | 37/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.732×** | -5.8 | 5e-07 | 33/47 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -5.2 | 2e-05 | 30/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -5.0 | 3e-05 | 32/48 (HOP62, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.835× | -4.7 | 1e-04 | 24/49 (NCI-H1792, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.788×** | -4.3 | 0.001 | 24/48 (LoVo, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.813×** | -3.8 | 0.005 | 24/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.822×** | -3.5 | 0.019 | 24/47 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.093 | 16/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 161 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.291× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 225 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -14.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 242 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.410× (z -10.2) |
| [[A549 (line)]] | wt | 146 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.349× (z -11.1) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.257× (z -10.2) |
| [[H4 (line)]] | wt | 173 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -8.6) |
| [[HOP62 (line)]] | alt | 198 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.395× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 130 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.288× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 157 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -11.5) |
| [[SW 900 (line)]] | alt | 185 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -17.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 118 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -10.1) |
| [[HCT15 (line)]] | alt | 262 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.312× (z -11.2) |
| [[HT-29 (line)]] | alt | 103 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.302× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 156 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 208 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0558× (z -31.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 91.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -15.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 81.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -14.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -16.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -32.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -16.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 199 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -15.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 114 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -14.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -9.0) |
| [[SNU-1 (line)]] | wt | 124 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.112× (z -20.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 87.5 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -12.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 64.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 97.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.1) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.359× (z -9.1) |
| [[PANC-1 (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0681× (z -23.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -16.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -14.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 60.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.428× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -15.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.127× (z -9.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.60 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[TRAPPC1]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[NDUFA2]] | +0.57 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TXNDC17]] | +0.56 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[CHPF]] | +0.55 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[PAG1]] | +0.55 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[B3GAT3]] | +0.55 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[SPTSSA]] | +0.55 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[UBL5]] | +0.55 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[VKORC1]] | +0.55 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[ANAPC11]] | +0.55 | +0.59 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6P3]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FBXO30]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[EIF5]] | -0.54 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[ZXDA]] | -0.53 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GABPB2]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ZCWPW1]] | -0.52 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[TSR2]] | -0.52 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[PSMD11]] | -0.51 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.51 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[CCNT2]] | -0.51 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[NEPRO-AS1]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises RIC1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without PLOD2 | 0.077 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RIC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RIC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ELF4]] | C | ELF4 activity raises RIC1's level | lines that do not express ELF4 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without ELF4 | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-13.5, 3.3); signed map (-37.7, 18.2). **Vector** length 90.9, 25.5% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | -0.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -16.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | RIC1 partner of RAB6A GEF complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:5,629,025-5,776,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA207C16.1; previously KIAA1432 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 7 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4ADV7](https://www.uniprot.org/uniprotkb/Q4ADV7) (Guanine nucleotide exchange factor subunit RIC1):

> The RIC1-RGP1 complex acts as a guanine nucleotide exchange factor (GEF), which activates RAB6A by exchanging bound GDP for free GTP, and may thereby be required for efficient fusion of endosome-derived vesicles with the Golgi compartment. The RIC1-RGP1 complex participates in the recycling of mannose-6-phosphate receptors. Required for phosphorylation and localization of GJA1. Is a regulator of procollagen transport and secretion, and is required for correct cartilage morphogenesis and …

**Summary**, from NCBI Gene [57589](https://www.ncbi.nlm.nih.gov/gene/57589):

> Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in several processes, including positive regulation of GTPase activity; regulation of extracellular matrix constituent secretion; and retrograde transport, endosome to Golgi. Located in cytosol and membrane. Part of Ric1-Rgp1 guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17686) · Entrez [57589](https://www.ncbi.nlm.nih.gov/gene/57589) · UniProt [Q4ADV7](https://www.uniprot.org/uniprotkb/Q4ADV7) · Ensembl [ENSG00000107036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107036)

## Data

Gene col 2822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2822); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2822]; `tensor/DDL_lfc|DDL_z.npy` [2822]; `embed/gene_vectors.npy` [2822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2822 or target_col == 2822). Every well: [[RIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
