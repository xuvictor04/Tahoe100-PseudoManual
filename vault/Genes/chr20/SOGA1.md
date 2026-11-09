---
symbol: "SOGA1"
type: "gene"
col: 7399
ensembl_id: "ENSG00000149639"
name: "microtubule crosslinking factor 2"
location: "20q11.23"
module: 22
arm: "+"
pooled_cpm: 47.97
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SOGA1

*microtubule crosslinking factor 2* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +5.3, q 6e-05, up in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1792 3.38×, NCI-H460 2.21×, HepG2/C3A 3.25×, NCI-H23 2.05×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 3.83×, HepG2/C3A 2.85×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.80×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.311× (z -19.6, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NACC2]] (+0.65, fdr 8e-06), [[USP13]] (+0.59, fdr 2e-05), [[KPNA2]] (+0.58, fdr 1e-05); moves opposite to [[MAP3K13]] (-0.53, fdr 3e-05), [[FRRS1]] (-0.53, fdr 2e-05), [[PIGH]] (-0.45, fdr 3e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[GGT7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1792 3.38×, NCI-H460 2.21×, HepG2/C3A 3.25×, NCI-H23 2.05×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 3.83×, HepG2/C3A 2.85×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.80×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.3 | 6e-05 | 23/45 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.4 | 0.17 | 8/45 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.21× | +3.3 | 0.20 | 14/45 (A-172, HEC-1-A, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.21× | +3.2 | 0.20 | 18/44 (H4, NCI-H460, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -19.6 | 0e+00 | 42/45 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -17.4 | 0e+00 | 42/45 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -14.9 | 0e+00 | 41/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -9.1 | 1e-17 | 31/45 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -9.1 | 2e-17 | 32/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -7.5 | 6e-12 | 27/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -7.4 | 8e-12 | 28/45 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -6.5 | 5e-09 | 31/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -6.3 | 1e-08 | 26/45 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -6.1 | 5e-08 | 27/45 (SHP-77, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -5.7 | 5e-07 | 26/45 (AN3 CA, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -5.6 | 9e-07 | 21/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -5.6 | 9e-07 | 27/45 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -5.2 | 1e-05 | 24/45 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.741×** | -5.0 | 2e-05 | 23/45 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -4.4 | 3e-04 | 24/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.8 | 1 | 11 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -14.1) |
| [[SW480 (line)]] | alt | 66.6 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -23.2) |
| [[LoVo (line)]] | wt | 32.0 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 44.5 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.2) |
| [[J82 (line)]] | alt | 77.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -15.6) |
| [[HOP62 (line)]] | alt | 72.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 97.5 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -20.0) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.230× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 85.2 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -13.9) |
| [[A-172 (line)]] | wt | 80.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.2) |
| [[A498 (line)]] | wt | 61.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -13.0) |
| [[Hs 766T (line)]] | wt | 94.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -14.0) |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -15.0) |
| [[SW1417 (line)]] | alt | 52.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.4) |
| [[C-33 A (line)]] | alt | 75.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.201× (z -12.2) |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.4) |
| [[PANC-1 (line)]] | alt | 55.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 63.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -12.7) |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -8.7) |
| [[A549 (line)]] | wt | 43.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -9.9) |
| [[C32 (line)]] | wt | 46.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -8.7) |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 31.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.3) |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -9.8) |
| [[A-427 (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 94.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0300× (z -10.2) |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.137× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 35.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACC2]] | +0.65 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[USP13]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KPNA2]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SETD1B]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[KNSTRN]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[UBTF]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HMGB3]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[JADE3]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[KMT2D]] | +0.53 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[TACC3]] | +0.52 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[EHMT1]] | +0.52 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[BRD1]] | +0.52 | +0.35 / +0.53 | both halves | 1e-04 | STRING 420 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K13]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[FRRS1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PIGH]] | -0.45 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[TMEM144]] | -0.44 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[RYBP]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[GGT7]] | -0.44 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[GPR160]] | -0.44 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RALGAPA2]] | -0.44 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[CYB5R4]] | -0.44 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[RAB2B]] | -0.43 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[PREPL]] | -0.43 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGT7]] | C | SOGA1 activity raises GGT7's level | lines that do not express SOGA1 (3) vs lines expressing it (47) | 8.67× lower at baseline in the lines without SOGA1 | 0.001 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, ODAD4, GGT7; co-absent with the target |
| cells under [[Lonafarnib (drug)]] 5 µM | C | SOGA1 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express SOGA1 (3) vs lines expressing it (45) | the lines without SOGA1: 0.08× the cells of the other lines | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, ODAD4, GGT7 |
| [[DNMT3A]] | C | SOGA1 activity raises DNMT3A's level | lines that do not express SOGA1 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without SOGA1 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, ODAD4, GGT7 |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.4, -59.4); signed map (-53.6, -44.2). **Vector** length 109, 30.5% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.6 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.2 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +1.5 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.2 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -19.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -17.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.6 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -14.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | microtubule crosslinking factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,777,447-36,863,538 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ132F21.1, FLJ44670, SOGA; previously C20orf117, KIAA0889, SOGA1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O94964](https://www.uniprot.org/uniprotkb/O94964) (Microtubule cross-linking factor 2):

> Microtubule-associated factor that enables integration of the centrosomal and Golgi-associated microtubules on the Golgi membrane, supporting directional migration. Preferentially acts on the perinuclear microtubules accumulated around the Golgi. Associates with the Golgi membrane through the N-terminal coiled-coil region and directly binds microtubules through the C-terminal domain (By similarity). Required for faithful chromosome segregation during mitosis. Regulates autophagy by playing a …

**Summary**, from NCBI Gene [140710](https://www.ncbi.nlm.nih.gov/gene/140710):

> Involved in chromosome segregation. Located in microtubule; midbody; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16111) · Entrez [140710](https://www.ncbi.nlm.nih.gov/gene/140710) · UniProt [O94964](https://www.uniprot.org/uniprotkb/O94964) · Ensembl [ENSG00000149639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149639)

## Data

Gene col 7399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7399); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7399]; `tensor/DDL_lfc|DDL_z.npy` [7399]; `embed/gene_vectors.npy` [7399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7399 or target_col == 7399). Every well: [[SOGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
