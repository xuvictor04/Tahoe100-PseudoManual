---
symbol: "UNC5C"
type: "gene"
col: 11251
ensembl_id: "ENSG00000182168"
name: "unc-5 netrin receptor C"
location: "4q22.3"
module: 9
arm: "+"
pooled_cpm: 10.61
n_lines_expressing: 19
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# UNC5C

*unc-5 netrin receptor C* — 4q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.49× (z +18.1, q 0e+00, up in 10 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.106×, SNU-1 0.203×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.164×, SNU-1 0.181×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.252×, SNU-1 0.377×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NREP]] (+0.71, fdr 1e-05), [[ANGPT1]] (+0.71, fdr 7e-06), [[LINC01013]] (+0.70, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LRP1B]] → it (grade B ⚠); 6 go from it, the strongest it → [[HOXD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +18.1 | 0e+00 | 10/16 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +12.3 | 3e-32 | 4/13 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +9.9 | 1e-20 | 6/16 (CFPAC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +7.9 | 3e-13 | 2/13 (CFPAC-1, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +7.0 | 2e-10 | 10/17 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.78×** | +5.9 | 4e-07 | 5/17 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.8 | 5e-07 | 4/16 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.8 | 1e-04 | 3/15 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.60×** | +4.6 | 3e-04 | 0/16 | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.5 | 4e-04 | 7/14 (H4, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 7e-04 | 8/17 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.003 | 8/17 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.7 | 0.008 | 3/16 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.017 | 8/16 (A-427, BT-474, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.017 | 8/16 (SW 900, A-427, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.074 | 4/16 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.106×, SNU-1 0.203×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.164×, SNU-1 0.181×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CHP-212 0.252×, SNU-1 0.377×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.727× | -3.0 | 0.54 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 45.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -10.5) |
| [[SNU-1 (line)]] | wt | 143 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -10.1) |
| [[CHP-212 (line)]] | wt | 443 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.5) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0633× (z -8.8) |
| [[A-172 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NREP]] | +0.71 | +0.52 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[ANGPT1]] | +0.71 | +0.58 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC01013]] | +0.70 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[COL11A1]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[HMCN1]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 | same gene group |
| [[MIR99AHG]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPHA5]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DMD]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[MMRN1]] | +0.65 | +0.57 / +0.66 | both halves | 8e-06 |  |
| [[PCDH18]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EPHA7]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP1B]] | B | LRP1B activity lowers UNC5C's level | lines that do not express LRP1B (24) vs lines expressing it (26) | 1.10× higher at baseline in the lines without LRP1B | 0.040 | ⚠ within organs, on part of the lines; also absent: GLRB, VEGFC, SPANXA2-OT1; maybe low, not absent |
| [[CUBN]] | B | CUBN activity raises UNC5C's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without CUBN | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[HOXD3]] | B | HOXD3 activity raises UNC5C's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 2.86× lower at baseline in the lines without HOXD3 | 0.069 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14 |
| [[TOP2A]] | B | TOP2A activity lowers UNC5C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GCG]] | C | GCG activity raises UNC5C's level | lines that do not express GCG (46) vs lines expressing it (4) | 4.77× lower at baseline in the lines without GCG | 0.036 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises UNC5C's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without PCDH18 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises UNC5C's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without MMRN1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises UNC5C's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 4.73× lower at baseline in the lines without MIR99AHG | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXD3]] | B | UNC5C activity raises HOXD3's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without UNC5C | 0.027 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent |
| [[LINC02941]] | C | UNC5C activity raises LINC02941's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without UNC5C | 0.053 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |
| [[LHFPL3-AS1]] | C | UNC5C activity raises LHFPL3-AS1's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without UNC5C | 0.082 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |
| [[SNCA]] | C | UNC5C activity raises SNCA's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without UNC5C | 0.089 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |
| [[LINC02240]] | C | UNC5C activity raises LINC02240's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 1.74× lower at baseline in the lines without UNC5C | 0.092 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |
| [[TYR]] | C | UNC5C activity raises TYR's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without UNC5C | 0.097 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 30.8); signed map (37.7, 33.7). **Vector** length 44.7, 11.2% of its response variance represented; |z| ≥ 3 in 413 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -0.8 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | +0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | unc-5 netrin receptor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.3 — chr4:95,162,504-95,549,206 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | I-set domain containing; ZU5 domain containing |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 4 pathways, smallest: Netrin mediated repulsion signals; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O95185](https://www.uniprot.org/uniprotkb/O95185) (Netrin receptor UNC5C):

> Receptor for netrin required for axon guidance (By similarity). Mediates axon repulsion of neuronal growth cones in the developing nervous system upon ligand binding (By similarity). NTN1/Netrin-1 binding might cause dissociation of UNC5C from polymerized TUBB3 in microtubules and thereby lead to increased microtubule dynamics and axon repulsion. Might also collaborate with DSCAM in NTN1-mediated axon repulsion independently of DCC (By similarity). Also involved in corticospinal tract axon …

**Summary**, from NCBI Gene [8633](https://www.ncbi.nlm.nih.gov/gene/8633):

> This gene product belongs to the UNC-5 family of netrin receptors. Netrins are secreted proteins that direct axon extension and cell migration during neural development. They are bifunctional proteins that act as attractants for some cell types and as repellents for others, and these opposite actions are thought to be mediated by two classes of receptors. The UNC-5 family of receptors mediate the repellent response to netrin; they are transmembrane proteins containing 2 immunoglobulin (Ig)-like …

**Accessions** — [HGNC:12569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12569) · Entrez [8633](https://www.ncbi.nlm.nih.gov/gene/8633) · UniProt [O95185](https://www.uniprot.org/uniprotkb/O95185) · Ensembl [ENSG00000182168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182168)

## Data

Gene col 11251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11251); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11251]; `tensor/DDL_lfc|DDL_z.npy` [11251]; `embed/gene_vectors.npy` [11251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11251 or target_col == 11251). Every well: [[UNC5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
