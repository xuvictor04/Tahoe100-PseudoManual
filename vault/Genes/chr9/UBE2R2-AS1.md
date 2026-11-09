---
symbol: "UBE2R2-AS1"
type: "gene"
col: 14019
ensembl_id: "ENSG00000235481"
name: "UBE2R2 antisense RNA 1"
location: "9p13.3"
module: 26
arm: "+"
pooled_cpm: 5.51
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# UBE2R2-AS1

*UBE2R2 antisense RNA 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.43× (z +34.1, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.894× (z -5.6, q 2e-05, down in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Dexamethasone (drug)]] 0.05 µM: 0.739× (z -3.9, q 0.024, down in 5 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.282×, LS 180 0.319×); [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0707×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (AsPC-1 0.263×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00393]] (+0.75, fdr 7e-06), [[FER1L6]] (+0.73, fdr 1e-05), [[CCNT2-AS1]] (+0.72, fdr 1e-05); moves opposite to [[MRPS31P4]] (-0.58, fdr 2e-04), [[STRA6LP]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.43×** | +34.1 | 0e+00 | 39/39 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.42×** | +16.2 | 0e+00 | 35/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.9 | 1e-30 | 8/11 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +11.5 | 2e-28 | 18/26 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +11.4 | 4e-28 | 6/15 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +10.6 | 3e-24 | 18/34 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.26×** | +10.6 | 4e-24 | 30/44 (SW480, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.0 | 1e-17 | 21/37 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.6 | 4e-16 | 17/37 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.8 | 5e-07 | 8/27 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +5.5 | 2e-06 | 9/27 (A498, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 1e-05 | 10/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +4.8 | 8e-05 | 12/45 (SW1417, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.4 | 4e-04 | 8/31 (SW48, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.8 | 0.006 | 8/37 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 12/38 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.011 | 5/45 (BT-474, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.018 | 8/44 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.028 | 4/44 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.061 | 5/44 (hTERT-HPNE, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14019.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.282×, LS 180 0.319×); [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0707×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (AsPC-1 0.263×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -5.6 | 2e-05 | 11/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.739×** | -3.9 | 0.024 | 5/44 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.768× | -3.2 | 0.23 | 6/41 (SW480, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.00 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.8) |
| [[HOP62 (line)]] | alt | 5.03 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.99× (z +13.0) | — |
| [[KATO III (line)]] | alt | 11.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 3.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +16.3) | — |
| [[A498 (line)]] | wt | 3.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +12.0) | — |
| [[A549 (line)]] | wt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 9.67 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0707× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 5.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 5.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 4.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 4.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 7.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +11.0) | — |
| [[J82 (line)]] | alt | 5.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 4.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 6.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 3.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 4.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +11.6) | — |
| [[A-172 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | +0.75 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[FER1L6]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | +0.72 | +0.55 / +0.68 | both halves | 1e-05 | same gene group |
| [[HRG-AS1]] | +0.70 | +0.46 / +0.71 | both halves | 2e-05 | same gene group |
| [[NUP210L]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.69 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PROSER2-AS1]] | +0.67 | +0.58 / +0.71 | both halves | 7e-06 | same gene group |
| [[ATXN7L3-AS1]] | +0.67 | +0.46 / +0.56 | both halves | 2e-05 | same gene group |
| [[C2orf88]] | +0.67 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DENND6A-AS1]] | +0.66 | +0.44 / +0.65 | both halves | 3e-05 | same gene group |
| [[SEPTIN9-DT]] | +0.65 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.58 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[STRA6LP]] | -0.57 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity lowers UBE2R2-AS1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.20× higher at baseline in the lines without DYNC2H1 | 0.010 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[LINC00589]] | B | LINC00589 activity raises UBE2R2-AS1's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without LINC00589 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[TOP2A]] | B | TOP2A activity lowers UBE2R2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KPNA7]] | B | KPNA7 activity raises UBE2R2-AS1's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without KPNA7 | 0.056 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[DYNC2H1]] | B | DYNC2H1 activity strengthens UBE2R2-AS1's drug response | lines that do not express DYNC2H1 (8) vs lines expressing it (39) | the lines without DYNC2H1 respond 0.35× as strongly (z diff +1.98); strongest at Dinaciclib 0.5 µM: 0.69x vs 2.54x (z diff +5.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.7, 20.9); signed map (30.0, 6.3). **Vector** length 75.6, 12.6% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.9 | +34.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +5.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | UBE2R2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p13.3 — chr9:33,732,970-33,818,795 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC01251 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49911) · Entrez [101929688](https://www.ncbi.nlm.nih.gov/gene/101929688) · Ensembl [ENSG00000235481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235481)

## Data

Gene col 14019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14019); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14019]; `tensor/DDL_lfc|DDL_z.npy` [14019]; `embed/gene_vectors.npy` [14019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14019 or target_col == 14019). Every well: [[UBE2R2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2R2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
