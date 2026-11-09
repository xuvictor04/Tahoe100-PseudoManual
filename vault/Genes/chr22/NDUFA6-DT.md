---
symbol: "NDUFA6-DT"
type: "gene"
col: 14115
ensembl_id: "ENSG00000237037"
name: "NDUFA6 divergent transcript"
location: "22q13.2"
module: 23
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NDUFA6-DT

*NDUFA6 divergent transcript* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +22.1, q 0e+00, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.734× (z -4.7, q 0.002, down in 15 of 35 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.134×, SW480 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H460 0.159×, HT-29 0.0806×; ⚠ toxic); [[Celecoxib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0751×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.101×).
> Its strongest partners by |cos| (52 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 48 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HHLA3]] (+0.68, fdr 1e-04), [[UNK]] (+0.67, fdr 5e-04), [[OXA1L-DT]] (+0.65, fdr 0.001, ⚠ one half only (not replicated)), [[LRRC37A3]] (+0.65, fdr 1e-04); moves opposite to [[CTNNBL1]] (-0.62, fdr 7e-05), [[ST6GALNAC4]] (-0.61, fdr 0.001, ⚠ one half only (not replicated)), [[RPUSD1]] (-0.58, fdr 4e-04), [[RGS19]] (-0.56, fdr 8e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +22.1 | 0e+00 | 38/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +21.5 | 0e+00 | 41/45 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +10.6 | 5e-24 | 28/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +10.1 | 7e-22 | 31/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +10.1 | 7e-22 | 24/33 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.4 | 5e-19 | 26/43 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +8.3 | 8e-15 | 24/46 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.8 | 8e-10 | 17/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +6.6 | 3e-09 | 19/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.5 | 6e-09 | 16/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +5.8 | 3e-07 | 12/47 (HOP62, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +5.7 | 7e-07 | 15/47 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 2e-06 | 15/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 7e-06 | 13/46 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.7 | 9e-05 | 10/48 (HOP62, A498, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.73×** | +4.5 | 2e-04 | 8/40 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.134×, SW480 0.278×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H460 0.159×, HT-29 0.0806×; ⚠ toxic); [[Celecoxib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0751×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -4.7 | 0.002 | 15/35 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -4.4 | 0.003 | 10/47 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.766×** | -4.2 | 0.006 | 13/46 (HT-29, KATO III, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.807× | -3.4 | 0.11 | 12/46 (LS 180, RPMI-7951, …) | top dose only | position effect removed |
| [[Flutamide (drug)]] 5 µM |  | 0.812× | -3.3 | 0.11 | 6/47 (C32, RPMI-7951, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | 0.813× | -3.2 | 0.11 | 10/34 (LS 180, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | 0.810× | -3.2 | 0.12 | 13/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Ritonavir (drug)]] 0.5 µM |  | 0.823× | -3.1 | 0.14 | 9/45 (NCI-H661, NCI-H460, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.823× | -3.0 | 0.14 | 4/48 (SW 1088, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.691× | -3.0 | 0.14 | 5/20 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.14 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -9.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 37.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.7) | — |
| [[SW480 (line)]] | alt | 8.62 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 3.65 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.118× (z -9.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.101× (z -8.9) |
| [[HOP62 (line)]] | alt | 6.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 6.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0806× (z -9.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 1 | — | [[Celecoxib (drug)]] 0.05 µM 0.0751× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 6.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.0) | — |
| [[A-172 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 42 of them with an alert (⚠; 42 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HHLA3]] | +0.68 | +0.81 / +0.36 | both halves | 1e-04 | same gene group |
| [[UNK]] | +0.67 | +0.74 / +0.24 | both halves | 5e-04 |  |
| [[OXA1L-DT]] | +0.65 | +0.77 / +0.15 | ⚠ one half (not replicated) | 0.001 | same gene group |
| [[LRRC37A3]] | +0.65 | +0.69 / +0.34 | both halves | 1e-04 |  |
| [[THAP9]] | +0.64 | +0.70 / +0.32 | both halves | 2e-04 |  |
| [[NFYC]] | +0.64 | +0.71 / +0.27 | both halves | 3e-04 |  |
| [[SEPTIN7-DT]] | +0.63 | +0.67 / +0.28 | both halves | 3e-04 | same gene group |
| [[PPP1R3F]] | +0.63 | +0.68 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[CYP20A1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TCEANC]] | +0.63 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.62 | +0.69 / +0.20 | both halves | 7e-04 |  |
| [[ICA1L]] | +0.62 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[USP34-DT]] | +0.62 | +0.62 / +0.29 | both halves | 2e-04 | same gene group |
| [[TMEM91]] | +0.61 | +0.49 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBL1]] | -0.62 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.67 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[RPUSD1]] | -0.58 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[NEIL2]] | -0.58 | -0.57 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[STUB1]] | -0.56 | -0.41 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[RGS19]] | -0.56 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[C20orf27]] | -0.55 | -0.57 / -0.02 | ⚠ one half (not replicated) | 0.007 |  |
| [[EDA]] | -0.55 | -0.53 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[WASF3]] | -0.54 | -0.63 / +0.14 | ⚠ one half (not replicated) | 1.00 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFA6-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.7, 11.2); signed map (21.7, -16.0). **Vector** length 55.0, 7.07% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +22.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +21.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +10.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +6.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.2 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NDUFA6 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.2 — chr22:42,090,931-42,137,742 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously NDUFA6-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45273) · Entrez [100132273](https://www.ncbi.nlm.nih.gov/gene/100132273) · Ensembl [ENSG00000237037](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237037)

## Data

Gene col 14115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14115); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14115]; `tensor/DDL_lfc|DDL_z.npy` [14115]; `embed/gene_vectors.npy` [14115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14115 or target_col == 14115). Every well: [[NDUFA6-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA6-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
