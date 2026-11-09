---
symbol: "GGPS1"
type: "gene"
col: 7664
ensembl_id: "ENSG00000152904"
name: "geranylgeranyl diphosphate synthase 1"
location: "1q42.3"
module: 95
arm: "+"
pooled_cpm: 24.82
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# GGPS1

*geranylgeranyl diphosphate synthase 1* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +19.9, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.273×, NCI-H1573 0.372×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.191×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.231×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (RPMI-7951 0.190×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCE-1]] (+0.79, fdr 1e-05, ⚠ same locus), [[AKT1S1]] (+0.79, fdr 7e-06), [[C11orf58]] (+0.78, fdr 7e-06), [[CCDC90B-AS1]] (+0.77, fdr 3e-05); moves opposite to [[WASF3]] (-0.75, fdr 1e-05), [[HACE1]] (-0.69, fdr 3e-05), [[L2HGDH]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +19.9 | 0e+00 | 44/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +17.1 | 0e+00 | 36/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +11.3 | 2e-27 | 37/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +10.8 | 7e-25 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.7 | 1e-24 | 31/43 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +10.6 | 2e-24 | 35/47 (SHP-77, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.8 | 4e-13 | 22/34 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 2e-08 | 31/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 4e-05 | 18/37 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.9 | 6e-05 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 20/48 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 22/46 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 14/48 (HOP62, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.24×** | +3.9 | 0.003 | 17/45 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.012 | 11/47 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.015 | 13/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.088 | 9/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.12× | +2.9 | 0.091 | 6/48 (SW1417, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.273×, NCI-H1573 0.372×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.191×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.231×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (RPMI-7951 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.703× | -3.4 | 0.45 | 10/30 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.8 | 14 (9 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.82× (z +18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.5) | — |
| [[SW480 (line)]] | alt | 29.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +20.8) | — |
| [[A-172 (line)]] | wt | 36.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 39.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 29.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 18.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[KATO III (line)]] | alt | 18.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +10.9) | [[Canagliflozin (drug)]] 0.05 µM 0.190× (z -9.0) |
| [[SW 900 (line)]] | alt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +14.6) | — |
| [[A498 (line)]] | wt | 28.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 38.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +10.2) | — |
| [[C32 (line)]] | wt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 33.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.5) | — |
| [[H4 (line)]] | wt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 34.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.231× (z -9.2) |
| [[HOP62 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.2) | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.3) |
| [[SHP-77 (line)]] | alt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.70× (z +9.1) | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCE-1]] | +0.79 | +0.87 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AKT1S1]] | +0.79 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[C11orf58]] | +0.78 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.77 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[INO80D]] | +0.74 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.74 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[THAP2]] | +0.73 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | +0.73 | +0.76 / +0.43 | both halves | 4e-05 |  |
| [[ZBED5]] | +0.72 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[BAZ2B]] | +0.71 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.70 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[ZBTB1]] | +0.70 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.75 | -0.73 / -0.51 | both halves | 1e-05 |  |
| [[HACE1]] | -0.69 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.69 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.67 | -0.67 / -0.39 | both halves | 5e-05 |  |
| [[TAF5L]] | -0.66 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[POMGNT2]] | -0.66 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.66 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[SCAI]] | -0.65 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[SKP2]] | -0.65 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.64 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ARL6]] | -0.64 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TBC1D2B]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GGPS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.771). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (4.9, 10.5); signed map (18.6, -21.6). **Vector** length 91.4, 19.5% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.52 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.53 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +19.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.9 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | geranylgeranyl diphosphate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,327,350-235,344,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GGPPS1 |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [O95749](https://www.uniprot.org/uniprotkb/O95749) (Geranylgeranyl pyrophosphate synthase):

> Catalyzes the trans-addition of the three molecules of IPP onto DMAPP to form geranylgeranyl pyrophosphate, an important precursor of carotenoids and geranylated proteins.

**Summary**, from NCBI Gene [9453](https://www.ncbi.nlm.nih.gov/gene/9453):

> This gene is a member of the prenyltransferase family and encodes a protein with geranylgeranyl diphosphate (GGPP) synthase activity. The enzyme catalyzes the synthesis of GGPP from farnesyl diphosphate and isopentenyl diphosphate. GGPP is an important molecule responsible for the C20-prenylation of proteins and for the regulation of a nuclear hormone receptor. Alternate transcriptional splice variants, both protein-coding and non-protein-coding, have been found for this gene. [provided by …

**Accessions** — [HGNC:4249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4249) · Entrez [9453](https://www.ncbi.nlm.nih.gov/gene/9453) · UniProt [O95749](https://www.uniprot.org/uniprotkb/O95749) · Ensembl [ENSG00000152904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152904)

## Data

Gene col 7664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7664); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7664]; `tensor/DDL_lfc|DDL_z.npy` [7664]; `embed/gene_vectors.npy` [7664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7664 or target_col == 7664). Every well: [[GGPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
