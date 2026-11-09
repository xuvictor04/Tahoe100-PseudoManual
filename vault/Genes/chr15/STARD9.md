---
symbol: "STARD9"
type: "gene"
col: 8255
ensembl_id: "ENSG00000159433"
name: "StAR related lipid transfer domain containing 9"
location: "15q15.2"
module: 30
arm: "+"
pooled_cpm: 42.14
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 36
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# STARD9

*StAR related lipid transfer domain containing 9* — 15q15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.58× (z +7.2, q 5e-10, up in 27 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -14.6, q 3e-45, down in 28 of 40 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.496× (z -11.1, q 2e-26, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C14orf132]] (+0.66, fdr 8e-06), [[GALNT11]] (+0.62, fdr 1e-05), [[FBXL2]] (+0.62, fdr 1e-05); moves opposite to [[MCTS1]] (-0.54, fdr 8e-05), [[AMIGO2]] (-0.52, fdr 5e-05), [[LEKR1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[THRB]] → it (grade B ⚠); 36 go from it, the strongest it → [[HACE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +7.2 | 5e-10 | 27/40 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.3 | 7e-08 | 22/40 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 1e-03 | 23/40 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.002 | 19/40 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +4.2 | 0.003 | 21/40 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.005 | 20/40 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +3.9 | 0.006 | 16/40 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +3.9 | 0.006 | 18/39 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.006 | 17/40 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.7 | 0.010 | 16/40 (NCI-H2030, SW1417, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.026 | 12/40 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.044 | 15/39 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.3 | 0.046 | 10/40 (RPMI-7951, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.077 | 10/40 (A-172, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.523×** | -14.6 | 3e-45 | 28/40 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.426×** | -13.0 | 3e-36 | 35/40 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -11.1 | 2e-26 | 33/40 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.514×** | -10.5 | 7e-24 | 34/39 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.553×** | -9.0 | 2e-17 | 25/34 (Hs 766T, A-427, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -8.7 | 3e-16 | 33/40 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.597×** | -7.6 | 3e-12 | 26/38 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -7.3 | 2e-11 | 27/40 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.672×** | -6.3 | 2e-08 | 25/40 (LOX-IMVI, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.665×** | -6.2 | 3e-08 | 27/39 (SNU-1, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -6.0 | 1e-07 | 24/40 (HEC-1-A, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -5.2 | 1e-05 | 26/40 (HEC-1-A, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -4.4 | 4e-04 | 17/40 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.761×** | -4.0 | 0.002 | 21/39 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -4.0 | 0.002 | 17/40 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.774×** | -3.9 | 0.004 | 20/40 (AN3 CA, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.005 | 17/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.038 | 11/39 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.043 | 11/40 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.0 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0886× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.254× (z -12.3) |
| [[PANC-1 (line)]] | alt | 71.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 69.9 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.4) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.8) |
| [[A-427 (line)]] | wt | 45.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -8.7) |
| [[SW1417 (line)]] | alt | 23.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.27× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 35.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.260× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 35.9 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.227× (z -13.0) |
| [[Hs 766T (line)]] | wt | 69.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0411× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 29.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 55.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -16.1) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.138× (z -11.6) |
| [[H4 (line)]] | wt | 52.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -8.7) |
| [[J82 (line)]] | alt | 84.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.285× (z -11.7) |
| [[C-33 A (line)]] | alt | 99.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 50.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 76.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.235× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.209× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 15.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 39.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -15.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW480 (line)]] | alt | 35.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.420× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 45.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C14orf132]] | +0.66 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[GALNT11]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FBXL2]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[CLTCL1]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD36]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[STX2]] | +0.58 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[CD81]] | +0.57 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ANKRD36B]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[STK32C]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[KATNAL1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.54 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[AMIGO2]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[LEKR1]] | -0.52 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[STYXL1]] | -0.51 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[ALOX12P2-1]] | -0.49 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[WDR5B]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[LPXN]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ERCC4]] | -0.48 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[KLHL2P1]] | -0.48 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[ANAPC13]] | -0.47 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[POU5F1B]] | -0.47 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[PDCL3P4]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THRB]] | B | THRB activity lowers STARD9's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.19× higher at baseline in the lines without THRB | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[ANK3]] | B | ANK3 activity lowers STARD9's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.04× higher at baseline in the lines without ANK3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[SNTA1]] | B | SNTA1 activity raises STARD9's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 4.16× lower at baseline in the lines without SNTA1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity raises STARD9's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.38× lower at baseline in the lines without RNF220 | 0.047 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity lowers STARD9's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 1.78× higher at baseline in the lines without POU5F1B | 0.078 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[RECK]] | C | RECK activity raises STARD9's level | lines that do not express RECK (12) vs lines expressing it (38) | 3.24× lower at baseline in the lines without RECK | 0.004 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9; co-absent with the target |
| [[KATNAL1]] | C | KATNAL1 activity raises STARD9's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 4.33× lower at baseline in the lines without KATNAL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17; co-absent with the target |
| [[CLTCL1]] | C | CLTCL1 activity raises STARD9's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 5.56× lower at baseline in the lines without CLTCL1 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[HACE1]] | C | HACE1 activity raises STARD9's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 4.67× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 34, C 2. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | B | STARD9 activity raises HACE1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.98× lower at baseline in the lines without STARD9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[MMAA]] | B | STARD9 activity lowers MMAA's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.81× higher at baseline in the lines without STARD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[STX2]] | B | STARD9 activity raises STX2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 3.37× lower at baseline in the lines without STARD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[CYTH3]] | B | STARD9 activity raises CYTH3's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without STARD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SNTA1]] | B | STARD9 activity raises SNTA1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without STARD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[SCAI]] | B | STARD9 activity raises SCAI's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without STARD9 | 0.008 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[KLHL2P1]] | B | STARD9 activity lowers KLHL2P1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.99× higher at baseline in the lines without STARD9 | 0.009 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[PKN1]] | B | STARD9 activity raises PKN1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without STARD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[MAST2]] | B | STARD9 activity raises MAST2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without STARD9 | 0.010 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[CLTCL1]] | B | STARD9 activity raises CLTCL1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without STARD9 | 0.020 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[NTAN1]] | B | STARD9 activity raises NTAN1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without STARD9 | 0.022 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[OGG1]] | B | STARD9 activity raises OGG1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without STARD9 | 0.025 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.3, -1.9); signed map (-38.0, -2.7). **Vector** length 93.4, 23.8% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +6.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.3 | -14.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.3 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | StAR related lipid transfer domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.2 — chr15:42,575,606-42,720,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1300, KIF16A |
| Gene groups (HGNC) | Kinesins; StAR related lipid transfer domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2P6](https://www.uniprot.org/uniprotkb/Q9P2P6) (StAR-related lipid transfer protein 9):

> Microtubule-dependent motor protein required for spindle pole assembly during mitosis. Required to stabilize the pericentriolar material (PCM).

**Summary**, from NCBI Gene [57519](https://www.ncbi.nlm.nih.gov/gene/57519):

> Enables microtubule binding activity and microtubule motor activity. Involved in spindle assembly. Located in centriole; cytoplasm; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19162) · Entrez [57519](https://www.ncbi.nlm.nih.gov/gene/57519) · UniProt [Q9P2P6](https://www.uniprot.org/uniprotkb/Q9P2P6) · Ensembl [ENSG00000159433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159433)

## Data

Gene col 8255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8255); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8255]; `tensor/DDL_lfc|DDL_z.npy` [8255]; `embed/gene_vectors.npy` [8255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8255 or target_col == 8255). Every well: [[STARD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
