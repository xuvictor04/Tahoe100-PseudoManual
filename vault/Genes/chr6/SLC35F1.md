---
symbol: "SLC35F1"
type: "gene"
col: 12193
ensembl_id: "ENSG00000196376"
name: "solute carrier family 35 member F1"
location: "6q22.2-q22.31"
module: 61
arm: "+"
pooled_cpm: 4.12
n_lines_expressing: 45
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 34
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SLC35F1

*solute carrier family 35 member F1* — 6q22.2-q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 22.1× (z +42.4, q 0e+00, up in 27 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.219×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR4]] (+0.78, fdr 7e-06), [[GRIA4]] (+0.76, fdr 7e-06), [[SGCZ]] (+0.75, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[B4GAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **22.1×** | +42.4 | 0e+00 | 27/28 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **11.5×** | +22.8 | 0e+00 | 31/33 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.83×** | +21.6 | 0e+00 | 23/27 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.08×** | +18.3 | 0e+00 | 23/26 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.78×** | +18.2 | 0e+00 | 30/39 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.59×** | +12.4 | 3e-33 | 25/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.51×** | +12.1 | 5e-32 | 25/40 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.4 | 3e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +8.9 | 5e-17 | 8/18 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +8.4 | 2e-15 | 23/34 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.27×** | +7.9 | 1e-13 | 22/38 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +7.9 | 1e-13 | 15/23 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +7.7 | 4e-13 | 1/5 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +7.5 | 4e-12 | 20/38 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.1 | 4e-11 | 15/40 (PANC-1, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +6.4 | 4e-09 | 11/32 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +6.3 | 8e-09 | 12/33 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +6.0 | 5e-08 | 16/39 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +5.9 | 1e-07 | 18/40 (NCI-H460, SNU-423, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12193.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.219×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -4.4 | 0.006 | 11/42 (A-427, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.23 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.3× (z +17.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.32 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.3× (z +17.3) | — |
| [[PANC-1 (line)]] | alt | 1.77 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 85.5× (z +19.5) | — |
| [[SK-MEL-2 (line)]] | alt | 93.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +27.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.8) |
| [[A-172 (line)]] | wt | 2.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 172× (z +17.8) | — |
| [[A498 (line)]] | wt | 1.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.0× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 2.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.5× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 2.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.3× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 113× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 5.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 8.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.0× (z +15.7) | — |
| [[A549 (line)]] | wt | 3.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 4.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 21.2× (z +9.4) | — |
| [[C32 (line)]] | wt | 2.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.2× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.8× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 1.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 1.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 101× (z +13.4) | — |
| [[J82 (line)]] | alt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 109× (z +16.0) | — |
| [[LoVo (line)]] | wt | 1.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 42.1× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.5× (z +13.3) | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 17.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.42× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 3.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 79.9× (z +14.7) | — |
| [[SW480 (line)]] | alt | 1.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.0) | — |
| [[A-427 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.923 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR4]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.71 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ACTN2]] | +0.69 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[ENTHD1]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NDRG4]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC35F1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.1% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NPFFR2]] | B | NPFFR2 activity raises SLC35F1's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 2.42× lower at baseline in the lines without NPFFR2 | 0.037 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[ZFPM2]] | B | ZFPM2 activity raises SLC35F1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without ZFPM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[PCSK2]] | B | PCSK2 activity raises SLC35F1's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without PCSK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[LINC01320]] | B | LINC01320 activity raises SLC35F1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.39× lower at baseline in the lines without LINC01320 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[LINC00457]] | B | LINC00457 activity raises SLC35F1's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without LINC00457 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GAT1]] | B | SLC35F1 activity raises B4GAT1's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without SLC35F1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[PIK3CD]] | B | SLC35F1 activity raises PIK3CD's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without SLC35F1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[EBI3]] | B | SLC35F1 activity raises EBI3's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without SLC35F1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[SSTR2]] | B | SLC35F1 activity raises SSTR2's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without SLC35F1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[GABBR1]] | B | SLC35F1 activity raises GABBR1's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 3.50× lower at baseline in the lines without SLC35F1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 30.9); signed map (34.6, 21.0). **Vector** length 66.4, 11.9% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +18.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +42.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.2-q22.31 — chr6:117,907,264-118,317,676 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ230I3.1; previously C6orf169 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1Q4](https://www.uniprot.org/uniprotkb/Q5T1Q4) (Solute carrier family 35 member F1):

> Putative solute transporter.

**Summary**, from NCBI Gene [222553](https://www.ncbi.nlm.nih.gov/gene/222553):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Located in synaptic vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21483) · Entrez [222553](https://www.ncbi.nlm.nih.gov/gene/222553) · UniProt [Q5T1Q4](https://www.uniprot.org/uniprotkb/Q5T1Q4) · Ensembl [ENSG00000196376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196376)

## Data

Gene col 12193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12193); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12193]; `tensor/DDL_lfc|DDL_z.npy` [12193]; `embed/gene_vectors.npy` [12193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12193 or target_col == 12193). Every well: [[SLC35F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
