---
symbol: "HS6ST3"
type: "gene"
col: 11667
ensembl_id: "ENSG00000185352"
name: "heparan sulfate 6-O-sulfotransferase 3"
location: "13q32.1"
module: 61
arm: "+"
pooled_cpm: 11.01
n_lines_expressing: 31
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# HS6ST3

*heparan sulfate 6-O-sulfotransferase 3* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.73× (z +30.8, q 0e+00, up in 21 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.0464×; ⚠ toxic; cell-cycle shift, explains ~59% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.0590×; ⚠ cell-cycle shift, explains ~71% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.185×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHB1]] (+0.69, fdr 7e-06), [[DACH2]] (+0.68, fdr 7e-06), [[SGCZ]] (+0.68, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[MTUS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.73×** | +30.8 | 0e+00 | 21/26 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **5.19×** | +26.6 | 0e+00 | 24/27 (NCI-H460, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **7.88×** | +23.6 | 0e+00 | 27/28 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.44×** | +19.3 | 0e+00 | 25/27 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.70×** | +17.7 | 0e+00 | 26/27 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +15.3 | 0e+00 | 16/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.26×** | +13.5 | 2e-39 | 22/27 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.21×** | +11.9 | 5e-31 | 25/28 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.84×** | +11.9 | 7e-31 | 18/26 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +10.6 | 1e-24 | 5/15 (BT-474, A498, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +10.2 | 2e-22 | 6/20 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +10.1 | 2e-22 | 14/21 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +10.0 | 4e-22 | 16/25 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.7 | 1e-20 | 15/28 (J82, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.27×** | +9.0 | 9e-18 | 2/10 (PANC-1, BT-474) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.13×** | +8.5 | 9e-16 | 19/28 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +7.7 | 6e-13 | 15/25 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +7.2 | 2e-11 | 10/23 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.0464×; ⚠ toxic; cell-cycle shift, explains ~59% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.0590×; ⚠ cell-cycle shift, explains ~71% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.185×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -4.8 | 0.001 | 10/30 (NCI-H460, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.47 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.9× (z +19.6) | — |
| [[J82 (line)]] | alt | 21.2 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.56× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0464× (z -15.7) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[PANC-1 (line)]] | alt | 3.57 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 51.4× (z +15.6) | — |
| [[A-427 (line)]] | wt | 4.76 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 11.6× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0590× (z -9.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H1573 (line)]] | alt | 66.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.47× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -8.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.80 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 33.6× (z +13.9) | — |
| [[A498 (line)]] | wt | 3.14 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.0× (z +14.9) | — |
| [[LoVo (line)]] | wt | 7.38 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.32× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 3.26 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 20.2× (z +13.0) | — |
| [[A-172 (line)]] | wt | 3.68 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.49× (z +9.4) | — |
| [[A549 (line)]] | wt | 3.25 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +12.2) | — |
| [[C32 (line)]] | wt | 2.88 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 57.1× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 2.96 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.1× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 24.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.63× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHB1]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DACH2]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 | same gene group |
| [[AFF2]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.65 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.64 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[SYN1]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[XKR4]] | +0.63 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ALK]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.61 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PLD5]] | +0.61 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HS6ST3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CACNA1C]] | B | CACNA1C activity raises HS6ST3's level | lines that do not express CACNA1C (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without CACNA1C | 0.090 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, PSD2, LINC01579; maybe low, not absent |
| [[ADAM28]] | B | ADAM28 activity raises HS6ST3's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.37× lower at baseline in the lines without ADAM28 | 0.099 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS2]] | B | HS6ST3 activity raises MTUS2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without HS6ST3 | 0.031 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[ATP8A2]] | B | HS6ST3 activity raises ATP8A2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without HS6ST3 | 0.071 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[IL3RA]] | B | HS6ST3 activity strengthens IL3RA's drug response | lines that do not express HS6ST3 (19) vs lines expressing it (29) | the lines without HS6ST3 respond 0.71× as strongly (z diff +1.16); strongest at Panobinostat 5 µM: 1.55x vs 2.61x (z diff +2.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PPP1R14C]] | B | HS6ST3 activity raises PPP1R14C's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without HS6ST3 | 0.087 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| cells under [[Vortioxetine (drug)]] 5 µM | B | HS6ST3 activity lowers the cells' numbers under Vortioxetine 5 µM (makes them more sensitive) | lines that do not express HS6ST3 (19) vs lines expressing it (29) | the lines without HS6ST3: 1.17× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[SRRM3]] | B | HS6ST3 activity raises SRRM3's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without HS6ST3 | 0.096 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[ENTREP2]] | C | HS6ST3 activity raises ENTREP2's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without HS6ST3 | 0.051 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 32.3); signed map (31.6, 19.8). **Vector** length 55.9, 11.2% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +26.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.6 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +8.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | +1.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | heparan sulfate 6-O-sulfotransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:96,090,107-96,839,562 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sulfotransferases, membrane bound; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZP7](https://www.uniprot.org/uniprotkb/Q8IZP7) (Heparan-sulfate 6-O-sulfotransferase 3):

> 6-O-sulfation enzyme which catalyzes the transfer of sulfate from 3'-phosphoadenosine 5'-phosphosulfate (PAPS) to position 6 of the N-sulfoglucosamine residue (GlcNS) of heparan sulfate.

**Summary**, from NCBI Gene [266722](https://www.ncbi.nlm.nih.gov/gene/266722):

> Heparan sulfate (HS) sulfotransferases, such as HS6ST3, modify HS to generate structures required for interactions between HS and a variety of proteins. These interactions are implicated in proliferation and differentiation, adhesion, migration, inflammation, blood coagulation, and other diverse processes (Habuchi et al., 2000 [PubMed 10644753]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19134) · Entrez [266722](https://www.ncbi.nlm.nih.gov/gene/266722) · UniProt [Q8IZP7](https://www.uniprot.org/uniprotkb/Q8IZP7) · Ensembl [ENSG00000185352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185352)

## Data

Gene col 11667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11667); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11667]; `tensor/DDL_lfc|DDL_z.npy` [11667]; `embed/gene_vectors.npy` [11667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11667 or target_col == 11667). Every well: [[HS6ST3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS6ST3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
