---
symbol: "MAPRE3"
type: "gene"
col: 1413
ensembl_id: "ENSG00000084764"
name: "microtubule associated protein RP/EB family member 3"
location: "2p23.3"
module: 57
arm: "+"
pooled_cpm: 16.06
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# MAPRE3

*microtubule associated protein RP/EB family member 3* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.72× (z +22.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.796× (z -3.8, q 0.069, down in 17 of 46 measured lines) ⚠ cell-cycle shift, explains ~23% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.108×, SW1417 0.369×, SK-MEL-2 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (COLO 205 0.0757×, NCI-H460 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.193×, LS 180 0.171×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (RPMI-7951 0.138×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5R1]] (+0.66, fdr 7e-06), [[NXPE3]] (+0.64, fdr 7e-06), [[DNM1]] (+0.63, fdr 1e-05); moves opposite to [[ZNF131]] (-0.56, fdr 1e-05), [[UBTF]] (-0.55, fdr 3e-05), [[SPRY3]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPEG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +22.1 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.63×** | +21.7 | 0e+00 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.13×** | +19.2 | 0e+00 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.88×** | +17.8 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.07×** | +17.8 | 0e+00 | 44/46 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.69×** | +16.6 | 0e+00 | 42/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.48×** | +15.3 | 0e+00 | 43/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +14.8 | 0e+00 | 40/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.22×** | +13.4 | 4e-39 | 40/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.59×** | +11.2 | 2e-27 | 42/47 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +10.1 | 3e-22 | 32/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +6.3 | 2e-08 | 20/46 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +6.1 | 5e-08 | 19/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 1e-07 | 21/47 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.44×** | +5.9 | 2e-07 | 18/41 (NCI-H2030, H4, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 3e-04 | 10/47 (J82, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.108×, SW1417 0.369×, SK-MEL-2 0.222×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (COLO 205 0.0757×, NCI-H460 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.193×, LS 180 0.171×; ⚠ toxic; transcription drop); [[Furosemide (drug)]] 0.5 µM in 1 line (RPMI-7951 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.796×** | -3.8 | 0.069 | 17/46 (C32, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | 0.818× | -3.4 | 0.20 | 16/45 (COLO 205, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.88× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 12.1 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.65× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 11.7 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.29× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.2 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.68× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +10.1) | — |
| [[A-172 (line)]] | wt | 26.4 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.88× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +9.8) | — |
| [[SW480 (line)]] | alt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +10.5) | — |
| [[A549 (line)]] | wt | 21.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 4.10× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.66× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.87× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.43× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.14× (z +8.5) | — |
| [[C32 (line)]] | wt | 23.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.00× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 18.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.138× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5R1]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DNM1]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NSFL1C]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[BLMH]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GCOM1]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MOCS2]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[HSD17B4]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ATG4A]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PKIG]] | +0.57 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF131]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[UBTF]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SPRY3]] | -0.53 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SIAH2-AS1]] | -0.52 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[EP300]] | -0.52 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[SNHG31]] | -0.51 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[CENPL]] | -0.51 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TRPV1]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TOB2]] | -0.51 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[PHC2-AS1]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[HMGB1]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPEG]] | B | SPEG activity raises MAPRE3's level | lines that do not express SPEG (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without SPEG | 0.069 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.6, -7.7); signed map (-27.9, -21.7). **Vector** length 95.8, 22.7% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +17.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.0 | +15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +11.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein RP/EB family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,970,637-27,027,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP3, EB3 |
| Gene groups (HGNC) | Microtubule associated protein RP/EB family |
| Hallmark sets | MYOGENESIS |
| Reactome | 3 pathways, smallest: Dengue Virus Attachment and Entry; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPY8](https://www.uniprot.org/uniprotkb/Q9UPY8) (Microtubule-associated protein RP/EB family member 3):

> Plus-end tracking protein (+TIP) that binds to the plus-end of microtubules and regulates the dynamics of the microtubule cytoskeleton. Promotes microtubule growth. May be involved in spindle function by stabilizing microtubules and anchoring them at centrosomes. Also acts as a regulator of minus-end microtubule organization: interacts with the complex formed by AKAP9 and PDE4DIP, leading to recruit CAMSAP2 to the Golgi apparatus, thereby tethering non-centrosomal minus-end microtubules to the …

**Summary**, from NCBI Gene [22924](https://www.ncbi.nlm.nih.gov/gene/22924):

> The protein encoded by this gene is a member of the RP/EB family of genes. The protein localizes to the cytoplasmic microtubule network and binds APCL, a homolog of the adenomatous polyposis coli tumor suppressor gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6892) · Entrez [22924](https://www.ncbi.nlm.nih.gov/gene/22924) · UniProt [Q9UPY8](https://www.uniprot.org/uniprotkb/Q9UPY8) · Ensembl [ENSG00000084764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084764)

## Data

Gene col 1413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1413); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1413]; `tensor/DDL_lfc|DDL_z.npy` [1413]; `embed/gene_vectors.npy` [1413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1413 or target_col == 1413). Every well: [[MAPRE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPRE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
