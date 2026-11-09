---
symbol: "ERC2"
type: "gene"
col: 11933
ensembl_id: "ENSG00000187672"
name: "ELKS/RAB6-interacting/CAST family member 2"
location: "3p14.3"
module: 61
arm: "+"
pooled_cpm: 10.3
n_lines_expressing: 30
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ERC2

*ELKS/RAB6-interacting/CAST family member 2* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.74× (z +28.1, q 0e+00, up in 22 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.118×, NCI-H23 0.155×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0807×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNTG2]] (+0.74, fdr 7e-06), [[CCDC85A]] (+0.67, fdr 7e-06), [[SNAP91]] (+0.65, fdr 7e-06); moves opposite to [[NUP133]] (-0.52, fdr 3e-05), [[NDUFV1]] (-0.51, fdr 3e-05), [[SLC25A14]] (-0.51, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC7A11-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.74×** | +28.1 | 0e+00 | 22/24 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +24.8 | 0e+00 | 17/22 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.19×** | +21.0 | 0e+00 | 24/26 (NCI-H460, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **4.92×** | +20.4 | 0e+00 | 20/24 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.28×** | +15.2 | 0e+00 | 21/24 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +12.0 | 5e-31 | 6/13 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.42×** | +11.3 | 1e-27 | 16/24 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +10.8 | 4e-25 | 6/17 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +10.7 | 6e-25 | 16/23 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +10.7 | 9e-25 | 21/26 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.09×** | +9.4 | 3e-19 | 15/22 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +9.0 | 1e-17 | 13/23 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.9 | 1e-13 | 12/27 (SW480, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +7.4 | 5e-12 | 16/24 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.3 | 2e-11 | 8/24 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +7.2 | 3e-11 | 15/25 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.39×** | +5.8 | 2e-07 | 14/24 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (BT-474 0.118×, NCI-H23 0.155×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0807×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.739× | -3.7 | 0.15 | 7/23 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.2 | 0.32 | 3/28 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.636× | -3.0 | 0.32 | 9/21 (H4, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Menadione (drug)]] 5 µM |  | 0.782× | -3.0 | 0.32 | 2/22 (C-33 A, HS-578T) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.81 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 132× (z +24.1) | — |
| [[NCI-H460 (line)]] | wt | 9.52 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.58× (z +16.8) | [[Digitoxin (drug)]] 5 µM 0.0807× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 25.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 59.6× (z +26.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 6.18 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.3× (z +21.8) | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.38× (z +10.4) | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -11.3) |
| [[SW480 (line)]] | alt | 9.75 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.31× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 3.57 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 412× (z +23.1) | — |
| [[NCI-H1573 (line)]] | alt | 7.85 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +12.0) | — |
| [[J82 (line)]] | alt | 16.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +15.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -9.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.97 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.58× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.61× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.14× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 4.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +13.5) | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTG2]] | +0.74 | +0.65 / +0.79 | both halves | 7e-06 |  |
| [[CCDC85A]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SNAP91]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[XKR4]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[KCNH1]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[KCNQ3]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.62 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[FMN2]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RGS7]] | +0.62 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[B3GALT1]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP133]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NDUFV1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A14]] | -0.51 | -0.32 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A11-AS1]] | B | SLC7A11-AS1 activity lowers ERC2's level | lines that do not express SLC7A11-AS1 (11) vs lines expressing it (39) | 1.98× higher at baseline in the lines without SLC7A11-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1; maybe low, not absent |
| [[RIMS2]] | B | RIMS2 activity raises ERC2's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without RIMS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[ELAVL2]] | B | ELAVL2 activity raises ERC2's level | lines that do not express ELAVL2 (34) vs lines expressing it (16) | 3.07× lower at baseline in the lines without ELAVL2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283982, MIR99AHG, DPP10 |
| [[TOP2A]] | B | TOP2A activity lowers ERC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FGF13]] | B | FGF13 activity raises ERC2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without FGF13 | 0.073 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[SVEP1]] | B | SVEP1 activity raises ERC2's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without SVEP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | ERC2 activity raises CACNA1C's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ERC2 | 0.006 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[SVEP1]] | B | ERC2 activity raises SVEP1's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without ERC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| cells under [[Anethole trithione (drug)]] 0.5 µM | B | ERC2 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express ERC2 (20) vs lines expressing it (28) | the lines without ERC2: 0.93× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | ERC2 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express ERC2 (20) vs lines expressing it (28) | the lines without ERC2: 1.29× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[RIMS2]] | B | ERC2 activity raises RIMS2's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 3.74× lower at baseline in the lines without ERC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[FMN2]] | C | ERC2 activity raises FMN2's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 2.86× lower at baseline in the lines without ERC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 30.7); signed map (32.8, 21.5). **Vector** length 63.2, 15.3% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +21.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +28.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +20.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -1.4 | +0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | +1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ELKS/RAB6-interacting/CAST family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:55,508,311-56,469,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAST, CAST1, KIAA0378, SPBC110, Spc110, ELKSL |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15083](https://www.uniprot.org/uniprotkb/O15083) (ERC protein 2):

> Thought to be involved in the organization of the cytomatrix at the nerve terminals active zone (CAZ) which regulates neurotransmitter release. Seems to act together with BSN. May recruit liprin-alpha proteins to the CAZ.

**Summary**, from NCBI Gene [26059](https://www.ncbi.nlm.nih.gov/gene/26059):

> This gene encodes a protein that belongs to the Rab3-interacting molecule (RIM)-binding protein family. Members of this protein family form part of the cytomatrix at the active zone (CAZ) complex and function as regulators of neurotransmitter release. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:31922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31922) · Entrez [26059](https://www.ncbi.nlm.nih.gov/gene/26059) · UniProt [O15083](https://www.uniprot.org/uniprotkb/O15083) · Ensembl [ENSG00000187672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187672)

## Data

Gene col 11933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11933); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11933]; `tensor/DDL_lfc|DDL_z.npy` [11933]; `embed/gene_vectors.npy` [11933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11933 or target_col == 11933). Every well: [[ERC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
