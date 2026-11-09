---
symbol: "HADHB"
type: "gene"
col: 6109
ensembl_id: "ENSG00000138029"
name: "hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta"
location: "2p23.3"
module: 5
arm: "-"
pooled_cpm: 82.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# HADHB

*hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +16.3, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.793× (z -5.4, q 3e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.421×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.507×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC1]] (+0.70, fdr 8e-06), [[SIRT2]] (+0.64, fdr 7e-06), [[CCNI]] (+0.64, fdr 7e-06); moves opposite to [[HNRNPAB]] (-0.67, fdr 7e-06), [[GRWD1]] (-0.62, fdr 1e-05), [[CCT5]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +16.3 | 0e+00 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +8.7 | 6e-16 | 39/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +8.1 | 9e-14 | 39/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +7.8 | 1e-12 | 33/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.6 | 2e-12 | 28/49 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +4.8 | 1e-04 | 21/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 5e-04 | 23/50 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.005 | 21/49 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.19× | +3.9 | 0.007 | 21/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.020 | 20/48 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.11× | +3.5 | 0.020 | 6/48 (A-427, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.020 | 21/44 (LS 180, SK-MEL-2, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.020 | 20/48 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Mifepristone (drug)]] 5 µM |  | 1.15× | +3.2 | 0.056 | 13/48 (HOP62, SW 900, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.060 | 9/48 (SW1417, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.421×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.507×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -5.4 | 3e-05 | 28/48 (HOP62, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -5.2 | 5e-05 | 29/48 (LS 180, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -4.3 | 0.004 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | **0.833×** | -4.1 | 0.005 | 23/47 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.1 | 0.005 | 21/48 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.850× | -3.8 | 0.012 | 19/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -3.8 | 0.013 | 19/47 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.859× | -3.6 | 0.025 | 17/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 70.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.4) | [[Docetaxel (drug)]] 0.05 µM 0.472× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 43.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.0) | — |
| [[LS 180 (line)]] | wt | 52.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 81.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 58.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.9) | — |
| [[J82 (line)]] | alt | 41.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 86.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +25.2) | — |
| [[A-172 (line)]] | wt | 82.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.2) | — |
| [[A498 (line)]] | wt | 66.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 99.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.3) | [[Auranofin (drug)]] 5 µM 0.507× (z -9.2) |
| [[PANC-1 (line)]] | alt | 94.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +20.0) | — |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.7) | — |
| [[A-427 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 81.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 90.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.1) | — |
| [[RKO (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 72.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.419× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 81.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 84.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.7) | — |
| [[SW480 (line)]] | alt | 96.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC1]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[SIRT2]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CCNI]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CCS]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CFAP36]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZCRB1]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TTC21A]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[NPHP3]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CDK7]] | +0.62 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[SEC22A]] | +0.62 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ACADSB]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 986 |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.67 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[GRWD1]] | -0.62 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[CCT5]] | -0.60 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[VANGL1]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[GBX2-AS1]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NAA15]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ZNF8]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[WDR77]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PPP2CA]] | -0.58 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[EIF5A]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[APPAT]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HADHB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APC]] | C | the direction of APC's effect on HADHB's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 40 not recorded | the APC-altered lines respond 1.91× as strongly (z diff -2.15); strongest at Panobinostat 5 µM: 2.16x vs 1.40x (z diff -4.3) | 0.091 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.0, -31.8); signed map (-15.1, 3.3). **Vector** length 111, 28.4% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +16.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.2 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.4 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains <1% of this change | -6.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,243,170-26,290,465 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTPB |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 13 pathways, smallest: Beta oxidation of palmitoyl-CoA to myristoyl-CoA; Beta oxidation of lauroyl-CoA to decanoyl-CoA-CoA; Beta oxidation of hexanoyl-CoA to butanoyl-CoA |
| Matched by | ensembl_id |

**Function**, from UniProt [P55084](https://www.uniprot.org/uniprotkb/P55084) (Trifunctional enzyme subunit beta, mitochondrial):

> Mitochondrial trifunctional enzyme catalyzes the last three of the four reactions of the mitochondrial beta-oxidation pathway. The mitochondrial beta-oxidation pathway is the major energy-producing process in tissues and is performed through cycles of four consecutive reactions. Each beta-oxidation cycle shortens the fatty acyl-CoA by two carbons, yielding one acetyl-CoA (for the citric acid cycle), one FADH(2), and one NADH (which donate electrons to the respiratory chain for ATP production). …

**Summary**, from NCBI Gene [3032](https://www.ncbi.nlm.nih.gov/gene/3032):

> This gene encodes the beta subunit of the mitochondrial trifunctional protein, which catalyzes the last three steps of mitochondrial beta-oxidation of long chain fatty acids. The mitochondrial membrane-bound heterocomplex is composed of four alpha and four beta subunits, with the beta subunit catalyzing the 3-ketoacyl-CoA thiolase activity. The encoded protein can also bind RNA and decreases the stability of some mRNAs. The genes of the alpha and beta subunits of the mitochondrial trifunctional …

**Accessions** — [HGNC:4803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4803) · Entrez [3032](https://www.ncbi.nlm.nih.gov/gene/3032) · UniProt [P55084](https://www.uniprot.org/uniprotkb/P55084) · Ensembl [ENSG00000138029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138029)

## Data

Gene col 6109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6109); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6109]; `tensor/DDL_lfc|DDL_z.npy` [6109]; `embed/gene_vectors.npy` [6109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6109 or target_col == 6109). Every well: [[HADHB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HADHB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
