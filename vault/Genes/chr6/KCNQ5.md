---
symbol: "KCNQ5"
type: "gene"
col: 11728
ensembl_id: "ENSG00000185760"
name: "potassium voltage-gated channel subfamily Q member 5"
location: "6q13"
module: 110
arm: "+"
pooled_cpm: 130.74
n_lines_expressing: 25
n_dd_up: 24
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# KCNQ5

*potassium voltage-gated channel subfamily Q member 5* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +11.5, q 1e-27, up in 3 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +10.1, q 2e-21, up in 4 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.670× (z -9.4, q 3e-18, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBX2-AS1]] (+0.62, fdr 7e-06), [[ZNF804A]] (+0.60, fdr 1e-05), [[MARCHF4]] (+0.60, fdr 7e-06); moves opposite to [[BAZ2A]] (-0.49, fdr 4e-05), [[SENP2]] (-0.49, fdr 3e-05), [[ZFYVE1]] (-0.48, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SACS]] → it (grade B ⚠); 2 go from it, the strongest it → [[TERT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +11.5 | 1e-27 | 3/24 (BT-474, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.1 | 2e-21 | 4/24 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +9.6 | 1e-19 | 5/21 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +8.4 | 6e-15 | 20/23 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.7 | 2e-12 | 12/22 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +7.5 | 9e-12 | 7/21 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.1 | 1e-10 | 2/25 (hTERT-HPNE, BT-474) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.5 | 2e-06 | 8/23 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 7/23 (BT-474, NCI-H23, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.002 | 12/23 (C32, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 9/24 (BT-474, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 10/23 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.007 | 0/24 | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.7 | 0.007 | 10/20 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.010 | 9/23 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.012 | 9/21 (HS-578T, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.018 | 8/22 (HS-578T, BT-474, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.020 | 9/23 (BT-474, HS-578T, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.021 | 9/23 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.049 | 10/23 (BT-474, HS-578T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.050 | 2/24 (SK-MEL-2, LOX-IMVI) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.051 | 6/24 (C32, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.670×** | -9.4 | 3e-18 | 21/23 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -9.0 | 5e-17 | 16/23 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -8.7 | 6e-16 | 18/23 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.615×** | -8.3 | 2e-14 | 15/23 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.680×** | -6.3 | 3e-08 | 16/23 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.747×** | -4.9 | 1e-04 | 13/25 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.813×** | -4.8 | 1e-04 | 5/23 (NCI-H460, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.763×** | -4.6 | 3e-04 | 12/24 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.800×** | -4.4 | 6e-04 | 12/23 (SK-MEL-2, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.808×** | -4.3 | 0.001 | 9/23 (NCI-H23, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.798×** | -3.8 | 0.006 | 8/22 (NCI-H2030, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.797×** | -3.6 | 0.017 | 4/23 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.839× | -3.4 | 0.033 | 11/24 (SK-MEL-2, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.820×** | -3.2 | 0.047 | 9/22 (NCI-H2030, H4, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.051 | 13/24 (A-172, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.873× | -3.2 | 0.051 | 0/23 | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.054 | 5/25 (SK-MEL-2, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 588 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -30.6) |
| [[A-427 (line)]] | wt | 356 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 424 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.8) |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -26.4) |
| [[A-172 (line)]] | wt | 601 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 296 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0802× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.7) |
| [[SHP-77 (line)]] | alt | 221 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 293 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -28.5) |
| [[C32 (line)]] | wt | 172 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.94× (z +9.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.2) |
| [[CHP-212 (line)]] | wt | 168 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.2) |
| [[HS-578T (line)]] | alt | 120 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.21× (z +9.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.2) |
| [[H4 (line)]] | wt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 70.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.04× (z +9.2) ⚠ unreliable plate only | — |
| [[SW 900 (line)]] | alt | 264 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.1) |
| [[A498 (line)]] | wt | 7.72 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 28.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.68 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 31.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBX2-AS1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZNF804A]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[HHIP]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CTPS1]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NTNG1]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CARD18]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[STK32B]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RGS4]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[HS6ST2]] | +0.55 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[GALNT14]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[MMP16]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2A]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SENP2]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ZFYVE1]] | -0.48 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RIOK3]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[HOOK2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[CCS]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[OPTN]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[OGA]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[LINC00674]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[FOXO4]] | -0.45 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MVP]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises KCNQ5's level | lines that do not express SACS (5) vs lines expressing it (45) | 3.31× lower at baseline in the lines without SACS | 0.034 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity weakens KCNQ5's drug response | lines that do not express KLHL14 (16) vs lines expressing it (8) | the lines without KLHL14 respond 1.97× as strongly (z diff -1.44); strongest at Dinaciclib 5 µM: 1.05x vs 0.45x (z diff -6.3) | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; both ways; artifact flags |
| [[MMP16]] | C | MMP16 activity raises KCNQ5's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 7.15× lower at baseline in the lines without MMP16 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |
| [[GABBR2]] | C | GABBR2 activity raises KCNQ5's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 4.02× lower at baseline in the lines without GABBR2 | 0.056 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent; co-absent with the target |
| [[MPDZ]] | C | MPDZ activity raises KCNQ5's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 7.67× lower at baseline in the lines without MPDZ | 0.068 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[ELOVL2]] | C | ELOVL2 activity raises KCNQ5's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 4.58× lower at baseline in the lines without ELOVL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046; co-absent with the target |
| [[ZNF804A]] | C | ZNF804A activity raises KCNQ5's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 5.41× lower at baseline in the lines without ZNF804A | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | KCNQ5 activity raises TERT's level | lines that do not express KCNQ5 (25) vs lines expressing it (25) | 1.45× lower at baseline in the lines without KCNQ5 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, PRR16, FAP |
| [[MMP16]] | C | KCNQ5 activity raises MMP16's level | lines that do not express KCNQ5 (25) vs lines expressing it (25) | 7.71× lower at baseline in the lines without KCNQ5 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, PRR16, FAP; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 22.4); signed map (18.2, 45.1). **Vector** length 94.9, 29.9% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +4.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.6 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily Q member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:72,621,792-73,198,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv7.5 |
| Gene groups (HGNC) | Potassium voltage-gated channels |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR82](https://www.uniprot.org/uniprotkb/Q9NR82) (Potassium voltage-gated channel subfamily KQT member 5):

> Pore-forming subunit of the voltage-gated potassium (Kv) channel broadly expressed in brain and involved in the regulation of neuronal excitability. Associates with KCNQ3/Kv7.3 pore-forming subunit to form a potassium channel which contributes to M-type current, a slowly activating and deactivating potassium conductance which plays a critical role in determining the subthreshold electrical excitability of neurons. Contributes, with other potassium channels, to the molecular diversity of a …

**Summary**, from NCBI Gene [56479](https://www.ncbi.nlm.nih.gov/gene/56479):

> This gene is a member of the KCNQ potassium channel gene family that is differentially expressed in subregions of the brain and in skeletal muscle. The protein encoded by this gene yields currents that activate slowly with depolarization and can form heteromeric channels with the protein encoded by the KCNQ3 gene. Currents expressed from this protein have voltage dependences and inhibitor sensitivities in common with M-currents. They are also inhibited by M1 muscarinic receptor activation. …

**Accessions** — [HGNC:6299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6299) · Entrez [56479](https://www.ncbi.nlm.nih.gov/gene/56479) · UniProt [Q9NR82](https://www.uniprot.org/uniprotkb/Q9NR82) · Ensembl [ENSG00000185760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185760)

## Data

Gene col 11728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11728); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11728]; `tensor/DDL_lfc|DDL_z.npy` [11728]; `embed/gene_vectors.npy` [11728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11728 or target_col == 11728). Every well: [[KCNQ5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
