---
symbol: "TBILA"
type: "gene"
col: 15348
ensembl_id: "ENSG00000261488"
name: "TGF-beta induced lncRNA"
location: "3q13.2"
module: 110
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 40
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# TBILA

*TGF-beta induced lncRNA* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.37× (z +8.3, q 7e-14, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.56× (z +6.9, q 8e-10, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.288× (z -4.8, q 1e-03, down in 15 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 0.05 µM in 1 line (BT-474 0.0686×); [[Demeclocycline (drug)]] 0.5 µM in 1 line (KATO III 0.0485×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf52]] (+0.76, fdr 7e-06, ⚠ read-through risk), [[SSUH2]] (+0.71, fdr 7e-06), [[PHEX]] (+0.68, fdr 7e-06), [[NEK10]] (+0.68, fdr 7e-06); moves opposite to [[RCOR3]] (-0.64, fdr 7e-06), [[SPATA7]] (-0.61, fdr 9e-06), [[TADA1]] (-0.60, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 40 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +8.3 | 7e-14 | 1/5 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +7.0 | 8e-10 | 2/4 (BT-474, HOP62) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +6.9 | 8e-10 | 23/37 (SNU-423, NCI-H2347, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +6.8 | 1e-09 | 6/13 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +5.7 | 1e-06 | 17/34 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +5.3 | 1e-05 | 9/23 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +4.9 | 7e-05 | 15/39 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.8 | 1e-04 | 11/40 (HOP62, NCI-H2347, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 11/31 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 9/40 (BT-474, A-172, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +3.8 | 0.007 | 12/40 (HOP62, A498, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.83×** | +3.8 | 0.007 | 12/38 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +3.8 | 0.007 | 11/37 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.63×** | +3.6 | 0.011 | 8/40 (NCI-H1573, SNU-423, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +3.6 | 0.011 | 4/34 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.011 | 6/38 (NCI-H1573, NCI-H23, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.026 | 12/29 (NCI-H1573, BT-474, …) | two highest doses |  |
| [[Acetohexamide (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.090 | 3/39 (A498, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Silodosin (drug)]] 0.05 µM in 1 line (BT-474 0.0686×); [[Demeclocycline (drug)]] 0.5 µM in 1 line (KATO III 0.0485×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.288×** | -4.8 | 1e-03 | 15/27 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -3.9 | 0.026 | 18/42 (HOP62, BT-474, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.722× | -3.4 | 0.14 | 9/39 (NCI-H1573, SNU-423, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.10 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0686× (z -9.2) |
| [[KATO III (line)]] | alt | 2.83 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.5 µM 0.0485× (z -8.6) |
| [[A-172 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.680 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf52]] | +0.76 | +0.66 / +0.80 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 2.4 kb 3′ of C3orf52 on the same strand (can correlate by spillover, not regulation) |
| [[SSUH2]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[PHEX]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NEK10]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SMCO2]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[CD44]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CREB5]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC01589]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[BACH1]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MPP4]] | +0.64 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[RNF32-AS1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[SPATA7]] | -0.61 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[TADA1]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TERF1]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TMEM143]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[COPS4]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[KANTR]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PEX3]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[PEX11B]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises TBILA's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.55× lower at baseline in the lines without C6orf141 | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[RAI14]] | B | RAI14 activity raises TBILA's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without RAI14 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[MGLL]] | B | MGLL activity raises TBILA's level | lines that do not express MGLL (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without MGLL | 0.040 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[LINC00707]] | B | LINC00707 activity raises TBILA's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 1.24× lower at baseline in the lines without LINC00707 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[ITGA2]] | B | ITGA2 activity raises TBILA's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without ITGA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[C3orf52]] | C | C3orf52 activity raises TBILA's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 2.48× lower at baseline in the lines without C3orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 0, C 40. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | TBILA activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.66× the cells of the other lines | 0.002 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[olaparib (drug)]] 5 µM | C | TBILA activity lowers the cells' numbers under olaparib 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.64× the cells of the other lines | 0.006 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Everolimus (drug)]] 5 µM | C | TBILA activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.28× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[PF-06260933 (drug)]] 5 µM | C | TBILA activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.55× the cells of the other lines | 0.010 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | C | TBILA activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.45× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | TBILA activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.75× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Tolcapone (drug)]] 5 µM | C | TBILA activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.79× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | TBILA activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.70× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Sulfatinib (drug)]] 5 µM | C | TBILA activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.72× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | TBILA activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.77× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Methylprednisolone succinate (drug)]] 5 µM | C | TBILA activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.34× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | TBILA activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.77× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -10.2); signed map (7.6, 42.1). **Vector** length 63.5, 9.99% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +2.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TGF-beta induced lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.2 — chr3:112,133,423-112,135,359 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53943) · Entrez [112806053](https://www.ncbi.nlm.nih.gov/gene/112806053) · Ensembl [ENSG00000261488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261488)

## Data

Gene col 15348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15348); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15348]; `tensor/DDL_lfc|DDL_z.npy` [15348]; `embed/gene_vectors.npy` [15348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15348 or target_col == 15348). Every well: [[TBILA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBILA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
