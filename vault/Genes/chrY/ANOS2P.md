---
symbol: "ANOS2P"
type: "gene"
col: 14290
ensembl_id: "ENSG00000241859"
name: "anosmin 2, pseudogene"
location: "Yq11.221"
module: 61
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 18
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ANOS2P

*anosmin 2, pseudogene* — Yq11.221

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.61× (z +12.6, q 8e-34, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +9.6, q 7e-20, up in 8 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.201×, HCT15 0.222×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HCT15 0.192×, LoVo 0.214×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.244×; ⚠ cell-cycle shift, explains ~31% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.221×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO2B1]] (+0.65, fdr 2e-05), [[CLIC2]] (+0.63, fdr 5e-05), [[DNAH6]] (+0.60, fdr 2e-05); moves opposite to [[CA5B]] (-0.55, fdr 5e-05), [[FBXW2]] (-0.53, fdr 4e-04), [[STRAP]] (-0.52, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKS1B]] → it (grade B ⚠); 4 go from it, the strongest it → [[PLXNC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.61×** | +12.6 | 8e-34 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +9.9 | 1e-20 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.61×** | +9.8 | 2e-20 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +9.6 | 7e-20 | 8/9 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +8.4 | 6e-15 | 5/7 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.00×** | +6.0 | 2e-07 | 1/3 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +5.5 | 3e-06 | 5/14 (A-427, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +4.8 | 1e-04 | 5/7 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.2 | 0.002 | 1/6 (J82) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.002 | 6/10 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.002 | 0/11 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.002 | 3/8 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.0 | 0.002 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +3.9 | 0.003 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.003 | 1/14 (NCI-H460) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +3.4 | 0.021 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +3.3 | 0.030 | 0/7 | all doses, flat | low cells (technical?); position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.66×** | +3.2 | 0.033 | 0/6 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.035 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.65×** | +3.2 | 0.035 | 1/6 (NCI-H460) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.036 | 5/11 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.039 | 0/11 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.056 | 7/12 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.201×, HCT15 0.222×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HCT15 0.192×, LoVo 0.214×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.244×; ⚠ cell-cycle shift, explains ~31% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HCT15 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 0.5 µM |  | 0.624× | -3.5 | 0.24 | 1/11 (HCT15) | inconsistent across doses | position effect removed |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.738× | -3.3 | 0.24 | 1/14 (SK-MEL-2) | top dose only |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.672× | -3.1 | 0.31 | 2/13 (C32, HCT15) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.657× | -3.1 | 0.31 | 1/13 (SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 47.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.221× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 1.58 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +9.4) | — |
| [[J82 (line)]] | alt | 5.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +10.2) | — |
| [[A-172 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.667 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.271 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO2B1]] | +0.65 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[CLIC2]] | +0.63 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[DNAH6]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[KCNMB2-AS1]] | +0.59 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ELAVL2]] | +0.59 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PATL2]] | +0.58 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[FRG1-DT]] | +0.58 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[LINC01933]] | +0.58 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[GRIA4]] | +0.58 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[TRIP6]] | +0.56 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[PLXNC1]] | +0.56 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[CHODL]] | +0.56 | +0.58 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA5B]] | -0.55 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[FBXW2]] | -0.53 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[STRAP]] | -0.52 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[NOMO2]] | -0.52 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[MFN1]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[NOMO3]] | -0.51 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[MSTO2P]] | -0.50 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[DCUN1D2]] | -0.50 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[RNF41]] | -0.50 | -0.41 / -0.23 | both halves | 5e-04 |  |
| [[GPR89A]] | -0.49 | -0.53 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS1B]] | B | ANKS1B activity raises ANOS2P's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without ANKS1B | 0.026 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[TOP2A]] | B | TOP2A activity lowers ANOS2P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EIF1AY]] | C | EIF1AY activity raises ANOS2P's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 3.37× lower at baseline in the lines without EIF1AY | 1e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNC1]] | B | ANOS2P activity raises PLXNC1's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without ANOS2P | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |
| [[MYO16]] | B | ANOS2P activity raises MYO16's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without ANOS2P | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |
| [[RBMS3-AS3]] | B | ANOS2P activity raises RBMS3-AS3's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without ANOS2P | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D |
| [[EIF1AY]] | C | ANOS2P activity raises EIF1AY's level | lines that do not express ANOS2P (32) vs lines expressing it (18) | 11.24× lower at baseline in the lines without ANOS2P | 5e-07 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: UTY, EIF1AY, KDM5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 25.7); signed map (40.6, 20.0). **Vector** length 24.0, 4.56% of its response variance represented; |z| ≥ 3 in 314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | -1.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.4 | -3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.4 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | anosmin 2, pseudogene |
| Locus type | pseudogene |
| Location | Yq11.221 — chrY:13,751,656-13,915,824 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | KAL-Y; previously ADMLY, KALP |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:6214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6214) · Entrez [3734](https://www.ncbi.nlm.nih.gov/gene/3734) · Ensembl [ENSG00000241859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241859)

## Data

Gene col 14290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14290); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14290]; `tensor/DDL_lfc|DDL_z.npy` [14290]; `embed/gene_vectors.npy` [14290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14290 or target_col == 14290). Every well: [[ANOS2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANOS2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
