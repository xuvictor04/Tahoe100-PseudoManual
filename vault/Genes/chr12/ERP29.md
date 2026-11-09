---
symbol: "ERP29"
type: "gene"
col: 1580
ensembl_id: "ENSG00000089248"
name: "endoplasmic reticulum protein 29"
location: "12q24.13"
module: 45
arm: "+"
pooled_cpm: 42.27
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ERP29

*endoplasmic reticulum protein 29* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +13.9, q 6e-41, up in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.32× (z +4.3, q 0.002, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.757× (z -4.3, q 0.009, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.225×, SNU-1 0.204×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.453×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.298×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAH1]] (+0.72, fdr 7e-06), [[DNASE2]] (+0.66, fdr 7e-06), [[USF2]] (+0.66, fdr 7e-06); moves opposite to [[NIPAL1]] (-0.61, fdr 1e-05), [[LINC01204]] (-0.58, fdr 1e-05), [[GEMIN4]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[VAT1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +13.9 | 6e-41 | 44/45 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +11.1 | 3e-26 | 39/39 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.7 | 2e-12 | 42/43 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +6.2 | 7e-08 | 39/46 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.002 | 34/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.003 | 34/48 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.41×** | +3.7 | 0.015 | 27/47 (NCI-H460, COLO 205, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.072 | 25/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.36×** | +3.3 | 0.072 | 28/47 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.22× | +3.1 | 0.11 | 23/48 (SW480, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.33× | +3.0 | 0.12 | 17/46 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.12 | 22/48 (SW 1271, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1580.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.225×, SNU-1 0.204×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.453×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.298×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -4.3 | 0.009 | 27/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -4.0 | 0.015 | 26/48 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 42.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 44.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.6× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 45.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 52.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.6) |
| [[KATO III (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +11.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -9.5) |
| [[C-33 A (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +10.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 60.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -8.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 81.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -8.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAH1]] | +0.72 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[DNASE2]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[USF2]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ARL6IP5]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[IDH1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[CTSD]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RHOT1]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[RTN3]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CLGN]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12B]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ANP32B]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[LINC01204]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GEMIN4]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[APEX2]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[AGO2]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SOWAHC]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[C11orf91]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[HAS3]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PHLDA1]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[POLR2D]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAT1]] | C | VAT1 activity weakens ERP29's drug response | lines that do not express VAT1 (3) vs lines expressing it (45) | the lines without VAT1 respond 1.09× as strongly (z diff -0.80); strongest at Dinaciclib 0.05 µM: 3.25x vs 2.14x (z diff -3.2) | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SH2B3, C12orf75, SKAP2; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-16.9, -19.1); signed map (-24.4, -3.8). **Vector** length 79.1, 23.2% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.3 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.3 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.0 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum protein 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,013,348-112,023,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERp28, ERp31, PDI-DB, PDIA9; previously C12orf8 |
| Gene groups (HGNC) | Protein disulfide isomerases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P30040](https://www.uniprot.org/uniprotkb/P30040) (Endoplasmic reticulum resident protein 29):

> Does not seem to be a disulfide isomerase. Plays an important role in the processing of secretory proteins within the endoplasmic reticulum (ER), possibly by participating in the folding of proteins in the ER.

**Summary**, from NCBI Gene [10961](https://www.ncbi.nlm.nih.gov/gene/10961):

> This gene encodes a protein which localizes to the lumen of the endoplasmic reticulum (ER). It is a member of the protein disulfide isomerase (PDI) protein family but lacks an active thioredoxin motif, suggesting that this protein does not function as a disulfide isomerase. The canonical protein dimerizes and is thought to play a role in the processing of secretory proteins within the ER. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by …

**Accessions** — [HGNC:13799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13799) · Entrez [10961](https://www.ncbi.nlm.nih.gov/gene/10961) · UniProt [P30040](https://www.uniprot.org/uniprotkb/P30040) · Ensembl [ENSG00000089248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089248)

## Data

Gene col 1580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1580); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1580]; `tensor/DDL_lfc|DDL_z.npy` [1580]; `embed/gene_vectors.npy` [1580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1580 or target_col == 1580). Every well: [[ERP29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERP29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
