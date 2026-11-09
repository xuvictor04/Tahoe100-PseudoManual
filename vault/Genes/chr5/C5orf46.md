---
symbol: "C5orf46"
type: "gene"
col: 10960
ensembl_id: "ENSG00000178776"
name: "chromosome 5 open reading frame 46"
location: "5q32"
module: 19
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 27
direction_downstream: 50
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# C5orf46

*chromosome 5 open reading frame 46* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.02× (z +9.7, q 1e-19, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.71× (z +4.1, q 0.004, up in 2 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0384×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.157×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIRLNT]] (+0.78, fdr 7e-06), [[BMPER]] (+0.69, fdr 7e-06), [[TNFRSF11B]] (+0.69, fdr 7e-06); moves opposite to [[ZMYND8]] (-0.47, fdr 5e-05), [[FOXC2]] (-0.46, fdr 6e-05), [[CCND3]] (-0.46, fdr 4e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[ABI3BP]] → it (grade C ⚠); 50 go from it, the strongest it → [[PALLD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.02×** | +9.7 | 1e-19 | 3/6 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.81×** | +9.2 | 1e-17 | 2/4 (SNU-423, NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.43×** | +8.6 | 2e-15 | 3/4 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.99×** | +4.2 | 0.003 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.2 | 0.004 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.004 | 2/13 (SNU-423, A498) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.8 | 0.012 | 1/8 (Hs 766T) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +3.7 | 0.013 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.46×** | +3.5 | 0.027 | 1/3 (A498) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +3.5 | 0.031 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.3 | 0.045 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.83×** | +3.3 | 0.049 | 4/10 (A498, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +3.2 | 0.055 | 1/6 (Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.055 | 5/13 (A498, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.055 | 1/12 (NCI-H460) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.74×** | +3.0 | 0.089 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.096 | 5/10 (NCI-H460, H4, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10960.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0384×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.114×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.157×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.543× | -3.3 | 0.41 | 6/12 (A498, NCI-H460, …) | rises with dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.512× | -3.1 | 0.41 | 0/13 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.570× | -3.1 | 0.41 | 8/13 (NCI-H460, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0384× (z -22.4) |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.158 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.744 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.841 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.201 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | +0.78 | +0.76 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[BMPER]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TNFRSF11B]] | +0.69 | +0.60 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[P3H2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[COL8A1]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[COL4A6]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.59 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[LYPLAL1-DT]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SULF1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ABI3BP]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GJA1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND8]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[FOXC2]] | -0.46 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CCND3]] | -0.46 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ITGA10]] | -0.45 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[BDH1]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABI3BP]] | C | ABI3BP activity raises C5orf46's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without ABI3BP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[PTN]] | C | PTN activity raises C5orf46's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without PTN | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises C5orf46's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without KCNE4 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises C5orf46's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.61× lower at baseline in the lines without ZNF736P9Y | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises C5orf46's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without PDCD1LG2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises C5orf46's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without ADAMTS6 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises C5orf46's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.31× lower at baseline in the lines without SIRLNT | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[CHSY3]] | C | CHSY3 activity raises C5orf46's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.95× lower at baseline in the lines without CHSY3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises C5orf46's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 1.97× lower at baseline in the lines without TNFRSF11B | 0.044 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises C5orf46's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without ALPK2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[NID2]] | C | NID2 activity raises C5orf46's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without NID2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises C5orf46's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.10× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 2, C 48. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PALLD]] | B | C5orf46 activity raises PALLD's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.93× lower at baseline in the lines without C5orf46 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN |
| [[SLCO1C1]] | B | C5orf46 activity raises SLCO1C1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.94× lower at baseline in the lines without C5orf46 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN |
| [[NID2]] | C | C5orf46 activity raises NID2's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.69× lower at baseline in the lines without C5orf46 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[LINC01411]] | C | C5orf46 activity raises LINC01411's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 9.25× lower at baseline in the lines without C5orf46 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[TIMP3]] | C | C5orf46 activity raises TIMP3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 7.22× lower at baseline in the lines without C5orf46 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[ABI3BP]] | C | C5orf46 activity raises ABI3BP's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.17× lower at baseline in the lines without C5orf46 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CHSY3]] | C | C5orf46 activity raises CHSY3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without C5orf46 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[FSTL1]] | C | C5orf46 activity raises FSTL1's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.97× lower at baseline in the lines without C5orf46 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[ADAMTS6]] | C | C5orf46 activity raises ADAMTS6's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.16× lower at baseline in the lines without C5orf46 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[ADAMTS16]] | C | C5orf46 activity raises ADAMTS16's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.17× lower at baseline in the lines without C5orf46 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CACNA2D3]] | C | C5orf46 activity raises CACNA2D3's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.25× lower at baseline in the lines without C5orf46 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[COL4A6]] | C | C5orf46 activity raises COL4A6's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without C5orf46 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 32.8); signed map (39.4, 44.2). **Vector** length 43.3, 15.4% of its response variance represented; |z| ≥ 3 in 322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 5 open reading frame 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:147,880,726-147,906,538 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23985, SSSP1, AP-64 |
| Matched by | ensembl_id |

UniProt [Q6UWT4](https://www.uniprot.org/uniprotkb/Q6UWT4) carries no function annotation.

**Summary**, from NCBI Gene [389336](https://www.ncbi.nlm.nih.gov/gene/389336):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33768) · Entrez [389336](https://www.ncbi.nlm.nih.gov/gene/389336) · UniProt [Q6UWT4](https://www.uniprot.org/uniprotkb/Q6UWT4) · Ensembl [ENSG00000178776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178776)

## Data

Gene col 10960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10960); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10960]; `tensor/DDL_lfc|DDL_z.npy` [10960]; `embed/gene_vectors.npy` [10960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10960 or target_col == 10960). Every well: [[C5orf46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C5orf46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
