---
symbol: "PIP4P2"
type: "gene"
col: 7871
ensembl_id: "ENSG00000155099"
name: "phosphatidylinositol-4,5-bisphosphate 4-phosphatase 2"
location: "8q21.3"
module: 45
arm: "+"
pooled_cpm: 29.74
n_lines_expressing: 46
n_dd_up: 23
n_dd_down: 24
n_dd_up_clean: 20
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PIP4P2

*phosphatidylinositol-4,5-bisphosphate 4-phosphatase 2* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +13.0, q 9e-36, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.664× (z -9.9, q 2e-20, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST3GAL5]] (+0.69, fdr 1e-05), [[TMEM14A]] (+0.67, fdr 1e-05), [[FAM102B]] (+0.67, fdr 1e-05); moves opposite to [[TMEM217]] (-0.65, fdr 1e-05), [[PBLD]] (-0.63, fdr 2e-05), [[SPON1-AS1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[CDK12]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +13.0 | 9e-36 | 38/44 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +12.7 | 1e-34 | 37/44 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +11.3 | 2e-27 | 33/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +10.8 | 5e-25 | 34/44 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +10.3 | 9e-23 | 36/44 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.4 | 6e-15 | 30/43 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +7.2 | 7e-11 | 29/44 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +6.8 | 6e-10 | 30/44 (RKO, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +6.6 | 3e-09 | 31/44 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +6.5 | 6e-09 | 27/44 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 8e-06 | 25/44 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +4.6 | 2e-04 | 22/44 (PANC-1, H4, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 5 µM |  | **1.64×** | +4.4 | 5e-04 | 14/44 (C32, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 22/44 (J82, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 13/44 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.004 | 15/44 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.023 | 9/44 (SW480, RKO, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -9.9 | 2e-20 | 31/43 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.602×** | -8.0 | 4e-13 | 25/37 (RKO, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.726×** | -7.7 | 2e-12 | 31/44 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -5.8 | 1e-06 | 22/44 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.701×** | -5.4 | 6e-06 | 23/33 (SW 900, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -5.3 | 9e-06 | 19/44 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.2 | 1e-05 | 26/44 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.745×** | -5.0 | 4e-05 | 22/43 (HS-578T, SNU-423, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -5.0 | 4e-05 | 18/44 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -5.0 | 4e-05 | 15/43 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.590×** | -4.7 | 1e-04 | 18/43 (NCI-H460, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.772×** | -4.3 | 7e-04 | 15/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 7e-04 | 11/44 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.003 | 13/44 (SHP-77, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -3.9 | 0.003 | 18/44 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.778×** | -3.8 | 0.004 | 16/44 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.780×** | -3.8 | 0.004 | 15/43 (A549, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.789×** | -3.6 | 0.008 | 18/43 (C32, HS-578T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 54.3 | 7 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.72× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.0 | 6 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.44× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 3.42× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 52.5 | 6 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.12× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.43× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.26× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -12.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.01× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -11.3) |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.3) |
| [[A-427 (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 45.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[C32 (line)]] | wt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -15.8) |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -11.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 70.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.6) |
| [[J82 (line)]] | alt | 21.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.03× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.274× (z -8.9) |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -14.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL5]] | +0.69 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TMEM14A]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[FAM102B]] | +0.67 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ARHGAP12]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ORC4]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PIGH]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FRRS1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ALAD]] | +0.63 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HMGN3]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RADX]] | +0.63 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ARL6]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[KBTBD3]] | +0.61 | +0.49 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM217]] | -0.65 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PBLD]] | -0.63 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SPON1-AS1]] | -0.63 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZCWPW1]] | -0.59 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LINC01355]] | -0.59 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.58 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.58 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[CDK12]] | -0.58 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[DNAJB12]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB8]] | -0.58 | -0.61 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIP4P2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers PIP4P2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDK12]] | C | PIP4P2 activity lowers CDK12's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 2.01× higher at baseline in the lines without PIP4P2 | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |
| [[PRKD3]] | C | PIP4P2 activity raises PRKD3's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without PIP4P2 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |
| [[LIX1L]] | C | PIP4P2 activity raises LIX1L's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 4.85× lower at baseline in the lines without PIP4P2 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |
| [[MPP1]] | C | PIP4P2 activity raises MPP1's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 3.08× lower at baseline in the lines without PIP4P2 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |
| [[VPS26C]] | C | PIP4P2 activity raises VPS26C's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without PIP4P2 | 0.075 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |
| [[HCG18]] | C | PIP4P2 activity weakens HCG18's drug response | lines that do not express PIP4P2 (4) vs lines expressing it (45) | the lines without PIP4P2 respond 1.30× as strongly (z diff -1.01); strongest at Digitoxin 5 µM: 0.43x vs 0.65x (z diff -4.5) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HPS3]] | C | PIP4P2 activity strengthens HPS3's drug response | lines that do not express PIP4P2 (4) vs lines expressing it (44) | the lines without PIP4P2 respond 0.58× as strongly (z diff +2.46); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 0.43x (z diff +5.1) | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.3, 5.8); signed map (-28.3, -6.8). **Vector** length 119, 31.4% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +13.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.2 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +7.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.6 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +12.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +6.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.5 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -3.8 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4,5-bisphosphate 4-phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:90,993,802-91,040,872 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762O076; previously TMEM55A |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4L2](https://www.uniprot.org/uniprotkb/Q8N4L2) (Type 2 phosphatidylinositol 4,5-bisphosphate 4-phosphatase):

> Catalyzes the hydrolysis of phosphatidylinositol-4,5-bisphosphate (PtdIns-4,5-P2) to phosphatidylinositol-4-phosphate (PtdIns-4-P). Does not hydrolyze phosphatidylinositol 3,4,5-trisphosphate, phosphatidylinositol 3,4-bisphosphate, inositol 3,5-bisphosphate, inositol 3,4-bisphosphate, phosphatidylinositol 5-monophosphate, phosphatidylinositol 4-monophosphate and phosphatidylinositol 3-monophosphate. Negatively regulates the phagocytosis of large particles by reducing phagosomal …

**Summary**, from NCBI Gene [55529](https://www.ncbi.nlm.nih.gov/gene/55529):

> TMEM55A catalyzes the degradation of phosphatidylinositol 4,5-bisphosphate (PtdIns-4,5-P2) by removing the 4-phosphate (Ungewickell et al., 2005 [PubMed 16365287]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25452) · Entrez [55529](https://www.ncbi.nlm.nih.gov/gene/55529) · UniProt [Q8N4L2](https://www.uniprot.org/uniprotkb/Q8N4L2) · Ensembl [ENSG00000155099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155099)

## Data

Gene col 7871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7871); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7871]; `tensor/DDL_lfc|DDL_z.npy` [7871]; `embed/gene_vectors.npy` [7871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7871 or target_col == 7871). Every well: [[PIP4P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP4P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
