---
symbol: "NUAK2"
type: "gene"
col: 8716
ensembl_id: "ENSG00000163545"
name: "NUAK family kinase 2"
location: "1q32.1"
module: 14
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 40
n_dd_up: 24
n_dd_down: 24
n_dd_up_clean: 19
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NUAK2

*NUAK family kinase 2* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.70× (z +35.3, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.554× (z -7.3, q 1e-10, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIE]] (+0.67, fdr 7e-06), [[CX3CL1]] (+0.64, fdr 1e-05), [[BCL3]] (+0.63, fdr 7e-06); moves opposite to [[GAN]] (-0.55, fdr 3e-05), [[TMEM11-DT]] (-0.55, fdr 1e-05), [[C9orf153]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CX3CL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8716.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.70×** | +35.3 | 0e+00 | 35/36 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **41.5×** | +25.6 | 0e+00 | 38/38 (NCI-H460, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **6.42×** | +23.5 | 0e+00 | 33/37 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.16×** | +15.1 | 0e+00 | 29/37 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **8.50×** | +14.7 | 0e+00 | 30/35 (HEC-1-A, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +8.9 | 5e-17 | 24/37 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +8.5 | 2e-15 | 21/32 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +8.4 | 4e-15 | 18/38 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +7.7 | 7e-13 | 20/38 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.14×** | +7.1 | 7e-11 | 23/38 (A-172, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.75×** | +6.8 | 6e-10 | 14/26 (J82, PANC-1, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 2e-07 | 18/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.49×** | +5.2 | 8e-06 | 16/36 (NCI-H460, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.8 | 7e-05 | 14/38 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +4.8 | 7e-05 | 16/37 (PANC-1, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.002 | 9/38 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.009 | 14/38 (SW480, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.010 | 12/37 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8716.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -7.3 | 1e-10 | 23/38 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -6.8 | 3e-09 | 20/37 (NCI-H23, Hs 766T, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.623×** | -6.2 | 1e-07 | 19/37 (NCI-H2030, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.646×** | -5.8 | 1e-06 | 17/37 (NCI-H23, HepG2/C3A, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.744×** | -5.5 | 4e-06 | 20/38 (HCT15, A549, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.665×** | -5.2 | 2e-05 | 12/38 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.683×** | -5.0 | 4e-05 | 16/37 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.9 | 8e-05 | 22/37 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -4.5 | 5e-04 | 16/37 (NCI-H23, A549, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.708×** | -4.4 | 7e-04 | 14/37 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.724×** | -4.3 | 0.001 | 16/38 (SW 1088, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.540×** | -4.2 | 0.001 | 11/38 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.739×** | -4.0 | 0.003 | 18/37 (NCI-H460, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.006 | 17/37 (NCI-H2347, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.009 | 10/38 (Panc 03.27, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.6 | 0.013 | 9/38 (A-172, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8716. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.2 | 13 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +24.7) | [[Ixazomib citrate (drug)]] 5 µM 0.260× (z -9.0) |
| [[A-172 (line)]] | wt | 32.3 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +22.0) | — |
| [[A549 (line)]] | wt | 65.0 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +23.9) | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 33.9 | 2 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 29.2× (z +11.1) | [[Ixazomib citrate (drug)]] 5 µM 0.103× (z -14.3) |
| [[A-427 (line)]] | wt | 17.4 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 9.77× (z +12.8) | [[AZD2858 (drug)]] 0.5 µM 0.106× (z -9.1) ⚠ toxic |
| [[A498 (line)]] | wt | 61.7 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +25.8) | [[Bortezomib (drug)]] 0.05 µM 0.195× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 37.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +17.7) | — |
| [[J82 (line)]] | alt | 41.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 4 | 1 | [[Harringtonine (drug)]] 5 µM 7.13× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 57.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 44.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 17.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +22.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 43.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +16.6) | — |
| [[SW480 (line)]] | alt | 10.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +15.1) | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[SNU-423 (line)]] | alt | 23.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +19.0) | — |
| [[C32 (line)]] | wt | 5.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 7.53 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 7.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 9.13 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +9.0) | [[Cepharanthine (drug)]] 0.5 µM 0.0674× (z -8.5) |
| [[BT-474 (line)]] | alt | 9.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0674× (z -11.8) |
| [[Hs 766T (line)]] | wt | 50.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.197× (z -8.6) |
| [[HS-578T (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 6.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.279× (z -8.8) |
| [[SW 900 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8716), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[BCL3]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CD83]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TPM1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FCHSD2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[IKBKE]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NFKBIA]] | +0.58 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NFKB1]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ANKRD33B]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAN]] | -0.55 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.55 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[C9orf153]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MFN1]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.53 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[MROH1]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CCDC32]] | -0.52 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[DCUN1D2]] | -0.52 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[IL17RA]] | -0.50 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[RAB22A]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[APTX]] | -0.50 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ZCCHC17]] | -0.50 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CX3CL1]] | B | CX3CL1 activity raises NUAK2's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without CX3CL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 5.9); signed map (43.7, 6.7). **Vector** length 110, 27.4% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +23.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +25.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +35.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +15.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.6 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.4 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -6.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | NUAK family kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,302,063-205,321,745 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNARK, FLJ90349 |
| Gene groups (HGNC) | NUAK family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H093](https://www.uniprot.org/uniprotkb/Q9H093) (NUAK family SNF1-like kinase 2):

> Stress-activated kinase involved in tolerance to glucose starvation. Induces cell-cell detachment by increasing F-actin conversion to G-actin. Expression is induced by CD95 or TNF, via NF-kappa-B. Protects cells from CD95-mediated apoptosis and is required for the increased motility and invasiveness of CD95-activated tumor cells. Phosphorylates LATS1 and LATS2. Plays a key role in neural tube closure during embryonic development through LATS2 phosphorylation and regulation of the nuclear …

**Summary**, from NCBI Gene [81788](https://www.ncbi.nlm.nih.gov/gene/81788):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in several processes, including cellular response to glucose starvation; protein phosphorylation; and regulation of hippo signaling. Located in nuclear speck. Implicated in anencephaly. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29558) · Entrez [81788](https://www.ncbi.nlm.nih.gov/gene/81788) · UniProt [Q9H093](https://www.uniprot.org/uniprotkb/Q9H093) · Ensembl [ENSG00000163545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163545)

## Data

Gene col 8716: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8716); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8716, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8716]; `tensor/DDL_lfc|DDL_z.npy` [8716]; `embed/gene_vectors.npy` [8716]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8716 or target_col == 8716). Every well: [[NUAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
