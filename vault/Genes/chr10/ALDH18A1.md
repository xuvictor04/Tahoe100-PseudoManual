---
symbol: "ALDH18A1"
type: "gene"
col: 674
ensembl_id: "ENSG00000059573"
name: "aldehyde dehydrogenase 18 family member A1"
location: "10q24.1"
module: 42
arm: "+"
pooled_cpm: 58.87
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ALDH18A1

*aldehyde dehydrogenase 18 family member A1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.50× (z +6.1, q 5e-07, up in 33 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.89× (z +5.1, q 1e-04, up in 30 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 2 lines (A-172 6.87×, HOP62 6.14×); [[PH-797804 (drug)]] 5 µM in 1 line (A-172 7.22×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.320× (z -24.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO2]] (+0.71, fdr 7e-06), [[GORASP2]] (+0.71, fdr 7e-06), [[SSR1]] (+0.68, fdr 7e-06); moves opposite to [[KANSL1L]] (-0.58, fdr 3e-05), [[WBP4]] (-0.56, fdr 3e-05), [[RESF1]] (-0.55, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 674.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 2 lines (A-172 6.87×, HOP62 6.14×); [[PH-797804 (drug)]] 5 µM in 1 line (A-172 7.22×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 2.40×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +6.1 | 5e-07 | 33/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +5.1 | 1e-04 | 30/49 (A-172, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.4 | 0.002 | 20/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.320×** | -24.4 | 0e+00 | 46/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.320×** | -16.6 | 0e+00 | 47/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -9.8 | 2e-20 | 40/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -9.8 | 2e-20 | 37/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -9.5 | 2e-19 | 41/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.551×** | -9.0 | 2e-17 | 40/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.665×** | -8.7 | 2e-16 | 44/48 (A498, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.612×** | -7.4 | 9e-12 | 36/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -7.2 | 4e-11 | 34/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -6.8 | 4e-10 | 34/46 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -6.6 | 2e-09 | 38/48 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -6.5 | 5e-09 | 33/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -6.1 | 5e-08 | 31/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -5.8 | 3e-07 | 33/48 (C32, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -5.4 | 2e-06 | 36/48 (C32, KATO III, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.799×** | -4.8 | 5e-05 | 26/48 (HS-578T, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.748×** | -4.2 | 7e-04 | 28/48 (C32, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 126 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -26.4) |
| [[HS-578T (line)]] | alt | 64.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.2) |
| [[C32 (line)]] | wt | 103 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -23.8) |
| [[HOP62 (line)]] | alt | 81.8 | 1 | 5 | [[TAK-901 (drug)]] 5 µM 6.14× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -26.0) |
| [[LoVo (line)]] | wt | 88.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -17.0) |
| [[A-172 (line)]] | wt | 58.3 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 7.22× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.6) |
| [[AsPC-1 (line)]] | alt | 59.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.0) |
| [[NCI-H460 (line)]] | wt | 53.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -17.2) |
| [[SW 900 (line)]] | alt | 54.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.9) |
| [[HT-29 (line)]] | alt | 66.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 40.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.7) |
| [[RKO (line)]] | wt | 87.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.0) |
| [[COLO 205 (line)]] | alt | 69.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 64.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -13.2) |
| [[J82 (line)]] | alt | 53.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.219× (z -11.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -14.9) |
| [[SW480 (line)]] | alt | 43.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -10.3) |
| [[A549 (line)]] | wt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.7) |
| [[AN3 CA (line)]] | alt | 88.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.6) |
| [[H4 (line)]] | wt | 88.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.6) |
| [[Hs 766T (line)]] | wt | 55.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 42.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.7) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.3) |
| [[SNU-1 (line)]] | wt | 88.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -24.2) |
| [[SNU-423 (line)]] | alt | 56.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -20.3) |
| [[SW1417 (line)]] | alt | 57.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.3) |
| [[A-427 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -13.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.1) |
| [[KATO III (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.6) |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0968× (z -8.8) |
| [[SW48 (line)]] | wt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.71 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[SSR1]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[NUS1]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 | STRING 450 |
| [[SEC63]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SEC13]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[STT3A]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[DDB1]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[COPG1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1L]] | -0.58 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[WBP4]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[RESF1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 | STRING 423 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises ALDH18A1's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without SLC1A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ALDH18A1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -32.6); signed map (-51.9, 8.8). **Vector** length 126, 41.5% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.51 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.6 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.7 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +2.5 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -24.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -9.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.8 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 18 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:95,605,941-95,656,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P5CS; previously GSAS, PYCS, SPG9 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: Glutamate and glutamine metabolism; Mitochondrial protein degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P54886](https://www.uniprot.org/uniprotkb/P54886) (Delta-1-pyrroline-5-carboxylate synthase):

> Bifunctional enzyme that converts glutamate to glutamate 5-semialdehyde, an intermediate in the biosynthesis of proline, ornithine and arginine.

**Summary**, from NCBI Gene [5832](https://www.ncbi.nlm.nih.gov/gene/5832):

> This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in this gene lead to hyperammonemia, hypoornithinemia, hypocitrullinemia, hypoargininemia and …

**Accessions** — [HGNC:9722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9722) · Entrez [5832](https://www.ncbi.nlm.nih.gov/gene/5832) · UniProt [P54886](https://www.uniprot.org/uniprotkb/P54886) · Ensembl [ENSG00000059573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059573)

## Data

Gene col 674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 674); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 674]; `tensor/DDL_lfc|DDL_z.npy` [674]; `embed/gene_vectors.npy` [674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 674 or target_col == 674). Every well: [[ALDH18A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH18A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
