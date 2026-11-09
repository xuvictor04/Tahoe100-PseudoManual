---
symbol: "SGF29"
type: "gene"
col: 10724
ensembl_id: "ENSG00000176476"
name: "SAGA complex associated factor 29"
location: "16p11.2"
module: 46
arm: "+"
pooled_cpm: 9.63
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SGF29

*SAGA complex associated factor 29* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +11.8, q 2e-29, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.378× (z -15.1, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTCF]] (+0.61, fdr 2e-05), [[MTG2]] (+0.60, fdr 1e-05), [[STARD7-AS1]] (+0.59, fdr 7e-05); moves opposite to [[NBEAL1]] (-0.49, fdr 4e-04), [[SPAG9]] (-0.48, fdr 2e-04), [[VAMP7]] (-0.46, fdr 8e-04, ⚠ not reproduced), [[BAIAP2-DT]] (-0.45, fdr 4e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FLJ12825]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.8 | 2e-29 | 29/44 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.7 | 3e-06 | 10/38 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 1e-05 | 17/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.002 | 11/44 (KATO III, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.2 | 0.003 | 11/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.8 | 0.014 | 14/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.037 | 5/46 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +3.5 | 0.038 | 11/47 (J82, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.042 | 5/46 (A-172, LoVo, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.064 | 8/48 (A-172, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -15.1 | 0e+00 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.608×** | -10.9 | 4e-25 | 35/46 (SNU-423, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -9.6 | 1e-19 | 31/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -7.8 | 6e-13 | 28/47 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.654×** | -6.6 | 6e-09 | 25/47 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.659×** | -6.4 | 1e-08 | 21/44 (SHP-77, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -6.1 | 9e-08 | 20/47 (NCI-H2030, SW48, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.715×** | -5.2 | 1e-05 | 21/47 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -5.2 | 1e-05 | 18/47 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.730×** | -4.9 | 6e-05 | 12/47 (SHP-77, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -4.6 | 2e-04 | 13/27 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -4.6 | 2e-04 | 12/40 (C32, J82, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -4.3 | 9e-04 | 17/47 (C-33 A, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.3 | 0.035 | 9/46 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.812×** | -3.2 | 0.048 | 5/48 (NCI-H460, SW 1088, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.051 | 11/44 (SNU-423, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.051 | 9/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -12.2) |
| [[A498 (line)]] | wt | 12.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.9) |
| [[LoVo (line)]] | wt | 9.88 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 5.62 | 0 | 2 | — | [[Hesperidin (drug)]] 0.5 µM 0.0594× (z -9.7) |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -9.8) |
| [[A-427 (line)]] | wt | 8.76 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.112× (z -10.0) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 9.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0800× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.11 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0709× (z -11.4) |
| [[J82 (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[LOX-IMVI (line)]] | wt | 4.86 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0907× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.261× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 6.88 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0977× (z -8.7) |
| [[SNU-423 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0846× (z -9.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTCF]] | +0.61 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MTG2]] | +0.60 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.59 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[AKAP8]] | +0.58 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R8]] | +0.57 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[ZBTB8A]] | +0.56 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[KLHL42]] | +0.56 | +0.52 / +0.25 | both halves | 4e-04 |  |
| [[SMAD1]] | +0.55 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[ASH2L]] | +0.54 | +0.38 / +0.48 | both halves | 6e-05 | pathway: Chromatin modifying enzymes |
| [[MRTO4]] | +0.54 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[FIZ1]] | +0.54 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[YDJC]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.49 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[SPAG9]] | -0.48 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[VAMP7]] | -0.46 | -0.19 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[BAIAP2-DT]] | -0.45 | -0.24 / -0.32 | both halves | 4e-04 |  |
| [[FAM8A1]] | -0.45 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[CAST]] | -0.45 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[OSBPL8]] | -0.45 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[HDAC1]] | -0.44 | -0.28 / -0.32 | both halves | 3e-04 | pathway: Chromatin modifying enzymes |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLJ12825]] | B | FLJ12825 activity strengthens SGF29's drug response | lines that do not express FLJ12825 (15) vs lines expressing it (33) | the lines without FLJ12825 respond 0.82× as strongly (z diff +0.58); strongest at Homoharringtonine 5 µM: 0.69x vs 0.47x (z diff +2.7) | 0.093 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.423). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.8, 17.4); signed map (-6.0, -17.9). **Vector** length 65.0, 9.61% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +1.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -15.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SAGA complex associated factor 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,553,915-28,591,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32446, TDRD29; previously CCDC101 |
| Gene groups (HGNC) | Tudor domain containing; ATAC complex; SAGA complex |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ES7](https://www.uniprot.org/uniprotkb/Q96ES7) (SAGA-associated factor 29):

> Chromatin reader component of some histone acetyltransferase (HAT) SAGA-type complexes like the TFTC-HAT, ATAC or STAGA complexes. SGF29 specifically recognizes and binds methylated 'Lys-4' of histone H3 (H3K4me), with a preference for trimethylated form (H3K4me3). In the SAGA-type complexes, SGF29 is required to recruit complexes to H3K4me. Involved in the response to endoplasmic reticulum (ER) stress by recruiting the SAGA complex to H3K4me, thereby promoting histone H3 acetylation and cell …

**Summary**, from NCBI Gene [112869](https://www.ncbi.nlm.nih.gov/gene/112869):

> CCDC101 is a subunit of 2 histone acetyltransferase complexes: the ADA2A (TADA2A; MIM 602276)-containing (ATAC) complex and the SPT3 (SUPT3H; MIM 602947)-TAF9 (MIM 600822)-GCN5 (KAT2A; MIM 602301)/PCAF (KAT2B; MIM 602303) acetylase (STAGA) complex. Both of these complexes contain either GCN5 or PCAF, which are paralogous acetyltransferases (Wang et al., 2008 [PubMed 18838386]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:25156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25156) · Entrez [112869](https://www.ncbi.nlm.nih.gov/gene/112869) · UniProt [Q96ES7](https://www.uniprot.org/uniprotkb/Q96ES7) · Ensembl [ENSG00000176476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176476)

## Data

Gene col 10724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10724); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10724]; `tensor/DDL_lfc|DDL_z.npy` [10724]; `embed/gene_vectors.npy` [10724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10724 or target_col == 10724). Every well: [[SGF29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGF29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
