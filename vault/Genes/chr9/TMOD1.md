---
symbol: "TMOD1"
type: "gene"
col: 5916
ensembl_id: "ENSG00000136842"
name: "tropomodulin 1"
location: "9q22.33"
module: 208
arm: "+"
pooled_cpm: 17.72
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 48
n_dd_up_clean: 20
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# TMOD1

*tropomodulin 1* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.81× (z +15.5, q 0e+00, up in 23 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.604× (z -10.7, q 9e-24, down in 21 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTAC1]] (+0.64, fdr 7e-06), [[VSTM4]] (+0.63, fdr 9e-06), [[RGS9]] (+0.61, fdr 1e-05); moves opposite to [[SLC26A2]] (-0.57, fdr 4e-05), [[GABPB1-AS1]] (-0.56, fdr 3e-05), [[YAP1]] (-0.56, fdr 3e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ABI3BP]] → it (grade B ⚠); 2 go from it, the strongest it → [[IQCH-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.81×** | +15.5 | 0e+00 | 23/33 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +14.9 | 0e+00 | 22/34 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.57×** | +14.2 | 2e-43 | 23/33 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +12.7 | 7e-35 | 19/33 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.24×** | +12.1 | 1e-31 | 22/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.12×** | +9.0 | 2e-17 | 23/32 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.77×** | +8.6 | 8e-16 | 22/32 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +8.5 | 2e-15 | 19/32 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.06×** | +5.0 | 3e-05 | 11/34 (Hs 766T, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.9 | 6e-05 | 9/34 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +4.4 | 6e-04 | 13/33 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.81×** | +4.2 | 0.002 | 13/34 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.79×** | +4.1 | 0.002 | 12/34 (H4, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +3.9 | 0.003 | 13/34 (RPMI-7951, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.004 | 4/32 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.008 | 8/33 (SW480, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.011 | 5/32 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.604×** | -10.7 | 9e-24 | 21/34 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.538×** | -9.3 | 6e-18 | 22/33 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -9.2 | 9e-18 | 20/32 (HS-578T, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.571×** | -8.4 | 8e-15 | 19/33 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.584×** | -8.0 | 1e-13 | 22/29 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -7.9 | 4e-13 | 24/33 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -7.1 | 1e-10 | 15/31 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -6.3 | 2e-08 | 18/32 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.3 | 2e-08 | 21/33 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.659×** | -6.2 | 3e-08 | 18/32 (A-172, NCI-H460, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -5.9 | 2e-07 | 22/33 (NCI-H1792, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.686×** | -5.6 | 9e-07 | 17/33 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.766×** | -5.6 | 9e-07 | 14/33 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.693×** | -5.5 | 2e-06 | 16/33 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.699×** | -5.3 | 3e-06 | 12/32 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.720×** | -4.9 | 4e-05 | 15/32 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.673×** | -4.7 | 8e-05 | 12/32 (SNU-423, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.741×** | -4.5 | 2e-04 | 16/33 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.742×** | -4.4 | 2e-04 | 14/33 (NCI-H1792, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 123 | 0 | 20 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -20.5) |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0827× (z -29.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -21.1) |
| [[HS-578T (line)]] | alt | 60.3 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0776× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 34.8 | 2 | 4 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.65× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -21.8) |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.339× (z -8.8) |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -9.7) |
| [[SHP-77 (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.49× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0259× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 1 | — | [[Allopurinol (drug)]] 0.5 µM 0.0490× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -15.9) |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.246× (z -9.7) |
| [[SW480 (line)]] | alt | 5.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.43× (z +9.0) | — |
| [[A-427 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTAC1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[VSTM4]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RGS9]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ARID5A]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GIPR]] | +0.60 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[LINC01411]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TTLL7]] | +0.59 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ZNF385A]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PGM2L1]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[F11R]] | +0.59 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[SIRLNT]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CYP26B1]] | +0.58 | +0.43 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A2]] | -0.57 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[GABPB1-AS1]] | -0.56 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[YAP1]] | -0.56 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ITPKB]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[LINC00886]] | -0.55 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LINC01145-1]] | -0.54 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[TBC1D5]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LINC01551]] | -0.53 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[PTPRG]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SLC12A2-DT]] | -0.51 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ECHDC1]] | -0.51 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABI3BP]] | B | ABI3BP activity raises TMOD1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.10× lower at baseline in the lines without ABI3BP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[IGFN1]] | B | IGFN1 activity raises TMOD1's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.96× lower at baseline in the lines without IGFN1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[CACNA2D3]] | B | CACNA2D3 activity raises TMOD1's level | lines that do not express CACNA2D3 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without CACNA2D3 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NCAM1, LINC01287, LINC00824 |
| [[SEMA6A]] | B | SEMA6A activity lowers TMOD1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 1.78× higher at baseline in the lines without SEMA6A | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |
| [[MAF]] | B | MAF activity raises TMOD1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without MAF | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[SIRLNT]] | B | SIRLNT activity raises TMOD1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without SIRLNT | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQCH-AS1]] | B | TMOD1 activity strengthens IQCH-AS1's drug response | lines that do not express TMOD1 (14) vs lines expressing it (34) | the lines without TMOD1 respond 0.87× as strongly (z diff +0.37); strongest at Homoharringtonine 5 µM: 1.41x vs 2.33x (z diff +2.6) | 0.012 | ⚠ within organs, on part of the lines; also absent: TGFB1I1, ABLIM3, ENSG00000285744; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ZNF385A]] | B | TMOD1 activity raises ZNF385A's level | lines that do not express TMOD1 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without TMOD1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TGFB1I1, ABLIM3, ENSG00000285744; maybe low, not absent |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.8, -1.8); signed map (-19.5, 27.2). **Vector** length 100, 24.9% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +14.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.9 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +15.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.7 | -10.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.4 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | tropomodulin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,501,180-97,601,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ETMOD; previously D9S57E, TMOD |
| Gene groups (HGNC) | Tropomodulins |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P28289](https://www.uniprot.org/uniprotkb/P28289) (Tropomodulin-1):

> Blocks the elongation and depolymerization of the actin filaments at the pointed end. The Tmod/TM complex contributes to the formation of the short actin protofilament, which in turn defines the geometry of the membrane skeleton. May play an important role in regulating the organization of actin filaments by preferentially binding to a specific tropomyosin isoform at its N-terminus.

**Summary**, from NCBI Gene [7111](https://www.ncbi.nlm.nih.gov/gene/7111):

> This gene encodes a member of the tropomodulin family. The encoded protein is an actin-capping protein that regulates tropomyosin by binding to its N-terminus, inhibiting depolymerization and elongation of the pointed end of actin filaments and thereby influencing the structure of the erythrocyte membrane skeleton. Multiple transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:11871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11871) · Entrez [7111](https://www.ncbi.nlm.nih.gov/gene/7111) · UniProt [P28289](https://www.uniprot.org/uniprotkb/P28289) · Ensembl [ENSG00000136842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136842)

## Data

Gene col 5916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5916); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5916]; `tensor/DDL_lfc|DDL_z.npy` [5916]; `embed/gene_vectors.npy` [5916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5916 or target_col == 5916). Every well: [[TMOD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMOD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
