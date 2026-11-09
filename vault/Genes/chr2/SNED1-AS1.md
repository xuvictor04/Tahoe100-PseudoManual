---
symbol: "SNED1-AS1"
type: "gene"
col: 13464
ensembl_id: "ENSG00000225521"
name: "SNED1 antisense RNA 1"
location: "2q37.3"
module: 37
arm: "+"
pooled_cpm: 6.58
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 24
n_dd_up_clean: 19
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SNED1-AS1

*SNED1 antisense RNA 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +5.8, q 2e-06, up in 18 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.405× (z -10.4, q 1e-22, down in 27 of 44 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.471× (z -9.0, q 6e-17, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYPK]] (+0.64, fdr 1e-05), [[TMEM269]] (+0.62, fdr 7e-06), [[ADAM20P1]] (+0.60, fdr 1e-05); moves opposite to [[CDYL]] (-0.48, fdr 4e-05), [[ARL14]] (-0.46, fdr 9e-05), [[TTPAL]] (-0.45, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.8 | 2e-06 | 18/42 (SHP-77, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.7 | 2e-06 | 16/39 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.48×** | +5.7 | 2e-06 | 15/44 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +5.6 | 3e-06 | 20/45 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 2e-05 | 13/43 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.004 | 11/43 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.004 | 5/40 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.005 | 10/45 (NCI-H1573, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.008 | 9/40 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.009 | 9/40 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Quinestrol (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.018 | 4/45 (NCI-H1573, A-427, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.023 | 10/45 (NCI-H23, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.025 | 5/45 (SW480, COLO 205, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.3 | 0.033 | 5/46 (BT-474, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +3.3 | 0.033 | 5/40 (BT-474, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.034 | 5/40 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.036 | 5/44 (BT-474, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.405×** | -10.4 | 1e-22 | 27/44 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.471×** | -9.0 | 6e-17 | 28/44 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.492×** | -8.5 | 4e-15 | 24/41 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -6.7 | 4e-09 | 23/43 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -6.5 | 1e-08 | 22/42 (SW480, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.595×** | -6.2 | 5e-08 | 19/45 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.584×** | -6.2 | 5e-08 | 16/34 (A498, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -5.6 | 1e-06 | 19/44 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.647×** | -5.2 | 1e-05 | 20/42 (A549, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.674×** | -4.7 | 1e-04 | 15/39 (SW480, CFPAC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.761×** | -4.6 | 2e-04 | 18/45 (PANC-1, hTERT-HPNE, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.681×** | -4.6 | 2e-04 | 10/45 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -4.5 | 2e-04 | 16/41 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.736×** | -3.7 | 0.010 | 15/38 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.753×** | -3.4 | 0.027 | 9/43 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.821×** | -3.3 | 0.031 | 5/46 (SW48, COLO 205, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.589×** | -3.3 | 0.031 | 8/36 (HEC-1-A, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.041 | 6/46 (CFPAC-1, NCI-H661, …) | top dose only |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.768×** | -3.1 | 0.046 | 11/41 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.053 | 12/42 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.053 | 11/44 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.616×** | -3.0 | 0.060 | 10/30 (NCI-H1792, SW48, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.2 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0829× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 14.0 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0339× (z -11.2) |
| [[SW48 (line)]] | wt | 11.2 | 0 | 3 (1 ⚠) | — | [[Allantoin (drug)]] 0.5 µM 0.0578× (z -10.2) |
| [[A549 (line)]] | wt | 7.68 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0738× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.122× (z -8.6) |
| [[HT-29 (line)]] | alt | 3.38 | 0 | 2 | — | [[Sildenafil (drug)]] 0.05 µM 0.0459× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -10.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0528× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -8.7) |
| [[A498 (line)]] | wt | 5.37 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0726× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0358× (z -9.8) |
| [[HOP62 (line)]] | alt | 4.33 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0986× (z -8.5) |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0524× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 7.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.158× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 9.94 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -9.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYPK]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.62 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ADAM20P1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LINC02036]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TSBP1-AS1]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[GAL3ST1]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[BNIPL]] | +0.58 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ADAM20]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.56 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LINC00159]] | +0.56 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TNXB]] | +0.56 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TMEM161B-DT]] | +0.55 | +0.66 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDYL]] | -0.48 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ARL14]] | -0.46 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[TTPAL]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MAP3K4]] | -0.44 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ODC1]] | -0.44 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SNED1-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -20.3); signed map (9.0, 6.5). **Vector** length 68.7, 11.5% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +1.9 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +5.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -10.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | SNED1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q37.3 — chr2:241,015,599-241,064,116 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41060) · Entrez [105373970](https://www.ncbi.nlm.nih.gov/gene/105373970) · Ensembl [ENSG00000225521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225521)

## Data

Gene col 13464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13464); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13464]; `tensor/DDL_lfc|DDL_z.npy` [13464]; `embed/gene_vectors.npy` [13464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13464 or target_col == 13464). Every well: [[SNED1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNED1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
