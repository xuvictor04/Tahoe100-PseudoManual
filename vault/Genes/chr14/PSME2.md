---
symbol: "PSME2"
type: "gene"
col: 2042
ensembl_id: "ENSG00000100911"
name: "proteasome activator subunit 2"
location: "14q12"
module: 70
arm: "+"
pooled_cpm: 65.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PSME2

*proteasome activator subunit 2* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +8.5, q 1e-14, up in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2030 3.07×, HOP62 3.73×, NCI-H460 3.14×, SW480 2.87×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (SNU-423 3.92×, hTERT-HPNE 3.99×, AsPC-1 3.41×, CFPAC-1 2.88×, …; ⚠ cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HOP62 7.51×, NCI-H460 5.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAP1]] (+0.81, fdr 7e-06), [[PSMB9]] (+0.80, fdr 7e-06), [[ISG15]] (+0.79, fdr 7e-06); moves opposite to [[MAPKAPK3]] (-0.58, fdr 2e-05), [[PAFAH1B2]] (-0.57, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2042.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H2030 3.07×, HOP62 3.73×, NCI-H460 3.14×, SW480 2.87×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (SNU-423 3.92×, hTERT-HPNE 3.99×, AsPC-1 3.41×, CFPAC-1 2.88×, …; ⚠ cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HOP62 7.51×, NCI-H460 5.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +8.5 | 1e-14 | 46/48 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.94×** | +6.9 | 1e-09 | 36/48 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **2.40×** | +6.6 | 6e-09 | 44/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **2.15×** | +5.8 | 1e-06 | 46/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.21×** | +5.8 | 1e-06 | 43/48 (hTERT-HPNE, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.20×** | +5.7 | 1e-06 | 36/41 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.05×** | +5.4 | 5e-06 | 41/48 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.1 | 3e-05 | 40/47 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.84×** | +4.6 | 3e-04 | 40/48 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.81×** | +4.3 | 1e-03 | 42/48 (HOP62, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.69×** | +4.0 | 0.004 | 37/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +3.9 | 0.004 | 35/48 (C32, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.63×** | +3.7 | 0.010 | 33/48 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.047 | 28/48 (HOP62, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **1.56×** | +3.2 | 0.047 | 25/47 (MIA PaCa-2, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | 0.747× | -3.0 | 0.53 | 25/48 (LoVo, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 21.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.51× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 56.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.8) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.2) | — |
| [[C32 (line)]] | wt | 33.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.2) | — |
| [[J82 (line)]] | alt | 69.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 48.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.3) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.4) | — |
| [[SW480 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.3) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 53.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.2) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.8) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[NCI-H2030 (line)]] | alt | 91.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.2) | — |
| [[A-172 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAP1]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 586 |
| [[PSMB9]] | +0.80 | +0.68 / +0.85 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 990 |
| [[ISG15]] | +0.79 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 577 |
| [[HLA-B]] | +0.78 | +0.62 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[HLA-F]] | +0.77 | +0.61 / +0.77 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 452 |
| [[GBP4]] | +0.77 | +0.62 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 407 |
| [[B2M]] | +0.76 | +0.67 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 634 |
| [[TRIM5]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IRF7]] | +0.72 | +0.58 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMB10]] | +0.72 | +0.51 / +0.78 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 979 |
| [[IFI27]] | +0.71 | +0.54 / +0.75 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMB8]] | +0.71 | +0.59 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 987 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK3]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[PAFAH1B2]] | -0.57 | -0.62 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PSME2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IFI44L]] | B | IFI44L activity raises PSME2's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without IFI44L | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[SLC37A1]] | B | SLC37A1 activity raises PSME2's level | lines that do not express SLC37A1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without SLC37A1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RSPH1, GRTP1, ABCA3; its own permutation p |
| [[BATF2]] | B | BATF2 activity raises PSME2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without BATF2 | 0.060 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[SP110]] | B | SP110 activity raises PSME2's level | lines that do not express SP110 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SP110 | 0.084 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[IFIH1]] | C | IFIH1 activity raises PSME2's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 1.52× lower at baseline in the lines without IFIH1 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent |
| [[ISG15]] | C | ISG15 activity raises PSME2's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ISG15 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[IFIT1]] | C | IFIT1 activity raises PSME2's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without IFIT1 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.2, 50.6); signed map (64.0, 28.3). **Vector** length 93.8, 38.5% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.66 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.65 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.66 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.0 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.3 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +3.1 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -5.8 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -5.6 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | proteasome activator subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,143,362-24,147,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PA28beta |
| Gene groups (HGNC) | Proteasome; MicroRNA protein coding host genes |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 12 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL46](https://www.uniprot.org/uniprotkb/Q9UL46) (Proteasome activator complex subunit 2):

> Implicated in immunoproteasome assembly and required for efficient antigen processing. The PA28 activator complex enhances the generation of class I binding peptides by altering the cleavage pattern of the proteasome.

**Summary**, from NCBI Gene [5721](https://www.ncbi.nlm.nih.gov/gene/5721):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9569) · Entrez [5721](https://www.ncbi.nlm.nih.gov/gene/5721) · UniProt [Q9UL46](https://www.uniprot.org/uniprotkb/Q9UL46) · Ensembl [ENSG00000100911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100911)

## Data

Gene col 2042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2042); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2042]; `tensor/DDL_lfc|DDL_z.npy` [2042]; `embed/gene_vectors.npy` [2042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2042 or target_col == 2042). Every well: [[PSME2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSME2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
