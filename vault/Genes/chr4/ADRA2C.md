---
symbol: "ADRA2C"
type: "gene"
col: 11495
ensembl_id: "ENSG00000184160"
name: "adrenoceptor alpha 2C"
location: "4p16.3"
module: 27
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ADRA2C

*adrenoceptor alpha 2C* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.01× (z +10.4, q 2e-22, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.62× (z +4.1, q 0.005, up in 5 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 8.93×, NCI-H1573 7.14×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 15.6×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 13.7×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ralimetinib dimesylate (drug)]] 0.05 µM: 0.533× (z -3.8, q 0.057, down in 11 of 27 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.541× (z -3.7, q 0.057, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.127×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.146×; ⚠ cell-cycle shift, explains ~23% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.161×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTUM]] (+0.56, fdr 1e-05), [[FGF20]] (+0.53, fdr 4e-05), [[APCDD1]] (+0.53, fdr 3e-05); moves opposite to [[SLC15A5]] (-0.53, fdr 1e-05), [[SCARA5]] (-0.50, fdr 3e-05), [[GTF2I-AS1]] (-0.48, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EFNA2]] → it (grade B ⚠); 9 go from it, the strongest it → [[MMP25-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 8.93×, NCI-H1573 7.14×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 15.6×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 13.7×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.01×** | +10.4 | 2e-22 | 2/2 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.61×** | +7.7 | 3e-12 | 6/6 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.52×** | +7.0 | 4e-10 | 3/4 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.6 | 6e-04 | 5/9 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.005 | 5/27 (NCI-H1573, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.75×** | +3.3 | 0.077 | 2/7 (A-427, SW480) | inconsistent across doses | low cells (technical?) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.70× | +3.2 | 0.11 | 1/22 (NCI-H460) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.0 | 0.15 | 3/10 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[vincristine (drug)]] 0.5 µM |  | 2.38× | +3.0 | 0.15 | 4/14 (NCI-H460, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.127×); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.146×; ⚠ cell-cycle shift, explains ~23% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.161×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.533×** | -3.8 | 0.057 | 11/27 (CHP-212, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.541×** | -3.7 | 0.057 | 9/24 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -3.6 | 0.062 | 9/18 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.577× | -3.3 | 0.13 | 9/23 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.14 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 15.6× (z +11.3) | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 8.14 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0572× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.740 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.891 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.131 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.612 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTUM]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FGF20]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[APCDD1]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[NKD2]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[EMID1]] | +0.49 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[GLS2]] | +0.49 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[CD72]] | +0.49 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[LRRC56]] | +0.49 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[HAGHL]] | +0.48 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[EFNA2]] | +0.48 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[ENTREP2]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[LINC01622]] | +0.48 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A5]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SCARA5]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GTF2I-AS1]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[LINC03000]] | -0.47 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[DPP10]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CHL1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[STX16]] | -0.46 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ADGRD1]] | -0.46 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[NRCAM]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SERPINB11]] | -0.44 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[GREM2]] | -0.44 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[EPGN]] | -0.44 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA2]] | B | EFNA2 activity raises ADRA2C's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without EFNA2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[LIMCH1]] | B | LIMCH1 activity lowers ADRA2C's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.38× higher at baseline in the lines without LIMCH1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[EPGN]] | B | EPGN activity raises ADRA2C's level | lines that do not express EPGN (41) vs lines expressing it (9) | 2.32× lower at baseline in the lines without EPGN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418 |
| [[NPTX1]] | B | NPTX1 activity raises ADRA2C's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 1.46× lower at baseline in the lines without NPTX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP25-AS1]] | B | ADRA2C activity raises MMP25-AS1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.39× lower at baseline in the lines without ADRA2C | 0.007 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[NTN1]] | B | ADRA2C activity raises NTN1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without ADRA2C | 0.009 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[RINL]] | B | ADRA2C activity lowers RINL's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.48× higher at baseline in the lines without ADRA2C | 0.009 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[CACHD1]] | B | ADRA2C activity raises CACHD1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without ADRA2C | 0.029 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[GSG1L]] | B | ADRA2C activity raises GSG1L's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without ADRA2C | 0.037 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[RINL]] | B | ADRA2C activity strengthens RINL's drug response | lines that do not express ADRA2C (17) vs lines expressing it (27) | the lines without ADRA2C respond 0.57× as strongly (z diff +0.93); strongest at Homoharringtonine 5 µM: 0.95x vs 1.67x (z diff +2.8) | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B; target measured in part of the lines; both ways; artifact flags |
| [[DNPH1]] | B | ADRA2C activity raises DNPH1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without ADRA2C | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[KCNQ4]] | B | ADRA2C activity raises KCNQ4's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without ADRA2C | 0.075 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[NKD2]] | C | ADRA2C activity raises NKD2's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.62× lower at baseline in the lines without ADRA2C | 0.020 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 40.9); signed map (61.6, 17.2). **Vector** length 37.7, 7.22% of its response variance represented; |z| ≥ 3 in 428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +7.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.9 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.0 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.0 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | adrenoceptor alpha 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:3,766,348-3,768,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADRARL2; previously ADRA2L2, ADRA2RL2 |
| Gene groups (HGNC) | Adrenoceptors |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 15 pathways, smallest: Adrenoceptors; Amine ligand-binding receptors; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P18825](https://www.uniprot.org/uniprotkb/P18825) (Alpha-2C adrenergic receptor):

> Alpha-2 adrenergic receptors are G protein-coupled receptors for catecholamines that activate the G(i/o) protein pathway, thereby promoting adenylyl cyclase inhibition, ERK1/2 stimulation, and voltage-gated calcium channels suppression. Control a variety of physiological processes, such as regulation of blood pressure, lipolysis and insulin release. ADRA2A and ADRA2C mediates the presynaptic feedback inhibition of neurotransmitter release from noradrenergic nerve terminals in sympathetic and …

**Summary**, from NCBI Gene [152](https://www.ncbi.nlm.nih.gov/gene/152):

> Alpha-2-adrenergic receptors are members of the G protein-coupled receptor superfamily. They include 3 highly homologous subtypes: alpha2A, alpha2B, and alpha2C. These receptors have a critical role in regulating neurotransmitter release from sympathetic nerves and from adrenergic neurons in the central nervous system. The mouse studies revealed that both the alpha2A and alpha2C subtypes were required for normal presynaptic control of transmitter release from sympathetic nerves in the heart and …

**Accessions** — [HGNC:283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:283) · Entrez [152](https://www.ncbi.nlm.nih.gov/gene/152) · UniProt [P18825](https://www.uniprot.org/uniprotkb/P18825) · Ensembl [ENSG00000184160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184160)

## Data

Gene col 11495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11495); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11495]; `tensor/DDL_lfc|DDL_z.npy` [11495]; `embed/gene_vectors.npy` [11495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11495 or target_col == 11495). Every well: [[ADRA2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADRA2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
