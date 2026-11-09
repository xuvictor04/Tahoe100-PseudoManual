---
symbol: "IFT57"
type: "gene"
col: 3554
ensembl_id: "ENSG00000114446"
name: "intraflagellar transport 57"
location: "3q13.12-q13.13"
module: 14
arm: "+"
pooled_cpm: 30.3
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IFT57

*intraflagellar transport 57* — 3q13.12-q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +16.8, q 0e+00, up in 41 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.230×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1271 0.0599×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD47]] (+0.55, fdr 1e-04), [[CFAP69]] (+0.54, fdr 2e-05), [[RSPH1]] (+0.53, fdr 1e-05); moves opposite to [[MOSMO]] (-0.53, fdr 1e-04), [[OSBPL5]] (-0.51, fdr 1e-05), [[LINC02458]] (-0.51, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +16.8 | 0e+00 | 41/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +15.9 | 0e+00 | 46/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +15.3 | 0e+00 | 46/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +14.9 | 0e+00 | 46/47 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +13.6 | 3e-40 | 45/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +12.9 | 2e-36 | 43/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +11.3 | 2e-27 | 37/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +10.7 | 1e-24 | 38/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.87×** | +9.9 | 2e-21 | 34/43 (PANC-1, LS 180, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +9.8 | 5e-21 | 39/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.93×** | +9.7 | 2e-20 | 33/41 (PANC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.87×** | +9.6 | 4e-20 | 25/35 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +8.0 | 5e-14 | 37/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.57×** | +7.1 | 4e-11 | 28/46 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.8 | 3e-10 | 35/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.8 | 5e-10 | 31/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.45×** | +5.9 | 8e-08 | 25/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +5.6 | 7e-07 | 27/47 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.5 | 9e-07 | 26/46 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3554.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.230×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1271 0.0599×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.7 | 0.002 | 5/47 (C32, COLO 205, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.678× | -3.2 | 0.42 | 9/46 (LS 180, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 45.9 | 8 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.22× (z +12.0) | — |
| [[LoVo (line)]] | wt | 23.0 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 5.04× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 25.4 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.15× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.23× (z +12.3) | — |
| [[A-172 (line)]] | wt | 28.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.7) | — |
| [[A498 (line)]] | wt | 41.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +10.3) | — |
| [[KATO III (line)]] | alt | 26.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 50.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +11.7) | — |
| [[A-427 (line)]] | wt | 39.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 2 | 0 | [[Belinostat (drug)]] 5 µM 4.00× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 29.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.20× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.3) | — |
| [[SW480 (line)]] | alt | 14.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.00× (z +8.6) | — |
| [[A549 (line)]] | wt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +15.6) | — |
| [[C32 (line)]] | wt | 20.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.90× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0599× (z -8.9) |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD47]] | +0.55 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[CFAP69]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[RSPH1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN15]] | +0.53 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[REL]] | +0.53 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[HINT3]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HHLA2]] | +0.50 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[VPS13C]] | +0.50 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RFK]] | +0.49 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MAK]] | +0.49 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CDKN2A]] | +0.49 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[GBP2]] | +0.49 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSMO]] | -0.53 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[OSBPL5]] | -0.51 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[LINC02458]] | -0.51 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[VSTM2L]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SKI]] | -0.50 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZNF275]] | -0.50 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[POLG]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[FAM53A]] | -0.49 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[PANK2]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[LINC00941]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZNF384]] | -0.48 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ZNF668]] | -0.48 | -0.52 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IFT57's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.3, 38.3); signed map (47.5, 4.2). **Vector** length 85.4, 21.3% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.6 | +9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.4 | +9.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.8 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.12-q13.13 — chr3:108,160,812-108,222,435 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10147, HIPPI, MHS4R2; previously ESRRBL1 |
| Gene groups (HGNC) | IFT-B2 complex |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWB7](https://www.uniprot.org/uniprotkb/Q9NWB7) (Intraflagellar transport protein 57 homolog):

> Required for the formation of cilia. Plays an indirect role in sonic hedgehog signaling, cilia being required for all activity of the hedgehog pathway (By similarity). Together with RAB23 and KIF17, it is required for the localization of specific G protein-coupled receptors, such as dopamime receptor DRD1, to primary cilia. Has pro-apoptotic function via its interaction with HIP1, leading to recruit caspase-8 (CASP8) and trigger apoptosis. Has the ability to bind DNA sequence motif …

**Summary**, from NCBI Gene [55081](https://www.ncbi.nlm.nih.gov/gene/55081):

> Predicted to enable DNA binding activity. Acts upstream of or within apoptotic process and regulation of apoptotic process. Located in ciliary base and photoreceptor connecting cilium. Part of intraciliary transport particle A. Implicated in orofaciodigital syndrome XVIII. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17367) · Entrez [55081](https://www.ncbi.nlm.nih.gov/gene/55081) · UniProt [Q9NWB7](https://www.uniprot.org/uniprotkb/Q9NWB7) · Ensembl [ENSG00000114446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114446)

## Data

Gene col 3554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3554); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3554]; `tensor/DDL_lfc|DDL_z.npy` [3554]; `embed/gene_vectors.npy` [3554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3554 or target_col == 3554). Every well: [[IFT57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
