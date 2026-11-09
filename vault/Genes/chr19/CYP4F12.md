---
symbol: "CYP4F12"
type: "gene"
col: 11792
ensembl_id: "ENSG00000186204"
name: "cytochrome P450 family 4 subfamily F member 12"
location: "19p13.12"
module: 44
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 18
n_dd_up: 36
n_dd_down: 8
n_dd_up_clean: 25
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 93
direction_downstream: 101
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CYP4F12

*cytochrome P450 family 4 subfamily F member 12* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.99× (z +12.4, q 2e-32, up in 14 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.491× (z -5.7, q 6e-06, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP3]] (+0.84, fdr 7e-06), [[PLEKHG6]] (+0.78, fdr 7e-06), [[PRR15L]] (+0.78, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 93 arrows point to it, the strongest [[MYH14]] → it (grade B ⚠); 101 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.99×** | +12.4 | 2e-32 | 14/16 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +9.7 | 6e-20 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +7.8 | 8e-13 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +7.8 | 8e-13 | 1/15 (Panc 03.27) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +7.6 | 5e-12 | 2/7 (LoVo, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.47×** | +7.2 | 5e-11 | 10/14 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +6.6 | 3e-09 | 11/16 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 5/16 (AsPC-1, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +5.6 | 1e-06 | 11/16 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +5.6 | 1e-06 | 10/16 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.97×** | +5.2 | 1e-05 | 8/15 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +5.0 | 3e-05 | 7/14 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.33×** | +4.8 | 6e-05 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.69×** | +4.8 | 7e-05 | 7/15 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +4.7 | 8e-05 | 6/16 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 3/16 (LS 180, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.003 | 6/16 (Panc 03.27, A549, …) | all doses, flat |  |
| [[Pioglitazone (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.005 | 5/15 (KATO III, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.491×** | -5.7 | 6e-06 | 13/16 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -5.3 | 4e-05 | 14/16 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.513×** | -5.2 | 4e-05 | 8/16 (A498, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -4.7 | 4e-04 | 12/15 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.595×** | -4.2 | 0.003 | 9/16 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.623×** | -3.6 | 0.030 | 0/14 | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.436×** | -3.5 | 0.039 | 3/16 (LS 180, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.652×** | -3.5 | 0.039 | 7/16 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.689× | -3.0 | 0.17 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 12.7 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0681× (z -16.5) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -15.7) |
| [[LS 180 (line)]] | wt | 55.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0306× (z -21.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -20.7) |
| [[LoVo (line)]] | wt | 6.62 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.60× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.0617× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.4) |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0447× (z -20.7) |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.2) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 5.53 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.46× (z +9.7) | — |
| [[A-172 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.570 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP3]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PLEKHG6]] | +0.78 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[USH1C]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.74 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.70 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[PRR15]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.69 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Biological oxidations |
| [[PROM2]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 8, C 85. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYH14]] | B | MYH14 activity raises CYP4F12's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 2.17× lower at baseline in the lines without MYH14 | 0.037 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CYP4F12's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without ELF3-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[FUT2]] | B | FUT2 activity raises CYP4F12's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.17× lower at baseline in the lines without FUT2 | 0.070 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[MANSC1]] | B | MANSC1 activity raises CYP4F12's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without MANSC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises CYP4F12's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without ATP8B1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[LNX1]] | B | LNX1 activity raises CYP4F12's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without LNX1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[IGSF9]] | B | IGSF9 activity raises CYP4F12's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without IGSF9 | 0.092 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[MCF2L]] | B | MCF2L activity raises CYP4F12's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.94× lower at baseline in the lines without MCF2L | 0.096 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[CDH17]] | C | CDH17 activity raises CYP4F12's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 7.08× lower at baseline in the lines without CDH17 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises CYP4F12's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 6.57× lower at baseline in the lines without MUC13 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises CYP4F12's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.77× lower at baseline in the lines without GCNT3 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises CYP4F12's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 4.03× lower at baseline in the lines without CYP4F3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |

### Downstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 30, C 71. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | CYP4F12 activity raises ELF3-AS1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.76× lower at baseline in the lines without CYP4F12 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[CARD14]] | B | CYP4F12 activity raises CARD14's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CYP4F12 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[BICDL2]] | B | CYP4F12 activity raises BICDL2's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.40× lower at baseline in the lines without CYP4F12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[BAG1]] | B | CYP4F12 activity raises BAG1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without CYP4F12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[MYH14]] | B | CYP4F12 activity raises MYH14's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.95× lower at baseline in the lines without CYP4F12 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[FUT2]] | B | CYP4F12 activity raises FUT2's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.33× lower at baseline in the lines without CYP4F12 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[RSPH1]] | B | CYP4F12 activity raises RSPH1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CYP4F12 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[LINC02580]] | B | CYP4F12 activity raises LINC02580's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without CYP4F12 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[ACSL3]] | B | CYP4F12 activity raises ACSL3's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.35× lower at baseline in the lines without CYP4F12 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[LNX1]] | B | CYP4F12 activity raises LNX1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.75× lower at baseline in the lines without CYP4F12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[ARHGEF16]] | B | CYP4F12 activity raises ARHGEF16's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.60× lower at baseline in the lines without CYP4F12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[IL22RA1]] | B | CYP4F12 activity raises IL22RA1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.71× lower at baseline in the lines without CYP4F12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 52.7); signed map (62.1, 5.3). **Vector** length 61.2, 20.9% of its response variance represented; |z| ≥ 3 in 418 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.57 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.57 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.57 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +5.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -1.6 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 4 subfamily F member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,673,018-15,697,174 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 4 |
| Reactome | 5 pathways, smallest: Fatty acids; Eicosanoids; Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCS2](https://www.uniprot.org/uniprotkb/Q9HCS2) (Cytochrome P450 4F12):

> A cytochrome P450 monooxygenase involved in the metabolism of endogenous polyunsaturated fatty acids (PUFAs). Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase). Catalyzes the hydroxylation of carbon hydrogen bonds, with preference for omega-2 position. Metabolizes (5Z,8Z,11Z,14Z)-eicosatetraenoic acid …

**Summary**, from NCBI Gene [66002](https://www.ncbi.nlm.nih.gov/gene/66002):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein likely localizes to the endoplasmic reticulum. When expressed in yeast the enzyme is capable of oxdizing arachidonic acid. It can also catalyze the epoxidation of 22:6n-3 and 22:5n-3 polyunsaturated long-chain fatty acids. This gene is part of a …

**Accessions** — [HGNC:18857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18857) · Entrez [66002](https://www.ncbi.nlm.nih.gov/gene/66002) · UniProt [Q9HCS2](https://www.uniprot.org/uniprotkb/Q9HCS2) · Ensembl [ENSG00000186204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186204)

## Data

Gene col 11792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11792); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11792]; `tensor/DDL_lfc|DDL_z.npy` [11792]; `embed/gene_vectors.npy` [11792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11792 or target_col == 11792). Every well: [[CYP4F12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP4F12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
