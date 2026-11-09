---
symbol: "GDNF"
type: "gene"
col: 9677
ensembl_id: "ENSG00000168621"
name: "glial cell derived neurotrophic factor"
location: "5p13.2"
module: 13
arm: "+"
pooled_cpm: 7.27
n_lines_expressing: 12
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 39
direction_downstream: 52
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GDNF

*glial cell derived neurotrophic factor* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.37× (z +15.3, q 0e+00, up in 5 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 0.0189×, C32 0.0464×, hTERT-HPNE 0.0470×; ⚠ toxic; transcription drop); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (HOP62 0.0199×, HS-578T 0.119×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0771×, HS-578T 0.0850×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0676×, C32 0.0990×); [[Budesonide (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 0.0648×, HOP62 0.0976×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDNF-AS1]] (+0.82, fdr 7e-06, ⚠ same locus), [[GPR68]] (+0.77, fdr 7e-06), [[INSYN2B]] (+0.75, fdr 7e-06), [[SAMD3]] (+0.71, fdr 1e-05); moves opposite to [[TMTC1]] (-0.50, fdr 4e-05), [[CMKLR2]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 52 go from it, the strongest it → [[LRIG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.37×** | +15.3 | 0e+00 | 5/8 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +7.7 | 3e-12 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +7.6 | 7e-12 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +7.0 | 3e-10 | 1/8 (J82) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +6.7 | 2e-09 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +5.0 | 6e-05 | 5/9 (hTERT-HPNE, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.9 | 1e-04 | 3/9 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +4.6 | 3e-04 | 2/8 (HepG2/C3A, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +4.2 | 0.002 | 5/9 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.1 | 0.002 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.002 | 0/9 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.002 | 4/9 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.9 | 0.004 | 2/8 (HepG2/C3A, J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +3.7 | 0.007 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.016 | 4/9 (SNU-423, HepG2/C3A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.96×** | +3.5 | 0.016 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9677.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 0.0189×, C32 0.0464×, hTERT-HPNE 0.0470×; ⚠ toxic; transcription drop); [[Clobetasol propionate (drug)]] 5 µM in 2 lines (HOP62 0.0199×, HS-578T 0.119×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.0771×, HS-578T 0.0850×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0676×, C32 0.0990×); [[Budesonide (drug)]] 0.5 µM in 2 lines (hTERT-HPNE 0.0648×, HOP62 0.0976×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.598× | -3.5 | 0.13 | 0/9 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.623× | -3.5 | 0.13 | 0/9 | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.610× | -3.4 | 0.13 | 0/9 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.645× | -3.3 | 0.16 | 4/9 (HOP62, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.646× | -3.0 | 0.26 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 51.2 | 0 | 23 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0189× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.127× (z -16.5) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 20 (7 ⚠) | — | [[Clobetasol propionate (drug)]] 5 µM 0.0199× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0470× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 0.5 µM 0.0648× (z -12.7) |
| [[RPMI-7951 (line)]] | alt | 48.8 | 0 | 8 (2 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.129× (z -10.7) |
| [[C32 (line)]] | wt | 173 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0464× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0990× (z -14.4) |
| [[A-172 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.548 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.523 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDNF-AS1]] | +0.82 | +0.84 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GPR68]] | +0.77 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.75 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[SYNDIG1]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[LINC01411]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[IL1B]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 | STRING 582 |
| [[TMEM200A]] | +0.66 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NTNG2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[IL11]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TSHZ3]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC1]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CMKLR2]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 3, C 36. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GDNF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RPSAP52]] | B | RPSAP52 activity raises GDNF's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without RPSAP52 | 0.097 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[CYGB]] | B | CYGB activity raises GDNF's level | lines that do not express CYGB (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without CYGB | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[ITIH5]] | C | ITIH5 activity raises GDNF's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 6.89× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises GDNF's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 2.47× lower at baseline in the lines without DIRAS3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises GDNF's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.35× lower at baseline in the lines without SPOCK1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises GDNF's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.94× lower at baseline in the lines without SEMA5A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises GDNF's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 7.41× lower at baseline in the lines without FCRLA | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises GDNF's level | lines that do not express BAALC (32) vs lines expressing it (18) | 3.94× lower at baseline in the lines without BAALC | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[THBS2]] | C | THBS2 activity raises GDNF's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 4.09× lower at baseline in the lines without THBS2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises GDNF's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.43× lower at baseline in the lines without COL15A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises GDNF's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.84× lower at baseline in the lines without VEPH1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |

### Downstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 11, C 41. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRIG1]] | B | GDNF activity raises LRIG1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.76× lower at baseline in the lines without GDNF | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[ITPR1]] | B | GDNF activity raises ITPR1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.49× lower at baseline in the lines without GDNF | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[CD82]] | B | GDNF activity raises CD82's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.46× lower at baseline in the lines without GDNF | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[ZCCHC24]] | B | GDNF activity raises ZCCHC24's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.59× lower at baseline in the lines without GDNF | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[TMEM158]] | B | GDNF activity raises TMEM158's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.01× lower at baseline in the lines without GDNF | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[CYGB]] | B | GDNF activity raises CYGB's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without GDNF | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[RPSAP52]] | B | GDNF activity raises RPSAP52's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without GDNF | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[SETBP1]] | B | GDNF activity raises SETBP1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.12× lower at baseline in the lines without GDNF | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[LINC01119]] | B | GDNF activity raises LINC01119's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.04× lower at baseline in the lines without GDNF | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[SYNJ2]] | B | GDNF activity raises SYNJ2's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.10× lower at baseline in the lines without GDNF | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[BOC]] | B | GDNF activity raises BOC's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.01× lower at baseline in the lines without GDNF | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[COL5A3]] | C | GDNF activity raises COL5A3's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.69× lower at baseline in the lines without GDNF | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 14.2); signed map (19.9, 48.0). **Vector** length 63.9, 25.8% of its response variance represented; |z| ≥ 3 in 427 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.0 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glial cell derived neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:37,812,677-37,840,041 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATF1, ATF2, HFB1-GDNF |
| Gene groups (HGNC) | GDNF family ligands |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 10 pathways, smallest: Formation of the ureteric bud; NCAM1 interactions; RET signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P39905](https://www.uniprot.org/uniprotkb/P39905) (Glial cell line-derived neurotrophic factor):

> Neurotrophic factor that enhances survival and morphological differentiation of dopaminergic neurons and increases their high-affinity dopamine uptake. Acts by binding to its coreceptor, GFRA1, leading to autophosphorylation and activation of the RET receptor. Involved in the development of the neural crest.

**Summary**, from NCBI Gene [2668](https://www.ncbi.nlm.nih.gov/gene/2668):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. The recombinant form of this protein, a highly conserved neurotrophic factor, was shown to promote the survival …

**Accessions** — [HGNC:4232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4232) · Entrez [2668](https://www.ncbi.nlm.nih.gov/gene/2668) · UniProt [P39905](https://www.uniprot.org/uniprotkb/P39905) · Ensembl [ENSG00000168621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168621)

## Data

Gene col 9677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9677); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9677]; `tensor/DDL_lfc|DDL_z.npy` [9677]; `embed/gene_vectors.npy` [9677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9677 or target_col == 9677). Every well: [[GDNF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDNF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
