---
symbol: "RBCK1"
type: "gene"
col: 4669
ensembl_id: "ENSG00000125826"
name: "RANBP2-type and C3HC4-type zinc finger containing 1"
location: "20p13"
module: 63
arm: "+"
pooled_cpm: 108.29
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# RBCK1

*RANBP2-type and C3HC4-type zinc finger containing 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.41× (z +6.2, q 3e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.370× (z -17.8, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SESN2]] (+0.72, fdr 7e-06), [[TRIB3]] (+0.71, fdr 7e-06, ⚠ same locus), [[GARS1]] (+0.66, fdr 7e-06), [[CARS1]] (+0.66, fdr 7e-06); moves opposite to [[ARHGDIB]] (-0.58, fdr 3e-05), [[TFAM]] (-0.58, fdr 1e-05), [[MBNL1]] (-0.57, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HKDC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4669.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.41×** | +6.2 | 3e-07 | 35/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.43×** | +4.6 | 0.001 | 34/48 (Panc 03.27, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 0.003 | 33/48 (H4, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +4.2 | 0.003 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.013 | 28/48 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.7 | 0.024 | 26/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.024 | 24/48 (HOP62, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.024 | 30/48 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.024 | 26/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.040 | 28/49 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.040 | 25/48 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.3 | 0.040 | 22/48 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.040 | 26/48 (LOX-IMVI, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.040 | 26/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.040 | 25/48 (AsPC-1, BT-474, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.045 | 23/48 (NCI-H1792, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4669.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.370×** | -17.8 | 0e+00 | 43/47 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -9.3 | 3e-18 | 40/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.476×** | -9.1 | 3e-17 | 40/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.541×** | -7.8 | 9e-13 | 40/48 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.566×** | -7.2 | 5e-11 | 37/48 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -7.2 | 5e-11 | 41/49 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.598×** | -6.5 | 6e-09 | 32/48 (CFPAC-1, A549, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.382×** | -6.4 | 1e-08 | 39/48 (C-33 A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.604×** | -6.4 | 1e-08 | 33/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -6.4 | 1e-08 | 31/47 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -6.2 | 3e-08 | 38/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.615×** | -6.2 | 4e-08 | 31/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -5.2 | 1e-05 | 32/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -4.7 | 9e-05 | 33/48 (A-172, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.769×** | -4.7 | 1e-04 | 25/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.677×** | -4.7 | 1e-04 | 28/47 (SW1417, BT-474, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -4.2 | 9e-04 | 26/48 (HepG2/C3A, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.723×** | -4.1 | 0.001 | 31/47 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.8 | 0.004 | 25/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.587×** | -3.5 | 0.012 | 25/49 (A-172, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4669. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 200 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -20.8) |
| [[KATO III (line)]] | alt | 215 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -23.1) |
| [[A549 (line)]] | wt | 196 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -28.4) |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 9 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.309× (z -11.3) |
| [[HT-29 (line)]] | alt | 169 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -24.9) |
| [[LS 180 (line)]] | wt | 148 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.6) |
| [[SNU-423 (line)]] | alt | 263 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.4) |
| [[SW480 (line)]] | alt | 87.4 | 1 | 6 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.19× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.9) |
| [[PANC-1 (line)]] | alt | 97.9 | 1 | 5 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.80× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -12.3) |
| [[SW1417 (line)]] | alt | 86.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.8) |
| [[CFPAC-1 (line)]] | alt | 340 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.6) |
| [[A-172 (line)]] | wt | 121 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 121 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.9) |
| [[BT-474 (line)]] | alt | 77.4 | 1 | 2 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.27× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 85.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -14.2) |
| [[RKO (line)]] | wt | 65.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -16.8) |
| [[A-427 (line)]] | wt | 55.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -8.7) |
| [[A498 (line)]] | wt | 86.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -13.3) |
| [[H4 (line)]] | wt | 91.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -10.4) |
| [[HOP62 (line)]] | alt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.282× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 51.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.4) |
| [[SW48 (line)]] | wt | 79.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.9) |
| [[C-33 A (line)]] | alt | 52.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0602× (z -10.2) |
| [[COLO 205 (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -14.6) |
| [[HS-578T (line)]] | alt | 87.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -15.9) |
| [[SW 1088 (line)]] | alt | 77.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0600× (z -9.3) |
| [[SW 900 (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -11.4) |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4669), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN2]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TRIB3]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 | ⚠ same locus (9.9 kb, same strand: neighbours can correlate without regulation) |
| [[GARS1]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CARS1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[SARS1]] | +0.62 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[DDIT3]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GOT1]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[SLC25A29]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SNHG12]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[SNHG7]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[BUD31]] | +0.59 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ADM2]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGDIB]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TFAM]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MBNL1]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CDK6]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DDAH1]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ADGRG6]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[UBE2E3]] | -0.55 | -0.38 / -0.60 | both halves | 6e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RHOBTB2]] | -0.54 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GNG12]] | -0.54 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[BTBD1]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[CAV1]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PTPN14]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HKDC1]] | B | HKDC1 activity raises RBCK1's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.21× lower at baseline in the lines without HKDC1 | 0.001 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A |
| [[ESRP1]] | B | ESRP1 activity raises RBCK1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without ESRP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[CEBPG]] | C | CEBPG's natural level strengthens RBCK1's drug response | CEBPG's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.03; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, 49.3); signed map (-12.3, 25.7). **Vector** length 137, 50.3% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.53 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.50 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +8.2 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.4 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.4 | +4.6 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +5.6 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.2 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +4.8 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -7.1 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.8 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.9 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.8 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -5.3 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -6.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -4.7 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -3.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RANBP2-type and C3HC4-type zinc finger containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:407,498-432,139 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RBCK2, XAP4, RNF54, ZRANB4, UBCE7IP3, HOIL1; previously C20orf18 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers RANBP2-type; Linear ubiquitin chain assembly complex; RBR E3 ubiquitin ligases |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, GLYCOLYSIS |
| Reactome | 8 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYM8](https://www.uniprot.org/uniprotkb/Q9BYM8) (RanBP-type and C3HC4-type zinc finger-containing protein 1):

> Atypical E3 ubiquitin ligase that catalyzes ubiquitination of both proteins and carbohydrates, and which is involved in various processes, such as glycophagy, NF-kappa-B activation and regulation of inflammation. Acts as a E3 ubiquitin-protein ligase, which accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes, and then transfers it to lysine residues of protein substrates. Also able to catalyze O-linked ubiquitination of serine and threonine residues on target proteins, instead of …

**Summary**, from NCBI Gene [10616](https://www.ncbi.nlm.nih.gov/gene/10616):

> Enables several functions, including identical protein binding activity; transcription coactivator activity; and ubiquitin binding activity. Involved in several processes, including T cell receptor signaling pathway; positive regulation of canonical NF-kappaB signal transduction; and protein linear polyubiquitination. Part of LUBAC complex. Implicated in glycogen storage disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15864) · Entrez [10616](https://www.ncbi.nlm.nih.gov/gene/10616) · UniProt [Q9BYM8](https://www.uniprot.org/uniprotkb/Q9BYM8) · Ensembl [ENSG00000125826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125826)

## Data

Gene col 4669: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4669); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4669, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4669]; `tensor/DDL_lfc|DDL_z.npy` [4669]; `embed/gene_vectors.npy` [4669]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4669 or target_col == 4669). Every well: [[RBCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
