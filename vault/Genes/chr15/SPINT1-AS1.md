---
symbol: "SPINT1-AS1"
type: "gene"
col: 15329
ensembl_id: "ENSG00000261183"
name: "SPINT1 antisense RNA 1"
location: "15q15.1"
module: 55
arm: "+"
pooled_cpm: 2.89
n_lines_expressing: 23
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 74
direction_downstream: 81
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SPINT1-AS1

*SPINT1 antisense RNA 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.19× (z +11.8, q 4e-29, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +5.0, q 6e-05, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.490× (z -5.4, q 5e-05, down in 14 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (LS 180 0.0281×, HT-29 0.0980×, KATO III 0.0775×, COLO 205 0.0458×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0849×, Panc 03.27 0.203×; ⚠ cell-cycle shift, explains ~62% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.157×, NCI-H1573 0.204×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN8]] (+0.71, fdr 7e-06), [[KCNE3]] (+0.70, fdr 7e-06), [[SYK]] (+0.70, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 74 arrows point to it, the strongest [[SLC44A3-AS1]] → it (grade B ⚠); 81 go from it, the strongest it → [[PRRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +11.8 | 4e-29 | 3/4 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.70×** | +11.5 | 5e-28 | 10/10 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.55×** | +8.7 | 6e-16 | 5/7 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.12×** | +5.6 | 4e-06 | 6/15 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.0 | 6e-05 | 2/15 (NCI-H2347, NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.7 | 2e-04 | 3/14 (SW1417, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.5 | 5e-04 | 2/20 (KATO III, COLO 205) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.5 | 6e-04 | 4/16 (HEC-1-A, SW1417, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.30×** | +3.8 | 0.010 | 1/10 (SW1417) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.7 | 0.012 | 2/15 (NCI-H1573, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.62×** | +3.6 | 0.019 | 1/16 (LoVo) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +3.3 | 0.040 | 1/4 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.054 | 3/14 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.066 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15329.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (LS 180 0.0281×, HT-29 0.0980×, KATO III 0.0775×, COLO 205 0.0458×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.0849×, Panc 03.27 0.203×; ⚠ cell-cycle shift, explains ~62% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (LS 180 0.157×, NCI-H1573 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -5.4 | 5e-05 | 14/19 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.611×** | -3.7 | 0.046 | 12/19 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -3.7 | 0.046 | 12/20 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.640× | -3.1 | 0.18 | 5/19 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.664× | -3.1 | 0.18 | 14/20 (LS 180, HT-29, …) | all doses, flat | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.655× | -3.1 | 0.18 | 3/19 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.669× | -3.0 | 0.18 | 2/20 (LS 180, NCI-H1573) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.672× | -3.0 | 0.18 | 1/20 (SW480) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 11.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0281× (z -17.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.157× (z -9.1) |
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -12.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.204× (z -9.1) |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 8.71 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0775× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 6.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -8.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW1417 (line)]] | alt | 8.96 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.827 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.823 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN8]] | +0.71 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SYK]] | +0.70 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[TNFRSF14-AS1]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 | same gene group |
| [[ST6GALNAC1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TMC4]] | +0.67 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[ABO]] | +0.66 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[FXYD3]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.65 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TMEM30B]] | +0.65 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[HNF1A-AS1]] | +0.64 | +0.57 / +0.50 | both halves | 1e-05 | same gene group |
| [[LINC01559]] | +0.64 | +0.70 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 10, C 64. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises SPINT1-AS1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without SLC44A3-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises SPINT1-AS1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without SLC44A3 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises SPINT1-AS1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without PROM2 | 0.030 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises SPINT1-AS1's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without POU5F1B | 0.036 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises SPINT1-AS1's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without HNF4G | 0.037 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[HDAC6]] | B | HDAC6 activity raises SPINT1-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MANSC1]] | B | MANSC1 activity raises SPINT1-AS1's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without MANSC1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[FCGRT]] | B | FCGRT activity raises SPINT1-AS1's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without FCGRT | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[KLF8]] | B | KLF8 activity raises SPINT1-AS1's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without KLF8 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[COLEC10]] | B | COLEC10 activity raises SPINT1-AS1's level | lines that do not express COLEC10 (31) vs lines expressing it (19) | 1.25× lower at baseline in the lines without COLEC10 | 0.096 | ⚠ within organs, on part of the lines; also absent: CCK, TRIM55, AJAP1 |
| [[LINC02967]] | C | LINC02967 activity raises SPINT1-AS1's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 4.75× lower at baseline in the lines without LINC02967 | 5e-06 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[KDF1]] | C | KDF1 activity raises SPINT1-AS1's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 4.26× lower at baseline in the lines without KDF1 | 1e-05 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3; co-absent with the target |

### Downstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 27, C 54. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG2]] | B | SPINT1-AS1 activity raises PRRG2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without SPINT1-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[SLC44A3]] | B | SPINT1-AS1 activity raises SLC44A3's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.55× lower at baseline in the lines without SPINT1-AS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[SLC44A3-AS1]] | B | SPINT1-AS1 activity raises SLC44A3-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.52× lower at baseline in the lines without SPINT1-AS1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[TMEM184A]] | B | SPINT1-AS1 activity raises TMEM184A's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without SPINT1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[BCAR3-AS1]] | B | SPINT1-AS1 activity raises BCAR3-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without SPINT1-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[MROH6]] | B | SPINT1-AS1 activity raises MROH6's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without SPINT1-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[TNFRSF14-AS1]] | B | SPINT1-AS1 activity raises TNFRSF14-AS1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without SPINT1-AS1 | 0.015 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | SPINT1-AS1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SPINT1-AS1 (27) vs lines expressing it (21) | the lines without SPINT1-AS1: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[POU5F1B]] | B | SPINT1-AS1 activity raises POU5F1B's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without SPINT1-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[MANSC1]] | B | SPINT1-AS1 activity raises MANSC1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.49× lower at baseline in the lines without SPINT1-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[RAMP1]] | B | SPINT1-AS1 activity raises RAMP1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without SPINT1-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[PROM2]] | B | SPINT1-AS1 activity raises PROM2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without SPINT1-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 48.9); signed map (62.3, 7.6). **Vector** length 43.7, 11.3% of its response variance represented; |z| ≥ 3 in 339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | SPINT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q15.1 — chr15:40,835,808-40,844,442 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-532F12.5 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53162) · Entrez [102724362](https://www.ncbi.nlm.nih.gov/gene/102724362) · Ensembl [ENSG00000261183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261183)

## Data

Gene col 15329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15329); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15329]; `tensor/DDL_lfc|DDL_z.npy` [15329]; `embed/gene_vectors.npy` [15329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15329 or target_col == 15329). Every well: [[SPINT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
