---
symbol: "SGIP1"
type: "gene"
col: 3991
ensembl_id: "ENSG00000118473"
name: "SH3GL interacting endocytic adaptor 1"
location: "1p31.3"
module: 19
arm: "+"
pooled_cpm: 59.51
n_lines_expressing: 19
n_dd_up: 6
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 22
direction_downstream: 26
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SGIP1

*SH3GL interacting endocytic adaptor 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +6.5, q 4e-08, up in 1 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +4.1, q 0.005, up in 1 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -7.5, q 5e-11, down in 16 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STC1]] (+0.75, fdr 7e-06), [[GRAMD1B]] (+0.74, fdr 7e-06), [[TCF4]] (+0.65, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 26 go from it, the strongest it → [[ITPR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.5 | 4e-08 | 1/18 (AN3 CA) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.2 | 6e-05 | 1/15 (H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.5 | 0.001 | 1/13 (C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.005 | 1/18 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.017 | 0/17 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.017 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.39× | +3.2 | 0.11 | 2/17 (NCI-H460, HOP62) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.38× | +3.1 | 0.11 | 5/16 (CHP-212, NCI-H460, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.11 | 4/17 (HOP62, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -7.5 | 5e-11 | 16/16 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -7.3 | 6e-11 | 14/16 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -7.0 | 4e-10 | 14/16 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.491×** | -6.4 | 2e-08 | 12/17 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.639×** | -6.1 | 1e-07 | 11/17 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.537×** | -6.1 | 1e-07 | 11/17 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.562×** | -5.6 | 2e-06 | 11/17 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.567×** | -5.5 | 2e-06 | 10/17 (RKO, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -5.4 | 3e-06 | 14/17 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.616×** | -4.6 | 2e-04 | 12/19 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.652×** | -4.2 | 0.001 | 6/17 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.001 | 13/17 (NCI-H460, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.571×** | -3.9 | 0.004 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.007 | 8/17 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.694×** | -3.6 | 0.014 | 6/17 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.697×** | -3.5 | 0.016 | 11/16 (NCI-H460, RKO, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.678×** | -3.5 | 0.016 | 7/16 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.019 | 13/18 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.026 | 12/17 (NCI-H23, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 154 | 0 | 34 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -30.5) |
| [[NCI-H460 (line)]] | wt | 44.6 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -18.7) |
| [[RKO (line)]] | wt | 109 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 1,124 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0550× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0955× (z -16.6) |
| [[SHP-77 (line)]] | alt | 1,267 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -23.0) |
| [[HS-578T (line)]] | alt | 171 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 61.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -17.6) |
| [[PANC-1 (line)]] | alt | 62.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -19.3) |
| [[CHP-212 (line)]] | wt | 74.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -8.9) |
| [[HOP62 (line)]] | alt | 43.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.219× (z -9.7) |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.5) |
| [[A-172 (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STC1]] | +0.75 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD1B]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TCF4]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SCUBE1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CRLF2]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[PDE3A]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BMPER]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PAEP]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SPOCK1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 2, C 20. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SGIP1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[ITPR1]] | B | ITPR1 activity raises SGIP1's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 3.29× lower at baseline in the lines without ITPR1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[HGF]] | C | HGF activity raises SGIP1's level | lines that do not express HGF (38) vs lines expressing it (12) | 9.33× lower at baseline in the lines without HGF | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[GAP43]] | C | GAP43 activity raises SGIP1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 4.10× lower at baseline in the lines without GAP43 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[TRPA1]] | C | TRPA1 activity raises SGIP1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 5.01× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises SGIP1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without SPOCK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises SGIP1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.96× lower at baseline in the lines without ITGA11 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises SGIP1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 4.63× lower at baseline in the lines without PDE3A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises SGIP1's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.37× lower at baseline in the lines without TCF4 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[SYNDIG1]] | C | SYNDIG1 activity raises SGIP1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.96× lower at baseline in the lines without SYNDIG1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises SGIP1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.80× lower at baseline in the lines without CDH13 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises SGIP1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.88× lower at baseline in the lines without RGS4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 9, C 17. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR1]] | B | SGIP1 activity raises ITPR1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without SGIP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[CHD1L]] | B | SGIP1 activity raises CHD1L's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without SGIP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[ELL2]] | B | SGIP1 activity raises ELL2's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without SGIP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[SETBP1]] | B | SGIP1 activity raises SETBP1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without SGIP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[SHANK1]] | B | SGIP1 activity raises SHANK1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without SGIP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[LRRC8C]] | B | SGIP1 activity raises LRRC8C's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without SGIP1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[TRIM9]] | B | SGIP1 activity raises TRIM9's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without SGIP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[CLEC11A]] | B | SGIP1 activity weakens CLEC11A's drug response | lines that do not express SGIP1 (16) vs lines expressing it (9) | the lines without SGIP1 respond 1.18× as strongly (z diff -0.26); rises at some drug-doses, falls at others (51% from rises): Panobinostat 0.5 µM: 2.18x vs 1.07x (z diff -2.5); Topotecan (hydrochloride) 5 µM: 1.64x vs 0.88x (z diff -2.3); Rutin (trihydrate) 0.05 µM: 0.59x vs 0.89x (z diff -1.3) | 0.090 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[MAML3]] | B | SGIP1 activity raises MAML3's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without SGIP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[HGF]] | C | SGIP1 activity raises HGF's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 4.02× lower at baseline in the lines without SGIP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[LAMA1]] | C | SGIP1 activity raises LAMA1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without SGIP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[TRPA1]] | C | SGIP1 activity raises TRPA1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without SGIP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 16.6); signed map (20.1, 52.7). **Vector** length 89.5, 29.3% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -1.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.2 | -6.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.9 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | SH3GL interacting endocytic adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:66,533,267-66,751,139 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761D221 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQI5](https://www.uniprot.org/uniprotkb/Q9BQI5) (SH3-containing GRB2-like protein 3-interacting protein 1):

> May function in clathrin-mediated endocytosis. Has both a membrane binding/tubulating activity and the ability to recruit proteins essential to the formation of functional clathrin-coated pits. Has a preference for membranes enriched in phosphatidylserine and phosphoinositides and is required for the endocytosis of the transferrin receptor. May also bind tubulin. May play a role in the regulation of energy homeostasis.

**Summary**, from NCBI Gene [84251](https://www.ncbi.nlm.nih.gov/gene/84251):

> SGIP1 functions as an endocytic protein that affects signaling by receptors in neuronal systems involved in energy homeostasis via its interaction with endophilins (see SH3GL3; MIM 603362) (Trevaskis et al., 2005 [PubMed 15919751] and Uezu et al., 2007 [PubMed 17626015]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25412) · Entrez [84251](https://www.ncbi.nlm.nih.gov/gene/84251) · UniProt [Q9BQI5](https://www.uniprot.org/uniprotkb/Q9BQI5) · Ensembl [ENSG00000118473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118473)

## Data

Gene col 3991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3991); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3991]; `tensor/DDL_lfc|DDL_z.npy` [3991]; `embed/gene_vectors.npy` [3991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3991 or target_col == 3991). Every well: [[SGIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
