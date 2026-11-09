---
symbol: "MIR100HG"
type: "gene"
col: 14929
ensembl_id: "ENSG00000255248"
name: "mir-100-let-7a-2-mir-125b-1 cluster host gene"
location: "11q24.1"
module: 151
arm: "+"
pooled_cpm: 164.46
n_lines_expressing: 30
n_dd_up: 1
n_dd_down: 42
n_dd_up_clean: 1
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 32
direction_downstream: 43
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# MIR100HG

*mir-100-let-7a-2-mir-125b-1 cluster host gene* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +4.1, q 0.024, up in 17 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 5.65×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 6.33×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 4.32×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.291× (z -16.2, q 0e+00, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPSAP52]] (+0.75, fdr 7e-06), [[LINC02454]] (+0.74, fdr 7e-06), [[HTR7]] (+0.68, fdr 7e-06).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); 43 go from it, the strongest it → [[ARSJ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 5.65×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 6.33×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 4.32×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.024 | 17/28 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.43× | +3.3 | 0.25 | 15/28 (Hs 766T, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.291×** | -16.2 | 0e+00 | 28/29 (LOX-IMVI, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.177×** | -16.0 | 0e+00 | 28/28 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.230×** | -13.6 | 7e-40 | 28/28 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.330×** | -10.3 | 2e-22 | 28/28 (LOX-IMVI, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.328×** | -9.3 | 2e-18 | 22/25 (SK-MEL-2, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.301×** | -8.9 | 4e-17 | 25/29 (SK-MEL-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.360×** | -8.5 | 1e-15 | 24/27 (RPMI-7951, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.376×** | -8.2 | 2e-14 | 25/30 (SW48, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.471×** | -7.9 | 2e-13 | 24/30 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -7.6 | 1e-12 | 21/28 (AN3 CA, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.406×** | -7.5 | 3e-12 | 24/27 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.463×** | -6.4 | 6e-09 | 24/28 (SK-MEL-2, SW48, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.569×** | -6.2 | 2e-08 | 25/29 (SK-MEL-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.516×** | -6.1 | 4e-08 | 23/28 (H4, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.594×** | -6.0 | 6e-08 | 24/28 (SK-MEL-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.446×** | -6.0 | 7e-08 | 23/29 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.490×** | -5.9 | 9e-08 | 23/28 (LOX-IMVI, SW48, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.343×** | -5.2 | 7e-06 | 26/28 (SW48, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.8 | 5e-05 | 16/28 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 215 | 0 | 19 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0700× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.123× (z -16.1) |
| [[SW48 (line)]] | wt | 613 | 0 | 17 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -21.2) |
| [[H4 (line)]] | wt | 732 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 308 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 841 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -23.8) |
| [[C32 (line)]] | wt | 129 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -12.4) |
| [[J82 (line)]] | alt | 260 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -18.6) |
| [[SW 900 (line)]] | alt | 290 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -14.3) |
| [[AN3 CA (line)]] | alt | 668 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.0) |
| [[Hs 766T (line)]] | wt | 110 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.287× (z -9.7) |
| [[SW 1271 (line)]] | alt | 502 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0584× (z -13.3) |
| [[A-172 (line)]] | wt | 251 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -12.6) |
| [[CHP-212 (line)]] | wt | 385 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -14.1) |
| [[HOP62 (line)]] | alt | 501 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -13.7) |
| [[PANC-1 (line)]] | alt | 258 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -11.5) |
| [[RKO (line)]] | wt | 102 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 364 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 280 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.218× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 99.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -10.9) |
| [[A498 (line)]] | wt | 79.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 223 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.381× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.263× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.204× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 214 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.9) |
| [[SNU-423 (line)]] | alt | 151 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -11.3) |
| [[HS-578T (line)]] | alt | 640 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -13.4) |
| [[A549 (line)]] | wt | 183 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.32× (z +11.4) | — |
| [[SW 1088 (line)]] | alt | 352 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0568× (z -11.1) |
| [[A-427 (line)]] | wt | 8.88 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 38.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 38.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSAP52]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[HTR7]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[FRMD4A]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[DNMBP]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[IQCJ-SCHIP1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[BACH1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NT5E]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 9, C 23. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises MIR100HG's level | lines that do not express CD59 (7) vs lines expressing it (43) | 4.96× lower at baseline in the lines without CD59 | 0.012 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises MIR100HG's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 4.76× lower at baseline in the lines without UBASH3B | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[TMEM156]] | B | TMEM156 activity raises MIR100HG's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without TMEM156 | 0.034 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[HAS2]] | B | HAS2 activity raises MIR100HG's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 3.60× lower at baseline in the lines without HAS2 | 0.039 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[HMGA2]] | B | HMGA2 activity raises MIR100HG's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 3.64× lower at baseline in the lines without HMGA2 | 0.044 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[MAP2K1]] | B | MAP2K1 activity raises MIR100HG's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.0% of all compounds | 0.048 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANTXR2]] | B | ANTXR2 activity raises MIR100HG's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 4.71× lower at baseline in the lines without ANTXR2 | 0.061 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[NPAS2]] | B | NPAS2 activity raises MIR100HG's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without NPAS2 | 0.068 | ⚠ within organs, on part of the lines |
| [[HRH1]] | B | HRH1 activity raises MIR100HG's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.87× lower at baseline in the lines without HRH1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[LINC02454]] | C | LINC02454 activity raises MIR100HG's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 8.47× lower at baseline in the lines without LINC02454 | 0.003 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises MIR100HG's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 7.14× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[VEGFC]] | C | VEGFC activity raises MIR100HG's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 5.71× lower at baseline in the lines without VEGFC | 0.004 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 21, C 22. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSJ]] | B | MIR100HG activity raises ARSJ's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without MIR100HG | 0.006 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[STX1A]] | B | MIR100HG activity raises STX1A's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without MIR100HG | 0.017 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[CD59]] | B | MIR100HG activity raises CD59's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.36× lower at baseline in the lines without MIR100HG | 0.019 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[SSH1]] | B | MIR100HG activity raises SSH1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without MIR100HG | 0.023 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[TMEM156]] | B | MIR100HG activity raises TMEM156's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.13× lower at baseline in the lines without MIR100HG | 0.025 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[ANTXR2]] | B | MIR100HG activity raises ANTXR2's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without MIR100HG | 0.035 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[RAI14]] | B | MIR100HG activity raises RAI14's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.40× lower at baseline in the lines without MIR100HG | 0.036 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[PRSS23]] | B | MIR100HG activity raises PRSS23's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.41× lower at baseline in the lines without MIR100HG | 0.048 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[RPSAP52]] | B | MIR100HG activity raises RPSAP52's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.83× lower at baseline in the lines without MIR100HG | 0.051 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[MIR222HG]] | B | MIR100HG activity raises MIR222HG's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without MIR100HG | 0.056 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HMGA2]] | B | MIR100HG activity raises HMGA2's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.76× lower at baseline in the lines without MIR100HG | 0.057 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[ABL1]] | B | MIR100HG activity raises ABL1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MIR100HG | 0.057 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.1, 8.7); signed map (12.5, 48.0). **Vector** length 129, 42.1% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.5 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.8 | -7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.1 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.8 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mir-100-let-7a-2-mir-125b-1 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q24.1 — chr11:122,028,325-122,556,721 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AGD1, lncRNA-N2, linc-NeD125 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [399959](https://www.ncbi.nlm.nih.gov/gene/399959):

> This gene produces long non-coding RNAs that act as regulators of cell proliferation. Alternative promoter usage and splicing results in multiple transcript variants. Some transcript variants may promote growth, while others may act to negatively regulate cell division. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:39522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39522) · Entrez [399959](https://www.ncbi.nlm.nih.gov/gene/399959) · Ensembl [ENSG00000255248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255248)

## Data

Gene col 14929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14929); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14929]; `tensor/DDL_lfc|DDL_z.npy` [14929]; `embed/gene_vectors.npy` [14929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14929 or target_col == 14929). Every well: [[MIR100HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR100HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
