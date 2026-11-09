---
symbol: "COL8A1"
type: "gene"
col: 6930
ensembl_id: "ENSG00000144810"
name: "collagen type VIII alpha 1 chain"
location: "3q12.1"
module: 19
arm: "+"
pooled_cpm: 108.96
n_lines_expressing: 19
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 23
direction_downstream: 22
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# COL8A1

*collagen type VIII alpha 1 chain* — 3q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +13.6, q 4e-39, up in 9 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +4.8, q 2e-04, up in 11 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.652× (z -6.5, q 6e-08, down in 12 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDC2]] (+0.65, fdr 7e-06), [[C5orf46]] (+0.62, fdr 7e-06), [[TRPA1]] (+0.60, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 22 go from it, the strongest it → [[TET1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.53×** | +13.6 | 4e-39 | 9/18 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.7 | 8e-20 | 8/16 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +7.4 | 2e-11 | 5/16 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.8 | 2e-04 | 11/17 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.011 | 11/18 (RPMI-7951, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.026 | 6/17 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.028 | 5/18 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6930.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.652×** | -6.5 | 6e-08 | 12/17 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -5.7 | 3e-06 | 10/17 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.611×** | -5.1 | 7e-05 | 12/17 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -5.0 | 1e-04 | 14/17 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -4.3 | 0.002 | 13/17 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -4.1 | 0.004 | 5/17 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -4.0 | 0.005 | 16/17 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -3.6 | 0.021 | 13/17 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -3.6 | 0.021 | 9/17 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.717×** | -3.6 | 0.022 | 1/16 (HS-578T) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.726×** | -3.4 | 0.031 | 3/16 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.031 | 10/17 (A-172, H4, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.650×** | -3.1 | 0.078 | 2/17 (A498, A-172) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 961 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0729× (z -23.8) |
| [[A-172 (line)]] | wt | 765 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.1) |
| [[SW480 (line)]] | alt | 71.7 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -13.0) |
| [[A498 (line)]] | wt | 99.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.2) |
| [[SNU-423 (line)]] | alt | 367 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.242× (z -10.5) |
| [[C32 (line)]] | wt | 83.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 403 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 80.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.0) |
| [[H4 (line)]] | wt | 73.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.7) |
| [[A-427 (line)]] | wt | 6.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.36 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 161 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC2]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[C5orf46]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TRPA1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[COL5A2]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 647 |
| [[P3H2]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Collagen biosynthesis and modifying enzymes; STRING 631 |
| [[SEMA3D]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TGFBI]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CACNA2D3]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[IGFBP7]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FBN1]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix; STRING 586 |
| [[KCNE4]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ELOVL2]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 1, C 22. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity lowers COL8A1's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[GREM2]] | C | GREM2 activity raises COL8A1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 6.93× lower at baseline in the lines without GREM2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[FN1]] | C | FN1 activity raises COL8A1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.96× lower at baseline in the lines without FN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises COL8A1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.97× lower at baseline in the lines without FBN1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises COL8A1's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 5.69× lower at baseline in the lines without KCNE4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[IL6]] | C | IL6 activity raises COL8A1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 5.80× lower at baseline in the lines without IL6 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises COL8A1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 4.91× lower at baseline in the lines without IGFBP7 | 0.019 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises COL8A1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 4.44× lower at baseline in the lines without COL1A2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises COL8A1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.65× lower at baseline in the lines without COL3A1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises COL8A1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without LOXL3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises COL8A1's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.82× lower at baseline in the lines without LINC01583 | 0.032 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises COL8A1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.10× lower at baseline in the lines without ABI3BP | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 1, C 21. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TET1]] | B | COL8A1 activity raises TET1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without COL8A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1 |
| [[IL6]] | C | COL8A1 activity raises IL6's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 9.53× lower at baseline in the lines without COL8A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[IGFBP7]] | C | COL8A1 activity raises IGFBP7's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 8.20× lower at baseline in the lines without COL8A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[FN1]] | C | COL8A1 activity raises FN1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 7.46× lower at baseline in the lines without COL8A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[EDIL3]] | C | COL8A1 activity raises EDIL3's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 7.16× lower at baseline in the lines without COL8A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[NID2]] | C | COL8A1 activity raises NID2's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without COL8A1 | 0.022 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[COL1A2]] | C | COL8A1 activity raises COL1A2's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 6.34× lower at baseline in the lines without COL8A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[FBN1]] | C | COL8A1 activity raises FBN1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 5.16× lower at baseline in the lines without COL8A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[HMCN1]] | C | COL8A1 activity raises HMCN1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 4.00× lower at baseline in the lines without COL8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[PRRX1]] | C | COL8A1 activity raises PRRX1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 4.00× lower at baseline in the lines without COL8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[EFEMP1]] | C | COL8A1 activity raises EFEMP1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without COL8A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[COL1A1]] | C | COL8A1 activity raises COL1A1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 5.14× lower at baseline in the lines without COL8A1 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 32.6); signed map (39.0, 44.4). **Vector** length 72.1, 25.5% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | collagen type VIII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.1 — chr3:99,638,475-99,799,226 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9568; previously C3orf7 |
| Gene groups (HGNC) | C1q domain containing; Network forming collagens |
| Reactome | 8 pathways, smallest: Collagen chain trimerization; Collagen degradation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [P27658](https://www.uniprot.org/uniprotkb/P27658) (Collagen alpha-1(VIII) chain):

> Macromolecular component of the subendothelium. Major component of the Descemet's membrane (basement membrane) of corneal endothelial cells. Also a component of the endothelia of blood vessels. Necessary for migration and proliferation of vascular smooth muscle cells and thus, has a potential role in the maintenance of vessel wall integrity and structure, in particular in atherogenesis.; Vastatin, the C-terminal fragment comprising the NC1 domain, inhibits aortic endothelial cell proliferation …

**Summary**, from NCBI Gene [1295](https://www.ncbi.nlm.nih.gov/gene/1295):

> This gene encodes one of the two alpha chains of type VIII collagen. The gene product is a short chain collagen and a major component of the basement membrane of the corneal endothelium. The type VIII collagen fibril can be either a homo- or a heterotrimer. Alternatively spliced transcript variants encoding the same protein have been observed. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:2215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2215) · Entrez [1295](https://www.ncbi.nlm.nih.gov/gene/1295) · UniProt [P27658](https://www.uniprot.org/uniprotkb/P27658) · Ensembl [ENSG00000144810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144810)

## Data

Gene col 6930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6930); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6930]; `tensor/DDL_lfc|DDL_z.npy` [6930]; `embed/gene_vectors.npy` [6930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6930 or target_col == 6930). Every well: [[COL8A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL8A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
