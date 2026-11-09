---
symbol: "SNCAIP"
type: "gene"
col: 757
ensembl_id: "ENSG00000064692"
name: "synuclein alpha interacting protein"
location: "5q23.2"
module: 9
arm: "+"
pooled_cpm: 6.28
n_lines_expressing: 30
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SNCAIP

*synuclein alpha interacting protein* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.67× (z +24.7, q 0e+00, up in 17 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.892× (z -4.1, q 0.020, down in 4 of 28 measured lines) ⚠ position not correctable. The strongest without an alert is [[Erlotinib (drug)]] 0.05 µM: 0.668× (z -3.8, q 0.045, down in 3 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.0760×, A-172 0.0754×, HOP62 0.0992×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.0318×, HOP62 0.0692×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (HOP62 0.227×, RKO 0.225×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.153×); [[Binimetinib (drug)]] 0.5 µM in 1 line (HOP62 0.190×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTSL1]] (+0.57, fdr 2e-05), [[COLEC10]] (+0.57, fdr 2e-05), [[LRFN5]] (+0.57, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PEX5L]] → it (grade B ⚠); 3 go from it, the strongest it → [[ACVR1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.67×** | +24.7 | 0e+00 | 17/21 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +14.4 | 2e-44 | 8/21 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.19×** | +11.7 | 3e-29 | 12/20 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +10.9 | 2e-25 | 13/24 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +10.2 | 3e-22 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.67×** | +9.9 | 4e-21 | 10/23 (HOP62, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +8.1 | 4e-14 | 13/24 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.0 | 1e-07 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.0 | 1e-07 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 4e-07 | 4/22 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.4 | 4e-06 | 5/27 (HS-578T, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.3 | 4e-06 | 10/20 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.4 | 5e-04 | 1/13 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +4.3 | 7e-04 | 11/27 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.56×** | +4.1 | 0.001 | 2/17 (hTERT-HPNE, LoVo) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.002 | 4/21 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.003 | 5/26 (HS-578T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.009 | 6/23 (LoVo, SHP-77, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.013 | 7/22 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 757.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SHP-77 0.0760×, A-172 0.0754×, HOP62 0.0992×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.0318×, HOP62 0.0692×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (HOP62 0.227×, RKO 0.225×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.153×); [[Binimetinib (drug)]] 0.5 µM in 1 line (HOP62 0.190×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -4.1 | 0.020 | 4/28 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.668×** | -3.8 | 0.045 | 3/25 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.791× | -3.4 | 0.14 | 7/24 (BT-474, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 29.9 | 0 | 7 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.337× (z -18.5) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.190× (z -9.6) |
| [[SHP-77 (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0318× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.153× (z -14.7) |
| [[A-172 (line)]] | wt | 20.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0754× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 2.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.3× (z +15.0) | — |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +11.2) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.165× (z -9.4) |
| [[RKO (line)]] | wt | 18.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.225× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.1) |
| [[J82 (line)]] | alt | 2.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 1.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +11.3) | — |
| [[SW48 (line)]] | wt | 2.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.861 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL1]] | +0.57 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[COLEC10]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[LRFN5]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SNTG1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[LINC01695]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[BAALC]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[KCND2]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[RDUR]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[VENTXP1]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[TRPM2]] | +0.52 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ENKUR]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DIP2C-AS1]] | +0.52 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEX5L]] | B | PEX5L activity raises SNCAIP's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without PEX5L | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[LINC02899]] | B | LINC02899 activity raises SNCAIP's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 2.56× lower at baseline in the lines without LINC02899 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1 |
| [[LINC01592]] | B | LINC01592 activity raises SNCAIP's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 2.78× lower at baseline in the lines without LINC01592 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SNCAIP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIK1]] | B | GRIK1 activity raises SNCAIP's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without GRIK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |
| [[ENKUR]] | B | ENKUR activity raises SNCAIP's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ENKUR | 0.045 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[SHANK1]] | B | SHANK1 activity raises SNCAIP's level | lines that do not express SHANK1 (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without SHANK1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TRIML2, HOXD8, ENSG00000242880 |
| [[LINC01320]] | B | LINC01320 activity raises SNCAIP's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 1.90× lower at baseline in the lines without LINC01320 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[SAMD3]] | B | SAMD3 activity raises SNCAIP's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without SAMD3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[BAALC]] | B | BAALC activity raises SNCAIP's level | lines that do not express BAALC (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without BAALC | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[RDUR]] | C | RDUR activity raises SNCAIP's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without RDUR | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACVR1C]] | B | SNCAIP activity raises ACVR1C's level | lines that do not express SNCAIP (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without SNCAIP | 0.032 | ⚠ within organs, on part of the lines; also absent: LIMCH1, RNF152, FLT1 |
| [[PLXNA4]] | B | SNCAIP activity raises PLXNA4's level | lines that do not express SNCAIP (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without SNCAIP | 0.078 | ⚠ within organs, on part of the lines; also absent: LIMCH1, RNF152, FLT1 |
| [[CA13]] | B | SNCAIP activity raises CA13's level | lines that do not express SNCAIP (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without SNCAIP | 0.092 | ⚠ within organs, on part of the lines; also absent: LIMCH1, RNF152, FLT1 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.423). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 26.8); signed map (37.5, 25.8). **Vector** length 67.9, 16.6% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +24.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.8 | +3.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | +0.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | synuclein alpha interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:122,311,354-122,464,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYPH1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6H5](https://www.uniprot.org/uniprotkb/Q9Y6H5) (Synphilin-1):

> Isoform 2 inhibits the ubiquitin ligase activity of SIAH1 and inhibits proteasomal degradation of target proteins. Isoform 2 inhibits autoubiquitination and proteasomal degradation of SIAH1, and thereby increases cellular levels of SIAH. Isoform 2 modulates SNCA monoubiquitination by SIAH1.

**Summary**, from NCBI Gene [9627](https://www.ncbi.nlm.nih.gov/gene/9627):

> This gene encodes a protein containing several protein-protein interaction domains, including ankyrin-like repeats, a coiled-coil domain, and an ATP/GTP-binding motif. The encoded protein interacts with alpha-synuclein in neuronal tissue and may play a role in the formation of cytoplasmic inclusions and neurodegeneration. A mutation in this gene has been associated with Parkinson's disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:11139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11139) · Entrez [9627](https://www.ncbi.nlm.nih.gov/gene/9627) · UniProt [Q9Y6H5](https://www.uniprot.org/uniprotkb/Q9Y6H5) · Ensembl [ENSG00000064692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064692)

## Data

Gene col 757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 757); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 757]; `tensor/DDL_lfc|DDL_z.npy` [757]; `embed/gene_vectors.npy` [757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 757 or target_col == 757). Every well: [[SNCAIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNCAIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
