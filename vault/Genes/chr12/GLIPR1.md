---
symbol: "GLIPR1"
type: "gene"
col: 6286
ensembl_id: "ENSG00000139278"
name: "GLI pathogenesis related 1"
location: "12q21.2"
module: 66
arm: "+"
pooled_cpm: 46.78
n_lines_expressing: 29
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# GLIPR1

*GLI pathogenesis related 1* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +12.2, q 3e-31, up in 21 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pralsetinib (drug)]] 0.05 µM: 1.40× (z +3.5, q 0.056, up in 4 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 4.05×, Hs 766T 3.92×, CFPAC-1 2.89×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 5.80×, SNU-423 5.89×, NCI-H1792 4.72×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 5.59×, SNU-423 5.33×, NCI-H1792 5.72×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.603× (z -5.7, q 8e-06, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALPK2]] (+0.64, fdr 7e-06), [[CALD1]] (+0.62, fdr 1e-05), [[THBS1]] (+0.60, fdr 2e-05); moves opposite to [[TTC9C]] (-0.51, fdr 3e-05), [[NELFA]] (-0.49, fdr 3e-05), [[FRG1DP]] (-0.49, fdr 3e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CCDC80]] → it (grade B ⚠); 7 go from it, the strongest it → [[NAV3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6286.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 4.05×, Hs 766T 3.92×, CFPAC-1 2.89×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 5.80×, SNU-423 5.89×, NCI-H1792 4.72×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 5.59×, SNU-423 5.33×, NCI-H1792 5.72×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +12.2 | 3e-31 | 21/27 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +11.7 | 5e-29 | 17/22 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +8.7 | 4e-16 | 18/25 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.056 | 4/28 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.069 | 9/27 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.1 | 0.15 | 4/22 (SNU-423, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.15 | 1/28 (NCI-H1573) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.15 | 8/28 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.31× | +3.0 | 0.15 | 8/27 (H4, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -5.7 | 8e-06 | 16/27 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.642×** | -5.0 | 2e-04 | 17/27 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.656×** | -4.7 | 4e-04 | 17/27 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.764×** | -4.3 | 0.003 | 13/27 (SHP-77, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.689×** | -4.2 | 0.003 | 18/26 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.498×** | -4.1 | 0.004 | 18/26 (A498, H4, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.683×** | -4.0 | 0.006 | 8/27 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.009 | 17/27 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.025 | 14/27 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.034 | 19/26 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.035 | 21/27 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.041 | 7/27 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.095 | 13/27 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.123× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 51.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.159× (z -11.5) |
| [[A-427 (line)]] | wt | 76.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -12.7) |
| [[HS-578T (line)]] | alt | 114 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +11.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.225× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 115 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.72× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 202 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 85.0 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0357× (z -9.2) |
| [[SW 900 (line)]] | alt | 71.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 185 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.77 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALPK2]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CALD1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[THBS1]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[WDR1]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TNC]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PDCD1LG2]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[VCL]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[C12orf75-AS1]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[EXT1]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CSRP1]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ABCC9]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TRIM55]] | +0.52 | +0.38 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NELFA]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[FRG1DP]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[AGAP3]] | -0.47 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ASB7]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[HINFP]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RENO1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[C1orf50]] | -0.45 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[SDHAP2]] | -0.45 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[ZNF836]] | -0.44 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[MTFMT]] | -0.44 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[MRPS36]] ⚠ | -0.43 | -0.40 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9P]] | -0.43 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC80]] | B | CCDC80 activity raises GLIPR1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without CCDC80 | 0.074 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[ADAM12]] | C | ADAM12 activity raises GLIPR1's level | lines that do not express ADAM12 (27) vs lines expressing it (23) | 4.12× lower at baseline in the lines without ADAM12 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1; co-absent with the target |
| [[C12orf75-AS1]] | C | C12orf75-AS1 activity raises GLIPR1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 3.44× lower at baseline in the lines without C12orf75-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1; co-absent with the target |
| [[AOX1]] | C | AOX1 activity raises GLIPR1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 3.31× lower at baseline in the lines without AOX1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises GLIPR1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 3.19× lower at baseline in the lines without TRPA1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises GLIPR1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.90× lower at baseline in the lines without ALPK2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[LINC00702]] | C | LINC00702 activity raises GLIPR1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without LINC00702 | 0.051 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG; co-absent with the target |
| [[NRG1]] | C | NRG1 activity raises GLIPR1's level | lines that do not express NRG1 (19) vs lines expressing it (31) | 3.18× lower at baseline in the lines without NRG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TRIM9, DOCK2, ADAM23; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises GLIPR1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.34× lower at baseline in the lines without PDCD1LG2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV3]] | B | GLIPR1 activity raises NAV3's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 4.12× lower at baseline in the lines without GLIPR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[STARD13]] | B | GLIPR1 activity raises STARD13's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.77× lower at baseline in the lines without GLIPR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[DGKI]] | B | GLIPR1 activity raises DGKI's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without GLIPR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[ABL2]] | B | GLIPR1 activity raises ABL2's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without GLIPR1 | 0.047 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent |
| [[AOX1]] | C | GLIPR1 activity raises AOX1's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without GLIPR1 | 0.056 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[C12orf75-AS1]] | C | GLIPR1 activity raises C12orf75-AS1's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without GLIPR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[ADAM12]] | C | GLIPR1 activity raises ADAM12's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 4.73× lower at baseline in the lines without GLIPR1 | 0.081 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.0, 17.7); signed map (44.9, 19.8). **Vector** length 104, 36.3% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.9 | -0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | GLI pathogenesis related 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:75,480,753-75,503,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RTVP1, GliPR |
| Gene groups (HGNC) | GLIPR family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: PPARA activates gene expression; Regulation of lipid metabolism by PPARalpha; Neutrophil degranulation |
| Matched by | ensembl_id |

UniProt [P48060](https://www.uniprot.org/uniprotkb/P48060) carries no function annotation.

**Summary**, from NCBI Gene [11010](https://www.ncbi.nlm.nih.gov/gene/11010):

> This gene encodes a protein with similarity to both the pathogenesis-related protein (PR) superfamily and the cysteine-rich secretory protein (CRISP) family. Increased expression of this gene is associated with myelomocytic differentiation in macrophage and decreased expression of this gene through gene methylation is associated with prostate cancer. The protein has proapoptotic activities in prostate and bladder cancer cells. This gene is a member of a cluster on chromosome 12 containing two …

**Accessions** — [HGNC:17001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17001) · Entrez [11010](https://www.ncbi.nlm.nih.gov/gene/11010) · UniProt [P48060](https://www.uniprot.org/uniprotkb/P48060) · Ensembl [ENSG00000139278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139278)

## Data

Gene col 6286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6286); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6286]; `tensor/DDL_lfc|DDL_z.npy` [6286]; `embed/gene_vectors.npy` [6286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6286 or target_col == 6286). Every well: [[GLIPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
