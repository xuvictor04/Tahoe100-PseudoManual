---
symbol: "HSF4"
type: "gene"
col: 2280
ensembl_id: "ENSG00000102878"
name: "heat shock transcription factor 4"
location: "16q22.1"
module: 103
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# HSF4

*heat shock transcription factor 4* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.49× (z +3.8, q 0.072, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.365× (z -14.2, q 1e-42, down in 36 of 43 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.308× (z -11.7, q 2e-29, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL8]] (+0.72, fdr 7e-06, ⚠ same locus), [[PNPLA7]] (+0.57, fdr 2e-04), [[JAK3]] (+0.54, fdr 3e-05), [[EOLA1]] (+0.53, fdr 3e-05); moves opposite to [[MPHOSPH6]] (-0.50, fdr 3e-05), [[COMMD8]] (-0.48, fdr 1e-04), [[ZMYM1]] (-0.48, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NOL3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.072 | 14/44 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 1.40× | +3.4 | 0.16 | 6/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.22 | 9/44 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.22 | 10/47 (NCI-H460, Hs 766T, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.34× | +3.1 | 0.22 | 8/48 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.365×** | -14.2 | 1e-42 | 36/43 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.289×** | -11.9 | 6e-30 | 41/45 (MIA PaCa-2, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.308×** | -11.7 | 2e-29 | 36/43 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.378×** | -9.7 | 5e-20 | 37/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.399×** | -9.1 | 9e-18 | 32/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.418×** | -8.7 | 4e-16 | 33/46 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.463×** | -7.6 | 2e-12 | 29/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.476×** | -7.4 | 1e-11 | 27/40 (HT-29, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.487×** | -7.1 | 6e-11 | 32/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.494×** | -7.0 | 1e-10 | 29/45 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.496×** | -7.0 | 2e-10 | 28/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.503×** | -6.8 | 4e-10 | 25/45 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.505×** | -6.8 | 5e-10 | 32/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.544×** | -5.7 | 5e-07 | 25/44 (HepG2/C3A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.564×** | -5.7 | 5e-07 | 21/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.636×** | -4.3 | 5e-04 | 17/46 (CFPAC-1, SW480, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.023 | 14/47 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -3.2 | 0.033 | 14/42 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.054 | 16/48 (MIA PaCa-2, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.0 | 0.061 | 13/47 (NCI-H460, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0354× (z -17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.170× (z -9.5) |
| [[PANC-1 (line)]] | alt | 6.49 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0506× (z -25.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 9.44 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0873× (z -11.6) |
| [[A549 (line)]] | wt | 8.65 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -17.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.212× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 8.07 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.128× (z -9.1) |
| [[HOP62 (line)]] | alt | 7.69 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 9.14 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.155× (z -9.1) |
| [[SW480 (line)]] | alt | 7.28 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.120× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 14.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.128× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0703× (z -16.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0595× (z -9.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HEC-1-A (line)]] | alt | 3.88 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0850× (z -10.1) |
| [[HS-578T (line)]] | alt | 4.60 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -9.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0594× (z -9.0) |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL8]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[PNPLA7]] | +0.57 | +0.31 / +0.65 | both halves | 2e-04 |  |
| [[JAK3]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[EOLA1]] | +0.53 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[NLGN2]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[LMNTD2]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[HYPK]] | +0.52 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[PRSS53]] | +0.51 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[AJM1]] | +0.50 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TNXB]] | +0.50 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[NUDT13]] | +0.50 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[SUOX]] | +0.50 | +0.19 / +0.57 | ⚠ one half (not replicated) | 9e-04 |  |
| [[B4GALNT4]] | +0.49 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.49 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.48 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ZMYM1]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CIAO1]] | -0.47 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MRPS33]] | -0.47 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[PTER]] | -0.46 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[MRPL47]] | -0.45 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[KLHL9]] | -0.45 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[METTL5]] | -0.45 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[ZFPM2-AS1]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[C12orf29]] | -0.44 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[ZNF22]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOL3]] | C | NOL3's natural level strengthens HSF4's drug response | NOL3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.57; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.2, -32.3); signed map (1.5, 11.7). **Vector** length 55.5, 8.04% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | heat shock transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,164,681-67,169,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CTM |
| Gene groups (HGNC) | Heat shock transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV5](https://www.uniprot.org/uniprotkb/Q9ULV5) (Heat shock factor protein 4):

> Heat-shock transcription factor that specifically binds heat shock promoter elements (HSE). Required for denucleation and organelle rupture and degradation that occur during eye lens terminal differentiation, when fiber cells that compose the lens degrade all membrane-bound organelles in order to provide lens with transparency to allow the passage of light (By similarity). In this process, may regulate denucleation of lens fiber cells in part by activating DNASE2B transcription (By similarity). …

**Summary**, from NCBI Gene [3299](https://www.ncbi.nlm.nih.gov/gene/3299):

> Heat-shock transcription factors (HSFs) activate heat-shock response genes under conditions of heat or other stresses. HSF4 lacks the carboxyl-terminal hydrophobic repeat which is shared among all vertebrate HSFs and has been suggested to be involved in the negative regulation of DNA binding activity. Two alternatively spliced transcripts encoding distinct isoforms and possessing different transcriptional activity have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5227) · Entrez [3299](https://www.ncbi.nlm.nih.gov/gene/3299) · UniProt [Q9ULV5](https://www.uniprot.org/uniprotkb/Q9ULV5) · Ensembl [ENSG00000102878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102878)

## Data

Gene col 2280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2280); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2280]; `tensor/DDL_lfc|DDL_z.npy` [2280]; `embed/gene_vectors.npy` [2280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2280 or target_col == 2280). Every well: [[HSF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
