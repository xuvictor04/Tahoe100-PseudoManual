---
symbol: "NUAK1"
type: "gene"
col: 1083
ensembl_id: "ENSG00000074590"
name: "NUAK family kinase 1"
location: "12q23.3"
module: 14
arm: "+"
pooled_cpm: 24.5
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NUAK1

*NUAK family kinase 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +13.0, q 4e-36, up in 28 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.16× (z +9.3, q 3e-18, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.434× (z -15.9, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD2]] (+0.61, fdr 1e-05), [[LINC00265]] (+0.60, fdr 4e-05), [[ARHGEF40]] (+0.57, fdr 2e-05); moves opposite to [[CA5B]] (-0.53, fdr 2e-04), [[RECQL]] (-0.51, fdr 3e-05), [[ZNF731P]] (-0.50, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[REEP2]] → it (grade B ⚠); 3 go from it, the strongest it → [[GLIS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.62×** | +13.0 | 4e-36 | 28/42 (A549, HepG2/C3A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.16×** | +9.3 | 3e-18 | 29/43 (HepG2/C3A, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +8.1 | 8e-14 | 24/42 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.34×** | +7.8 | 9e-13 | 24/43 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +7.1 | 2e-10 | 20/43 (NCI-H460, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +5.4 | 7e-06 | 15/42 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | composition shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 13/42 (A498, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 4e-05 | 14/41 (HOP62, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +4.9 | 7e-05 | 16/42 (A549, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 0.001 | 10/43 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 13/40 (LoVo, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.004 | 9/42 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.6 | 0.015 | 14/38 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.5 | 0.019 | 10/38 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.52×** | +3.4 | 0.024 | 10/40 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.061 | 5/43 (PANC-1, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.434×** | -15.9 | 0e+00 | 35/43 (Hs 766T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -15.5 | 0e+00 | 33/43 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -12.6 | 3e-34 | 30/42 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -7.4 | 1e-11 | 25/42 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -6.8 | 1e-09 | 20/42 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.729×** | -5.8 | 6e-07 | 14/27 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.747×** | -5.4 | 7e-06 | 17/40 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -5.2 | 2e-05 | 22/43 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.563×** | -4.7 | 2e-04 | 14/39 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.786×** | -3.7 | 0.011 | 15/31 (HS-578T, LoVo, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.019 | 9/42 (A-172, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.019 | 11/42 (NCI-H1792, HepG2/C3A, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.023 | 4/43 (J82, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.836× | -3.4 | 0.023 | 14/42 (NCI-H2030, AN3 CA, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -3.4 | 0.024 | 9/42 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.052 | 2/43 (Hs 766T, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.054 | 15/41 (NCI-H2030, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 41.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 24.1 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -15.1) |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.309× (z -11.2) |
| [[PANC-1 (line)]] | alt | 49.5 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.402× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -11.2) |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -10.7) |
| [[SW480 (line)]] | alt | 25.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.215× (z -13.3) |
| [[A-172 (line)]] | wt | 84.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -11.9) |
| [[A498 (line)]] | wt | 35.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -10.3) |
| [[A549 (line)]] | wt | 25.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.2) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 37.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Panobinostat (drug)]] 5 µM 0.215× (z -9.4) |
| [[SW48 (line)]] | wt | 32.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.6) |
| [[A-427 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.157× (z -12.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -9.5) |
| [[AN3 CA (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD2]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LINC00265]] | +0.60 | +0.68 / +0.40 | both halves | 4e-05 |  |
| [[ARHGEF40]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CCDC102A]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RARG]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ZFHX2]] | +0.56 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[TMEM17]] | +0.56 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ATP23]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[ZNF219]] | +0.55 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[REPIN1]] | +0.54 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[REEP2]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.54 | +0.62 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA5B]] | -0.53 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[RECQL]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF731P]] | -0.50 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[ODF2]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TMED5]] | -0.49 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PMPCA]] | -0.47 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[MTG1]] | -0.47 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[GRK6]] | -0.46 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[FARP2]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[BCAP31]] | -0.46 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[TPD52L2]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TREX2]] | -0.46 | -0.50 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[REEP2]] | B | REEP2 activity raises NUAK1's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.44× lower at baseline in the lines without REEP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[SYNPO]] | B | SYNPO activity raises NUAK1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.29× lower at baseline in the lines without SYNPO | 0.022 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ABL1]] | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD33B]] | B | ANKRD33B activity raises NUAK1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without ANKRD33B | 0.080 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[PPM1H]] | B | PPM1H activity strengthens NUAK1's drug response | lines that do not express PPM1H (11) vs lines expressing it (32) | the lines without PPM1H respond 0.49× as strongly (z diff +1.55); strongest at Panobinostat 5 µM: 0.60x vs 0.37x (z diff +3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIS2]] | B | NUAK1 activity raises GLIS2's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without NUAK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1; its own permutation p |
| [[TPD52L2]] | B | NUAK1 activity raises TPD52L2's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without NUAK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1; its own permutation p |
| [[SYNPO]] | B | NUAK1 activity raises SYNPO's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 3.76× lower at baseline in the lines without NUAK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.1, 6.5); signed map (41.7, 0.5). **Vector** length 95.4, 21.8% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.1 | +13.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +5.0 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.3 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -15.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -15.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -12.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NUAK family kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,063,345-106,138,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARK5, KIAA0537 |
| Gene groups (HGNC) | NUAK family kinases |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Phosphorylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60285](https://www.uniprot.org/uniprotkb/O60285) (NUAK family SNF1-like kinase 1):

> Serine/threonine-protein kinase involved in various processes such as cell adhesion, regulation of cell ploidy and senescence, cell proliferation and tumor progression. Phosphorylates ATM, CASP6, LATS1, PPP1R12A and p53/TP53. Acts as a regulator of cellular senescence and cellular ploidy by mediating phosphorylation of 'Ser-464' of LATS1, thereby controlling its stability. Controls cell adhesion by regulating activity of the myosin protein phosphatase 1 (PP1) complex. Acts by mediating …

**Summary**, from NCBI Gene [9891](https://www.ncbi.nlm.nih.gov/gene/9891):

> Enables p53 binding activity and protein serine/threonine kinase activity. Involved in protein phosphorylation; regulation of cell adhesion; and regulation of cellular senescence. Located in cytoplasm; fibrillar center; and nucleoplasm. Implicated in uterine fibroid. Biomarker of uterine fibroid. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14311) · Entrez [9891](https://www.ncbi.nlm.nih.gov/gene/9891) · UniProt [O60285](https://www.uniprot.org/uniprotkb/O60285) · Ensembl [ENSG00000074590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074590)

## Data

Gene col 1083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1083); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1083]; `tensor/DDL_lfc|DDL_z.npy` [1083]; `embed/gene_vectors.npy` [1083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1083 or target_col == 1083). Every well: [[NUAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
