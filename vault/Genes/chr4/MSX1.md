---
symbol: "MSX1"
type: "gene"
col: 8640
ensembl_id: "ENSG00000163132"
name: "msh homeobox 1"
location: "4p16.2"
module: 127
arm: "+"
pooled_cpm: 5.11
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# MSX1

*msh homeobox 1* — 4p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.01× (z +16.8, q 0e+00, up in 35 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 5 µM in 1 line (SHP-77 0.0393×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDX2]] (+0.67, fdr 7e-06), [[SPHK1]] (+0.67, fdr 7e-06), [[IRX5]] (+0.66, fdr 7e-06); moves opposite to [[PRPF8]] (-0.69, fdr 2e-05), [[MRPL42]] (-0.68, fdr 3e-05), [[EMC1]] (-0.67, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[LHPP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.01×** | +16.8 | 0e+00 | 35/35 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.85×** | +10.9 | 4e-25 | 26/30 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.87×** | +9.0 | 3e-17 | 36/38 (HOP62, SK-MEL-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.46×** | +6.6 | 5e-09 | 25/25 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **3.33×** | +6.4 | 2e-08 | 23/28 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.07×** | +6.0 | 2e-07 | 21/31 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.05×** | +5.9 | 2e-07 | 26/33 (A498, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.04×** | +5.9 | 2e-07 | 28/37 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.73×** | +5.7 | 6e-07 | 26/39 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +5.0 | 4e-05 | 20/31 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +4.8 | 8e-05 | 26/39 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.6 | 2e-04 | 24/40 (Hs 766T, A-172, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.19×** | +4.5 | 3e-04 | 21/35 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.18×** | +4.5 | 3e-04 | 25/40 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **2.06×** | +4.1 | 0.001 | 20/40 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +4.1 | 0.002 | 20/39 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +4.0 | 0.002 | 18/36 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.99×** | +3.9 | 0.003 | 21/37 (A498, HOP62, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.94×** | +3.8 | 0.004 | 18/38 (A-172, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8640.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Decitabine (drug)]] 5 µM in 1 line (SHP-77 0.0393×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentagastrin (drug)]] 5 µM |  | 0.661× | -3.4 | 0.34 | 14/42 (SW 1088, LoVo, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.671× | -3.2 | 0.34 | 18/39 (C-33 A, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.16 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +15.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +11.2) | — |
| [[A498 (line)]] | wt | 7.60 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.4) | — |
| [[CFPAC-1 (line)]] | alt | 6.08 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +13.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 5.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 8.52 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +8.7) | — |
| [[A-172 (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +11.8) | — |
| [[A549 (line)]] | wt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.0× (z +11.6) | — |
| [[C32 (line)]] | wt | 3.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.67× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +8.9) | — |
| [[J82 (line)]] | alt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.3) | — |
| [[LoVo (line)]] | wt | 6.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 1.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 3.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 6.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 5.09 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0393× (z -8.5) |
| [[SNU-423 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +10.0) | — |
| [[SW480 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.8) | — |
| [[A-427 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDX2]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SPHK1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[IRX5]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.66 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[ZBTB7A]] | +0.64 | +0.32 / +0.74 | both halves | 2e-04 |  |
| [[ZNF503]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ING2]] | +0.61 | +0.37 / +0.71 | both halves | 8e-05 |  |
| [[MILIP]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC00685]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.58 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[EGLN2]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ERVK3-1]] | +0.57 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF8]] | -0.69 | -0.47 / -0.76 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.68 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[EMC1]] | -0.67 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[SRP9]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SNRNP200]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.62 | -0.66 / -0.57 | both halves | 8e-06 |  |
| [[TAF6]] | -0.62 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[API5]] | -0.62 | -0.16 / -0.72 | ⚠ one half (not replicated) | 0.001 |  |
| [[NONO]] | -0.62 | -0.35 / -0.69 | both halves | 1e-04 |  |
| [[ATP5F1A]] | -0.61 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[AGO1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[CS]] | -0.60 | -0.35 / -0.62 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MSX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHO1]] | B | PLEKHO1 activity raises MSX1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without PLEKHO1 | 0.032 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[DPYSL3]] | B | DPYSL3 activity raises MSX1's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without DPYSL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |
| [[NKX3-1]] | B | NKX3-1 activity raises MSX1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.31× lower at baseline in the lines without NKX3-1 | 0.078 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHPP]] | B | MSX1 activity raises LHPP's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without MSX1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[AGO1]] | B | MSX1 activity raises AGO1's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MSX1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[RPGRIP1L]] | B | MSX1 activity raises RPGRIP1L's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 2.18× lower at baseline in the lines without MSX1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[SLMAP]] | B | MSX1 activity lowers SLMAP's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without MSX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[PHOSPHO2]] | B | MSX1 activity raises PHOSPHO2's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without MSX1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[HSPA1A]] | B | MSX1 activity lowers HSPA1A's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 2.46× higher at baseline in the lines without MSX1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[LIN7C]] | B | MSX1 activity lowers LIN7C's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without MSX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[DPYSL3]] | B | MSX1 activity raises DPYSL3's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 3.41× lower at baseline in the lines without MSX1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[EGLN2]] | B | MSX1 activity lowers EGLN2's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without MSX1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction -0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.2, -23.5); signed map (-3.5, 8.4). **Vector** length 60.1, 12.8% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.8 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.6 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | -2.2 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | msh homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.2 — chr4:4,859,665-4,863,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HYD1, OFC5; previously HOX7 |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Hallmark sets | ANGIOGENESIS, UV_RESPONSE_UP, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Specification of the neural plate border; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P28360](https://www.uniprot.org/uniprotkb/P28360) (Homeobox protein MSX-1):

> Acts as a transcriptional repressor (By similarity). Capable of transcription autoinactivation (By similarity). Binds to the consensus sequence 5'-C/GTAAT-3' in downstream activin regulatory elements (DARE) in the gene promoter, thereby repressing the transcription of CGA/alpha-GSU and GNRHR (By similarity). Represses transcription of myoblast differentiation factors (By similarity). Binds to core enhancer regions in target gene promoters of myoblast differentiation factors with binding …

**Summary**, from NCBI Gene [4487](https://www.ncbi.nlm.nih.gov/gene/4487):

> This gene encodes a member of the muscle segment homeobox gene family. The encoded protein functions as a transcriptional repressor during embryogenesis through interactions with components of the core transcription complex and other homeoproteins. It may also have roles in limb-pattern formation, craniofacial development, particularly odontogenesis, and tumor growth inhibition. Mutations in this gene, which was once known as homeobox 7, have been associated with nonsyndromic cleft lip with or …

**Accessions** — [HGNC:7391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7391) · Entrez [4487](https://www.ncbi.nlm.nih.gov/gene/4487) · UniProt [P28360](https://www.uniprot.org/uniprotkb/P28360) · Ensembl [ENSG00000163132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163132)

## Data

Gene col 8640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8640); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8640]; `tensor/DDL_lfc|DDL_z.npy` [8640]; `embed/gene_vectors.npy` [8640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8640 or target_col == 8640). Every well: [[MSX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
