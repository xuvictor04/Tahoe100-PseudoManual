---
symbol: "HOXB5"
type: "gene"
col: 4157
ensembl_id: "ENSG00000120075"
name: "homeobox B5"
location: "17q21.32"
module: 201
arm: "+"
pooled_cpm: 6.4
n_lines_expressing: 39
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXB5

*homeobox B5* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +8.5, q 2e-14, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -9.8, q 1e-19, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB6]] (+0.86, fdr 7e-06, ⚠ same locus), [[HOXB3]] (+0.81, fdr 7e-06, ⚠ read-through risk), [[HOXB-AS3]] (+0.75, fdr 7e-06, ⚠ same locus), [[HOXA3]] (+0.66, fdr 1e-05), [[AGAP3]] (+0.64, fdr 1e-05), [[HOXA9]] (+0.63, fdr 2e-05); moves opposite to [[TTPAL]] (-0.59, fdr 7e-06), [[SETX]] (-0.58, fdr 2e-05), [[BCL7B]] (-0.58, fdr 1e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXB3]] → it (grade C ⚠); 6 go from it, the strongest it → [[NDUFAF7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +8.5 | 2e-14 | 22/30 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.6 | 9e-04 | 14/36 (C32, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.6 | 9e-04 | 12/19 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.2 | 0.003 | 5/10 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.2 | 0.003 | 10/21 (LS 180, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.30×** | +4.0 | 0.007 | 5/28 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.045 | 7/33 (SNU-423, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.4 | 0.045 | 7/29 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.045 | 7/36 (SW1417, HT-29, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.4 | 0.045 | 3/9 (A-172, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 1.41× | +3.0 | 0.13 | 5/24 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -9.8 | 1e-19 | 24/31 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -6.5 | 3e-08 | 17/36 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.506×** | -6.0 | 5e-07 | 18/36 (PANC-1, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.503×** | -5.8 | 1e-06 | 19/34 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -5.5 | 4e-06 | 16/31 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -4.2 | 0.002 | 16/36 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -4.2 | 0.002 | 15/35 (SW1417, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -4.2 | 0.002 | 14/35 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.623×** | -4.1 | 0.002 | 12/36 (PANC-1, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.656×** | -3.7 | 0.013 | 12/36 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.658×** | -3.7 | 0.013 | 17/36 (SW48, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -3.6 | 0.017 | 14/36 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.153× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -14.2) |
| [[SW480 (line)]] | alt | 15.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.9) |
| [[SHP-77 (line)]] | alt | 18.9 | 1 | 2 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 4.62× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.0568× (z -12.6) |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -9.3) |
| [[A-172 (line)]] | wt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.0) |
| [[A549 (line)]] | wt | 2.71 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0335× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0849× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0668× (z -9.7) |
| [[SW1417 (line)]] | alt | 26.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -9.8) |
| [[A-427 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB6]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | same gene group; STRING 982; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB3]] | +0.81 | +0.83 / +0.75 | both halves | 7e-06 | same gene group; STRING 874; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of HOXB3 on the same strand (can correlate by spillover, not regulation) |
| [[HOXB-AS3]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HOXB4]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | same gene group; STRING 958; ⚠ same locus (12.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA3]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 | same gene group; STRING 400 |
| [[HOXB8]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | same gene group; STRING 911; ⚠ same locus (17.6 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP3]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HOXA9]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 | same gene group; STRING 410 |
| [[HOXA10]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | same gene group |
| [[SMAD5]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RCOR3]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[IST1]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[TIAL1]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[ASB7]] | +0.59 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.59 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[SATB2-AS1]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTPAL]] | -0.59 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SETX]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[BCL7B]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SLC35F6]] | -0.56 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[GTF2H3]] | -0.55 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ZKSCAN2]] | -0.55 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PUF60]] | -0.54 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PDAP1]] | -0.53 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[EIF2S1]] | -0.52 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[ATP9B]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB3]] | C | HOXB3 activity raises HOXB5's level | lines that do not express HOXB3 (9) vs lines expressing it (41) | 3.36× lower at baseline in the lines without HOXB3 | 0.024 | ⚠ within organs, on part of the lines; also absent: HOXB6; co-absent with the target |
| [[HOXB8]] | C | HOXB8 activity raises HOXB5's level | lines that do not express HOXB8 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without HOXB8 | 0.056 | ⚠ within organs, on part of the lines; also absent: FAM83F, LINC02086, ZBTB7C; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFAF7]] | B | HOXB5, [[HOXB6]] activity lowers NDUFAF7's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.12× higher at baseline in the lines without HOXB5, HOXB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[SMAD5]] | B | HOXB5, [[HOXB6]] activity lowers SMAD5's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.31× higher at baseline in the lines without HOXB5, HOXB6 | 0.063 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[HOXB-AS3]] | B | HOXB5, [[HOXB6]] activity raises HOXB-AS3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.59× lower at baseline in the lines without HOXB5, HOXB6 | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[TTPAL]] | B | HOXB5, [[HOXB6]] activity lowers TTPAL's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 1.24× higher at baseline in the lines without HOXB5, HOXB6 | 0.097 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent genes |
| [[HOXB3]] | C | HOXB5, [[HOXB6]] activity raises HOXB3's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 4.32× lower at baseline in the lines without HOXB5, HOXB6 | 0.008 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |
| [[HOXB8]] | C | HOXB5, [[HOXB6]] activity raises HOXB8's level | lines that do not express HOXB5, HOXB6 (11) vs lines expressing them (39) | 2.35× lower at baseline in the lines without HOXB5, HOXB6 | 0.021 | ⚠ within organs, on part of the lines; also absent: HOXB3, HOXB8; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.1, 26.7); signed map (39.2, -4.1). **Vector** length 59.2, 11.3% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | homeobox B5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,591,257-48,593,779 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX2, HOX2A |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P09067](https://www.uniprot.org/uniprotkb/P09067) (Homeobox protein Hox-B5):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3215](https://www.ncbi.nlm.nih.gov/gene/3215):

> This gene is a member of the Antp homeobox family and encodes a nuclear protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded protein functions as a sequence-specific transcription factor that is involved in lung and gut development. Increased expression of this gene is associated with a distinct biologic subset of acute myeloid leukemia (AML) and the occurrence of bronchopulmonary sequestration (BPS) and congenital …

**Accessions** — [HGNC:5116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5116) · Entrez [3215](https://www.ncbi.nlm.nih.gov/gene/3215) · UniProt [P09067](https://www.uniprot.org/uniprotkb/P09067) · Ensembl [ENSG00000120075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120075)

## Data

Gene col 4157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4157); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4157]; `tensor/DDL_lfc|DDL_z.npy` [4157]; `embed/gene_vectors.npy` [4157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4157 or target_col == 4157). Every well: [[HOXB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
