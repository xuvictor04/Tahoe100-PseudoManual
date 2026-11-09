---
symbol: "EFCAB5"
type: "gene"
col: 10768
ensembl_id: "ENSG00000176927"
name: "EF-hand calcium binding domain 5"
location: "17q11.2"
module: 26
arm: "+"
pooled_cpm: 4.26
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# EFCAB5

*EF-hand calcium binding domain 5* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.7× (z +38.8, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.711× (z -4.0, q 0.044, down in 7 of 45 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0679×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0851×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (KATO III 0.0733×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALINC1]] (+0.81, fdr 7e-06), [[MMADHC-DT]] (+0.80, fdr 3e-04), [[PPP1R12A-AS2]] (+0.80, fdr 1e-04); moves opposite to [[STUB1]] (-0.68, fdr 0.004, ⚠ not reproduced), [[ST6GALNAC4]] (-0.67, fdr 1e-03, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.7×** | +38.8 | 0e+00 | 33/33 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.11×** | +21.9 | 0e+00 | 29/31 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.04×** | +20.1 | 0e+00 | 34/36 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +17.7 | 0e+00 | 32/36 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.89×** | +17.4 | 0e+00 | 34/45 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +13.7 | 6e-41 | 6/8 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +13.1 | 2e-37 | 14/21 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.04×** | +12.9 | 3e-36 | 33/41 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.10×** | +12.6 | 9e-35 | 19/22 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.54×** | +10.8 | 2e-25 | 21/34 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.93×** | +10.8 | 2e-25 | 25/45 (A498, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.8 | 2e-25 | 6/7 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.52×** | +10.7 | 4e-25 | 30/41 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +9.0 | 1e-17 | 25/42 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.93×** | +7.7 | 7e-13 | 20/45 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +6.9 | 2e-10 | 21/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.33×** | +4.6 | 1e-04 | 10/45 (A498, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 4e-04 | 11/41 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 7e-04 | 8/39 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0679×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0851×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (KATO III 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -4.0 | 0.044 | 7/45 (A498, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.0 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.70× (z +15.7) | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +16.3) | — |
| [[A-172 (line)]] | wt | 4.40 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 2.59 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 3.23 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +10.7) | [[Omeprazole (drug)]] 0.5 µM 0.0679× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 2.51 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +17.1) | — |
| [[SW480 (line)]] | alt | 3.81 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +16.9) | — |
| [[KATO III (line)]] | alt | 4.85 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.62× (z +11.9) | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0733× (z -9.1) |
| [[LS 180 (line)]] | wt | 3.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.12 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 3.93 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +15.3) | — |
| [[A549 (line)]] | wt | 3.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.9× (z +13.1) | — |
| [[C32 (line)]] | wt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0851× (z -9.2) |
| [[HS-578T (line)]] | alt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +11.6) | — |
| [[J82 (line)]] | alt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +10.3) | — |
| [[LoVo (line)]] | wt | 2.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +10.9) | — |
| [[RKO (line)]] | wt | 3.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.1× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 2.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +11.1) | — |
| [[A-427 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALINC1]] | +0.81 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.80 | +0.82 / +0.28 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.82 / +0.34 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | +0.79 | +0.78 / +0.46 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.77 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[PBLD]] | +0.76 | +0.74 / +0.24 | both halves | 5e-04 |  |
| [[CCDC90B-AS1]] | +0.76 | +0.79 / +0.24 | both halves | 5e-04 |  |
| [[LINC01090]] | +0.76 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.76 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[AHI1-DT]] | +0.76 | +0.74 / +0.36 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | +0.76 | +0.79 / +0.26 | both halves | 4e-04 |  |
| [[INTS6-AS1]] | +0.75 | +0.78 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.68 | -0.48 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[ST6GALNAC4]] | -0.67 | -0.65 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EFCAB5's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC01358]] | B | LINC01358 activity raises EFCAB5's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without LINC01358 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.1, 20.3); signed map (26.5, -4.7). **Vector** length 83.1, 15.6% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +38.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +21.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.0 | +17.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +20.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,929,200-30,108,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46247 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [A4FU69](https://www.uniprot.org/uniprotkb/A4FU69) carries no function annotation.

**Summary**, from NCBI Gene [374786](https://www.ncbi.nlm.nih.gov/gene/374786):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24801) · Entrez [374786](https://www.ncbi.nlm.nih.gov/gene/374786) · UniProt [A4FU69](https://www.uniprot.org/uniprotkb/A4FU69) · Ensembl [ENSG00000176927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176927)

## Data

Gene col 10768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10768); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10768]; `tensor/DDL_lfc|DDL_z.npy` [10768]; `embed/gene_vectors.npy` [10768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10768 or target_col == 10768). Every well: [[EFCAB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
