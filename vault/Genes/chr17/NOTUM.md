---
symbol: "NOTUM"
type: "gene"
col: 11651
ensembl_id: "ENSG00000185269"
name: "notum, palmitoleoyl-protein carboxylesterase"
location: "17q25.3"
module: 27
arm: "+"
pooled_cpm: 10.2
n_lines_expressing: 19
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 14
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# NOTUM

*notum, palmitoleoyl-protein carboxylesterase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.89× (z +9.6, q 3e-19, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +7.2, q 1e-10, up in 7 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.585× (z -3.8, q 0.037, down in 10 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.133×, SW480 0.118×; ⚠ cell-cycle shift, explains ~49% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.213×, NCI-H1792 0.280×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0829×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP2-AS1]] (+0.76, fdr 7e-06), [[FGF20]] (+0.74, fdr 7e-06), [[APCDD1]] (+0.73, fdr 7e-06); moves opposite to [[ITGB1BP1]] (-0.42, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLC25A24P1]] → it (grade C ⚠); 14 go from it, the strongest it → [[CD72]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +9.6 | 3e-19 | 2/8 (SW1417, SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +7.9 | 7e-13 | 2/6 (PANC-1, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +7.2 | 1e-10 | 7/13 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.5 | 5e-06 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.9 | 1e-04 | 2/14 (NCI-H2030, KATO III) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.12×** | +3.8 | 0.013 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.09×** | +3.7 | 0.013 | 1/14 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.09×** | +3.7 | 0.013 | 5/13 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +3.7 | 0.013 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +3.6 | 0.020 | 4/14 (KATO III, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.025 | 2/14 (NCI-H23, HCT15) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.072 | 1/14 (NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11651.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.133×, SW480 0.118×; ⚠ cell-cycle shift, explains ~49% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.213×, NCI-H1792 0.280×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.0829×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.585×** | -3.8 | 0.037 | 10/14 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -3.8 | 0.037 | 8/14 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.621× | -3.2 | 0.30 | 0/16 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 95.7 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0829× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 71.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -11.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.6) |
| [[A-172 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[FGF20]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 | STRING 560 |
| [[PSD2]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[F10]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CHDH]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[PHYHIPL]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[ST18]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[B3GAT1-DT]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.60 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[LINC01622]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.42 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises NOTUM's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.18× lower at baseline in the lines without SLC25A24P1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[COLGALT2]] | C | COLGALT2 activity raises NOTUM's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 2.36× lower at baseline in the lines without COLGALT2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises NOTUM's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without PHYHIPL | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[FGF20]] | C | FGF20 activity raises NOTUM's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 5.05× lower at baseline in the lines without FGF20 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises NOTUM's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.63× lower at baseline in the lines without JAKMIP2-AS1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises NOTUM's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without LINC00491 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[F10]] | C | F10 activity raises NOTUM's level | lines that do not express F10 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without F10 | 0.069 | ⚠ within organs, on part of the lines; also absent: SELENOP, NIHCOLE, NOTUM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD72]] | B | NOTUM activity raises CD72's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without NOTUM | 0.005 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[PSD2]] | B | NOTUM activity raises PSD2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without NOTUM | 0.016 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[MYH7B]] | B | NOTUM activity raises MYH7B's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without NOTUM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[LARGE2]] | B | NOTUM activity raises LARGE2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without NOTUM | 0.041 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7 |
| [[NMNAT3]] | C | NOTUM activity raises NMNAT3's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without NOTUM | 0.006 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[AXIN2]] | C | NOTUM activity raises AXIN2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without NOTUM | 0.024 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[VSNL1]] | C | NOTUM activity raises VSNL1's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without NOTUM | 0.032 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[BMP5]] | C | NOTUM activity raises BMP5's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without NOTUM | 0.035 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[IGFL4]] | C | NOTUM activity raises IGFL4's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without NOTUM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[MYT1]] | C | NOTUM activity raises MYT1's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without NOTUM | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[CHDH]] | C | NOTUM activity raises CHDH's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without NOTUM | 0.057 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[CDX2]] | C | NOTUM activity raises CDX2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without NOTUM | 0.070 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 43.3); signed map (62.5, 16.5). **Vector** length 41.4, 11.8% of its response variance represented; |z| ≥ 3 in 287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -1.3 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -3.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | notum, palmitoleoyl-protein carboxylesterase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,952,507-81,961,840 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: Release of Hh-Np from the secreting cell; Hedgehog ligand biogenesis; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P988](https://www.uniprot.org/uniprotkb/Q6P988) (Palmitoleoyl-protein carboxylesterase NOTUM):

> Carboxylesterase that acts as a key negative regulator of the Wnt signaling pathway by specifically mediating depalmitoleoylation of WNT proteins. Serine palmitoleoylation of WNT proteins is required for efficient binding to frizzled receptors.

**Summary**, from NCBI Gene [147111](https://www.ncbi.nlm.nih.gov/gene/147111):

> Enables palmitoleyl hydrolase activity. Involved in negative regulation of Wnt signaling pathway and protein depalmitoleylation. Acts upstream of or within bone development and regulation of bone mineralization. Predicted to be located in endoplasmic reticulum lumen and extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27106) · Entrez [147111](https://www.ncbi.nlm.nih.gov/gene/147111) · UniProt [Q6P988](https://www.uniprot.org/uniprotkb/Q6P988) · Ensembl [ENSG00000185269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185269)

## Data

Gene col 11651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11651); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11651]; `tensor/DDL_lfc|DDL_z.npy` [11651]; `embed/gene_vectors.npy` [11651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11651 or target_col == 11651). Every well: [[NOTUM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTUM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
