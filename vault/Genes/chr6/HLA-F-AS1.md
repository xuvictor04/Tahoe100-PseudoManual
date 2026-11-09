---
symbol: "HLA-F-AS1"
type: "gene"
col: 13231
ensembl_id: "ENSG00000214922"
name: "HLA-F antisense RNA 1"
location: "6p22.1"
module: 40
arm: "+"
pooled_cpm: 15.51
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# HLA-F-AS1

*HLA-F antisense RNA 1* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +20.6, q 0e+00, up in 34 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.446× (z -11.5, q 4e-28, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICE]] (+0.74, fdr 7e-06, ⚠ same locus), [[LINC02210-CRHR1]] (+0.63, fdr 1e-05), [[RAB6A]] (+0.63, fdr 2e-05), [[DEDD2]] (+0.61, fdr 4e-05); moves opposite to [[ANAPC7]] (-0.62, fdr 2e-05), [[TMEM185B]] (-0.58, fdr 1e-05), [[ZNF644]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MICE]] → it (grade B ⚠); 10 go from it, the strongest it → [[FARSB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +20.6 | 0e+00 | 34/38 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +12.4 | 9e-33 | 33/39 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.2 | 9e-08 | 20/39 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 2e-07 | 20/41 (LS 180, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +5.7 | 1e-06 | 17/41 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.3 | 9e-06 | 7/28 (J82, C32, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 16/41 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.1 | 3e-05 | 13/38 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 4e-05 | 14/41 (A498, LS 180, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +4.9 | 4e-05 | 15/41 (LS 180, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.35×** | +4.5 | 4e-04 | 12/42 (NCI-H460, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +4.4 | 6e-04 | 15/40 (SK-MEL-2, J82, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 10/42 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +4.3 | 7e-04 | 8/39 (H4, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.001 | 11/42 (J82, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 17/42 (NCI-H2030, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.19× | +3.7 | 0.008 | 10/42 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.008 | 7/41 (J82, A-172, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.446×** | -11.5 | 4e-28 | 26/41 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -8.0 | 5e-13 | 22/41 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -4.9 | 2e-04 | 16/34 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.736×** | -4.2 | 0.004 | 16/25 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.757×** | -4.1 | 0.004 | 15/42 (KATO III, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -3.9 | 0.008 | 14/37 (A-172, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.630×** | -3.6 | 0.027 | 14/41 (CFPAC-1, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.789×** | -3.5 | 0.032 | 8/39 (C32, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.098 | 15/39 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.810× | -3.1 | 0.10 | 6/40 (Hs 766T, HCT15, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.813× | -3.1 | 0.11 | 10/41 (CFPAC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 94.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -35.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.181× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 42.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.239× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.284× (z -9.3) |
| [[C32 (line)]] | wt | 18.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0824× (z -13.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 28.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 15.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -12.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0379× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HT-29 (line)]] | alt | 45.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 31.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[Panc 03.27 (line)]] | alt | 32.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.45× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0662× (z -13.3) |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0608× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.107× (z -8.5) |
| [[SW480 (line)]] | alt | 18.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +10.7) | — |
| [[A498 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +18.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0521× (z -10.9) |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HOP62 (line)]] | alt | 6.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.9) | — |
| [[J82 (line)]] | alt | 8.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 7.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.41× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 5.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICE]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02210-CRHR1]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[DEDD2]] | +0.61 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[ATG9B]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CRELD1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PIK3C2A]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SLC2A1-DT]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[MED31]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CLK3]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TSC22D4]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NQO2]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[DPM1]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC7]] | -0.62 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.58 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[FKTN]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[RUVBL1]] | -0.56 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DPH6]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[XRN2]] | -0.56 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SAYSD1]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[POGLUT1]] | -0.55 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[FARSB]] | -0.55 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[COA7]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICE]] | B | MICE activity raises HLA-F-AS1's level | lines that do not express MICE (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without MICE | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[KCNK6]] | B | KCNK6 activity raises HLA-F-AS1's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without KCNK6 | 0.026 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises HLA-F-AS1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.16× lower at baseline in the lines without ATP6V0D2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FARSB]] | B | HLA-F-AS1 activity lowers FARSB's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.77× higher at baseline in the lines without HLA-F-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[SF3B3]] | B | HLA-F-AS1 activity lowers SF3B3's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.55× higher at baseline in the lines without HLA-F-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[MICA]] | B | HLA-F-AS1 activity raises MICA's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without HLA-F-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[ATIC]] | B | HLA-F-AS1 activity lowers ATIC's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without HLA-F-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[ANAPC7]] | B | HLA-F-AS1 activity lowers ANAPC7's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.44× higher at baseline in the lines without HLA-F-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[PPME1]] | B | HLA-F-AS1 activity lowers PPME1's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.48× higher at baseline in the lines without HLA-F-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[PRRC2A]] | B | HLA-F-AS1 activity lowers PRRC2A's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without HLA-F-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[XRN2]] | B | HLA-F-AS1 activity lowers XRN2's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.21× higher at baseline in the lines without HLA-F-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[SRCAP]] | B | HLA-F-AS1 activity lowers SRCAP's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without HLA-F-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[CEP41]] | B | HLA-F-AS1 activity lowers CEP41's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 1.95× higher at baseline in the lines without HLA-F-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.9, -22.4); signed map (-26.3, 26.5). **Vector** length 93.2, 19.9% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +20.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.6 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -3.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.6 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | HLA-F antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.1 — chr6:29,726,601-29,749,049 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26645) · Entrez [285830](https://www.ncbi.nlm.nih.gov/gene/285830) · Ensembl [ENSG00000214922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214922)

## Data

Gene col 13231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13231); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13231]; `tensor/DDL_lfc|DDL_z.npy` [13231]; `embed/gene_vectors.npy` [13231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13231 or target_col == 13231). Every well: [[HLA-F-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-F-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
