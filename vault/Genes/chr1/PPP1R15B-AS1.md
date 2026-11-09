---
symbol: "PPP1R15B-AS1"
type: "gene"
col: 13529
ensembl_id: "ENSG00000226330"
name: "PPP1R15B and PIK3C2B antisense RNA 1"
location: "1q32.1"
module: 26
arm: "+"
pooled_cpm: 12.6
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PPP1R15B-AS1

*PPP1R15B and PIK3C2B antisense RNA 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.67× (z +28.2, q 0e+00, up in 43 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0900×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.230×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHBP1-AS1]] (+0.68, fdr 7e-06), [[FAM184B]] (+0.68, fdr 1e-05), [[MED28-DT]] (+0.67, fdr 2e-05); moves opposite to [[FITM2]] (-0.73, fdr 8e-06), [[COMMD2]] (-0.70, fdr 1e-05), [[KBTBD6]] (-0.62, fdr 4e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.67×** | +28.2 | 0e+00 | 43/43 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +15.7 | 0e+00 | 29/45 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +12.0 | 1e-30 | 32/35 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +11.4 | 1e-27 | 21/25 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.7 | 7e-25 | 20/27 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +9.9 | 4e-21 | 30/44 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.1 | 4e-14 | 25/45 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.62×** | +7.4 | 1e-11 | 24/46 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.8 | 8e-10 | 20/48 (HOP62, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.54×** | +6.3 | 1e-08 | 22/46 (J82, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +5.8 | 3e-07 | 20/46 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.6 | 9e-07 | 23/46 (BT-474, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.32×** | +4.3 | 8e-04 | 14/47 (NCI-H460, SW 900, …) | rises with dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 6/46 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +3.7 | 0.008 | 9/46 (NCI-H460, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.055 | 5/45 (J82, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.065 | 8/46 (SW480, A-427, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.099 | 6/45 (NCI-H2030, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0900×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.7 | 0.12 | 6/48 (NCI-H2347, A-427, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.806× | -3.1 | 0.42 | 7/45 (AN3 CA, Panc 03.27, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.870× | -3.1 | 0.42 | 11/48 (NCI-H23, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.87× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.0) | — |
| [[A-172 (line)]] | wt | 7.97 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +12.6) | — |
| [[A549 (line)]] | wt | 12.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +16.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.230× (z -8.7) |
| [[C32 (line)]] | wt | 9.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 9.09 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 8.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +9.6) | — |
| [[A498 (line)]] | wt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 9.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.19× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 10.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 7.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 9.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +8.5) | — |
| [[LoVo (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 8.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 9.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 9.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +14.3) | — |
| [[RKO (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 8.34 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0900× (z -9.8) |
| [[SW 900 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.1) | — |
| [[SW480 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +15.6) | — |
| [[A-427 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1-AS1]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[FAM184B]] | +0.68 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MED28-DT]] | +0.67 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LMNB1-DT]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CEACAM16-AS1]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | same gene group |
| [[SPEN-AS1]] | +0.67 | +0.52 / +0.52 | both halves | 1e-05 | same gene group |
| [[FAM174B]] | +0.67 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CTDSPL2-DT]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TPTE2P6]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[C2orf88]] | +0.66 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UBE2R2-AS1]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[DEPDC4]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FITM2]] | -0.73 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[COMMD2]] | -0.70 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[KBTBD6]] | -0.62 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[WRAP73]] | -0.61 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[MLX]] | -0.61 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MOCS1]] | -0.61 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CNEP1R1]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GPATCH11]] | -0.58 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[COG2]] | -0.58 | -0.15 / -0.65 | ⚠ one half (not replicated) | 0.001 |  |
| [[NDUFA12]] | -0.58 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[ZNF445]] | -0.57 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[MRPS31P4]] | -0.56 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[SLC39A3]] | -0.56 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity raises PPP1R15B-AS1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without PLEKHA6 | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PPP1R15B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises PPP1R15B-AS1's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without SEPTIN9-DT | 0.059 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises PPP1R15B-AS1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.34× lower at baseline in the lines without ZNF341-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.4, 23.0); signed map (31.1, 1.2). **Vector** length 70.9, 11.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +28.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R15B and PIK3C2B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:204,377,850-204,435,846 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AL606489.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55838) · Entrez [122455336](https://www.ncbi.nlm.nih.gov/gene/122455336) · Ensembl [ENSG00000226330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226330)

## Data

Gene col 13529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13529); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13529]; `tensor/DDL_lfc|DDL_z.npy` [13529]; `embed/gene_vectors.npy` [13529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13529 or target_col == 13529). Every well: [[PPP1R15B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R15B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
