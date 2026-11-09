---
symbol: "ZNF66"
type: "gene"
col: 8327
ensembl_id: "ENSG00000160229"
name: "zinc finger protein 66"
location: "19p12"
module: 91
arm: "+"
pooled_cpm: 5.57
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 27
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF66

*zinc finger protein 66* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +14.2, q 7e-43, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.693× (z -4.3, q 0.011, down in 11 of 27 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.112×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (BT-474 0.0709×); [[Berbamine (drug)]] 0.5 µM in 1 line (SNU-1 0.0648×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF100]] (+0.76, fdr 7e-06), [[ZNF726]] (+0.69, fdr 7e-06), [[ZNF486]] (+0.67, fdr 7e-06); moves opposite to [[NIPSNAP1]] (-0.47, fdr 1e-04), [[ADA]] (-0.47, fdr 9e-05), [[SBF2]] (-0.45, fdr 4e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[ZNF681]] → it (grade B ⚠); 27 go from it, the strongest it → [[ZNF736]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +14.2 | 7e-43 | 25/31 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.61×** | +11.1 | 4e-26 | 28/35 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +9.6 | 2e-19 | 29/35 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.7 | 1e-12 | 17/36 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.12×** | +7.6 | 3e-12 | 21/35 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.90×** | +7.2 | 8e-11 | 12/22 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.2 | 5e-08 | 12/29 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.42×** | +5.7 | 7e-07 | 11/29 (SW480, SHP-77, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +5.7 | 9e-07 | 13/34 (SNU-423, SW480, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.61×** | +5.3 | 8e-06 | 14/28 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.47×** | +4.5 | 4e-04 | 10/35 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.019 | 4/35 (SW480, RPMI-7951, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.047 | 7/30 (A-172, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.33×** | +3.3 | 0.047 | 8/33 (SW480, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.048 | 4/35 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.055 | 3/35 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.069 | 2/26 (SW480, RKO) | top dose only | noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.078 | 2/35 (SNU-1, NCI-H1792) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8327.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.112×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (BT-474 0.0709×); [[Berbamine (drug)]] 0.5 µM in 1 line (SNU-1 0.0648×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -4.3 | 0.011 | 11/27 (AN3 CA, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.756× | -3.2 | 0.33 | 7/35 (SW480, PANC-1, …) | inconsistent across doses | composition shift |
| [[Sunitinib (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.39 | 5/35 (SW 1271, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 10.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +8.7) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -10.5) |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0764× (z -8.5) |
| [[BT-474 (line)]] | alt | 7.37 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0709× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0680× (z -8.6) |
| [[J82 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +11.8) | — |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0648× (z -9.2) |
| [[SW480 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.0) | — |
| [[A-172 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF100]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 | same gene group |
| [[ZNF726]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZNF486]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF85]] | +0.67 | +0.76 / +0.59 | both halves | 7e-06 | same gene group |
| [[ZNF724]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF695]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF431]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | same gene group |
| [[ZNF714]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 | same gene group |
| [[ZNF273]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 | same gene group |
| [[ZNF681]] | +0.62 | +0.71 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF682]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 | same gene group |
| [[C5orf34]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPSNAP1]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ADA]] | -0.47 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[SBF2]] | -0.45 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF681]] | B | ZNF681 activity raises ZNF66's level | lines that do not express ZNF681 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without ZNF681 | 0.006 | ⚠ within organs, on part of the lines; also absent: RPSAP58, ZNF649, ZNF793 |
| [[ZNF736]] | B | ZNF736 activity raises ZNF66's level | lines that do not express ZNF736 (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without ZNF736 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, IQCA1 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF66's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF730]] | B | ZNF730 activity raises ZNF66's level | lines that do not express ZNF730 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without ZNF730 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF667, LINC03047, ENSG00000288016 |
| [[ZNF525]] | B | ZNF525 activity raises ZNF66's level | lines that do not express ZNF525 (10) vs lines expressing it (40) | 3.11× lower at baseline in the lines without ZNF525 | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF331, ZNF577, ZNF83 |
| [[ZNF486]] | B | ZNF486 activity raises ZNF66's level | lines that do not express ZNF486 (22) vs lines expressing it (28) | 1.68× lower at baseline in the lines without ZNF486 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, CDK15, ENSG00000287335 |
| [[ZNF682]] | B | ZNF682 activity raises ZNF66's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 2.11× lower at baseline in the lines without ZNF682 | 0.071 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3 |
| [[ZNF85]] | C | ZNF85 activity raises ZNF66's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 2.88× lower at baseline in the lines without ZNF85 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726; co-absent with the target |
| [[ZNF724]] | C | ZNF724 activity raises ZNF66's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 3.61× lower at baseline in the lines without ZNF724 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises ZNF66's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without MYBL2 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[ZNF726]] | C | ZNF726 activity raises ZNF66's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without ZNF726 | 0.072 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES; co-absent with the target |
| [[ZNF100]] | C | ZNF100 activity raises ZNF66's level | lines that do not express ZNF100 (9) vs lines expressing it (41) | 3.00× lower at baseline in the lines without ZNF100 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF66, ENSG00000269237, SORT1; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF736]] | B | ZNF66 activity raises ZNF736's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 4.05× lower at baseline in the lines without ZNF66 | 0.024 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF519]] | B | ZNF66 activity raises ZNF519's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without ZNF66 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF253]] | B | ZNF66 activity raises ZNF253's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without ZNF66 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[FANCD2]] | B | ZNF66 activity raises FANCD2's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.25× lower at baseline in the lines without ZNF66 | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF700]] | B | ZNF66 activity raises ZNF700's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without ZNF66 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF486]] | B | ZNF66 activity raises ZNF486's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 2.60× lower at baseline in the lines without ZNF66 | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[WDHD1]] | B | ZNF66 activity raises WDHD1's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without ZNF66 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF525]] | B | ZNF66 activity raises ZNF525's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 2.52× lower at baseline in the lines without ZNF66 | 0.045 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[RAD51AP1]] | B | ZNF66 activity raises RAD51AP1's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without ZNF66 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF680]] | B | ZNF66 activity raises ZNF680's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.45× lower at baseline in the lines without ZNF66 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[RNASEH2A]] | B | ZNF66 activity raises RNASEH2A's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without ZNF66 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[ZNF675]] | B | ZNF66 activity raises ZNF675's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 2.25× lower at baseline in the lines without ZNF66 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-44.8, -46.9); signed map (-39.7, -35.6). **Vector** length 38.5, 4.63% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of endogenous retroelements by KRAB-ZFP proteins* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.2 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +2.1 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.0 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.6 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +0.8 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +2.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 66 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:20,776,304-20,809,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16537; previously ZNF66P |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN08](https://www.uniprot.org/uniprotkb/Q6ZN08) (Zinc finger protein 66):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7617](https://www.ncbi.nlm.nih.gov/gene/7617):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13135) · Entrez [7617](https://www.ncbi.nlm.nih.gov/gene/7617) · UniProt [Q6ZN08](https://www.uniprot.org/uniprotkb/Q6ZN08) · Ensembl [ENSG00000160229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160229)

## Data

Gene col 8327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8327); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8327]; `tensor/DDL_lfc|DDL_z.npy` [8327]; `embed/gene_vectors.npy` [8327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8327 or target_col == 8327). Every well: [[ZNF66 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF66.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
