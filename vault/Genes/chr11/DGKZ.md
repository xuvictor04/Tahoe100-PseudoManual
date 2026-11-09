---
symbol: "DGKZ"
type: "gene"
col: 7340
ensembl_id: "ENSG00000149091"
name: "diacylglycerol kinase zeta"
location: "11p11.2"
module: 2
arm: "+"
pooled_cpm: 23.4
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DGKZ

*diacylglycerol kinase zeta* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +13.5, q 1e-38, up in 26 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.50× (z +8.5, q 2e-15, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.803× (z -6.1, q 7e-07, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~16% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.340×, PANC-1 0.457×, MIA PaCa-2 0.372×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HCT15 0.0631×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.187×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (hTERT-HPNE 0.169×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0808×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX2]] (+0.70, fdr 7e-06), [[TCF3]] (+0.67, fdr 8e-06), [[SHANK3]] (+0.67, fdr 8e-06); moves opposite to [[FAM200A]] (-0.60, fdr 1e-05), [[C11orf71]] (-0.57, fdr 3e-05), [[PEX12]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRAF7]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +13.5 | 1e-38 | 26/32 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.87×** | +13.2 | 3e-37 | 31/40 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +10.0 | 4e-21 | 29/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +9.7 | 3e-20 | 21/36 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +9.7 | 4e-20 | 32/47 (HT-29, NCI-H1792, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +9.4 | 4e-19 | 31/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +8.5 | 2e-15 | 32/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.4 | 1e-11 | 29/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +7.4 | 1e-11 | 27/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.9 | 4e-10 | 30/47 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +5.5 | 2e-06 | 19/47 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.5 | 3e-04 | 22/47 (SK-MEL-2, SNU-423, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.23×** | +4.3 | 9e-04 | 16/47 (SW480, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +4.1 | 0.002 | 16/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.20×** | +3.9 | 0.004 | 12/47 (SW480, H4, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.014 | 10/44 (A498, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.014 | 8/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.028 | 6/48 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.054 | 4/48 (SW1417, SK-MEL-2, …) | top dose only | plate-row cell shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.071 | 8/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.098 | 3/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.340×, PANC-1 0.457×, MIA PaCa-2 0.372×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HCT15 0.0631×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.187×; ⚠ toxic; transcription drop); [[Menadione (drug)]] 5 µM in 1 line (hTERT-HPNE 0.169×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (AN3 CA 0.0808×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.803×** | -6.1 | 7e-07 | 21/48 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.4 | 0.003 | 3/48 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.830×** | -3.9 | 0.015 | 15/48 (CHP-212, H4, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.1 | 0.26 | 10/48 (A-172, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 28.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +12.7) | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0808× (z -8.7) |
| [[C32 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0631× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.169× (z -8.7) |
| [[KATO III (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX2]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TCF3]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[SHANK3]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 | same gene group |
| [[PACS2]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DOP1B]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NOMO1]] | +0.61 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MAPK1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | pathway: G alpha (q) signalling events |
| [[FAM20B]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GNAZ]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | -0.60 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[C11orf71]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PEX12]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[AEBP2]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[HELQ]] | -0.56 | -0.60 / -0.43 | both halves | 4e-05 |  |
| [[ZNF830]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CREB3L4]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[METTL18]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SNW1]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GPANK1]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[C1orf131]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF7]] | C | TRAF7's natural level weakens DGKZ's drug response | TRAF7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.09; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.1, -23.5); signed map (-44.3, -8.3). **Vector** length 81.8, 14.9% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.4 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.8 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.6 | +9.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.4 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,332,905-46,380,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAGK5, hDGKzeta, DGK-ZETA, DAGK6 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Diacylglycerol kinase family; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13574](https://www.uniprot.org/uniprotkb/Q13574) (Diacylglycerol kinase zeta):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes. Also plays an important role in the biosynthesis of complex lipids (Probable). Does not exhibit an acyl chain-dependent substrate specificity among …

**Summary**, from NCBI Gene [8525](https://www.ncbi.nlm.nih.gov/gene/8525):

> The protein encoded by this gene belongs to the eukaryotic diacylglycerol kinase family. It may attenuate protein kinase C activity by regulating diacylglycerol levels in intracellular signaling cascade and signal transduction. Alternative splicing occurs at this locus and multiple transcript variants encoding distinct isoforms have been identified. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:2857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2857) · Entrez [8525](https://www.ncbi.nlm.nih.gov/gene/8525) · UniProt [Q13574](https://www.uniprot.org/uniprotkb/Q13574) · Ensembl [ENSG00000149091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149091)

## Data

Gene col 7340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7340); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7340]; `tensor/DDL_lfc|DDL_z.npy` [7340]; `embed/gene_vectors.npy` [7340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7340 or target_col == 7340). Every well: [[DGKZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
