---
symbol: "GABBR2"
type: "gene"
col: 5938
ensembl_id: "ENSG00000136928"
name: "gamma-aminobutyric acid type B receptor subunit 2"
location: "9q22.33"
module: 19
arm: "+"
pooled_cpm: 9.82
n_lines_expressing: 25
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GABBR2

*gamma-aminobutyric acid type B receptor subunit 2* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.64× (z +20.2, q 0e+00, up in 10 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0590×, PANC-1 0.162×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.102×, PANC-1 0.145×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0799×; ⚠ cell-cycle shift, explains ~49% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.116×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB4]] (+0.70, fdr 1e-05), [[ESM1]] (+0.67, fdr 8e-06), [[NCKAP5-AS2]] (+0.65, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C2orf72]] → it (grade B ⚠); 6 go from it, the strongest it → [[FIBCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +20.2 | 0e+00 | 10/16 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +14.7 | 0e+00 | 7/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +14.1 | 1e-42 | 2/6 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +8.6 | 1e-15 | 10/17 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +8.5 | 2e-15 | 11/20 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.3 | 3e-11 | 3/6 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.9 | 5e-10 | 4/16 (A549, H4, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.8 | 7e-10 | 7/18 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.2 | 3e-08 | 7/19 (A549, SHP-77, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +6.1 | 8e-08 | 2/18 (SHP-77, HEC-1-A) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.7 | 7e-07 | 5/16 (A549, SHP-77, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.64×** | +5.5 | 2e-06 | 4/21 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.8 | 8e-05 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.4 | 4e-04 | 1/13 (SW480) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.3 | 6e-04 | 1/13 (HEC-1-A) | top dose only | cell-cycle shift (explains ~22% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 0.001 | 4/17 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.015 | 3/19 (SHP-77, SW 900, …) | two highest doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.031 | 2/16 (SW1417, PANC-1) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.032 | 2/20 (A549, A-427) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.037 | 4/21 (C-33 A, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.039 | 1/16 (SHP-77) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +3.0 | 0.060 | 2/15 (C-33 A, SHP-77) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0590×, PANC-1 0.162×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.102×, PANC-1 0.145×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0799×; ⚠ cell-cycle shift, explains ~49% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.719× | -3.5 | 0.13 | 4/19 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.702× | -3.5 | 0.13 | 5/22 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.737× | -3.4 | 0.13 | 6/19 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.19 | 6/19 (NCI-H460, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.759× | -3.1 | 0.19 | 8/20 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.760× | -3.0 | 0.19 | 7/21 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.4 | 0 | 21 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -24.1) |
| [[SHP-77 (line)]] | alt | 62.9 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 4.11 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +8.5) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0825× (z -9.2) |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -18.4) |
| [[SW480 (line)]] | alt | 2.48 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.0) | — |
| [[A549 (line)]] | wt | 2.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0919× (z -8.8) ⚠ transcription drop; unreliable plate only |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB4]] | +0.70 | +0.56 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[ESM1]] | +0.67 | +0.68 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Neuronal System |
| [[PLAC4]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NRCAM]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SPDYE10]] | +0.60 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[CTNND2]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SLC4A11]] | +0.60 | +0.56 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[RTN1]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LINC01257]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DPP10]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf72]] | B | C2orf72 activity lowers GABBR2's level | lines that do not express C2orf72 (6) vs lines expressing it (44) | 1.93× higher at baseline in the lines without C2orf72 | 0.021 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CMBL, TPPP |
| [[ELOVL2]] | B | ELOVL2 activity raises GABBR2's level | lines that do not express ELOVL2 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without ELOVL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, SPP1, LINC03046 |
| [[TTTY14]] | B | TTTY14 activity raises GABBR2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without TTTY14 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[TOP2A]] | B | TOP2A activity lowers GABBR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NCKAP5-AS2]] | B | NCKAP5-AS2 activity raises GABBR2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without NCKAP5-AS2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D |
| [[KCNE4]] | B | KCNE4 activity raises GABBR2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without KCNE4 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[LIN7A]] | C | LIN7A activity raises GABBR2's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without LIN7A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIBCD1]] | B | GABBR2 activity raises FIBCD1's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without GABBR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| [[DOK1]] | B | GABBR2 activity raises DOK1's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 1.32× lower at baseline in the lines without GABBR2 | 0.060 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | GABBR2 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express GABBR2 (25) vs lines expressing it (23) | the lines without GABBR2: 1.15× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | GABBR2 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express GABBR2 (25) vs lines expressing it (23) | the lines without GABBR2: 0.89× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| [[EDARADD]] | C | GABBR2 activity raises EDARADD's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without GABBR2 | 0.026 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent; co-absent with the target |
| [[KCNQ5]] | C | GABBR2 activity raises KCNQ5's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 4.02× lower at baseline in the lines without GABBR2 | 0.056 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 36.8); signed map (42.7, 45.8). **Vector** length 52.4, 12.6% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +4.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type B receptor subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,288,109-98,708,935 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HG20, GABABR2, GPRC3B; previously GPR51 |
| Gene groups (HGNC) | Gamma-aminobutyric acid type B receptor subunits |
| Reactome | 16 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); Activation of G protein gated Potassium channels; G protein gated Potassium channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O75899](https://www.uniprot.org/uniprotkb/O75899) (Gamma-aminobutyric acid type B receptor subunit 2):

> Component of a heterodimeric G protein-coupled receptor for GABA, formed by GABBR1 and GABBR2. Within the heterodimeric GABA receptor, only GABBR1 seems to bind agonists, while GABBR2 mediates coupling to G proteins. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors, such as adenylate cyclase. Signaling inhibits adenylate cyclase, stimulates phospholipase A2, activates …

**Summary**, from NCBI Gene [9568](https://www.ncbi.nlm.nih.gov/gene/9568):

> The multi-pass membrane protein encoded by this gene belongs to the G-protein coupled receptor 3 family and GABA-B receptor subfamily. The GABA-B receptors inhibit neuronal activity through G protein-coupled second-messenger systems, which regulate the release of neurotransmitters, and the activity of ion channels and adenylyl cyclase. This receptor subunit forms an active heterodimeric complex with GABA-B receptor subunit 1, neither of which is effective on its own. Allelic variants of this …

**Accessions** — [HGNC:4507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4507) · Entrez [9568](https://www.ncbi.nlm.nih.gov/gene/9568) · UniProt [O75899](https://www.uniprot.org/uniprotkb/O75899) · Ensembl [ENSG00000136928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136928)

## Data

Gene col 5938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5938); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5938]; `tensor/DDL_lfc|DDL_z.npy` [5938]; `embed/gene_vectors.npy` [5938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5938 or target_col == 5938). Every well: [[GABBR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABBR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
