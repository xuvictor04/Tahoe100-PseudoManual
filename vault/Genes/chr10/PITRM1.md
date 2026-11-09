---
symbol: "PITRM1"
type: "gene"
col: 2905
ensembl_id: "ENSG00000107959"
name: "pitrilysin metallopeptidase 1"
location: "10p15.2"
module: 54
arm: "-"
pooled_cpm: 63.56
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# PITRM1

*pitrilysin metallopeptidase 1* — 10p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +19.1, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.897× (z -6.8, q 7e-09, down in 5 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.822× (z -3.6, q 0.099, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC200]] (+0.67, fdr 7e-06), [[LINC00910]] (+0.60, fdr 1e-05), [[DESI1]] (+0.58, fdr 1e-05); moves opposite to [[C15orf61]] (-0.62, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[MTF2]] (-0.56, fdr 2e-05), [[RSBN1L]] (-0.53, fdr 3e-05), [[NDUFB6]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +19.1 | 0e+00 | 39/47 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +17.5 | 0e+00 | 44/49 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +16.0 | 0e+00 | 44/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +13.4 | 7e-39 | 44/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +12.4 | 4e-33 | 41/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.77×** | +10.4 | 3e-23 | 39/48 (A-427, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.0 | 2e-17 | 38/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.9 | 5e-17 | 41/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.1 | 5e-14 | 37/48 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +7.9 | 1e-13 | 37/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.3 | 1e-11 | 33/48 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.3 | 1e-11 | 33/48 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.44×** | +6.4 | 7e-09 | 27/41 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 1e-08 | 32/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.40×** | +6.1 | 4e-08 | 23/48 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 24/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 25/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 3e-04 | 25/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -6.8 | 7e-09 | 5/49 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.099 | 20/48 (RKO, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.5 | 0.100 | 19/47 (SW48, C-33 A, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.881× | -3.3 | 0.15 | 10/49 (NCI-H460, NCI-H2122, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 64.7 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.6) | — |
| [[AsPC-1 (line)]] | alt | 77.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.9) | — |
| [[LoVo (line)]] | wt | 82.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.3) | — |
| [[A498 (line)]] | wt | 86.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 81.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +22.7) | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +21.7) | — |
| [[NCI-H460 (line)]] | wt | 55.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.1) | — |
| [[SW480 (line)]] | alt | 45.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.0) | — |
| [[A549 (line)]] | wt | 75.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 65.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.4) | — |
| [[SW1417 (line)]] | alt | 58.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +11.3) | — |
| [[A-172 (line)]] | wt | 75.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.9) | — |
| [[A-427 (line)]] | wt | 57.1 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.6) | — |
| [[KATO III (line)]] | alt | 58.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 89.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 84.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 49.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 48.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 63.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.0) | — |
| [[SW48 (line)]] | wt | 56.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 85.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.0) | — |
| [[Hs 766T (line)]] | wt | 55.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 72.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 65.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.6) | — |
| [[J82 (line)]] | alt | 48.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 56.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.2) | — |
| [[C32 (line)]] | wt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.3) | — |
| [[H4 (line)]] | wt | 64.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 46.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 62.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 74.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 28.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 48.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 49.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC200]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC00910]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DESI1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PPP4R1L]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PSMD8]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[GLS]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[DYNC1H1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ACADVL]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[FLNA]] | +0.55 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[TAX1BP3]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TMEM43]] | +0.53 | +0.37 / +0.52 | both halves | 8e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | -0.62 | -0.53 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTF2]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RSBN1L]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NDUFB6]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ZNF567]] | -0.53 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[LRP6]] | -0.53 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ZNF45]] | -0.52 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[USP42]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[LSM2]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NDUFC2]] | -0.51 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[IRAK1BP1]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PKDCC]] | -0.51 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | -0.51 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PITRM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.1, -13.1); signed map (2.6, 21.2). **Vector** length 97.5, 25.9% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | pitrilysin metallopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.2 — chr10:3,137,728-3,172,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MP1, KIAA1104, hMP1, PreP |
| Gene groups (HGNC) | M16 metallopeptidases |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JRX3](https://www.uniprot.org/uniprotkb/Q5JRX3) (Presequence protease, mitochondrial):

> Metalloendopeptidase of the mitochondrial matrix that functions in peptide cleavage and degradation rather than in protein processing. Has an ATP-independent activity. Specifically cleaves peptides in the range of 5 to 65 residues. Shows a preference for cleavage after small polar residues and before basic residues, but without any positional preference. Degrades the transit peptides of mitochondrial proteins after their cleavage. Also degrades other unstructured peptides. It is also able to …

**Summary**, from NCBI Gene [10531](https://www.ncbi.nlm.nih.gov/gene/10531):

> The protein encoded by this gene is an ATP-dependent metalloprotease that degrades post-cleavage mitochondrial transit peptides. The encoded protein binds zinc and can also degrade amyloid beta A4 protein, suggesting a possible role in Alzheimer's disease. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:17663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17663) · Entrez [10531](https://www.ncbi.nlm.nih.gov/gene/10531) · UniProt [Q5JRX3](https://www.uniprot.org/uniprotkb/Q5JRX3) · Ensembl [ENSG00000107959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107959)

## Data

Gene col 2905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2905); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2905]; `tensor/DDL_lfc|DDL_z.npy` [2905]; `embed/gene_vectors.npy` [2905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2905 or target_col == 2905). Every well: [[PITRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
