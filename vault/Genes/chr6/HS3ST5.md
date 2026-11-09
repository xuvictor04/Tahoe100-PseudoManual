---
symbol: "HS3ST5"
type: "gene"
col: 14643
ensembl_id: "ENSG00000249853"
name: "heparan sulfate-glucosamine 3-sulfotransferase 5"
location: "6q21-q22.1"
module: 27
arm: "+"
pooled_cpm: 9.84
n_lines_expressing: 21
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 21
direction_downstream: 29
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# HS3ST5

*heparan sulfate-glucosamine 3-sulfotransferase 5* — 6q21-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.43× (z +15.5, q 0e+00, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.740× (z -3.8, q 0.085, down in 6 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H661 0.0717×, SW480 0.109×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0980×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.192×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST18]] (+0.72, fdr 7e-06), [[JAKMIP2-AS1]] (+0.70, fdr 7e-06), [[LINC01980]] (+0.70, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[SERPINF1]] → it (grade B ⚠); 29 go from it, the strongest it → [[ADAMTS19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +15.5 | 0e+00 | 8/14 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.85×** | +13.2 | 4e-37 | 13/18 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +10.5 | 2e-23 | 2/6 (CFPAC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +9.2 | 3e-18 | 4/11 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +8.1 | 6e-14 | 4/7 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.28×** | +7.3 | 2e-11 | 11/14 (CFPAC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +6.7 | 2e-09 | 11/18 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.61×** | +5.8 | 4e-07 | 4/18 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +5.4 | 5e-06 | 2/15 (HepG2/C3A, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.8 | 8e-05 | 2/15 (SW 900, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 8e-05 | 4/16 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 4e-04 | 1/16 (SW480) | all doses, flat | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **2.50×** | +4.3 | 8e-04 | 1/12 (SW480) | top dose only | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.66×** | +4.2 | 8e-04 | 3/15 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.2 | 8e-04 | 9/16 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.002 | 3/15 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.002 | 3/14 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +3.4 | 0.018 | 5/16 (CFPAC-1, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H661 0.0717×, SW480 0.109×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0980×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.122×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.192×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.085 | 6/18 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 0.673× | -3.4 | 0.20 | 6/17 (LOX-IMVI, SW480, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.692× | -3.3 | 0.20 | 4/15 (SW 900, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -11.1) |
| [[NCI-H661 (line)]] | alt | 606 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0717× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -9.5) |
| [[A-172 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST18]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[JAKMIP2-AS1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[LINC01980]] | +0.70 | +0.70 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[SMOC2]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[DACH1]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[FGF20]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LINC02466]] | +0.66 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS19]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[PHYHIPL]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP25]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DKK2]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 4, C 17. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINF1]] | B | SERPINF1 activity raises HS3ST5's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 2.06× lower at baseline in the lines without SERPINF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HS3ST5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises HS3ST5's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without OPRD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[AXIN2]] | B | AXIN2 activity raises HS3ST5's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without AXIN2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[RUNX1T1]] | C | RUNX1T1 activity raises HS3ST5's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.90× lower at baseline in the lines without RUNX1T1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises HS3ST5's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 3.74× lower at baseline in the lines without JAKMIP2-AS1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises HS3ST5's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 3.77× lower at baseline in the lines without SLC25A24P1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises HS3ST5's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 4.37× lower at baseline in the lines without LGR5 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises HS3ST5's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without RIMBP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises HS3ST5's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without RMST | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises HS3ST5's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without POU3F2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises HS3ST5's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without GABRG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 14, C 15. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS19]] | B | HS3ST5 activity raises ADAMTS19's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without HS3ST5 | 0.009 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[PROX1-AS1]] | B | HS3ST5 activity raises PROX1-AS1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without HS3ST5 | 0.013 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[DKK2]] | B | HS3ST5 activity raises DKK2's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without HS3ST5 | 0.025 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[NPAS3]] | B | HS3ST5 activity raises NPAS3's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without HS3ST5 | 0.029 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[F10]] | B | HS3ST5 activity raises F10's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.59× lower at baseline in the lines without HS3ST5 | 0.040 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[PROX1]] | B | HS3ST5 activity raises PROX1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without HS3ST5 | 0.048 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[NKD1]] | B | HS3ST5 activity raises NKD1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without HS3ST5 | 0.057 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[LINC01622]] | B | HS3ST5 activity raises LINC01622's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.03× lower at baseline in the lines without HS3ST5 | 0.061 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[LINC02254]] | B | HS3ST5 activity raises LINC02254's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.14× lower at baseline in the lines without HS3ST5 | 0.086 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[SLC7A8]] | B | HS3ST5 activity raises SLC7A8's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.16× lower at baseline in the lines without HS3ST5 | 0.089 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[SLCO6A1]] | B | HS3ST5 activity raises SLCO6A1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without HS3ST5 | 0.091 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[MAN1A1]] | B | HS3ST5 activity raises MAN1A1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without HS3ST5 | 0.095 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 41.7); signed map (62.8, 17.4). **Vector** length 39.8, 9.26% of its response variance represented; |z| ≥ 3 in 393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +4.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.2 | -3.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | +0.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate-glucosamine 3-sulfotransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21-q22.1 — chr6:114,055,596-114,343,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 3-OST-5 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZT8](https://www.uniprot.org/uniprotkb/Q8IZT8) (Heparan sulfate glucosamine 3-O-sulfotransferase 5):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the transfer of a sulfo group to position 3 of glucosamine residues in heparan. Catalyzes the rate limiting step in the biosynthesis of heparan sulfate (HSact). This modification is a crucial step in the biosynthesis of anticoagulant heparan sulfate as it completes the structure of the antithrombin pentasaccharide binding site. Also generates GlcUA-GlcNS or IdoUA-GlcNS and IdoUA2S-GlcNH2. The substrate-specific …

**Summary**, from NCBI Gene [222537](https://www.ncbi.nlm.nih.gov/gene/222537):

> HS3ST5 belongs to a group of heparan sulfate 3-O-sulfotransferases (EC 2.8.2.23) that transfer sulfate from 3-prime-phosphoadenosine 5-prime phosphosulfate (PAPS) to heparan sulfate and heparin (Mochizuki et al., 2003 [PubMed 12740361]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19419) · Entrez [222537](https://www.ncbi.nlm.nih.gov/gene/222537) · UniProt [Q8IZT8](https://www.uniprot.org/uniprotkb/Q8IZT8) · Ensembl [ENSG00000249853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249853)

## Data

Gene col 14643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14643); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14643]; `tensor/DDL_lfc|DDL_z.npy` [14643]; `embed/gene_vectors.npy` [14643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14643 or target_col == 14643). Every well: [[HS3ST5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS3ST5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
