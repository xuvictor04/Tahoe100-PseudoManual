---
symbol: "MAD2L1-DT"
type: "gene"
col: 14721
ensembl_id: "ENSG00000250938"
name: "MAD2L1 divergent transcript"
location: "4q27"
module: 10
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MAD2L1-DT

*MAD2L1 divergent transcript* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.22× (z +17.4, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.457× (z -6.7, q 1e-08, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.497× (z -6.0, q 6e-07, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.89, fdr 7e-06), [[PCNX4-DT]] (+0.88, fdr 8e-06), [[TMEM202-AS1]] (+0.85, fdr 3e-05); moves opposite to [[MAST3]] (-0.71, fdr 8e-04, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.22×** | +17.4 | 0e+00 | 42/42 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +8.5 | 8e-15 | 33/43 (HCT15, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +7.6 | 4e-12 | 31/45 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +7.4 | 1e-11 | 30/42 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +6.8 | 9e-10 | 29/40 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.7 | 1e-09 | 32/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.0 | 1e-07 | 18/32 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.7 | 1e-06 | 26/43 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +4.6 | 2e-04 | 19/46 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.5 | 3e-04 | 6/15 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.5 | 3e-04 | 7/20 (HEC-1-A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +4.5 | 3e-04 | 21/46 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.9 | 0.005 | 13/28 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.006 | 20/45 (NCI-H1573, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.007 | 15/47 (C32, HepG2/C3A, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.012 | 13/45 (C32, SW480, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.1 | 0.055 | 10/45 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.055 | 8/48 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.078 | 17/44 (C32, NCI-H23, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.457×** | -6.7 | 1e-08 | 27/47 (SNU-1, KATO III, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.497×** | -6.0 | 6e-07 | 25/46 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -5.4 | 1e-05 | 26/46 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -4.1 | 0.006 | 16/45 (A-427, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.645×** | -3.8 | 0.017 | 17/41 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.630×** | -3.7 | 0.017 | 19/45 (CFPAC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.45 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 6.79 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +9.4) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.146× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +13.3) | — |
| [[A-172 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0653× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0637× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 5.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 8.09 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0382× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 4.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +9.1) | — |
| [[A-427 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.89 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.88 | +0.90 / +0.58 | both halves | 8e-06 | same gene group |
| [[TMEM202-AS1]] | +0.85 | +0.86 / +0.45 | both halves | 3e-05 |  |
| [[BDNF-AS]] | +0.84 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.84 | +0.81 / +0.57 | both halves | 1e-05 | same gene group |
| [[USP38-DT]] | +0.84 | +0.85 / +0.65 | both halves | 7e-06 | same gene group |
| [[CFAP418-AS1]] | +0.83 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.83 | +0.81 / +0.56 | both halves | 1e-05 | same gene group |
| [[DPH6-DT]] | +0.81 | +0.84 / +0.49 | both halves | 1e-05 | same gene group |
| [[ANKRD17-DT]] | +0.81 | +0.79 / +0.55 | both halves | 1e-05 | same gene group |
| [[SEPTIN7-DT]] | +0.81 | +0.81 / +0.49 | both halves | 1e-05 | same gene group |
| [[OXA1L-DT]] | +0.81 | +0.79 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.71 | -0.67 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAD2L1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises MAD2L1-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without FSIP2-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[FAP]] | B | FAP activity raises MAD2L1-DT's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without FAP | 0.029 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[ZNF382]] | B | ZNF382 activity raises MAD2L1-DT's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.72× lower at baseline in the lines without ZNF382 | 0.042 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[PSMB5]] | B | PSMB5 activity raises MAD2L1-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises MAD2L1-DT's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without ST8SIA5 | 0.082 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MAD2L1-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RNF32-DT]] | B | RNF32-DT activity lowers MAD2L1-DT's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 1.54× higher at baseline in the lines without RNF32-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[HECTD2]] | B | HECTD2 activity raises MAD2L1-DT's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without HECTD2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises MAD2L1-DT's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without FBXO38-DT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[RGS14]] | C | RGS14 activity lowers MAD2L1-DT's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.33× higher at baseline in the lines without RGS14 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.853). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.4, 16.3); signed map (27.8, -9.6). **Vector** length 80.0, 15.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | +0.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAD2L1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q27 — chr4:120,066,904-120,564,789 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55546) · Entrez [121009649](https://www.ncbi.nlm.nih.gov/gene/121009649) · Ensembl [ENSG00000250938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250938)

## Data

Gene col 14721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14721); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14721]; `tensor/DDL_lfc|DDL_z.npy` [14721]; `embed/gene_vectors.npy` [14721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14721 or target_col == 14721). Every well: [[MAD2L1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAD2L1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
