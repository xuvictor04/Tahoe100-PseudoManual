---
symbol: "ZRANB3"
type: "gene"
col: 4312
ensembl_id: "ENSG00000121988"
name: "zinc finger RANBP2-type containing 3"
location: "2q21.3"
module: 71
arm: "+"
pooled_cpm: 68.32
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# ZRANB3

*zinc finger RANBP2-type containing 3* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.2, q 1e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.603× (z -7.5, q 5e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF876P]] (+0.75, fdr 7e-06), [[GEN1]] (+0.69, fdr 7e-06), [[HCCS-DT]] (+0.69, fdr 7e-06); moves opposite to [[CAPN5]] (-0.59, fdr 2e-05), [[YPEL2]] (-0.57, fdr 1e-05), [[DOK4]] (-0.56, fdr 2e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.2 | 1e-21 | 38/48 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +6.6 | 1e-08 | 36/48 (SW480, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.4 | 1e-05 | 31/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +5.2 | 3e-05 | 28/48 (HT-29, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.004 | 27/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.005 | 26/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.012 | 17/48 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.012 | 21/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.6 | 0.019 | 15/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.019 | 18/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.026 | 20/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.043 | 20/48 (RKO, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.051 | 20/48 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.052 | 14/49 (LS 180, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.25×** | +3.2 | 0.061 | 20/43 (SHP-77, AsPC-1, …) | rises with dose | composition shift |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.062 | 15/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.063 | 12/48 (HEC-1-A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -7.5 | 5e-11 | 35/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.714×** | -7.0 | 5e-10 | 31/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.637×** | -6.4 | 3e-08 | 31/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -6.0 | 3e-07 | 32/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -5.5 | 6e-06 | 28/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -5.3 | 1e-05 | 24/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -5.1 | 3e-05 | 28/48 (HCT15, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -5.0 | 4e-05 | 25/48 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -5.0 | 4e-05 | 31/48 (SNU-1, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -4.7 | 2e-04 | 28/49 (PANC-1, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.738×** | -4.5 | 3e-04 | 31/48 (AN3 CA, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.753×** | -4.2 | 0.001 | 23/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.005 | 18/48 (KATO III, LoVo, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.629×** | -3.6 | 0.013 | 20/48 (HEC-1-A, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.013 | 22/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.809×** | -3.0 | 0.081 | 10/48 (A-172, AsPC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 76.6 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -10.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -10.3) |
| [[PANC-1 (line)]] | alt | 106 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -14.4) |
| [[SW480 (line)]] | alt | 115 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.405× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 92.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 72.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 68.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 71.9 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -10.2) |
| [[SHP-77 (line)]] | alt | 57.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.16× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 84.4 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0443× (z -11.1) |
| [[SW 900 (line)]] | alt | 79.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -10.9) ⚠ toxic |
| [[A498 (line)]] | wt | 79.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 120 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.468× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 78.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 45.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[LoVo (line)]] | wt | 53.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H2347 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.403× (z -8.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 38.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 43.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.8) | — |
| [[A-427 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF876P]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GEN1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[HCCS-DT]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[VRK1]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[HELLPAR]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ALG8]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[XRCC2]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ZNF718]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[KNTC1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[FANCC]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CENPO]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[NSD2]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN5]] | -0.59 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[YPEL2]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[DOK4]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CNKSR1]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PIGH]] | -0.54 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[UBE2B]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[VPS37D]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ALAD]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity lowers ZRANB3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.47× higher at baseline in the lines without IRF6 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TOP2A]] | B | TOP2A activity lowers ZRANB3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CENPP]] | C | CENPP activity raises ZRANB3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.67× lower at baseline in the lines without CENPP | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[BMF]] | C | BMF activity lowers ZRANB3's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.08× higher at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |
| [[NAT1]] | C | NAT1 activity lowers ZRANB3's level | lines that do not express NAT1 (3) vs lines expressing it (47) | 2.08× higher at baseline in the lines without NAT1 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IKBKE, RASSF5, FUCA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.3, -44.3); signed map (-41.9, -49.4). **Vector** length 118, 38.0% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.0 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.2 | +5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +0.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.6 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.9 | -7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.8 | -4.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger RANBP2-type containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,136,916-135,531,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B1727, AH2 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; SNF2 related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5FWF4](https://www.uniprot.org/uniprotkb/Q5FWF4) (DNA annealing helicase and endonuclease ZRANB3):

> DNA annealing helicase and endonuclease required to maintain genome stability at stalled or collapsed replication forks by facilitating fork restart and limiting inappropriate recombination that could occur during template switching events. Recruited to the sites of stalled DNA replication by polyubiquitinated PCNA and acts as a structure-specific endonuclease that cleaves the replication fork D-loop intermediate, generating an accessible 3'-OH group in the template of the leading strand, which …

**Summary**, from NCBI Gene [84083](https://www.ncbi.nlm.nih.gov/gene/84083):

> Enables ATP-dependent DNA/DNA annealing activity; DNA endonuclease activity; and K63-linked polyubiquitin modification-dependent protein binding activity. Involved in DNA repair; replication fork reversal; and response to UV. Located in nuclear replication fork and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25249) · Entrez [84083](https://www.ncbi.nlm.nih.gov/gene/84083) · UniProt [Q5FWF4](https://www.uniprot.org/uniprotkb/Q5FWF4) · Ensembl [ENSG00000121988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121988)

## Data

Gene col 4312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4312); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4312]; `tensor/DDL_lfc|DDL_z.npy` [4312]; `embed/gene_vectors.npy` [4312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4312 or target_col == 4312). Every well: [[ZRANB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRANB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
