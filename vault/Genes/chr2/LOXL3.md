---
symbol: "LOXL3"
type: "gene"
col: 3659
ensembl_id: "ENSG00000115318"
name: "lysyl oxidase like 3"
location: "2p13.1"
module: 87
arm: "+"
pooled_cpm: 11.33
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 37
direction_downstream: 30
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# LOXL3

*lysyl oxidase like 3* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +7.9, q 2e-12, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.563× (z -6.6, q 1e-08, down in 15 of 22 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AEBP1]] (+0.77, fdr 7e-06), [[SDC2]] (+0.71, fdr 7e-06), [[COL19A1]] (+0.71, fdr 7e-06); moves opposite to [[ARHGEF5]] (-0.46, fdr 4e-04), [[PATJ]] (-0.45, fdr 1e-04), [[MIR3936HG]] (-0.44, fdr 5e-05).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[CTTNBP2]] → it (grade B ⚠); 30 go from it, the strongest it → [[EFR3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.9 | 2e-12 | 4/17 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.7 | 5e-12 | 4/13 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.4 | 3e-11 | 2/8 (HS-578T, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.8 | 2e-04 | 2/8 (HS-578T, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.002 | 3/21 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.2 | 0.003 | 1/12 (A498) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.014 | 5/18 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.044 | 2/18 (SNU-1, HS-578T) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.063 | 2/13 (SNU-1, HS-578T) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.071 | 3/21 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.072 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.563×** | -6.6 | 1e-08 | 15/22 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -6.6 | 1e-08 | 13/21 (SNU-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -6.4 | 2e-08 | 13/17 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -5.6 | 3e-06 | 10/21 (SNU-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -4.7 | 3e-04 | 10/21 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -4.3 | 0.001 | 4/20 (SNU-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -4.3 | 0.001 | 10/21 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.003 | 10/21 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.053 | 7/22 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.061 | 1/20 (SW 1088) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 328 | 0 | 27 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0298× (z -35.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0482× (z -21.7) |
| [[C32 (line)]] | wt | 98.7 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0600× (z -22.0) |
| [[RPMI-7951 (line)]] | alt | 77.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0403× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 95.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -20.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0469× (z -20.0) |
| [[HS-578T (line)]] | alt | 64.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 7.25 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0505× (z -9.0) |
| [[A-172 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AEBP1]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SDC2]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[COL19A1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | pathway: Collagen formation |
| [[COL1A2]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures |
| [[PRRX1]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[A2M]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 | pathway: Extracellular matrix organization |
| [[MIR3681HG]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RHOJ]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CTHRC1]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF5]] | -0.46 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[PATJ]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MIR3936HG]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ARHGEF34P]] | -0.43 | -0.46 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 6, C 31. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTTNBP2]] | B | CTTNBP2 activity raises LOXL3's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without CTTNBP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR |
| [[IGFBP7]] | B | IGFBP7 activity raises LOXL3's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without IGFBP7 | 0.066 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1 |
| [[TRPM8]] | B | TRPM8 activity raises LOXL3's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.78× lower at baseline in the lines without TRPM8 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity raises LOXL3's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.40× lower at baseline in the lines without NRN1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[STAG3]] | B | STAG3 activity raises LOXL3's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without STAG3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[FLT1]] | B | FLT1 activity raises LOXL3's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without FLT1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[AEBP1]] | C | AEBP1 activity raises LOXL3's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.45× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises LOXL3's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.84× lower at baseline in the lines without KCNE4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises LOXL3's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without LEF1-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises LOXL3's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.77× lower at baseline in the lines without EDNRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LEF1]] | C | LEF1 activity raises LOXL3's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without LEF1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises LOXL3's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.49× lower at baseline in the lines without DIRAS3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 7, C 23. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFR3B]] | B | LOXL3 activity raises EFR3B's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.38× lower at baseline in the lines without LOXL3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[TET1]] | B | LOXL3 activity raises TET1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.53× lower at baseline in the lines without LOXL3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[TMEM45A]] | B | LOXL3 activity raises TMEM45A's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without LOXL3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[MIR3681HG]] | B | LOXL3 activity raises MIR3681HG's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.97× lower at baseline in the lines without LOXL3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[SRPX]] | B | LOXL3 activity raises SRPX's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without LOXL3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[FZD1]] | B | LOXL3 activity raises FZD1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 1.40× lower at baseline in the lines without LOXL3 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[EPHA3]] | B | LOXL3 activity raises EPHA3's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without LOXL3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[TNFRSF19]] | C | LOXL3 activity raises TNFRSF19's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.94× lower at baseline in the lines without LOXL3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | LOXL3 activity raises KCNE4's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.88× lower at baseline in the lines without LOXL3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[COL1A2]] | C | LOXL3 activity raises COL1A2's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 5.87× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[LEF1]] | C | LOXL3 activity raises LEF1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 3.59× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | LOXL3 activity raises AEBP1's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.7, 27.5); signed map (28.1, 40.3). **Vector** length 60.3, 14.7% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | lysyl oxidase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,532,258-74,555,690 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Lysyl oxidase family |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Elastic fibre formation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [P58215](https://www.uniprot.org/uniprotkb/P58215) (Lysyl oxidase homolog 3):

> Protein-lysine 6-oxidase that mediates the oxidation of peptidyl lysine residues to allysine in target proteins. Catalyzes the post-translational oxidative deamination of peptidyl lysine residues in precursors of elastin and different types of collagens, a prerequisite in the formation of cross-links between collagens and elastin. Required for somite boundary formation by catalyzing oxidation of fibronectin (FN1), enhancing integrin signaling in myofibers and their adhesion to the myotendinous …

**Summary**, from NCBI Gene [84695](https://www.ncbi.nlm.nih.gov/gene/84695):

> This gene encodes a lysyl oxidase, which likely functions as an amine oxidase and plays a role in the formation of crosslinks in collagens and elastin. Deletion of the related gene in mouse causes neonatal mortality with cleft palate, spine deformity, and defects in collagen organization. A mutation in this gene was found in a family with Stickler syndrome. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:13869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13869) · Entrez [84695](https://www.ncbi.nlm.nih.gov/gene/84695) · UniProt [P58215](https://www.uniprot.org/uniprotkb/P58215) · Ensembl [ENSG00000115318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115318)

## Data

Gene col 3659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3659); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3659]; `tensor/DDL_lfc|DDL_z.npy` [3659]; `embed/gene_vectors.npy` [3659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3659 or target_col == 3659). Every well: [[LOXL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOXL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
