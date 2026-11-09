---
symbol: "C21orf91-OT1"
type: "gene"
col: 14248
ensembl_id: "ENSG00000240770"
name: "C21orf91 overlapping transcript 1"
location: "21q21.1"
module: 39
arm: "+"
pooled_cpm: 3.57
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# C21orf91-OT1

*C21orf91 overlapping transcript 1* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.68× (z +20.4, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.430× (z -7.0, q 1e-09, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.83, fdr 7e-06), [[HCLS1]] (+0.81, fdr 7e-06), [[USP50]] (+0.80, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[XG]] → it (grade B ⚠); 17 go from it, the strongest it → [[GSTA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.68×** | +20.4 | 0e+00 | 35/35 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.14×** | +16.6 | 0e+00 | 32/39 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +10.1 | 1e-21 | 29/35 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.87×** | +8.7 | 4e-16 | 38/43 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +8.6 | 8e-16 | 28/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +7.7 | 1e-12 | 24/36 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.63×** | +7.5 | 4e-12 | 28/41 (SW480, A-427, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +6.3 | 2e-08 | 23/42 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.1 | 2e-05 | 14/42 (HOP62, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.48×** | +4.6 | 3e-04 | 18/43 (SNU-1, NCI-H2347, …) | rises with dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.4 | 5e-04 | 12/42 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.0 | 0.003 | 1/4 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.006 | 10/40 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **2.41×** | +3.8 | 0.006 | 5/43 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.008 | 9/40 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.008 | 12/42 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.010 | 13/39 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.430×** | -7.0 | 1e-09 | 22/42 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.466×** | -6.1 | 3e-07 | 14/23 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -5.7 | 2e-06 | 19/31 (LoVo, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.003 | 10/42 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.047 | 6/43 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.666× | -3.3 | 0.10 | 11/32 (RKO, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.680× | -3.2 | 0.10 | 11/41 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.677× | -3.1 | 0.12 | 14/39 (A-172, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.65 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0518× (z -12.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 3.51 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +9.7) | [[Flutamide (drug)]] 0.5 µM 0.0597× (z -9.8) |
| [[HOP62 (line)]] | alt | 2.76 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 2.01 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +9.7) | [[Belinostat (drug)]] 0.5 µM 0.0628× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 6.65 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0242× (z -9.8) |
| [[HS-578T (line)]] | alt | 2.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 2.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.96× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 9.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 5.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.80× (z +9.0) | — |
| [[SW480 (line)]] | alt | 4.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +11.1) | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.83 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.81 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[USP50]] | +0.80 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[THUMPD3-AS1]] | +0.79 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[ERI2]] | +0.79 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[FAM151B]] | +0.78 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.78 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[LINC03016]] | +0.78 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.78 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.78 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.78 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.77 | +0.83 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XG]] | B | XG activity raises C21orf91-OT1's level | lines that do not express XG (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without XG | 0.020 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C21orf91-OT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC13A3]] | B | SLC13A3 activity raises C21orf91-OT1's level | lines that do not express SLC13A3 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without SLC13A3 | 0.070 | ⚠ within organs, on part of the lines; also absent: TLN2; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises C21orf91-OT1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without IMPA1P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[MCF2]] | C | MCF2 activity raises C21orf91-OT1's level | lines that do not express MCF2 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without MCF2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTA4]] | B | C21orf91-OT1 activity lowers GSTA4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.95× higher at baseline in the lines without C21orf91-OT1 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[INTS6]] | B | C21orf91-OT1 activity raises INTS6's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without C21orf91-OT1 | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[PARD6G-AS1]] | B | C21orf91-OT1 activity lowers PARD6G-AS1's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without C21orf91-OT1 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[STPG4]] | B | C21orf91-OT1 activity raises STPG4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without C21orf91-OT1 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[HPX]] | B | C21orf91-OT1 activity raises HPX's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without C21orf91-OT1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[SEMA4A]] | B | C21orf91-OT1 activity raises SEMA4A's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without C21orf91-OT1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[CEMIP2]] | B | C21orf91-OT1 activity raises CEMIP2's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without C21orf91-OT1 | 0.053 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[SLC9A1]] | B | C21orf91-OT1 activity raises SLC9A1's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without C21orf91-OT1 | 0.053 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[LINC01191]] | B | C21orf91-OT1 activity raises LINC01191's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without C21orf91-OT1 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[PYGM]] | B | C21orf91-OT1 activity raises PYGM's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without C21orf91-OT1 | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[CDKL4]] | B | C21orf91-OT1 activity raises CDKL4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without C21orf91-OT1 | 0.066 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[LINC00910]] | B | C21orf91-OT1 activity lowers LINC00910's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without C21orf91-OT1 | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, -14.2); signed map (16.8, 7.9). **Vector** length 74.4, 12.6% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +20.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | C21orf91 overlapping transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q21.1 — chr21:17,763,315-17,792,523 (-) |
| Ensembl biotype | lncRNA |
| Also known as | D21S2089E; previously NCRNA00285 |
| Gene groups (HGNC) | Overlapping transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16729) · Entrez [246312](https://www.ncbi.nlm.nih.gov/gene/246312) · Ensembl [ENSG00000240770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240770)

## Data

Gene col 14248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14248); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14248]; `tensor/DDL_lfc|DDL_z.npy` [14248]; `embed/gene_vectors.npy` [14248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14248 or target_col == 14248). Every well: [[C21orf91-OT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C21orf91-OT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
