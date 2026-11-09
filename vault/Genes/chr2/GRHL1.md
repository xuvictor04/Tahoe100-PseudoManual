---
symbol: "GRHL1"
type: "gene"
col: 5544
ensembl_id: "ENSG00000134317"
name: "grainyhead like transcription factor 1"
location: "2p25.1"
module: 5
arm: "-"
pooled_cpm: 16.09
n_lines_expressing: 45
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GRHL1

*grainyhead like transcription factor 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.51× (z +23.7, q 0e+00, up in 39 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (NCI-H661 0.0687×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A4]] (+0.63, fdr 1e-05), [[SYP]] (+0.62, fdr 1e-05), [[TMCC2]] (+0.61, fdr 1e-05); moves opposite to [[ALG8]] (-0.64, fdr 1e-05), [[COX10]] (-0.62, fdr 1e-05), [[NOL11]] (-0.62, fdr 4e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BACH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.51×** | +23.7 | 0e+00 | 39/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.15×** | +20.2 | 0e+00 | 42/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.06×** | +18.1 | 0e+00 | 42/42 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.56×** | +16.9 | 0e+00 | 40/42 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +11.6 | 5e-29 | 16/22 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.72×** | +11.2 | 6e-27 | 39/42 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.73×** | +10.7 | 5e-25 | 35/41 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.3 | 4e-23 | 30/40 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +10.2 | 2e-22 | 22/28 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.38×** | +9.6 | 3e-20 | 21/34 (SW 900, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +9.5 | 7e-20 | 31/39 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.24×** | +9.0 | 1e-17 | 28/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.9 | 2e-17 | 34/43 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.9 | 2e-13 | 23/34 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.01×** | +7.8 | 2e-13 | 33/40 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.9 | 2e-10 | 29/42 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.4 | 5e-09 | 22/42 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +6.4 | 5e-09 | 24/42 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +6.2 | 2e-08 | 25/42 (LS 180, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +6.1 | 3e-08 | 22/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Omeprazole (drug)]] 0.5 µM in 1 line (NCI-H661 0.0687×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.804× | -3.4 | 0.27 | 17/42 (COLO 205, A-172, …) | rises with dose | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.810× | -3.3 | 0.27 | 10/43 (SW480, NCI-H661, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.751× | -3.2 | 0.27 | 12/42 (J82, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.4 | 14 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +21.7) | — |
| [[LS 180 (line)]] | wt | 25.0 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +16.4) | — |
| [[SW1417 (line)]] | alt | 44.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +27.5) | — |
| [[LoVo (line)]] | wt | 13.5 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.68× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 5.00 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 16.6 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.80× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 7.39 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +16.3) | — |
| [[HEC-1-A (line)]] | alt | 7.76 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 8.22 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 26.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 8.59 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +17.3) | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.4) | — |
| [[A-427 (line)]] | wt | 21.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +10.2) | — |
| [[A498 (line)]] | wt | 12.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +12.0) | — |
| [[A549 (line)]] | wt | 6.92 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.1× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 7.34 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 4.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.5× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 16.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 37.1× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 5.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.23× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 6.16 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.3× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.32× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 5.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.66× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 52.1 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0687× (z -9.1) |
| [[RKO (line)]] | wt | 7.98 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 4.62 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 22.2× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A4]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SYP]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TMCC2]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ABHD8]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[TSPAN15]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MAST1]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RND1]] | +0.57 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ADGRB2]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[KMT2C]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PPP2R5B]] | +0.55 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[GNG7]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | -0.64 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[COX10]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[NOL11]] | -0.62 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[PALB2]] | -0.60 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[METTL13]] | -0.59 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[PIGW]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TSR1]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[E2F3]] | -0.56 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[UBIAD1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FARS2]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SMARCAD1]] | -0.54 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ACAD9]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACH2]] | B | BACH2 activity raises GRHL1's level | lines that do not express BACH2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without BACH2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CKB, KLRK1-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (26.7, -0.5); signed map (19.7, 21.9). **Vector** length 80.6, 18.0% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.3 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | +0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | grainyhead like transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:9,951,693-10,002,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LBP-32, MGR; previously TFCP2L2 |
| Gene groups (HGNC) | Grainyhead like transcription factor family |
| Reactome | 7 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; PPARA activates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZI5](https://www.uniprot.org/uniprotkb/Q9NZI5) (Grainyhead-like protein 1 homolog):

> Transcription factor involved in epithelial development. Binds directly to the consensus DNA sequence 5'-AACCGGTT-3'. Important regulator of DSG1 in the context of hair anchorage and epidermal differentiation, participates in the maintenance of the skin barrier. There is no genetic interaction with GRHL3, nor functional cooperativity due to diverse target gene selectivity during epithelia development (By similarity). May play a role in regulating glucose homeostasis and insulin signaling.; …

**Summary**, from NCBI Gene [29841](https://www.ncbi.nlm.nih.gov/gene/29841):

> This gene encodes a member of the grainyhead family of transcription factors. The encoded protein can exist as a homodimer or can form heterodimers with sister-of-mammalian grainyhead or brother-of-mammalian grainyhead. This protein functions as a transcription factor during development. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:17923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17923) · Entrez [29841](https://www.ncbi.nlm.nih.gov/gene/29841) · UniProt [Q9NZI5](https://www.uniprot.org/uniprotkb/Q9NZI5) · Ensembl [ENSG00000134317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134317)

## Data

Gene col 5544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5544); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5544]; `tensor/DDL_lfc|DDL_z.npy` [5544]; `embed/gene_vectors.npy` [5544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5544 or target_col == 5544). Every well: [[GRHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
