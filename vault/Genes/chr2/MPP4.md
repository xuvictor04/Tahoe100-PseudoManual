---
symbol: "MPP4"
type: "gene"
col: 1335
ensembl_id: "ENSG00000082126"
name: "MAGUK p55 scaffold protein 4"
location: "2q33.1"
module: 39
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MPP4

*MAGUK p55 scaffold protein 4* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.06× (z +15.0, q 0e+00, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.491× (z -5.4, q 4e-05, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.84, fdr 7e-06), [[PITRM1-AS1]] (+0.84, fdr 7e-06), [[CHADL]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[AOX1]] → it (grade B ⚠); 14 go from it, the strongest it → [[ALDH8A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.06×** | +15.0 | 0e+00 | 31/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.03×** | +14.9 | 0e+00 | 34/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.63×** | +9.8 | 3e-20 | 34/44 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.49×** | +9.4 | 5e-19 | 29/41 (A-172, C32, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.25×** | +8.9 | 6e-17 | 24/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +8.9 | 6e-17 | 6/10 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +7.9 | 2e-13 | 21/32 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +7.3 | 2e-11 | 4/9 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +6.8 | 8e-10 | 25/37 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.07×** | +5.5 | 2e-06 | 21/43 (A498, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.98×** | +5.2 | 1e-05 | 20/43 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.92×** | +4.9 | 4e-05 | 16/44 (LoVo, A549, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.90×** | +4.9 | 5e-05 | 18/44 (A498, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.8 | 6e-05 | 10/18 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +4.8 | 6e-05 | 19/43 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.94×** | +4.7 | 9e-05 | 19/39 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +4.7 | 1e-04 | 14/41 (LoVo, CHP-212, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.3 | 5e-04 | 14/44 (A498, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +3.5 | 0.012 | 10/44 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.048 | 10/40 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +3.0 | 0.077 | 5/42 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.491×** | -5.4 | 4e-05 | 21/42 (A-427, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -4.6 | 1e-03 | 21/42 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.548×** | -4.3 | 0.003 | 11/39 (SNU-423, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.568×** | -4.3 | 0.003 | 17/42 (hTERT-HPNE, H4, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.365×** | -4.0 | 0.007 | 8/33 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -3.7 | 0.019 | 18/33 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.633×** | -3.5 | 0.042 | 11/44 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.05 µM |  | **0.622×** | -3.3 | 0.061 | 13/39 (A549, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -3.3 | 0.061 | 20/44 (A549, H4, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Erlotinib (drug)]] 5 µM |  | **0.640×** | -3.3 | 0.065 | 16/40 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.089 | 6/44 (SNU-423, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.655×** | -3.1 | 0.089 | 9/32 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -3.1 | 0.089 | 11/39 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.33 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +14.4) | [[Digitoxin (drug)]] 5 µM 0.0796× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 5.31 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0749× (z -8.6) |
| [[A498 (line)]] | wt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +9.2) | — |
| [[C32 (line)]] | wt | 7.67 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0467× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0543× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +9.6) | — |
| [[LoVo (line)]] | wt | 2.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 8.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 7.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0848× (z -9.3) |
| [[SW480 (line)]] | alt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.84 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.84 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[CHADL]] | +0.83 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[OIT3]] | +0.83 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.83 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.83 | +0.87 / +0.75 | both halves | 7e-06 |  |
| [[DPYS]] | +0.83 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.83 | +0.83 / +0.80 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.82 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.81 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[USP50]] | +0.81 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.81 | +0.83 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AOX1]] | B | AOX1 activity raises MPP4's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without AOX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MPP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASGR1]] | B | ASGR1 activity raises MPP4's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without ASGR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[CD226]] | B | CD226 activity raises MPP4's level | lines that do not express CD226 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without CD226 | 0.037 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises MPP4's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without NEK10 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises MPP4's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without SLC26A4 | 0.062 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity raises MPP4's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without SCUBE2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises MPP4's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without LINC00334 | 0.064 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[ADORA1]] | B | ADORA1 activity raises MPP4's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without ADORA1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[SPOCK2]] | C | SPOCK2 activity raises MPP4's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SPOCK2 | 0.075 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent; co-absent with the target |
| [[MMP25]] | C | MMP25 activity raises MPP4's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH8A1]] | C | MPP4 activity raises ALDH8A1's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[BLZF2P]] | C | MPP4 activity raises BLZF2P's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[MC1R]] | C | MPP4 activity raises MC1R's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[USP50]] | C | MPP4 activity raises USP50's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[ROPN1L]] | C | MPP4 activity raises ROPN1L's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[LINC00486]] | C | MPP4 activity raises LINC00486's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[EFCAB10]] | C | MPP4 activity raises EFCAB10's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without MPP4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[MSS51]] | C | MPP4 activity raises MSS51's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without MPP4 | 0.071 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent |
| [[SPATA32]] | C | MPP4 activity raises SPATA32's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without MPP4 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; co-absent with the target |
| [[PLAC8L1]] | C | MPP4 activity raises PLAC8L1's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without MPP4 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent |
| [[ALPK3]] | C | MPP4 activity lowers ALPK3's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 3.36× higher at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |
| [[PILRA]] | C | MPP4 activity raises PILRA's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 2.73× lower at baseline in the lines without MPP4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, -14.0); signed map (17.9, 9.7). **Vector** length 81.7, 15.3% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +15.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.7 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | MAGUK p55 scaffold protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,644,870-201,698,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DLG6 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JB8](https://www.uniprot.org/uniprotkb/Q96JB8) (MAGUK p55 subfamily member 4):

> May play a role in retinal photoreceptors development.

**Summary**, from NCBI Gene [58538](https://www.ncbi.nlm.nih.gov/gene/58538):

> This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) protein family, with an N-terminal PDZ domain, a central src homology 3 region (SH3), and a C-terminal guanylate kinase-like (GUK) domain. The protein is localized to the outer limiting membrane in the retina, and is thought to function in photoreceptor polarity and the organization of specialized intercellular junctions. Alternatively spliced transcript variants have been described, but their biological validity has …

**Accessions** — [HGNC:13680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13680) · Entrez [58538](https://www.ncbi.nlm.nih.gov/gene/58538) · UniProt [Q96JB8](https://www.uniprot.org/uniprotkb/Q96JB8) · Ensembl [ENSG00000082126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082126)

## Data

Gene col 1335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1335); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1335]; `tensor/DDL_lfc|DDL_z.npy` [1335]; `embed/gene_vectors.npy` [1335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1335 or target_col == 1335). Every well: [[MPP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
