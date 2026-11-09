---
symbol: "HOXB-AS3"
type: "gene"
col: 13888
ensembl_id: "ENSG00000233101"
name: "HOXB cluster antisense RNA 3"
location: "17q21.32"
module: 21
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HOXB-AS3

*HOXB cluster antisense RNA 3* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +15.9, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.684× (z -5.0, q 2e-04, down in 15 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.757× (z -3.7, q 0.049, down in 8 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.206×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.206×; ⚠ cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0741×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AsPC-1 0.0677×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0904×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB3]] (+0.77, fdr 7e-06, ⚠ same locus), [[C2CD5-AS1]] (+0.76, fdr 1e-05), [[HOXB6]] (+0.75, fdr 7e-06, ⚠ same locus), [[HOXA-AS2]] (+0.72, fdr 1e-05), [[TSPOAP1-AS1]] (+0.71, fdr 2e-05); moves opposite to [[SLC39A3]] (-0.61, fdr 4e-05), [[MLX]] (-0.59, fdr 3e-05), [[HAUS7]] (-0.58, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HOXB4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +15.9 | 0e+00 | 37/40 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +9.0 | 6e-17 | 20/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.2 | 6e-14 | 7/10 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.5 | 1e-08 | 10/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.6 | 2e-06 | 15/34 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.5 | 4e-06 | 12/39 (PANC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 10/46 (SW480, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.002 | 9/40 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 9/38 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.9 | 0.006 | 11/42 (A-427, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.2 | 0.067 | 6/45 (LoVo, HS-578T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.067 | 0/42 | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.067 | 3/44 (hTERT-HPNE, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.1 | 0.078 | 7/35 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.092 | 7/47 (SW1417, A-172, …) | top dose only |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.093 | 4/45 (Panc 03.27, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.097 | 4/43 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13888.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.206×; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.206×; ⚠ cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0741×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AsPC-1 0.0677×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0904×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.684×** | -5.0 | 2e-04 | 15/46 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.686×** | -4.9 | 2e-04 | 16/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -3.7 | 0.049 | 8/45 (A498, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.761×** | -3.6 | 0.051 | 11/46 (hTERT-HPNE, SW480, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -3.3 | 0.093 | 9/46 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | 0.779× | -3.3 | 0.10 | 6/40 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.6) | — |
| [[A498 (line)]] | wt | 5.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 5.82 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0677× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 4.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.18 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0741× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.31 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0904× (z -9.7) |
| [[PANC-1 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.6) | — |
| [[A-427 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB3]] | +0.77 | +0.73 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C2CD5-AS1]] | +0.76 | +0.55 / +0.73 | both halves | 1e-05 | same gene group |
| [[HOXB6]] | +0.75 | +0.63 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXA-AS2]] | +0.72 | +0.50 / +0.72 | both halves | 1e-05 | same gene group |
| [[TSPOAP1-AS1]] | +0.71 | +0.48 / +0.80 | both halves | 2e-05 | same gene group |
| [[CHMP3-AS1]] | +0.69 | +0.41 / +0.70 | both halves | 4e-05 | same gene group |
| [[HOXB4]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC00938]] | +0.68 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.68 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF451-AS1]] | +0.68 | +0.42 / +0.72 | both halves | 4e-05 | same gene group |
| [[TICAM2-AS1]] | +0.67 | +0.43 / +0.74 | both halves | 3e-05 | same gene group |
| [[ZNF821]] | +0.67 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LRRC37A16P]] | +0.66 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[G2E3-AS1]] | +0.66 | +0.47 / +0.64 | both halves | 2e-05 | same gene group |
| [[SPATA21]] | +0.65 | +0.37 / +0.68 | both halves | 8e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A3]] | -0.61 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MLX]] | -0.59 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[HAUS7]] | -0.58 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[RPUSD1]] | -0.58 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB4]] | B | HOXB4 activity raises HOXB-AS3's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without HOXB4 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXB8]] | B | HOXB8 activity raises HOXB-AS3's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without HOXB8 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C |
| [[HDAC6]] | B | HDAC6 activity raises HOXB-AS3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXB5]], [[HOXB6]] | B | HOXB5, HOXB6 activity raises HOXB-AS3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.59× lower at baseline in the lines without HOXB5, HOXB6 | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises HOXB-AS3's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.9, 26.5); signed map (39.0, -3.8). **Vector** length 55.4, 7.52% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.0 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.6 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | HOXB cluster antisense RNA 3 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.32 — chr17:48,549,630-48,606,414 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HLZ6](https://www.uniprot.org/uniprotkb/C0HLZ6) (HOXB-AS3 peptide):

> Blocks the binding of HNRNPA1 to the intronic sequences flanking exon 9 of the PKM gene by competitively binding to the HNRNPA1 RGG-box motif. This inhibits inclusion of exon 9 and promotes inclusion of exon 10, suppressing formation of the PKM M2 isoform and promoting production of the M1 isoform. Also suppresses HNRNPA1-mediated processing of microRNA 18a (miR-18a). Promotes MYC stability through interaction with IGF2BP2.

**Summary**, from NCBI Gene [404266](https://www.ncbi.nlm.nih.gov/gene/404266):

> Involved in negative regulation of pre-miRNA processing; protein stabilization; and regulation of RNA splicing. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40283) · Entrez [404266](https://www.ncbi.nlm.nih.gov/gene/404266) · UniProt [C0HLZ6](https://www.uniprot.org/uniprotkb/C0HLZ6) · Ensembl [ENSG00000233101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233101)

## Data

Gene col 13888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13888); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13888]; `tensor/DDL_lfc|DDL_z.npy` [13888]; `embed/gene_vectors.npy` [13888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13888 or target_col == 13888). Every well: [[HOXB-AS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB-AS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
