---
symbol: "ABI3BP"
type: "gene"
col: 7782
ensembl_id: "ENSG00000154175"
name: "ABI family member 3 binding protein"
location: "3q12.2"
module: 13
arm: "+"
pooled_cpm: 45.35
n_lines_expressing: 18
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 49
direction_downstream: 49
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ABI3BP

*ABI family member 3 binding protein* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +11.7, q 4e-29, up in 4 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.669× (z -5.5, q 2e-05, down in 5 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZEB2]] (+0.70, fdr 7e-06), [[SEMA5A]] (+0.66, fdr 7e-06), [[GRIN2A]] (+0.65, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 49 go from it, the strongest it → [[TMOD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +11.7 | 4e-29 | 4/16 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +10.9 | 4e-25 | 9/16 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.9 | 1e-16 | 2/14 (CFPAC-1, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +8.2 | 2e-14 | 2/11 (CFPAC-1, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.2 | 8e-08 | 1/12 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +5.7 | 9e-07 | 0/16 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.7 | 9e-07 | 8/16 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 2e-06 | 6/16 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 3/16 (CHP-212, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 12/17 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 0/16 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 11/16 (A549, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.005 | 0/15 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.006 | 9/16 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.013 | 4/16 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.018 | 10/16 (A549, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.034 | 4/16 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.669×** | -5.5 | 2e-05 | 5/16 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -4.5 | 0.002 | 11/16 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.734×** | -4.3 | 0.004 | 7/16 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.744×** | -3.8 | 0.017 | 2/16 (SW 1271, H4) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.023 | 10/16 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.770×** | -3.6 | 0.027 | 7/16 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.771×** | -3.6 | 0.027 | 7/14 (A549, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.772×** | -3.6 | 0.027 | 8/16 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.798× | -3.1 | 0.12 | 8/16 (A-172, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 197 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0393× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 552 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0578× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 21.9 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 59.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 397 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 159 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.235× (z -8.7) |
| [[A-427 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.71 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 317 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.93 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZEB2]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SEMA5A]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2A]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SLC8A1]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PKD1L1-AS1]] | +0.65 | +0.56 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[APBB1IP]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[LINC01435]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[BMPER]] | +0.61 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[P3H2]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MSC-AS1]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PTGFR]] | +0.59 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 2, C 47. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers ABI3BP's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[LINC00536]] | B | LINC00536 activity raises ABI3BP's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without LINC00536 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent |
| [[PTGFR]] | C | PTGFR activity raises ABI3BP's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 4.63× lower at baseline in the lines without PTGFR | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises ABI3BP's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.17× lower at baseline in the lines without C5orf46 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[IRAG2]] | C | IRAG2 activity raises ABI3BP's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 7.56× lower at baseline in the lines without IRAG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises ABI3BP's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.82× lower at baseline in the lines without PDGFRB | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises ABI3BP's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.85× lower at baseline in the lines without ADAMTS6 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises ABI3BP's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 5.09× lower at baseline in the lines without APBB1IP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[LINC01435]] | C | LINC01435 activity raises ABI3BP's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 3.90× lower at baseline in the lines without LINC01435 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865; co-absent with the target |
| [[LINC02968]] | C | LINC02968 activity raises ABI3BP's level | lines that do not express LINC02968 (27) vs lines expressing it (23) | 4.14× lower at baseline in the lines without LINC02968 | 0.008 | ⚠ within organs, on part of the lines; also absent: LCP1, OR9Q1, IL11; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises ABI3BP's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 4.54× lower at baseline in the lines without OR9Q1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises ABI3BP's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.82× lower at baseline in the lines without SIRLNT | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 8, C 41. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMOD1]] | B | ABI3BP activity raises TMOD1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.10× lower at baseline in the lines without ABI3BP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[GSDME]] | B | ABI3BP activity raises GSDME's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.32× lower at baseline in the lines without ABI3BP | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[PAPSS2]] | B | ABI3BP activity raises PAPSS2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.67× lower at baseline in the lines without ABI3BP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[LINC00536]] | B | ABI3BP activity raises LINC00536's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.49× lower at baseline in the lines without ABI3BP | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[SLC41A2]] | B | ABI3BP activity raises SLC41A2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without ABI3BP | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[NR3C1]] | B | ABI3BP activity raises NR3C1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.92× lower at baseline in the lines without ABI3BP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[SLC41A2]] | B | ABI3BP activity weakens SLC41A2's drug response | lines that do not express ABI3BP (30) vs lines expressing it (17) | the lines without ABI3BP respond 1.07× as strongly (z diff -0.06); strongest at Homoharringtonine 0.5 µM: 2.33x vs 1.32x (z diff -4.9) | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[P2RX7]] | B | ABI3BP activity raises P2RX7's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.15× lower at baseline in the lines without ABI3BP | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[OR9Q1]] | C | ABI3BP activity raises OR9Q1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.32× lower at baseline in the lines without ABI3BP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[CA12]] | C | ABI3BP activity raises CA12's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 5.04× lower at baseline in the lines without ABI3BP | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[ADAMTS6]] | C | ABI3BP activity raises ADAMTS6's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.49× lower at baseline in the lines without ABI3BP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[GBP5]] | C | ABI3BP activity raises GBP5's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without ABI3BP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 18.8); signed map (28.9, 46.7). **Vector** length 59.3, 19.3% of its response variance represented; |z| ≥ 3 in 486 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -5.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.6 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ABI family member 3 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,749,156-100,993,515 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NESHBP, DKFZP586L2024, TARSH |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

UniProt [Q7Z7G0](https://www.uniprot.org/uniprotkb/Q7Z7G0) carries no function annotation.

**Summary**, from NCBI Gene [25890](https://www.ncbi.nlm.nih.gov/gene/25890):

> Predicted to enable actin filament binding activity; collagen binding activity; and heparin binding activity. Predicted to be involved in actin cytoskeleton organization; regulation of dendritic spine morphogenesis; and regulation of postsynaptic density assembly. Predicted to act upstream of or within extracellular matrix organization and positive regulation of cell-substrate adhesion. Located in extracellular matrix and obsolete extracellular space. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:17265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17265) · Entrez [25890](https://www.ncbi.nlm.nih.gov/gene/25890) · UniProt [Q7Z7G0](https://www.uniprot.org/uniprotkb/Q7Z7G0) · Ensembl [ENSG00000154175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154175)

## Data

Gene col 7782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7782); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7782]; `tensor/DDL_lfc|DDL_z.npy` [7782]; `embed/gene_vectors.npy` [7782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7782 or target_col == 7782). Every well: [[ABI3BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABI3BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
