---
symbol: "ZNF529-AS1"
type: "gene"
col: 13906
ensembl_id: "ENSG00000233527"
name: "ZNF529 antisense RNA 1"
location: "19q13.12"
module: 15
arm: "+"
pooled_cpm: 15.97
n_lines_expressing: 42
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 11
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZNF529-AS1

*ZNF529 antisense RNA 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.84× (z +13.8, q 1e-40, up in 34 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.449× (z -10.6, q 1e-23, down in 36 of 40 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.790× (z -4.4, q 6e-04, down in 19 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.0841×, HOP62 0.207×, C32 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.285×, HOP62 0.298×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (HOP62 0.212×, HEC-1-A 0.312×; ⚠ cell-cycle shift, explains ~62% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0804×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF345]] (+0.75, fdr 7e-06), [[SLC25A17]] (+0.74, fdr 7e-06), [[ZBTB8OS]] (+0.73, fdr 7e-06); moves opposite to [[THEM6]] (-0.64, fdr 4e-05), [[HLTF]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZNF382]] → it (grade B ⚠); 11 go from it, the strongest it → [[DOCK7-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +13.8 | 1e-40 | 34/39 (PANC-1, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.45×** | +6.9 | 1e-09 | 23/40 (HS-578T, NCI-H2030, …) | rises with dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.2 | 1e-07 | 20/39 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.9 | 5e-07 | 19/34 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.009 | 14/38 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.34×** | +3.6 | 0.025 | 13/40 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.6 | 0.025 | 12/39 (H4, HS-578T, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.051 | 9/40 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.051 | 11/39 (HOP62, Panc 03.27, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.056 | 13/39 (C32, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.10 | 8/39 (C32, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.0841×, HOP62 0.207×, C32 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.285×, HOP62 0.298×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (HOP62 0.212×, HEC-1-A 0.312×; ⚠ cell-cycle shift, explains ~62% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0804×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.449×** | -10.6 | 1e-23 | 36/40 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.495×** | -9.2 | 1e-17 | 29/40 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.547×** | -8.0 | 2e-13 | 27/39 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.629×** | -5.9 | 5e-07 | 19/37 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.685×** | -4.8 | 2e-04 | 19/39 (HOP62, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.698×** | -4.6 | 4e-04 | 13/21 (HEC-1-A, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **0.710×** | -4.5 | 4e-04 | 17/38 (H4, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.4 | 6e-04 | 19/40 (C32, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.742×** | -4.0 | 0.004 | 15/40 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.814×** | -3.9 | 0.006 | 19/39 (HEC-1-A, HOP62, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.008 | 14/39 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.788×** | -3.2 | 0.069 | 13/40 (SNU-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.789×** | -3.2 | 0.069 | 14/33 (HOP62, SK-MEL-2, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 51.8 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 42.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0850× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 3.23× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 4.39× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -11.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 23.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.40× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0841× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 8.02 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.88× (z +8.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 32.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +11.9) | — |
| [[RKO (line)]] | wt | 23.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.96× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -8.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 6.59 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0804× (z -9.4) |
| [[C32 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.120× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.218× (z -9.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF345]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.74 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB8OS]] | +0.73 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF234]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF778]] | +0.71 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[PGLS-DT]] | +0.70 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[GPN2]] | +0.70 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ZNF790]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.68 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[TAS2R4]] | +0.68 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZNF586]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[HLTF]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF382]] | B | ZNF382 activity raises ZNF529-AS1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 3.68× lower at baseline in the lines without ZNF382 | 5e-04 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[ARHGAP18]] | B | ARHGAP18 activity lowers ZNF529-AS1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 2.40× higher at baseline in the lines without ARHGAP18 | 0.012 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[LINC01535]] | B | LINC01535 activity raises ZNF529-AS1's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 2.40× lower at baseline in the lines without LINC01535 | 0.030 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |
| [[ZNF737]] | B | ZNF737 activity raises ZNF529-AS1's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 2.49× lower at baseline in the lines without ZNF737 | 0.039 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |
| [[ZNF808]] | B | ZNF808 activity raises ZNF529-AS1's level | lines that do not express ZNF808 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without ZNF808 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF468, ZNF28, ZNF888 |
| [[ZNF790]] | C | ZNF790 activity raises ZNF529-AS1's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 2.98× lower at baseline in the lines without ZNF790 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569; co-absent with the target |
| [[ZNF345]] | C | ZNF345 activity raises ZNF529-AS1's level | lines that do not express ZNF345 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without ZNF345 | 0.008 | ⚠ within organs, on part of the lines; also absent: ZNF790, DNAH14, ZNF606; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK7-DT]] | B | ZNF529-AS1 activity raises DOCK7-DT's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without ZNF529-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[FRG1HP]] | B | ZNF529-AS1 activity raises FRG1HP's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.55× lower at baseline in the lines without ZNF529-AS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF175]] | B | ZNF529-AS1 activity raises ZNF175's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 2.84× lower at baseline in the lines without ZNF529-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF493]] | B | ZNF529-AS1 activity raises ZNF493's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without ZNF529-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF91]] | B | ZNF529-AS1 activity raises ZNF91's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 2.11× lower at baseline in the lines without ZNF529-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF382]] | B | ZNF529-AS1 activity raises ZNF382's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 3.08× lower at baseline in the lines without ZNF529-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[NOXRED1]] | B | ZNF529-AS1 activity raises NOXRED1's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without ZNF529-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZBTB8OS]] | B | ZNF529-AS1 activity raises ZBTB8OS's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without ZNF529-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[CYP27A1]] | B | ZNF529-AS1 activity raises CYP27A1's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without ZNF529-AS1 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[ZNF345]] | C | ZNF529-AS1 activity raises ZNF345's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 6.07× lower at baseline in the lines without ZNF529-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2; co-absent with the target |
| [[ZNF790]] | C | ZNF529-AS1 activity raises ZNF790's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 4.55× lower at baseline in the lines without ZNF529-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.5, 24.7); signed map (1.6, -2.7). **Vector** length 89.8, 20.3% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.4 | +13.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.9 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.5 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.1 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.9 | -8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ZNF529 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.12 — chr19:36,573,070-36,594,712 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51275) · Entrez [101927599](https://www.ncbi.nlm.nih.gov/gene/101927599) · Ensembl [ENSG00000233527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233527)

## Data

Gene col 13906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13906); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13906]; `tensor/DDL_lfc|DDL_z.npy` [13906]; `embed/gene_vectors.npy` [13906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13906 or target_col == 13906). Every well: [[ZNF529-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF529-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
