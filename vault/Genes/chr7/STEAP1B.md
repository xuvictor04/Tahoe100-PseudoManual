---
symbol: "STEAP1B"
type: "gene"
col: 2685
ensembl_id: "ENSG00000105889"
name: "STEAP family member 1B"
location: "7p15.3"
module: 19
arm: "+"
pooled_cpm: 39.63
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# STEAP1B

*STEAP family member 1B* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +11.6, q 3e-28, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.05 µM: 0.725× (z -4.1, q 0.019, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.157×, NCI-H23 0.412×, SK-MEL-2 0.460×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.174×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.204×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.218×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (H4 0.181×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00922]] (+0.61, fdr 1e-05), [[LSAMP]] (+0.59, fdr 1e-05), [[BMPER]] (+0.56, fdr 1e-05); moves opposite to [[MRPS31P4]] (-0.46, fdr 2e-04), [[NET1]] (-0.45, fdr 1e-04), [[UNC93B1]] (-0.45, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PAPPA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +11.6 | 3e-28 | 40/46 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +11.1 | 2e-26 | 31/44 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.4 | 2e-11 | 23/33 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.9 | 5e-07 | 25/39 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.003 | 19/47 (A498, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.022 | 16/47 (NCI-H2347, LoVo, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.068 | 17/46 (SNU-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rucaparib (phosphate) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.071 | 10/47 (SW1417, SNU-1, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.2 | 0.071 | 13/47 (A498, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.27×** | +3.2 | 0.071 | 16/45 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.1 | 0.092 | 16/43 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.092 | 15/47 (NCI-H2347, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.26× | +3.0 | 0.11 | 13/46 (SW48, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2685.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 0.157×, NCI-H23 0.412×, SK-MEL-2 0.460×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.128×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.174×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.204×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.218×); [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (H4 0.181×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.05 µM |  | **0.725×** | -4.1 | 0.019 | 17/47 (NCI-H661, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.4 | 0.15 | 20/46 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | 0.771× | -3.4 | 0.15 | 13/47 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.790× | -3.2 | 0.19 | 9/47 (C-33 A, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 250 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 53.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -16.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[A498 (line)]] | wt | 25.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.1) | — |
| [[A549 (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +13.7) | — |
| [[H4 (line)]] | wt | 55.4 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.181× (z -9.7) |
| [[LoVo (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 26.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00922]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BMPER]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PCDH15]] | +0.55 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[LINC02755]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[LINC01684]] | +0.53 | +0.59 / +0.31 | both halves | 2e-04 |  |
| [[ANO3]] | +0.53 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[C12orf40]] | +0.53 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[SLCO1C1]] | +0.52 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[AQP4-AS1]] | +0.52 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[RIMS1]] | +0.52 | +0.50 / +0.43 | both halves | 4e-05 |  |
| [[BASP1-AS1]] | +0.51 | +0.48 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.46 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[NET1]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[UNC93B1]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[ABHD16A]] | -0.45 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[AGFG2]] | -0.45 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPPA]] | B | PAPPA activity raises STEAP1B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without PAPPA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[KCNMB2]] | B | KCNMB2 activity raises STEAP1B's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without KCNMB2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[GLIS3]] | B | GLIS3 activity raises STEAP1B's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without GLIS3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[HECW2]] | B | HECW2 activity raises STEAP1B's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without HECW2 | 0.058 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[MSC-AS1]] | B | MSC-AS1 activity raises STEAP1B's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without MSC-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[KCNMB2]] | B | KCNMB2 activity weakens STEAP1B's drug response | lines that do not express KCNMB2 (17) vs lines expressing it (30) | the lines without KCNMB2 respond 1.33× as strongly (z diff -0.44); strongest at Idarubicin (hydrochloride) 5 µM: 2.34x vs 1.52x (z diff -3.0) | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[CTNND2]] | B | CTNND2 activity raises STEAP1B's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.65× lower at baseline in the lines without CTNND2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[PCDH15]] | B | PCDH15 activity raises STEAP1B's level | lines that do not express PCDH15 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without PCDH15 | 0.097 | ⚠ within organs, on part of the lines; also absent: ANKRD7, ENSG00000236230, NR2F1; maybe low, not absent |
| [[PXDNL]] | C | PXDNL's natural level weakens STEAP1B's drug response | PXDNL's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.25; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, 33.9); signed map (42.0, 39.5). **Vector** length 75.0, 14.5% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | STEAP family member 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:22,419,444-22,727,613 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | STEAP family |
| Matched by | ensembl_id |

UniProt [Q6NZ63](https://www.uniprot.org/uniprotkb/Q6NZ63) carries no function annotation.

**Summary**, from NCBI Gene [256227](https://www.ncbi.nlm.nih.gov/gene/256227):

> Predicted to be located in membrane. Predicted to be active in endosome and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:41907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41907) · Entrez [256227](https://www.ncbi.nlm.nih.gov/gene/256227) · UniProt [Q6NZ63](https://www.uniprot.org/uniprotkb/Q6NZ63) · Ensembl [ENSG00000105889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105889)

## Data

Gene col 2685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2685); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2685]; `tensor/DDL_lfc|DDL_z.npy` [2685]; `embed/gene_vectors.npy` [2685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2685 or target_col == 2685). Every well: [[STEAP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
