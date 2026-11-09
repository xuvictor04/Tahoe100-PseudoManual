---
symbol: "BTF3L4"
type: "gene"
col: 5594
ensembl_id: "ENSG00000134717"
name: "basic transcription factor 3 like 4"
location: "1p32.3"
module: 33
arm: "+"
pooled_cpm: 47.75
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# BTF3L4

*basic transcription factor 3 like 4* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.90× (z +6.9, q 3e-09, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.10×; ⚠ cell-cycle shift, explains ~70% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.699× (z -10.5, q 7e-23, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YARS1]] (+0.58, fdr 1e-05), [[KLHDC4]] (+0.57, fdr 1e-05), [[RPF2]] (+0.56, fdr 1e-05); moves opposite to [[SLC5A3]] (-0.53, fdr 3e-05), [[MRPS6]] (-0.51, fdr 4e-05), [[DNAI7]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZMIZ1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5594.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.10×; ⚠ cell-cycle shift, explains ~70% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +6.9 | 3e-09 | 34/49 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.6 | 0.001 | 22/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +4.4 | 0.002 | 16/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.023 | 17/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.6 | 0.030 | 19/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.065 | 13/47 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.080 | 11/48 (HT-29, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.088 | 14/48 (H4, hTERT-HPNE, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -10.5 | 7e-23 | 37/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -8.6 | 2e-15 | 37/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -7.6 | 6e-12 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.712×** | -7.0 | 3e-10 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -5.6 | 3e-06 | 25/47 (H4, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.772×** | -5.1 | 3e-05 | 23/42 (A-427, SW48, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -4.5 | 6e-04 | 23/48 (HEC-1-A, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.809×** | -4.4 | 9e-04 | 23/48 (PANC-1, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.3 | 0.001 | 21/47 (LS 180, AN3 CA, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.2 | 0.002 | 19/48 (A498, H4, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.841× | -3.4 | 0.030 | 21/48 (RKO, SW48, …) | all doses, flat | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.732×** | -3.4 | 0.037 | 16/43 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.857× | -3.0 | 0.100 | 19/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.864× | -3.0 | 0.11 | 16/48 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 98.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -12.4) |
| [[SW480 (line)]] | alt | 53.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -14.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -13.4) |
| [[A498 (line)]] | wt | 35.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.540× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.8) |
| [[H4 (line)]] | wt | 52.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 46.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.269× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.3) |
| [[RKO (line)]] | wt | 56.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.8) |
| [[SHP-77 (line)]] | alt | 62.7 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0599× (z -15.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 76.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -8.8) |
| [[A-172 (line)]] | wt | 24.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.8) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[A-427 (line)]] | wt | 69.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.9) |
| [[AN3 CA (line)]] | alt | 62.1 | 0 | 1 | — | [[Sunitinib (drug)]] 0.5 µM 0.213× (z -8.6) |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.384× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.359× (z -9.0) |
| [[HT-29 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 73.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.361× (z -11.9) |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0813× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS1]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[KLHDC4]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RPF2]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMEM209]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NUP35]] | +0.55 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PEX7]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[COA1]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[GTF3C2]] | +0.52 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[BLTP3A]] | +0.52 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PTRH2]] | +0.52 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SCAP]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MDM4]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A3]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DNAI7]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZMIZ1]] | -0.50 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[DNAJA1]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MICALL2]] | -0.46 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ACVR1C]] | -0.45 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[HSPA1B]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[BAIAP2]] | -0.44 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[LINC00310]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TUBB3]] | -0.43 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[UBB]] | -0.43 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMIZ1]] | C | ZMIZ1 activity lowers BTF3L4's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without ZMIZ1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.7, -42.0); signed map (-10.9, -59.4). **Vector** length 104, 24.7% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -8.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.2 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | basic transcription factor 3 like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,056,199-52,090,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23908 |
| Matched by | ensembl_id |

UniProt [Q96K17](https://www.uniprot.org/uniprotkb/Q96K17) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30547) · Entrez [91408](https://www.ncbi.nlm.nih.gov/gene/91408) · UniProt [Q96K17](https://www.uniprot.org/uniprotkb/Q96K17) · Ensembl [ENSG00000134717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134717)

## Data

Gene col 5594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5594); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5594]; `tensor/DDL_lfc|DDL_z.npy` [5594]; `embed/gene_vectors.npy` [5594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5594 or target_col == 5594). Every well: [[BTF3L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTF3L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
