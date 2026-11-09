---
symbol: "KRT81"
type: "gene"
col: 12979
ensembl_id: "ENSG00000205426"
name: "keratin 81"
location: "12q13.13"
module: 136
arm: "+"
pooled_cpm: 18.67
n_lines_expressing: 16
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# KRT81

*keratin 81* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.7× (z +12.8, q 1e-34, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 2.19× (z +4.2, q 0.003, up in 11 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.0825×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 0.0687×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPG]] (+0.52, fdr 4e-05), [[PROSER2]] (+0.50, fdr 7e-05), [[RPL26L1]] (+0.45, fdr 1e-04); moves opposite to [[MLLT6]] (-0.46, fdr 1e-04), [[ZBTB1]] (-0.40, fdr 6e-04), [[HSD17B14]] (-0.40, fdr 4e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[VGLL3]] → it (grade C ⚠); 8 go from it, the strongest it → [[PORCN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.7×** | +12.8 | 1e-34 | 10/13 (A549, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.62×** | +9.8 | 3e-20 | 9/11 (A549, SW 900, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.20×** | +9.1 | 2e-17 | 10/12 (SNU-423, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.19×** | +4.2 | 0.003 | 11/13 (SNU-423, Panc 03.27, …) | all doses, flat | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **3.55×** | +4.1 | 0.004 | 11/13 (SW 900, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.051 | 1/14 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **3.77×** | +3.2 | 0.098 | 5/11 (Panc 03.27, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.80× | +3.2 | 0.10 | 9/13 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.49× | +3.1 | 0.11 | 10/15 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | 1.80× | +3.1 | 0.11 | 5/13 (SNU-423, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.80× | +3.1 | 0.11 | 12/13 (Panc 03.27, A-172, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.84× | +3.0 | 0.11 | 7/13 (SW480, A-172, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.0825×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (J82 0.0687×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.545× | -3.3 | 0.35 | 5/13 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.550× | -3.2 | 0.35 | 8/14 (J82, A549, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Tadalafil (drug)]] 5 µM |  | 0.547× | -3.1 | 0.35 | 1/13 (SW480) | top dose only |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.571× | -3.0 | 0.38 | 0/14 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 23.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -12.7) |
| [[A549 (line)]] | wt | 422 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.24× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.991 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPG]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[PROSER2]] | +0.50 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[RPL26L1]] | +0.45 | +0.32 / +0.33 | both halves | 1e-04 |  |
| [[TMEM184B]] | +0.43 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[ARHGAP29]] | +0.43 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[RHOC]] | +0.43 | +0.38 / +0.29 | both halves | 2e-04 |  |
| [[FLNB-AS1]] | +0.43 | +0.32 / +0.35 | both halves | 2e-04 |  |
| [[TWF2]] | +0.43 | +0.46 / +0.27 | both halves | 3e-04 |  |
| [[KRT7]] | +0.43 | +0.30 / +0.56 | both halves | 2e-04 | same gene group; pathway: Formation of the cornified envelope; STRING 546; ⚠ same locus (33.7 kb: neighbours can correlate without regulation) |
| [[MAP6]] | +0.43 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[TMCC1]] | +0.42 | +0.30 / +0.35 | both halves | 2e-04 |  |
| [[MARCHF2]] | +0.42 | +0.36 / +0.27 | both halves | 3e-04 |  |
| [[RRAS]] | +0.42 | +0.38 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT6]] | -0.46 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ZBTB1]] | -0.40 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[HSD17B14]] | -0.40 | -0.26 / -0.24 | both halves | 4e-04 |  |
| [[PLEKHA4]] | -0.39 | -0.28 / -0.24 | both halves | 5e-04 |  |
| [[RBM15]] | -0.38 | -0.26 / -0.24 | both halves | 4e-04 |  |
| [[FAM111A]] | -0.37 | -0.28 / -0.25 | both halves | 4e-04 |  |
| [[SLC12A7]] | -0.37 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[SLC43A3]] | -0.37 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[CASP8]] | -0.37 | -0.30 / -0.28 | both halves | 3e-04 |  |
| [[LGALS8]] | -0.37 | -0.25 / -0.25 | both halves | 4e-04 |  |
| [[RBM43]] | -0.36 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[JADE2]] | -0.36 | -0.33 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VGLL3]] | C | VGLL3 activity raises KRT81's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 4.15× lower at baseline in the lines without VGLL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882; co-absent with the target |
| [[KRT7]] | C | KRT7 activity raises KRT81's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 4.63× lower at baseline in the lines without KRT7 | 0.016 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises KRT81's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.55× lower at baseline in the lines without SLC43A3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |
| [[LINC00842]] | C | LINC00842 activity raises KRT81's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 3.54× lower at baseline in the lines without LINC00842 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[SCN9A]] | C | SCN9A activity raises KRT81's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 3.78× lower at baseline in the lines without SCN9A | 0.079 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1; co-absent with the target |
| [[F3]] | C | F3 activity raises KRT81's level | lines that do not express F3 (24) vs lines expressing it (26) | 3.69× lower at baseline in the lines without F3 | 0.079 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PORCN]] | B | KRT81 activity raises PORCN's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without KRT81 | 0.022 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[TMOD3]] | B | KRT81 activity strengthens TMOD3's drug response | lines that do not express KRT81 (34) vs lines expressing it (15) | the lines without KRT81 respond 0.72× as strongly (z diff +1.56); strongest at Panobinostat 0.5 µM: 0.78x vs 0.66x (z diff +3.2) | 0.058 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; target measured in part of the lines; artifact flags |
| [[SPTLC2]] | B | KRT81 activity raises SPTLC2's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 1.21× lower at baseline in the lines without KRT81 | 0.071 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[ZNF185]] | B | KRT81 activity raises ZNF185's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without KRT81 | 0.079 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[ANXA2]] | B | KRT81 activity raises ANXA2's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without KRT81 | 0.089 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9 |
| [[KRT7]] | C | KRT81 activity raises KRT7's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without KRT81 | 0.008 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; co-absent with the target |
| [[SLC43A3]] | C | KRT81 activity raises SLC43A3's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 3.82× lower at baseline in the lines without KRT81 | 0.027 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; co-absent with the target |
| [[VGLL3]] | C | KRT81 activity raises VGLL3's level | lines that do not express KRT81 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without KRT81 | 0.083 | ⚠ within organs, on part of the lines; also absent: CARD11, ANXA8, PSG9; co-absent with the target |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.369). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, 59.7); signed map (-3.1, 38.1). **Vector** length 35.2, 10.3% of its response variance represented; |z| ≥ 3 in 284 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +4.2 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.5 |
|  | [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.6 | -1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -0.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | keratin 81 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:52,285,913-52,291,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hb-1; previously KRTHB1 |
| Gene groups (HGNC) | Keratins, type II |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14533](https://www.uniprot.org/uniprotkb/Q14533) (Keratin, type II cuticular Hb1):

> Structural component of intermediate filaments in the hair cortex. Forms obligate heterodimers with type I hair keratins, which assemble into keratin intermediate filaments that contribute to the structural integrity and mechanical strength of the hair shaft.

**Summary**, from NCBI Gene [3887](https://www.ncbi.nlm.nih.gov/gene/3887):

> The protein encoded by this gene is a member of the keratin gene family. As a type II hair keratin, it is a basic protein which heterodimerizes with type I keratins to form hair and nails. The type II hair keratins are clustered in a region of chromosome 12q13 and are grouped into two distinct subfamilies based on structure similarity. One subfamily, consisting of KRTHB1, KRTHB3, and KRTHB6, is highly related. The other less-related subfamily includes KRTHB2, KRTHB4, and KRTHB5. All hair …

**Accessions** — [HGNC:6458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6458) · Entrez [3887](https://www.ncbi.nlm.nih.gov/gene/3887) · UniProt [Q14533](https://www.uniprot.org/uniprotkb/Q14533) · Ensembl [ENSG00000205426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205426)

## Data

Gene col 12979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12979); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12979]; `tensor/DDL_lfc|DDL_z.npy` [12979]; `embed/gene_vectors.npy` [12979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12979 or target_col == 12979). Every well: [[KRT81 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT81.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
