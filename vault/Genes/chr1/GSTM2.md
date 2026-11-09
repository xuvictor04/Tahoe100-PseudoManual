---
symbol: "GSTM2"
type: "gene"
col: 13099
ensembl_id: "ENSG00000213366"
name: "glutathione S-transferase mu 2"
location: "1p13.3"
module: 50
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GSTM2

*glutathione S-transferase mu 2* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.71× (z +8.8, q 7e-16, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.44× (z +8.2, q 5e-14, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.460× (z -6.9, q 3e-09, down in 17 of 35 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.449× (z -6.8, q 4e-09, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC183]] (+0.63, fdr 1e-05), [[GSTM4]] (+0.62, fdr 7e-06, ⚠ same locus), [[FN3K]] (+0.58, fdr 2e-05), [[ASAH1]] (+0.56, fdr 6e-05); moves opposite to [[CCDC137]] (-0.56, fdr 1e-04), [[ENOX2]] (-0.50, fdr 1e-04), [[EIF5B]] (-0.50, fdr 3e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LURAP1]] → it (grade B ⚠); 3 go from it, the strongest it → [[GSTM4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +8.8 | 7e-16 | 1/1 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +8.7 | 7e-16 | 3/4 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +8.2 | 5e-14 | 23/42 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +7.4 | 2e-11 | 21/39 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.68×** | +6.7 | 2e-09 | 12/41 (A-172, C32, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.5 | 6e-09 | 10/26 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.95×** | +6.1 | 7e-08 | 15/40 (PANC-1, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.1 | 3e-05 | 9/40 (A498, HEC-1-A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +4.7 | 1e-04 | 9/43 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +4.4 | 7e-04 | 9/39 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 4/38 (A498, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.8 | 0.008 | 1/10 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.011 | 4/42 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.018 | 4/33 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.46×** | +3.5 | 0.019 | 5/32 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.019 | 7/42 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.055 | 4/28 (SW480, LS 180, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.062 | 5/37 (RKO, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.091 | 3/32 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.099 | 4/33 (A-172, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13099.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.460×** | -6.9 | 3e-09 | 17/35 (HOP62, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.449×** | -6.8 | 4e-09 | 21/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.500×** | -6.4 | 2e-08 | 17/36 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.512×** | -6.2 | 8e-08 | 21/42 (C32, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.629×** | -4.3 | 0.002 | 15/37 (COLO 205, C32, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.639×** | -4.1 | 0.004 | 12/36 (LoVo, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.673×** | -3.6 | 0.022 | 13/32 (SW480, AN3 CA, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.669×** | -3.6 | 0.022 | 9/36 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.092 | 11/41 (NCI-H1573, J82, …) | top dose only |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | 0.713× | -3.1 | 0.11 | 4/34 (A-427, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.721× | -3.0 | 0.11 | 11/43 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.796× | -3.0 | 0.11 | 11/38 (A-427, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.725× | -3.0 | 0.12 | 5/40 (PANC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.72 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.126× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 9.07 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0549× (z -10.3) |
| [[A-172 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.933 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC183]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | same gene group; pathway: Biological oxidations; STRING 973; ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[FN3K]] | +0.58 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ASAH1]] | +0.56 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[GAA]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LMNTD2]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MORF4L1]] | +0.55 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[EMC10]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TCEA2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.54 | +0.39 / +0.55 | both halves | 5e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[IL11RA]] | +0.53 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[GDPD3]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[KNDC1]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC137]] | -0.56 | -0.32 / -0.57 | both halves | 1e-04 |  |
| [[ENOX2]] | -0.50 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[EIF5B]] | -0.50 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[SMC6]] | -0.50 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[TASOR2]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[EEA1]] | -0.49 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[RNF34]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[VPS25]] | -0.49 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[C14orf119]] | -0.49 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[EIF6]] | -0.48 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[MRPL36]] | -0.48 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[H3-3B]] | -0.47 | -0.28 / -0.57 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1]] | B | LURAP1 activity raises GSTM2's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.18× lower at baseline in the lines without LURAP1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTM4]] | C | GSTM2 activity raises GSTM4's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without GSTM2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent; its own permutation p |
| [[FN3K]] | C | GSTM2 activity raises FN3K's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without GSTM2 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent |
| [[GAA]] | C | GSTM2 activity raises GAA's level | lines that do not express GSTM2 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without GSTM2 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLEC2D, IMPG2, ENSG00000286952; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.1, -7.9); signed map (-28.0, -3.2). **Vector** length 36.9, 3.83% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +3.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.3 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.5 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.3 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase mu 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,668,022-109,709,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GST4 |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 3 pathways, smallest: Glutathione conjugation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P28161](https://www.uniprot.org/uniprotkb/P28161) (Glutathione S-transferase Mu 2):

> Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles. Participates in the formation of novel hepoxilin regioisomers.

**Summary**, from NCBI Gene [2946](https://www.ncbi.nlm.nih.gov/gene/2946):

> Cytosolic and membrane-bound forms of glutathione S-transferase are encoded by two distinct supergene families. At present, eight distinct classes of the soluble cytoplasmic mammalian glutathione S-transferases have been identified: alpha, kappa, mu, omega, pi, sigma, theta and zeta. This gene encodes a glutathione S-transferase that belongs to the mu class. The mu class of enzymes functions in the detoxification of electrophilic compounds, including carcinogens, therapeutic drugs, …

**Accessions** — [HGNC:4634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4634) · Entrez [2946](https://www.ncbi.nlm.nih.gov/gene/2946) · UniProt [P28161](https://www.uniprot.org/uniprotkb/P28161) · Ensembl [ENSG00000213366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213366)

## Data

Gene col 13099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13099); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13099]; `tensor/DDL_lfc|DDL_z.npy` [13099]; `embed/gene_vectors.npy` [13099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13099 or target_col == 13099). Every well: [[GSTM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
