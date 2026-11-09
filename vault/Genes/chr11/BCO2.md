---
symbol: "BCO2"
type: "gene"
col: 12423
ensembl_id: "ENSG00000197580"
name: "beta-carotene oxygenase 2"
location: "11q23.1"
module: 37
arm: "+"
pooled_cpm: 5.54
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 1
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# BCO2

*beta-carotene oxygenase 2* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.00× (z +20.3, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.447× (z -4.4, q 0.007, down in 15 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (LS 180 0.0506×); [[Fulvestrant (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0579×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.237×; ⚠ unreliable plate only); [[Allantoin (drug)]] 0.5 µM in 1 line (COLO 205 0.101×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF4]] (+0.59, fdr 1e-05), [[MAP7D2]] (+0.59, fdr 1e-05), [[LEPR]] (+0.58, fdr 3e-05); moves opposite to [[CHAMP1]] (-0.61, fdr 3e-05), [[RMND5B]] (-0.60, fdr 3e-05), [[MTMR9]] (-0.55, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Paclitaxel (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +20.3 | 0e+00 | 38/40 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.08×** | +16.8 | 0e+00 | 40/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.40×** | +15.3 | 0e+00 | 41/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.52×** | +13.0 | 1e-36 | 40/46 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.38×** | +12.6 | 1e-34 | 24/47 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +12.1 | 6e-32 | 21/36 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.05×** | +11.5 | 9e-29 | 31/45 (SW480, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.67×** | +10.1 | 3e-22 | 34/46 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +9.7 | 1e-20 | 34/46 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +8.7 | 2e-16 | 22/38 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.74×** | +8.1 | 3e-14 | 21/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.16×** | +8.0 | 9e-14 | 32/46 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.6 | 9e-07 | 16/45 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.74×** | +5.4 | 2e-06 | 14/43 (PANC-1, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +4.9 | 5e-05 | 17/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.7 | 9e-05 | 15/46 (AsPC-1, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12423.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (LS 180 0.0506×); [[Fulvestrant (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0579×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.237×; ⚠ unreliable plate only); [[Allantoin (drug)]] 0.5 µM in 1 line (COLO 205 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -4.4 | 0.007 | 15/42 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.785× | -3.6 | 0.10 | 16/46 (A498, COLO 205, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM |  | 0.801× | -3.3 | 0.18 | 6/48 (A498, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.735× | -3.2 | 0.18 | 14/45 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.654× | -3.2 | 0.18 | 12/40 (LS 180, LoVo, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.17 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.55× (z +12.5) | — |
| [[KATO III (line)]] | alt | 7.98 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 7.08× (z +11.8) | — |
| [[A498 (line)]] | wt | 15.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -8.5) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 10.5 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.53× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 9.36 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 1.67 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 23.8× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 3.11 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 9.66× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.101× (z -8.5) |
| [[HS-578T (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0506× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 3.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 3.58 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0579× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 6.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.8) | — |
| [[A-172 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF4]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MAP7D2]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LEPR]] | +0.58 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[LINC02641]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[LINC02762]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 | ⚠ same locus (46.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02763]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GRK3]] | +0.56 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[C9orf153]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LSMEM1]] | +0.56 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CCDC146]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CTSD]] | +0.56 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[ALDH2]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CMYA5]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | -0.61 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[RMND5B]] | -0.60 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MTMR9]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZNF623]] | -0.54 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[MTRES1]] | -0.53 | -0.29 / -0.29 | both halves | 2e-04 |  |
| [[USP4]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZNF696]] | -0.52 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[RNF34]] | -0.51 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[PAK1IP1]] | -0.51 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[MDM1]] | -0.51 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[ZSCAN9]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MPHOSPH6]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BCO2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Paclitaxel (drug)]] 5 µM | C | BCO2's natural level raises the cells' numbers under Paclitaxel 5 µM (protects the cells) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Volasertib (drug)]] 0.5 µM | C | BCO2's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Belzutifan (drug)]] 5 µM | C | BCO2's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.430 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | BCO2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.484 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.6, -17.6); signed map (10.5, 3.1). **Vector** length 65.5, 10.6% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +20.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +12.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | beta-carotene oxygenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,175,510-112,224,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34464, B-DIOX-II; previously BCDO2 |
| Gene groups (HGNC) | Beta-carotene oxygenases |
| Reactome | 5 pathways, smallest: Retinoid metabolism and transport; Metabolism of fat-soluble vitamins; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYV7](https://www.uniprot.org/uniprotkb/Q9BYV7) (Carotenoid-cleaving dioxygenase, mitochondrial):

> Broad specificity mitochondrial dioxygenase that mediates the asymmetric oxidative cleavage of carotenoids. Cleaves carotenes (pure hydrocarbon carotenoids) such as all-trans-beta-carotene and lycopene as well as xanthophylls (oxygenated carotenoids) such as zeaxanthin, lutein and beta-cryptoxanthin at both the 9,10 and the 9',10' carbon-carbon double bond. Through its function in carotenoids metabolism regulates oxidative stress and the production of important signaling molecules.

**Summary**, from NCBI Gene [83875](https://www.ncbi.nlm.nih.gov/gene/83875):

> This gene encodes an enzyme which oxidizes carotenoids such as beta-carotene during the biosynthesis of vitamin A. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18503) · Entrez [83875](https://www.ncbi.nlm.nih.gov/gene/83875) · UniProt [Q9BYV7](https://www.uniprot.org/uniprotkb/Q9BYV7) · Ensembl [ENSG00000197580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197580)

## Data

Gene col 12423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12423); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12423]; `tensor/DDL_lfc|DDL_z.npy` [12423]; `embed/gene_vectors.npy` [12423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12423 or target_col == 12423). Every well: [[BCO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
