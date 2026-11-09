---
symbol: "GRIA4"
type: "gene"
col: 7643
ensembl_id: "ENSG00000152578"
name: "glutamate ionotropic receptor AMPA type subunit 4"
location: "11q22.3"
module: 61
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# GRIA4

*glutamate ionotropic receptor AMPA type subunit 4* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.0× (z +29.3, q 0e+00, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.234×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.237×; ⚠ toxic; transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SHP-77 0.0682×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR4]] (+0.81, fdr 7e-06), [[GALNTL6]] (+0.80, fdr 7e-06), [[CNTN5]] (+0.80, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MIR3681HG]] → it (grade B ⚠); 2 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.0×** | +29.3 | 0e+00 | 27/29 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.6×** | +20.4 | 0e+00 | 9/11 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.79×** | +19.1 | 0e+00 | 23/25 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **8.62×** | +17.2 | 0e+00 | 1/2 (NCI-H1792) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.36×** | +16.6 | 0e+00 | 2/2 (NCI-H1792, SHP-77) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.68×** | +14.4 | 3e-45 | 27/35 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.91×** | +13.0 | 7e-37 | 32/41 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.92×** | +11.8 | 3e-30 | 17/27 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.19×** | +10.0 | 9e-22 | 23/36 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +8.0 | 8e-14 | 5/9 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +7.7 | 5e-13 | 8/18 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +6.7 | 1e-09 | 5/42 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +5.9 | 2e-07 | 15/32 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.6 | 8e-07 | 4/14 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.42×** | +5.5 | 1e-06 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.1 | 1e-05 | 4/41 (PANC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.0 | 2e-05 | 16/40 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.6 | 1e-04 | 5/28 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +4.3 | 4e-04 | 9/41 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 5e-04 | 11/39 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.2 | 8e-04 | 9/30 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.010 | 4/17 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7643.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.234×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.237×; ⚠ toxic; transcription drop); [[Torkinib (drug)]] 5 µM in 1 line (SHP-77 0.0682×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -3.4 | 0.41 | 13/47 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.32 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 175× (z +18.7) | — |
| [[hTERT-HPNE (line)]] | wt | 7.61 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 157× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 1.23 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +15.7) | — |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -9.0) |
| [[HOP62 (line)]] | alt | 1.46 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 42.9× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 13.0× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.9× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 1.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 82.1× (z +12.9) | — |
| [[J82 (line)]] | alt | 1.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 7.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.11× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 141× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 1.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 2.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.6× (z +12.7) | — |
| [[SW480 (line)]] | alt | 0.956 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.8) | — |
| [[A-427 (line)]] | wt | 0.912 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.952 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.876 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.769 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR4]] | +0.81 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 | STRING 459 |
| [[SGCZ]] | +0.79 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[CNTNAP4]] | +0.79 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.76 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.76 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.76 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[XIRP2]] | +0.76 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3681HG]] | B | MIR3681HG activity raises GRIA4's level | lines that do not express MIR3681HG (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without MIR3681HG | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000225649, BAALC, LINC02930; maybe low, not absent |
| [[HLA-L-1]] | B | HLA-L-1 activity raises GRIA4's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 1.03× lower at baseline in the lines without HLA-L-1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |
| [[DGKB]] | B | DGKB activity raises GRIA4's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without DGKB | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[NAALADL2-AS2]] | B | NAALADL2-AS2 activity strengthens GRIA4's drug response | lines that do not express NAALADL2-AS2 (30) vs lines expressing it (12) | the lines without NAALADL2-AS2 respond 0.83× as strongly (z diff +0.52); strongest at Homoharringtonine 0.5 µM: 2.83x vs 9.94x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers GRIA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCND2]] | B | KCND2 activity raises GRIA4's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.64× lower at baseline in the lines without KCND2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[NPFFR2]] | B | NPFFR2 activity raises GRIA4's level | lines that do not express NPFFR2 (33) vs lines expressing it (17) | 1.90× lower at baseline in the lines without NPFFR2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SCUBE1, ENSG00000266450, GRIA2 |
| [[NRXN1]] | B | NRXN1 activity raises GRIA4's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without NRXN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[GRIK1]] | B | GRIK1 activity raises GRIA4's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 1.64× lower at baseline in the lines without GRIK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | GRIA4's natural level weakens CLVS1's drug response | GRIA4's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.36; direction clear | 0.048 | ⚠ tissue can mimic it; precision caveat |
| [[LINC02307]] | C | GRIA4's natural level weakens LINC02307's drug response | GRIA4's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.32; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 29.3); signed map (33.1, 15.1). **Vector** length 53.5, 8.18% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +29.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +17.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor AMPA type subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:105,609,535-105,982,090 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluA4, GLURD, GluR-4, GluR-D, GLUR4C; previously GLUR4 |
| Gene groups (HGNC) | Glutamate ionotropic receptor AMPA type subunits |
| Reactome | 11 pathways, smallest: Activation of AMPA receptors; Trafficking of GluR2-containing AMPA receptors; Synaptic adhesion-like molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P48058](https://www.uniprot.org/uniprotkb/P48058) (Glutamate receptor 4):

> Ionotropic glutamate receptor that functions as a ligand-gated cation channel, gated by L-glutamate and glutamatergic agonists such as alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA), quisqualic acid, and kainic acid (By similarity). L-glutamate acts as an excitatory neurotransmitter at many synapses in the central nervous system and plays an important role in fast excitatory synaptic transmission (By similarity). Binding of the excitatory neurotransmitter L-glutamate induces a …

**Summary**, from NCBI Gene [2893](https://www.ncbi.nlm.nih.gov/gene/2893):

> Glutamate receptors are the predominant excitatory neurotransmitter receptors in the mammalian brain and are activated in a variety of normal neurophysiologic processes. These receptors are heteromeric protein complexes composed of multiple subunits, arranged to form ligand-gated ion channels. The classification of glutamate receptors is based on their activation by different pharmacologic agonists. The subunit encoded by this gene belongs to a family of AMPA …

**Accessions** — [HGNC:4574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4574) · Entrez [2893](https://www.ncbi.nlm.nih.gov/gene/2893) · UniProt [P48058](https://www.uniprot.org/uniprotkb/P48058) · Ensembl [ENSG00000152578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152578)

## Data

Gene col 7643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7643); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7643]; `tensor/DDL_lfc|DDL_z.npy` [7643]; `embed/gene_vectors.npy` [7643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7643 or target_col == 7643). Every well: [[GRIA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
