---
symbol: "TM2D3"
type: "gene"
col: 11513
ensembl_id: "ENSG00000184277"
name: "TM2 domain containing 3"
location: "15q26.3"
module: 24
arm: "+"
pooled_cpm: 30.01
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TM2D3

*TM2 domain containing 3* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.49× (z +7.6, q 2e-11, up in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.25× (z +4.4, q 0.003, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.580× (z -9.7, q 2e-19, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.0986×, NCI-H1573 0.191×, SHP-77 0.208×, A549 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.298×, A498 0.346×, SK-MEL-2 0.213×; ⚠ toxic; transcription drop); [[Sunitinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.144×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.377×); [[Fluvoxamine (drug)]] 0.05 µM in 1 line (AN3 CA 0.134×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLASRP]] (+0.59, fdr 1e-05), [[MTIF3]] (+0.59, fdr 1e-05), [[PCGF1]] (+0.59, fdr 1e-05, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[RPP21]] (+0.58, fdr 2e-05); moves opposite to [[MAPRE1]] (-0.60, fdr 4e-05), [[APP]] (-0.54, fdr 1e-04), [[EPB41L2]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.6 | 2e-11 | 35/47 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.4 | 0.003 | 15/48 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.004 | 18/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.15× | +4.0 | 0.009 | 20/47 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.013 | 17/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.015 | 17/48 (Hs 766T, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.070 | 16/47 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.16× | +3.0 | 0.19 | 20/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.0986×, NCI-H1573 0.191×, SHP-77 0.208×, A549 0.257×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.298×, A498 0.346×, SK-MEL-2 0.213×; ⚠ toxic; transcription drop); [[Sunitinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.144×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.377×); [[Fluvoxamine (drug)]] 0.05 µM in 1 line (AN3 CA 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.580×** | -9.7 | 2e-19 | 27/44 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -9.0 | 4e-17 | 22/37 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.740×** | -5.9 | 5e-07 | 28/48 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.796×** | -4.1 | 0.005 | 17/40 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.706×** | -3.6 | 0.038 | 18/43 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.849× | -3.2 | 0.13 | 16/48 (HOP62, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 35.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +19.4) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -10.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -9.2) |
| [[A498 (line)]] | wt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -11.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 35.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.5) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 5 µM 0.191× (z -15.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 39.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.96× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A549 (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 41.1 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.134× (z -8.8) |
| [[C32 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.2) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -20.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.144× (z -12.2) ⚠ toxic |
| [[J82 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.5) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.468× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 8 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASRP]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | +0.59 | +0.50 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MRPL43]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | +0.57 | +0.43 / +0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX14]] | +0.56 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[LAMTOR5]] | +0.56 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[TARS2]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[FBXL15]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[MINCR]] | +0.55 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[SCNM1]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PUS3]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TMEM101]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.60 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[APP]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.50 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[STIP1]] | -0.50 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[TMX1]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DHFR]] | -0.49 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[YWHAZ]] | -0.49 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PABIR2]] | -0.48 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ACSL5]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TM2D3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.589). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.5, -13.8); signed map (-16.7, -4.5). **Vector** length 86.5, 16.6% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.5 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TM2 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,621,444-101,652,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BLP2, FLJ22604 |
| Gene groups (HGNC) | TM2 domain containing family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRN9](https://www.uniprot.org/uniprotkb/Q9BRN9) (TM2 domain-containing protein 3):

> Positive regulator of Notch signaling, required for activation of NOTCH1 intracellular processing and NOTCH1 localization to the cell membrane.

**Summary**, from NCBI Gene [80213](https://www.ncbi.nlm.nih.gov/gene/80213):

> The protein encoded by this gene contains a structural module related to that of the seven transmembrane domain G protein-coupled receptor superfamily. This protein has sequence and structural similarities to the beta-amyloid binding protein (BBP), but, unlike BBP, it does not regulate a response to beta-amyloid peptide. This protein may have regulatory roles in cell death or proliferation signal cascades. Several alternatively spliced transcript variants of this gene are described but the full …

**Accessions** — [HGNC:24128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24128) · Entrez [80213](https://www.ncbi.nlm.nih.gov/gene/80213) · UniProt [Q9BRN9](https://www.uniprot.org/uniprotkb/Q9BRN9) · Ensembl [ENSG00000184277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184277)

## Data

Gene col 11513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11513); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11513]; `tensor/DDL_lfc|DDL_z.npy` [11513]; `embed/gene_vectors.npy` [11513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11513 or target_col == 11513). Every well: [[TM2D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM2D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
