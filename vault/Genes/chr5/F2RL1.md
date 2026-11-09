---
symbol: "F2RL1"
type: "gene"
col: 8911
ensembl_id: "ENSG00000164251"
name: "F2R like trypsin receptor 1"
location: "5q13.3"
module: 78
arm: "+"
pooled_cpm: 37.66
n_lines_expressing: 30
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 11
direction_downstream: 18
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# F2RL1

*F2R like trypsin receptor 1* — 5q13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 2.43×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.662× (z -5.2, q 1e-04, down in 16 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR222HG]] (+0.65, fdr 7e-06), [[JAG1]] (+0.62, fdr 8e-06), [[TNFRSF21]] (+0.62, fdr 7e-06); moves opposite to [[FAM193B]] (-0.51, fdr 5e-05), [[DDRGK1]] (-0.51, fdr 4e-05), [[MZT2A]] (-0.50, fdr 6e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MALL]] → it (grade B ⚠); 18 go from it, the strongest it → [[VPS37B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 2.43×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | 1.44× | +3.2 | 0.73 | 14/28 (CFPAC-1, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.2 | 1e-04 | 16/28 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.601×** | -4.3 | 0.004 | 22/28 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.640×** | -4.2 | 0.004 | 17/28 (A549, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.672×** | -4.2 | 0.004 | 15/28 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.627×** | -4.1 | 0.004 | 15/28 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.686×** | -4.0 | 0.005 | 16/28 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -3.9 | 0.007 | 17/28 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.008 | 14/28 (A549, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.735×** | -3.8 | 0.008 | 15/28 (NCI-H1573, NCI-H2347, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -3.7 | 0.013 | 16/28 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.015 | 18/28 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.017 | 15/28 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.576×** | -3.5 | 0.022 | 21/28 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.023 | 15/28 (PANC-1, HOP62, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.683×** | -3.4 | 0.029 | 16/28 (PANC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.042 | 14/28 (PANC-1, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 3 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.423× (z -12.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.5) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -11.4) |
| [[HT-29 (line)]] | alt | 70.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.6) |
| [[LoVo (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0413× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -11.0) |
| [[LS 180 (line)]] | wt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -12.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 82.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.191× (z -9.1) |
| [[HOP62 (line)]] | alt | 90.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.433× (z -11.3) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR222HG]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[JAG1]] | +0.62 | +0.61 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFRSF21]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ITPRID2]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CLIC1]] | +0.58 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ITGB1]] | +0.58 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NES]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.57 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[CDC42EP2]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM193B]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[DDRGK1]] | -0.51 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[MZT2A]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[RAB40C]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[PPP3CC]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PNISR]] | -0.49 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TRPM7]] | -0.49 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[COG7]] | -0.49 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[TOM1]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[TUT4]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[FNTB]] | -0.48 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[LINC02256]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MALL]] | B | MALL activity raises F2RL1's level | lines that do not express MALL (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without MALL | 0.042 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[JAG1]] | B | JAG1 activity raises F2RL1's level | lines that do not express JAG1 (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without JAG1 | 0.055 | ⚠ within organs, on part of the lines; also absent: DENND3, SHB, IER3 |
| [[EPHA2]] | B | EPHA2 activity raises F2RL1's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 3.43× lower at baseline in the lines without EPHA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises F2RL1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without SMAD3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises F2RL1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.59× lower at baseline in the lines without ITGA2 | 0.096 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[FGD6]] | C | FGD6 activity raises F2RL1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 5.70× lower at baseline in the lines without FGD6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent; co-absent with the target |
| [[KRT15]] | C | KRT15 activity raises F2RL1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 4.35× lower at baseline in the lines without KRT15 | 0.012 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088; co-absent with the target |
| [[PRSS22]] | C | PRSS22 activity raises F2RL1's level | lines that do not express PRSS22 (28) vs lines expressing it (22) | 4.76× lower at baseline in the lines without PRSS22 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ESRP2, CDH1, ST14; co-absent with the target |
| [[LAMC2]] | C | LAMC2 activity raises F2RL1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without LAMC2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1; co-absent with the target |
| [[LIPG]] | C | LIPG activity raises F2RL1's level | lines that do not express LIPG (25) vs lines expressing it (25) | 3.37× lower at baseline in the lines without LIPG | 0.059 | ⚠ within organs, on part of the lines; also absent: GALNT3, GRHL2, LIPH; co-absent with the target |
| [[IL1RN]] | C | IL1RN activity raises F2RL1's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without IL1RN | 0.079 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS37B]] | B | F2RL1 activity raises VPS37B's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without F2RL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[KRT8]] | B | F2RL1 activity raises KRT8's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 3.81× lower at baseline in the lines without F2RL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[KRT18]] | B | F2RL1 activity raises KRT18's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.02× lower at baseline in the lines without F2RL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[DSC2]] | B | F2RL1 activity raises DSC2's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.11× lower at baseline in the lines without F2RL1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[MYO5B]] | B | F2RL1 activity raises MYO5B's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.35× lower at baseline in the lines without F2RL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[EPHA2]] | B | F2RL1 activity raises EPHA2's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 2.87× lower at baseline in the lines without F2RL1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[SHB]] | B | F2RL1 activity raises SHB's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without F2RL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[SMAD3]] | B | F2RL1 activity raises SMAD3's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without F2RL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[YWHAZ]] | B | F2RL1 activity raises YWHAZ's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without F2RL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[ABHD11]] | B | F2RL1 activity raises ABHD11's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without F2RL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[WDR1]] | B | F2RL1 activity raises WDR1's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without F2RL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[YWHAZ]] | B | F2RL1 activity strengthens YWHAZ's drug response | lines that do not express F2RL1 (20) vs lines expressing it (29) | the lines without F2RL1 respond 0.89× as strongly (z diff +0.46); strongest at Panobinostat 5 µM: 0.70x vs 0.58x (z diff +2.2) | 0.060 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.6, 3.6); signed map (5.3, 43.1). **Vector** length 96.4, 31.9% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.4 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +2.0 | +2.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -3.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | F2R like trypsin receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:76,818,933-76,835,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAR2; previously GPR11 |
| Gene groups (HGNC) | F2R receptors |
| Hallmark sets | KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P55085](https://www.uniprot.org/uniprotkb/P55085) (Proteinase-activated receptor 2):

> Receptor for trypsin and trypsin-like enzymes coupled to G proteins. Its function is mediated through the activation of several signaling pathways including phospholipase C (PLC), intracellular calcium, mitogen-activated protein kinase (MAPK), I-kappaB kinase/NF-kappaB and Rho. Can also be transactivated by cleaved F2R/PAR1. Involved in modulation of inflammatory responses and regulation of innate and adaptive immunity, and acts as a sensor for proteolytic enzymes generated during infection. …

**Summary**, from NCBI Gene [2150](https://www.ncbi.nlm.nih.gov/gene/2150):

> This gene encodes a member of the G-protein coupled receptor 1 family of proteins. The encoded cell surface receptor is activated through proteolytic cleavage of its extracellular amino terminus, resulting in a new amino terminus that acts as a tethered ligand that binds to an extracellular loop domain. Activation of the receptor has been shown to stimulate vascular smooth muscle relaxation, dilate blood vessels, increase blood flow, and lower blood pressure. This protein is also important in …

**Accessions** — [HGNC:3538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3538) · Entrez [2150](https://www.ncbi.nlm.nih.gov/gene/2150) · UniProt [P55085](https://www.uniprot.org/uniprotkb/P55085) · Ensembl [ENSG00000164251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164251)

## Data

Gene col 8911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8911); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8911]; `tensor/DDL_lfc|DDL_z.npy` [8911]; `embed/gene_vectors.npy` [8911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8911 or target_col == 8911). Every well: [[F2RL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/F2RL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
