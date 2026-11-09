---
symbol: "GLRB"
type: "gene"
col: 3076
ensembl_id: "ENSG00000109738"
name: "glycine receptor beta"
location: "4q32.1"
module: 19
arm: "+"
pooled_cpm: 6.22
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GLRB

*glycine receptor beta* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.95× (z +20.5, q 0e+00, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.670× (z -7.6, q 2e-11, down in 17 of 26 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.693× (z -7.0, q 8e-10, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNCA]] (+0.61, fdr 7e-06), [[SLITRK5]] (+0.60, fdr 7e-06), [[SFMBT2]] (+0.60, fdr 1e-05); moves opposite to [[RECQL5]] (-0.51, fdr 5e-05), [[SMIM12]] (-0.49, fdr 2e-04), [[RABL2A]] (-0.49, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SYT1]] → it (grade B ⚠); 2 go from it, the strongest it → [[CDR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.95×** | +20.5 | 0e+00 | 25/28 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.30×** | +16.0 | 0e+00 | 21/26 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +8.6 | 2e-15 | 16/27 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +8.0 | 2e-13 | 17/27 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.4 | 2e-11 | 5/14 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +6.2 | 7e-08 | 14/27 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +5.7 | 1e-06 | 12/27 (NCI-H2347, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.53×** | +5.7 | 1e-06 | 11/27 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +5.2 | 2e-05 | 9/28 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +5.0 | 3e-05 | 11/27 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.003 | 8/27 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.9 | 0.004 | 7/27 (NCI-H460, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.013 | 4/27 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.015 | 7/22 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +3.5 | 0.015 | 5/27 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.015 | 3/28 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.061 | 4/27 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.081 | 5/26 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.096 | 8/27 (NCI-H2347, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.670×** | -7.6 | 2e-11 | 17/26 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -7.0 | 8e-10 | 16/26 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.638×** | -5.7 | 2e-06 | 13/26 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -5.7 | 2e-06 | 14/27 (NCI-H460, SW 900, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.478×** | -5.2 | 2e-05 | 8/26 (SW 900, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.013 | 7/26 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.8 | 0.013 | 9/28 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.756×** | -3.6 | 0.020 | 10/26 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.021 | 9/27 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.023 | 13/27 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.048 | 4/27 (BT-474, NCI-H661, …) | rises with dose |  |
| [[Resveratrol (drug)]] 5 µM |  | 0.848× | -3.1 | 0.081 | 3/27 (NCI-H2030, CHP-212, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.794×** | -3.1 | 0.083 | 10/26 (AN3 CA, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Valdecoxib (drug)]] 0.5 µM |  | **0.798×** | -3.0 | 0.096 | 5/27 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.799×** | -3.0 | 0.096 | 10/27 (NCI-H460, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.287× (z -9.1) |
| [[AN3 CA (line)]] | alt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0797× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 8.67 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.45× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 4.93 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0868× (z -8.6) ⚠ transcription drop · without an alert: [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0742× (z -8.5) |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.1) |
| [[A-427 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 3.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.82× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 7.70 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0923× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 5.91 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0746× (z -9.5) |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.540 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNCA]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SLITRK5]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[SFMBT2]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM170B]] | +0.59 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[ASXL3]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PRKAR2B]] | +0.55 | +0.37 / +0.64 | both halves | 8e-05 | pathway: Neuronal System |
| [[ARHGAP28]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SCN9A]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[WDR17]] | +0.54 | +0.32 / +0.61 | both halves | 1e-04 |  |
| [[TMEM108]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PRICKLE1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL5]] | -0.51 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SMIM12]] | -0.49 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[RABL2A]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.47 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[ACAD9]] | -0.47 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[ATXN1L]] | -0.47 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[UBAP1L]] | -0.47 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CDR2]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[TRIM39]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[CEP89]] | -0.46 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[ERICH1]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[KRIT1]] | -0.45 | -0.30 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT1]] | B | SYT1 activity raises GLRB's level | lines that do not express SYT1 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without SYT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: EDIL3, LAYN, PRRX1 |
| [[CNKSR2]] | B | CNKSR2 activity weakens GLRB's drug response | lines that do not express CNKSR2 (16) vs lines expressing it (12) | the lines without CNKSR2 respond 1.22× as strongly (z diff -0.29); strongest at Dinaciclib 5 µM: 1.42x vs 0.49x (z diff -5.0) | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers GLRB's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[MOXD1]] | C | MOXD1 activity raises GLRB's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 2.52× lower at baseline in the lines without MOXD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDR2]] | B | GLRB activity lowers CDR2's level | lines that do not express GLRB (19) vs lines expressing it (31) | 1.28× higher at baseline in the lines without GLRB | 0.036 | ⚠ within organs, on part of the lines; also absent: ELOVL4, LRP1B, PRR16 |
| [[PDGFC]] | C | GLRB activity raises PDGFC's level | lines that do not express GLRB (19) vs lines expressing it (31) | 3.66× lower at baseline in the lines without GLRB | 0.025 | ⚠ within organs, on part of the lines; also absent: ELOVL4, LRP1B, PRR16; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.1, 35.6); signed map (39.4, 38.7). **Vector** length 59.7, 12.6% of its response variance represented; |z| ≥ 3 in 649 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +20.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | +3.5 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.0 | +1.1 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.2 | -7.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glycine receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:157,076,125-157,172,090 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycine receptors |
| Reactome | 3 pathways, smallest: Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [P48167](https://www.uniprot.org/uniprotkb/P48167) (Glycine receptor subunit beta):

> Subunit of heteromeric glycine-gated chloride channels. Plays an important role in the down-regulation of neuronal excitability. Contributes to the generation of inhibitory postsynaptic currents.

**Summary**, from NCBI Gene [2743](https://www.ncbi.nlm.nih.gov/gene/2743):

> This gene encodes the beta subunit of the glycine receptor, which is a pentamer composed of alpha and beta subunits. The receptor functions as a neurotransmitter-gated ion channel, which produces hyperpolarization via increased chloride conductance due to the binding of glycine to the receptor. Mutations in this gene cause startle disease, also known as hereditary hyperekplexia or congenital stiff-person syndrome, a disease characterized by muscular rigidity. Alternative splicing results in …

**Accessions** — [HGNC:4329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4329) · Entrez [2743](https://www.ncbi.nlm.nih.gov/gene/2743) · UniProt [P48167](https://www.uniprot.org/uniprotkb/P48167) · Ensembl [ENSG00000109738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109738)

## Data

Gene col 3076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3076); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3076]; `tensor/DDL_lfc|DDL_z.npy` [3076]; `embed/gene_vectors.npy` [3076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3076 or target_col == 3076). Every well: [[GLRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
