---
symbol: "GLS2"
type: "gene"
col: 5701
ensembl_id: "ENSG00000135423"
name: "glutaminase 2"
location: "12q13.3"
module: 62
arm: "+"
pooled_cpm: 3.3
n_lines_expressing: 36
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# GLS2

*glutaminase 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +12.7, q 4e-34, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.639× (z -4.4, q 0.007, down in 8 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW1417 0.0907×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.405×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK8]] (+0.64, fdr 7e-06), [[ZNF423]] (+0.63, fdr 1e-05), [[PINCR]] (+0.61, fdr 1e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ENTHD1]] → it (grade B ⚠); 10 go from it, the strongest it → [[SCAMP5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +12.7 | 4e-34 | 18/24 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +11.1 | 5e-26 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.20×** | +7.6 | 8e-12 | 3/10 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +7.5 | 1e-11 | 2/6 (NCI-H2347, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.1 | 1e-10 | 14/27 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +6.9 | 4e-10 | 5/13 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.7 | 2e-09 | 9/27 (LoVo, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +6.5 | 5e-09 | 10/20 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.83×** | +5.8 | 4e-07 | 13/31 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.83×** | +5.8 | 5e-07 | 14/29 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +5.5 | 2e-06 | 7/27 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 4e-06 | 15/26 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.0 | 3e-05 | 7/24 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.68×** | +5.0 | 3e-05 | 10/29 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.8 | 6e-05 | 7/29 (LoVo, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.7 | 9e-05 | 10/27 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.65×** | +4.4 | 3e-04 | 6/16 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +4.2 | 9e-04 | 5/24 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 1e-03 | 4/19 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.003 | 11/30 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Orlistat (drug)]] 0.05 µM |  | **1.52×** | +3.7 | 0.005 | 2/18 (SW48, HEC-1-A) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.011 | 1/17 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW1417 0.0907×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.405×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -4.4 | 0.007 | 8/27 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.731× | -3.0 | 0.65 | 11/26 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.30 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 1.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 5.39 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0907× (z -9.5) |
| [[SW480 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.4) |
| [[A-172 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.818 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.845 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK8]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZNF423]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PINCR]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FDXR]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 742 |
| [[SPATA18]] | +0.57 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[EDA2R]] | +0.53 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[GDF15]] | +0.52 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[DDB2]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[TYMSOS]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[HES6]] | +0.52 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[LIF-AS2]] | +0.52 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[HTR2C]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTHD1]] | B | ENTHD1 activity lowers GLS2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.15× higher at baseline in the lines without ENTHD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[TOP2A]] | B | TOP2A activity lowers GLS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens GLS2's drug response | lines that do not express PINCR (21) vs lines expressing it (10) | the lines without PINCR respond 1.05× as strongly (z diff -0.05); strongest at Doxorubicin (hydrochloride) 5 µM: 1.63x vs 4.95x (z diff +3.9) | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; the reference differs; artifact flags |
| [[HES6]] | B | HES6 activity raises GLS2's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without HES6 | 0.062 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises GLS2's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.97× lower at baseline in the lines without CYFIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[ROR2]] | B | ROR2 activity raises GLS2's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without ROR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |
| [[GRIN2C]] | B | GRIN2C activity raises GLS2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without GRIN2C | 0.099 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens GLS2's drug response | recorded loss-of-function mutation of TP53 in 22 lines vs 9 not recorded | the TP53-altered lines respond 0.92× as strongly (z diff +0.19); strongest at Doxorubicin (hydrochloride) 5 µM: 1.62x vs 7.89x (z diff +5.3) | 0.621 over the table, 0.036 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAMP5]] | B | GLS2 activity raises SCAMP5's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without GLS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[CEP85L]] | B | GLS2 activity lowers CEP85L's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 2.08× higher at baseline in the lines without GLS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[ZFPM1]] | B | GLS2 activity lowers ZFPM1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without GLS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[DRAM1]] | B | GLS2 activity lowers DRAM1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.86× higher at baseline in the lines without GLS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[TCP11L1]] | B | GLS2 activity lowers TCP11L1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.65× higher at baseline in the lines without GLS2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[TCP11L1]] | B | GLS2 activity weakens TCP11L1's drug response | lines that do not express GLS2 (14) vs lines expressing it (34) | the lines without GLS2 respond 1.73× as strongly (z diff -2.54); strongest at Belinostat 5 µM: 0.45x vs 0.65x (z diff -4.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[STX6]] | B | GLS2 activity lowers STX6's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.23× higher at baseline in the lines without GLS2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| cells under [[Panobinostat (drug)]] 5 µM | B | GLS2 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express GLS2 (14) vs lines expressing it (34) | the lines without GLS2: 0.67× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[CDIP1]] | B | GLS2 activity raises CDIP1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.08× lower at baseline in the lines without GLS2 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[DYRK3]] | B | GLS2 activity lowers DYRK3's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 2.78× higher at baseline in the lines without GLS2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 36.9); signed map (43.4, -22.8). **Vector** length 41.3, 6.61% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.0 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | glutaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,470,944-56,488,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GA, GLS, LGA, hLGA |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 8 pathways, smallest: Glutamate and glutamine metabolism; Glutamate Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI32](https://www.uniprot.org/uniprotkb/Q9UI32) (Glutaminase liver isoform, mitochondrial):

> Plays an important role in the regulation of glutamine catabolism. Promotes mitochondrial respiration and increases ATP generation in cells by catalyzing the synthesis of glutamate and alpha-ketoglutarate. Increases cellular anti-oxidant function via NADH and glutathione production. May play a role in preventing tumor proliferation.

**Summary**, from NCBI Gene [27165](https://www.ncbi.nlm.nih.gov/gene/27165):

> The protein encoded by this gene is a mitochondrial phosphate-activated glutaminase that catalyzes the hydrolysis of glutamine to stoichiometric amounts of glutamate and ammonia. Originally thought to be liver-specific, this protein has been found in other tissues as well. Alternative splicing results in multiple transcript variants that encode different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:29570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29570) · Entrez [27165](https://www.ncbi.nlm.nih.gov/gene/27165) · UniProt [Q9UI32](https://www.uniprot.org/uniprotkb/Q9UI32) · Ensembl [ENSG00000135423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135423)

## Data

Gene col 5701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5701); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5701]; `tensor/DDL_lfc|DDL_z.npy` [5701]; `embed/gene_vectors.npy` [5701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5701 or target_col == 5701). Every well: [[GLS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
