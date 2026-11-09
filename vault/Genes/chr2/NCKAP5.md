---
symbol: "NCKAP5"
type: "gene"
col: 10749
ensembl_id: "ENSG00000176771"
name: "NCK associated protein 5"
location: "2q21.2"
module: 19
arm: "+"
pooled_cpm: 75.0
n_lines_expressing: 28
n_dd_up: 8
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 20
direction_downstream: 13
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NCKAP5

*NCK associated protein 5* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +10.0, q 1e-20, up in 10 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +7.0, q 8e-10, up in 12 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.495× (z -10.3, q 6e-22, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK3]] (+0.68, fdr 7e-06), [[BMPER]] (+0.66, fdr 7e-06), [[SLC4A4]] (+0.65, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[WDR72]] → it (grade B ⚠); 13 go from it, the strongest it → [[LINC01483]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.0 | 1e-20 | 10/23 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +7.0 | 8e-10 | 12/26 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.6 | 6e-09 | 7/27 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.8 | 7e-07 | 12/27 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.0 | 7e-05 | 5/23 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.007 | 3/27 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.008 | 6/26 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.037 | 5/26 (COLO 205, H4, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.495×** | -10.3 | 6e-22 | 18/26 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.580×** | -7.9 | 5e-13 | 17/26 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.592×** | -7.6 | 4e-12 | 17/26 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -6.9 | 8e-10 | 19/26 (NCI-H460, SHP-77, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -6.3 | 4e-08 | 23/26 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -5.9 | 3e-07 | 18/26 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.692×** | -5.4 | 7e-06 | 15/26 (SNU-423, A498, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -5.3 | 7e-06 | 22/25 (COLO 205, SHP-77, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -5.1 | 3e-05 | 21/26 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -4.9 | 6e-05 | 18/25 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.716×** | -4.9 | 6e-05 | 14/26 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.716×** | -4.7 | 1e-04 | 11/26 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.798×** | -4.6 | 2e-04 | 14/26 (SNU-423, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.733×** | -4.5 | 2e-04 | 14/26 (SNU-423, A498, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.742×** | -4.3 | 5e-04 | 13/26 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.743×** | -4.3 | 5e-04 | 13/26 (SNU-423, Hs 766T, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.812×** | -4.3 | 6e-04 | 14/27 (Hs 766T, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 293 | 0 | 22 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -26.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.138× (z -16.6) |
| [[SHP-77 (line)]] | alt | 894 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -27.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -20.8) |
| [[COLO 205 (line)]] | alt | 772 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0718× (z -23.3) |
| [[SNU-423 (line)]] | alt | 157 | 0 | 13 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 233 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.0) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -11.0) |
| [[A549 (line)]] | wt | 63.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.3) |
| [[C32 (line)]] | wt | 71.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.330× (z -9.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HEC-1-A (line)]] | alt | 30.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 77.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -9.0) |
| [[SW1417 (line)]] | alt | 32.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.32× (z +14.5) | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0825× (z -8.7) |
| [[HS-578T (line)]] | alt | 71.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -9.5) |
| [[A-172 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 17.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK3]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[BMPER]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SLC4A4]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[COL22A1]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TRPA1]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[COL4A6]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CNTN1]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[F2RL2]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[CDH11]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FRMPD4]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[STEAP1B-AS1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 8, C 12. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR72]] | B | WDR72 activity raises NCKAP5's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without WDR72 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[TSHZ2]] | B | TSHZ2 activity raises NCKAP5's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without TSHZ2 | 0.041 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[SULF1]] | B | SULF1 activity raises NCKAP5's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without SULF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT |
| [[TARID]] | B | TARID activity raises NCKAP5's level | lines that do not express TARID (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TARID | 0.046 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[LSAMP]] | B | LSAMP activity raises NCKAP5's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without LSAMP | 0.049 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[LINC02994]] | B | LINC02994 activity raises NCKAP5's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without LINC02994 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598 |
| [[NR3C1]] | B | NR3C1 activity lowers NCKAP5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[BMPER]] | B | BMPER activity raises NCKAP5's level | lines that do not express BMPER (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without BMPER | 0.096 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises NCKAP5's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 4.44× lower at baseline in the lines without NCKAP5-AS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[UNC5D]] | C | UNC5D activity raises NCKAP5's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.44× lower at baseline in the lines without UNC5D | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises NCKAP5's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.83× lower at baseline in the lines without CDH6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[SPP1]] | C | SPP1 activity raises NCKAP5's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.12× lower at baseline in the lines without SPP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01483]] | B | NCKAP5 activity raises LINC01483's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without NCKAP5 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[TARID]] | B | NCKAP5 activity raises TARID's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without NCKAP5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[HORMAD1]] | B | NCKAP5 activity raises HORMAD1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without NCKAP5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[CNTN1]] | B | NCKAP5 activity raises CNTN1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.06× lower at baseline in the lines without NCKAP5 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[WDR72]] | B | NCKAP5 activity raises WDR72's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without NCKAP5 | 0.061 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[LINC02994]] | B | NCKAP5 activity raises LINC02994's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.33× lower at baseline in the lines without NCKAP5 | 0.066 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[SMOC1]] | B | NCKAP5 activity raises SMOC1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without NCKAP5 | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent |
| [[EYA2]] | C | NCKAP5 activity raises EYA2's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without NCKAP5 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[SETBP1]] | C | NCKAP5 activity raises SETBP1's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 4.94× lower at baseline in the lines without NCKAP5 | 0.043 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[ITIH5]] | C | NCKAP5 activity raises ITIH5's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without NCKAP5 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[UNC5D]] | C | NCKAP5 activity raises UNC5D's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without NCKAP5 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5 activity raises NCKAP5-AS2's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without NCKAP5 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 33.0); signed map (39.5, 44.3). **Vector** length 91.0, 25.1% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.2 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.1 | -4.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.7 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | NCK associated protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.2 — chr2:132,671,788-133,568,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAP5, ERIH1, ERIH2 |
| Matched by | ensembl_id |

UniProt [O14513](https://www.uniprot.org/uniprotkb/O14513) carries no function annotation.

**Summary**, from NCBI Gene [344148](https://www.ncbi.nlm.nih.gov/gene/344148):

> Predicted to be involved in microtubule bundle formation and microtubule depolymerization. Predicted to be active in microtubule plus-end. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29847) · Entrez [344148](https://www.ncbi.nlm.nih.gov/gene/344148) · UniProt [O14513](https://www.uniprot.org/uniprotkb/O14513) · Ensembl [ENSG00000176771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176771)

## Data

Gene col 10749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10749); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10749]; `tensor/DDL_lfc|DDL_z.npy` [10749]; `embed/gene_vectors.npy` [10749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10749 or target_col == 10749). Every well: [[NCKAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCKAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
