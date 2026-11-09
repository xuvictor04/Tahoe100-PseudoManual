---
symbol: "CDK2"
type: "gene"
col: 4427
ensembl_id: "ENSG00000123374"
name: "cyclin dependent kinase 2"
location: "12q13.2"
module: 6
arm: "+"
pooled_cpm: 16.45
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDK2

*cyclin dependent kinase 2* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (24 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +17.8, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.29× (z +5.6, q 9e-07, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -12.5, q 3e-33, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCA]] (+0.79, fdr 7e-06), [[MYBL2]] (+0.79, fdr 7e-06), [[TK1]] (+0.79, fdr 7e-06); moves opposite to [[SNHG32]] (-0.69, fdr 7e-06), [[CCDC174]] (-0.68, fdr 1e-05), [[ATF4]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 27 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.13×** | +17.8 | 0e+00 | 40/41 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.00×** | +16.5 | 0e+00 | 26/27 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.58×** | +13.6 | 4e-40 | 31/36 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.24×** | +12.5 | 6e-34 | 40/45 (SW480, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.93×** | +10.2 | 1e-22 | 31/47 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.92×** | +10.2 | 2e-22 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.87×** | +9.7 | 2e-20 | 34/47 (SW480, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.83×** | +9.4 | 4e-19 | 34/47 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.79×** | +9.0 | 1e-17 | 30/47 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.65×** | +7.8 | 2e-13 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.69×** | +7.8 | 2e-13 | 28/46 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.60×** | +7.3 | 2e-11 | 28/45 (SW1417, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.37×** | +6.9 | 2e-10 | 22/46 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.7 | 1e-09 | 2/48 (RKO, SHP-77) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.51×** | +6.1 | 3e-08 | 24/42 (SK-MEL-2, LoVo, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.6 | 9e-07 | 17/48 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Lopinavir (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.023 | 3/47 (SW480, C-33 A, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.035 | 8/48 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.20×** | +2.9 | 0.081 | 6/45 (BT-474, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4427.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -12.5 | 3e-33 | 36/46 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -9.3 | 4e-18 | 31/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.844× | -3.7 | 0.036 | 16/48 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.045 | 12/48 (A-427, hTERT-HPNE, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -3.5 | 0.052 | 17/46 (A-427, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.816× | -3.2 | 0.14 | 17/45 (SNU-1, A498, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | 0.688× | -3.0 | 0.18 | 8/44 (A-427, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.818× | -3.0 | 0.18 | 12/48 (A-427, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 54.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.18× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Vinblastine (sulfate) (drug)]] 5 µM 0.458× (z -8.7) |
| [[SW480 (line)]] | alt | 24.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-427 (line)]] | wt | 29.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -14.3) |
| [[PANC-1 (line)]] | alt | 13.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.69× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0723× (z -10.8) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0863× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.1) |
| [[KATO III (line)]] | alt | 15.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.37× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.86 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Adenosine (drug)]] 0.05 µM 0.169× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 10.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.5) |
| [[RKO (line)]] | wt | 34.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.8) |
| [[A498 (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 1 | — | [[Rapamycin (drug)]] 0.5 µM 0.176× (z -8.6) |
| [[LoVo (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.6) |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0541× (z -17.8) |
| [[A-172 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCA]] | +0.79 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.79 | +0.75 / +0.82 | both halves | 7e-06 | pathway: G0 and Early G1; STRING 986 |
| [[TK1]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 | pathway: G1/S Transition; STRING 440 |
| [[CENPK]] | +0.79 | +0.78 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PCLAF]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.78 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[WDR76]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[MCM8]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 661 |
| [[GINS2]] | +0.77 | +0.85 / +0.68 | both halves | 7e-06 | pathway: DNA Replication |
| [[CLSPN]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 736 |
| [[XRCC2]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[MCM3]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 973 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG32]] | -0.69 | -0.76 / -0.61 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.68 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[ATF4]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[WASHC1]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[SNHG8]] | -0.63 | -0.67 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.783). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.3, -42.1); signed map (-36.5, -44.6). **Vector** length 107, 26.4% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.59 to 65); *DNA strand elongation* (reactome, mean cos +0.64 to 28); *E2F G1/S* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.2 | +10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.4 | +17.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.2 | +16.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.1 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,966,781-55,972,789 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, APOPTOSIS, UV_RESPONSE_UP, MYC_TARGETS_V1 |
| Reactome | 69 pathways, smallest: G2 Phase; Phosphorylation of proteins involved in G1/S transition by active Cyclin E:Cdk2 complexes; PTK6 Regulates Cell Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P24941](https://www.uniprot.org/uniprotkb/P24941) (Cyclin-dependent kinase 2):

> Serine/threonine-protein kinase involved in the control of the cell cycle; essential for meiosis, but dispensable for mitosis. Phosphorylates CABLES1, CTNNB1, CDK2AP2, ERCC6, NBN, USP37, p53/TP53, NPM1, CDK7, RB1, BRCA2, MYC, NPAT, SUV39H1, EZH2. Triggers duplication of centrosomes and DNA. Acts at the G1-S transition to promote the E2F transcriptional program and the initiation of DNA synthesis, and modulates G2 progression; controls the timing of entry into mitosis/meiosis by controlling the …

**Summary**, from NCBI Gene [1017](https://www.ncbi.nlm.nih.gov/gene/1017):

> This gene encodes a member of a family of serine/threonine protein kinases that participate in cell cycle regulation. The encoded protein is the catalytic subunit of the cyclin-dependent protein kinase complex, which regulates progression through the cell cycle. Activity of this protein is especially critical during the G1 to S phase transition. This protein associates with and regulated by other subunits of the complex including cyclin A or E, CDK inhibitor p21Cip1 (CDKN1A), and p27Kip1 …

**Accessions** — [HGNC:1771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1771) · Entrez [1017](https://www.ncbi.nlm.nih.gov/gene/1017) · UniProt [P24941](https://www.uniprot.org/uniprotkb/P24941) · Ensembl [ENSG00000123374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123374)

## Data

Gene col 4427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4427); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4427]; `tensor/DDL_lfc|DDL_z.npy` [4427]; `embed/gene_vectors.npy` [4427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4427 or target_col == 4427). Every well: [[CDK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
