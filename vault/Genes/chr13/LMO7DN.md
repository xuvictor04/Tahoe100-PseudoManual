---
symbol: "LMO7DN"
type: "gene"
col: 10954
ensembl_id: "ENSG00000178734"
name: "LMO7 downstream neighbor"
location: "13q22.2"
module: 39
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 36
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 23
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LMO7DN

*LMO7 downstream neighbor* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.19× (z +8.7, q 1e-15, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 3.76× (z +7.3, q 6e-11, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.490× (z -4.6, q 0.003, down in 14 of 30 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.513× (z -4.3, q 0.006, down in 14 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (AsPC-1 0.0103×, NCI-H1573 0.0670×; ⚠ cell-cycle shift, explains ~42% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H1573 0.0659×, LoVo 0.0186×; ⚠ cell-cycle shift, explains ~26% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (AsPC-1 0.0390×, NCI-H1573 0.149×; ⚠ unreliable plate only); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0292×); [[Digitoxin (drug)]] 0.5 µM in 1 line (AsPC-1 0.0349×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.249×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OIT3]] (+0.76, fdr 7e-06), [[FNDC7]] (+0.74, fdr 7e-06), [[SLC22A14]] (+0.74, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL17A1]] → it (grade B ⚠); 23 go from it, the strongest it → [[IMPA1P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.19×** | +8.7 | 1e-15 | 1/5 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.96×** | +8.1 | 2e-13 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **3.76×** | +7.3 | 6e-11 | 26/32 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +6.2 | 6e-08 | 1/10 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.52×** | +5.9 | 5e-07 | 9/23 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.6 | 2e-06 | 6/30 (COLO 205, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +5.5 | 3e-06 | 6/22 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +5.0 | 4e-05 | 6/23 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **2.11×** | +4.6 | 3e-04 | 9/24 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.06×** | +4.3 | 9e-04 | 10/27 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +4.2 | 0.002 | 3/16 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.82×** | +3.8 | 0.007 | 5/27 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.052 | 3/23 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.79×** | +3.2 | 0.055 | 0/31 | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.65×** | +3.2 | 0.055 | 5/31 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.055 | 4/28 (AsPC-1, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10954.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (AsPC-1 0.0103×, NCI-H1573 0.0670×; ⚠ cell-cycle shift, explains ~42% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H1573 0.0659×, LoVo 0.0186×; ⚠ cell-cycle shift, explains ~26% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (AsPC-1 0.0390×, NCI-H1573 0.149×; ⚠ unreliable plate only); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 0.0292×); [[Digitoxin (drug)]] 0.5 µM in 1 line (AsPC-1 0.0349×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.490×** | -4.6 | 0.003 | 14/30 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -4.3 | 0.006 | 14/27 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.477×** | -4.1 | 0.008 | 15/29 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.669×** | -3.6 | 0.037 | 11/27 (LOX-IMVI, J82, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -3.6 | 0.037 | 13/31 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.572× | -3.1 | 0.18 | 10/32 (AsPC-1, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 32.0 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0192× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0292× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 7.34 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0103× (z -11.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0349× (z -9.5) |
| [[LoVo (line)]] | wt | 12.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.0186× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Elagolix sodium (drug)]] 0.5 µM 0.0380× (z -8.7) |
| [[A-172 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.993 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.826 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OIT3]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.72 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MPP4]] | +0.71 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[XG]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL17A1]] | B | COL17A1 activity raises LMO7DN's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 3.25× lower at baseline in the lines without COL17A1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[MROH3P]] | B | MROH3P activity raises LMO7DN's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without MROH3P | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TOP2A]] | B | TOP2A activity lowers LMO7DN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSC2]] | B | DSC2 activity raises LMO7DN's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without DSC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[HDAC6]] | B | HDAC6 activity raises LMO7DN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KRT86]] | B | KRT86 activity raises LMO7DN's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.78× lower at baseline in the lines without KRT86 | 0.084 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[LSMEM2]] | B | LSMEM2 activity raises LMO7DN's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without LSMEM2 | 0.099 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[LMO7]] | C | LMO7 activity raises LMO7DN's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without LMO7 | 0.015 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPA1P1]] | B | LMO7DN activity raises IMPA1P1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.71× lower at baseline in the lines without LMO7DN | 0.005 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[FHDC1]] | B | LMO7DN activity raises FHDC1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without LMO7DN | 0.012 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MROH3P]] | B | LMO7DN activity raises MROH3P's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without LMO7DN | 0.019 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MTNR1A]] | B | LMO7DN activity raises MTNR1A's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without LMO7DN | 0.023 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[SEMA4A]] | B | LMO7DN activity raises SEMA4A's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without LMO7DN | 0.028 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[LINC00654]] | B | LMO7DN activity raises LINC00654's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without LMO7DN | 0.038 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MYRFL]] | B | LMO7DN activity raises MYRFL's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without LMO7DN | 0.039 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[PLEKHA6]] | B | LMO7DN activity raises PLEKHA6's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without LMO7DN | 0.041 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[PHYHD1]] | B | LMO7DN activity raises PHYHD1's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without LMO7DN | 0.044 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[OIT3]] | B | LMO7DN activity raises OIT3's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without LMO7DN | 0.044 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[FBXW10B]] | B | LMO7DN activity raises FBXW10B's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without LMO7DN | 0.055 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[TRIM72]] | B | LMO7DN activity raises TRIM72's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without LMO7DN | 0.055 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, -15.0); signed map (17.1, 10.1). **Vector** length 61.6, 13.5% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LMO7 downstream neighbor |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q22.2 — chr13:75,870,590-75,883,811 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C13orf45, LMO7DN-IT1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [F2Z398](https://www.uniprot.org/uniprotkb/F2Z398) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44370) · Entrez [729420](https://www.ncbi.nlm.nih.gov/gene/729420) · UniProt [F2Z398](https://www.uniprot.org/uniprotkb/F2Z398) · Ensembl [ENSG00000178734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178734)

## Data

Gene col 10954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10954); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10954]; `tensor/DDL_lfc|DDL_z.npy` [10954]; `embed/gene_vectors.npy` [10954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10954 or target_col == 10954). Every well: [[LMO7DN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO7DN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
