---
symbol: "ARHGAP40"
type: "gene"
col: 4484
ensembl_id: "ENSG00000124143"
name: "Rho GTPase activating protein 40"
location: "20q11.23"
module: 14
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ARHGAP40

*Rho GTPase activating protein 40* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.16× (z +17.9, q 0e+00, up in 13 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.132×, NCI-H2030 0.0785×, RKO 0.166×; ⚠ cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0885×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.125×; ⚠ cell-cycle shift, explains ~54% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0507×); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0586×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNQ4]] (+0.58, fdr 2e-05), [[LINC00460]] (+0.57, fdr 2e-05), [[ZNF385C]] (+0.56, fdr 1e-05); moves opposite to [[FAM227A]] (-0.48, fdr 1e-04), [[C2CD3]] (-0.43, fdr 3e-04), [[KIAA2026]] (-0.43, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SUN3]] → it (grade B ⚠); 4 go from it, the strongest it → [[PTX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.16×** | +17.9 | 0e+00 | 13/20 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +12.9 | 1e-35 | 9/21 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.69×** | +8.8 | 2e-16 | 12/20 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +7.8 | 1e-12 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.6 | 3e-12 | 14/26 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +7.4 | 9e-12 | 8/23 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +6.9 | 6e-10 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 11/23 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.46×** | +4.8 | 1e-04 | 6/26 (NCI-H2347, HCT15, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.8 | 1e-04 | 1/8 (SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.3 | 8e-04 | 1/13 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.006 | 0/20 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.8 | 0.007 | 0/5 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.8 | 0.007 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.035 | 4/13 (A-427, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.045 | 6/27 (RKO, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4484.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.132×, NCI-H2030 0.0785×, RKO 0.166×; ⚠ cell-cycle shift, explains <1% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0885×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.125×; ⚠ cell-cycle shift, explains ~54% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0507×); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.0586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[venetoclax (drug)]] 0.05 µM |  | 0.696× | -3.0 | 0.61 | 3/25 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 122× (z +16.0) | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -10.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 9.35 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -11.5) ⚠ cell-cycle shift, explains <1% of this change |
| [[CFPAC-1 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 9.15 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0586× (z -9.3) |
| [[HOP62 (line)]] | alt | 1.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.0× (z +12.5) | — |
| [[J82 (line)]] | alt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.9× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 6.18 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0785× (z -9.8) ⚠ cell-cycle shift, explains <1% of this change |
| [[NCI-H2347 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0885× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 0.997 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.89 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0507× (z -10.0) |
| [[SNU-423 (line)]] | alt | 1.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.6× (z +14.5) | — |
| [[A-427 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.738 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.845 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.838 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNQ4]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ZNF385C]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CA13]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[EBI3]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EMILIN2]] | +0.54 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PLLP]] | +0.53 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SCN1B]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ICAM2]] | +0.50 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[EPHX4]] | +0.50 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[SCARF1]] | +0.50 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[RBMXL1]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM227A]] | -0.48 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[C2CD3]] | -0.43 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[KIAA2026]] | -0.43 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[CETN2]] | -0.41 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUN3]] | B | SUN3 activity raises ARHGAP40's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without SUN3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises ARHGAP40's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 1.72× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[KCNK5]] | B | KCNK5 activity raises ARHGAP40's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without KCNK5 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTX3]] | B | ARHGAP40 activity raises PTX3's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without ARHGAP40 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[FHL3]] | B | ARHGAP40 activity raises FHL3's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without ARHGAP40 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[SLC2A14]] | B | ARHGAP40 activity raises SLC2A14's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ARHGAP40 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[STX11]] | B | ARHGAP40 activity raises STX11's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without ARHGAP40 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.333). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, 21.9); signed map (13.1, 25.1). **Vector** length 47.9, 9.07% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +17.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,601,809-38,651,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1100H13.4; previously C20orf95 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TG30](https://www.uniprot.org/uniprotkb/Q5TG30) (Rho GTPase-activating protein 40):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [343578](https://www.ncbi.nlm.nih.gov/gene/343578):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of actin filament polymerization and regulation of small GTPase mediated signal transduction. Predicted to be located in cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16226) · Entrez [343578](https://www.ncbi.nlm.nih.gov/gene/343578) · UniProt [Q5TG30](https://www.uniprot.org/uniprotkb/Q5TG30) · Ensembl [ENSG00000124143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124143)

## Data

Gene col 4484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4484); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4484]; `tensor/DDL_lfc|DDL_z.npy` [4484]; `embed/gene_vectors.npy` [4484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4484 or target_col == 4484). Every well: [[ARHGAP40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
