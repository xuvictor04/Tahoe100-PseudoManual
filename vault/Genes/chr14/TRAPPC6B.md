---
symbol: "TRAPPC6B"
type: "gene"
col: 11284
ensembl_id: "ENSG00000182400"
name: "trafficking protein particle complex subunit 6B"
location: "14q21.1"
module: 68
arm: "+"
pooled_cpm: 29.79
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TRAPPC6B

*trafficking protein particle complex subunit 6B* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +21.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.823× (z -4.4, q 0.006, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.182×, C32 0.135×, SHP-77 0.287×, NCI-H460 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vismodegib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0714×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RC3H2]] (+0.71, fdr 7e-06), [[TAB3]] (+0.64, fdr 1e-05), [[WAC-AS1]] (+0.63, fdr 2e-05); moves opposite to [[RNF216]] (-0.59, fdr 1e-05), [[RRP1B]] (-0.59, fdr 3e-05), [[GARNL3]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +21.0 | 0e+00 | 44/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +20.4 | 0e+00 | 45/48 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +15.9 | 0e+00 | 41/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +12.3 | 8e-33 | 44/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +12.0 | 3e-31 | 40/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +11.5 | 8e-29 | 39/48 (J82, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +11.4 | 3e-28 | 40/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +10.9 | 1e-25 | 40/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +10.0 | 2e-21 | 36/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.9 | 2e-21 | 32/48 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +9.1 | 4e-18 | 33/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +8.7 | 1e-16 | 33/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +7.7 | 9e-13 | 25/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +6.8 | 5e-10 | 23/48 (Panc 03.27, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.2 | 2e-08 | 26/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 3e-07 | 27/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 2e-04 | 15/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11284.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.182×, C32 0.135×, SHP-77 0.287×, NCI-H460 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vismodegib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0714×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -4.4 | 0.006 | 21/48 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.905× | -3.2 | 0.39 | 8/48 (CHP-212, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.9 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 26.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 44.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.5) | — |
| [[LoVo (line)]] | wt | 31.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 31.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.6) | — |
| [[SW480 (line)]] | alt | 36.5 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 50.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 43.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.0) | — |
| [[A-427 (line)]] | wt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0714× (z -10.1) |
| [[C32 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.6) | — |
| [[J82 (line)]] | alt | 19.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 42.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | — |
| [[RKO (line)]] | wt | 26.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.4) | — |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RC3H2]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TAB3]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[WAC-AS1]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ZNF490]] | +0.63 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.62 | +0.68 / +0.40 | both halves | 4e-05 |  |
| [[ZNF44]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[IFT46]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SENP8]] | +0.60 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[SYNRG]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[STXBP2]] | +0.60 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[METTL6]] | +0.59 | +0.63 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF216]] | -0.59 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RRP1B]] | -0.59 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[GARNL3]] | -0.58 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[GNB1L]] | -0.57 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SPATA5]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CHCHD6]] | -0.57 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[PACC1]] | -0.56 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[TMEM201]] | -0.56 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ARHGAP8]] | -0.55 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[CAMK2G]] | -0.55 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[LRRC20]] | -0.55 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[SIMC1]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRAPPC6B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-20.7, 21.1); signed map (18.9, -17.6). **Vector** length 74.5, 14.4% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +20.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +12.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.6 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +3.1 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:39,147,811-39,170,532 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SZ2](https://www.uniprot.org/uniprotkb/Q86SZ2) (Trafficking protein particle complex subunit 6B):

> Component of a transport protein particle (TRAPP) complex that may function in specific stages of inter-organelle traffic. Specifically involved in the early development of neural circuitry, likely by controlling the frequency and amplitude of intracellular calcium transients implicated in the regulation of neuron differentiation and survival (Probable).

**Summary**, from NCBI Gene [122553](https://www.ncbi.nlm.nih.gov/gene/122553):

> TRAPPC6B is a component of TRAPP complexes, which are tethering complexes involved in vesicle transport (Kummel et al., 2005 [PubMed 16025134]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23066) · Entrez [122553](https://www.ncbi.nlm.nih.gov/gene/122553) · UniProt [Q86SZ2](https://www.uniprot.org/uniprotkb/Q86SZ2) · Ensembl [ENSG00000182400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182400)

## Data

Gene col 11284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11284); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11284]; `tensor/DDL_lfc|DDL_z.npy` [11284]; `embed/gene_vectors.npy` [11284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11284 or target_col == 11284). Every well: [[TRAPPC6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
