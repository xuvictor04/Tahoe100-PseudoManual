---
symbol: "PJVK"
type: "gene"
col: 12850
ensembl_id: "ENSG00000204311"
name: "pejvakin"
location: "2q31.2"
module: 35
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PJVK

*pejvakin* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +17.1, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.473× (z -6.8, q 8e-09, down in 19 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0458×; ⚠ cell-cycle shift, explains ~25% of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0733×; ⚠ transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.0801×); [[Eplerenone (drug)]] 0.5 µM in 1 line (HOP62 0.0584×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19A-DT]] (+0.83, fdr 7e-06), [[ATE1OSP]] (+0.79, fdr 1e-05), [[SUMO2P17]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +17.1 | 0e+00 | 33/33 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.94×** | +13.3 | 4e-38 | 5/5 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.05×** | +12.6 | 2e-34 | 12/14 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +12.1 | 2e-31 | 3/3 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +7.0 | 3e-10 | 6/14 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +6.7 | 2e-09 | 13/32 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +4.9 | 9e-05 | 10/30 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.8 | 1e-04 | 7/25 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.45×** | +4.7 | 2e-04 | 13/44 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 6e-04 | 8/44 (NCI-H2030, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.037 | 7/31 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.073 | 5/32 (SW 900, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.090 | 10/38 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0458×; ⚠ cell-cycle shift, explains ~25% of this change); [[Allantoin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0733×; ⚠ transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.0801×); [[Eplerenone (drug)]] 0.5 µM in 1 line (HOP62 0.0584×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.473×** | -6.8 | 8e-09 | 19/39 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.563×** | -5.2 | 6e-05 | 21/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.587×** | -4.8 | 3e-04 | 17/40 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.675×** | -3.5 | 0.056 | 15/43 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.683×** | -3.5 | 0.063 | 14/38 (A-172, SNU-1, …) | all doses, flat |  |
| [[Verapamil (drug)]] 0.05 µM |  | 0.687× | -3.1 | 0.16 | 7/38 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.526× | -3.0 | 0.18 | 8/36 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.527× | -3.0 | 0.18 | 5/26 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.45 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0801× (z -9.2) |
| [[HOP62 (line)]] | alt | 1.63 | 0 | 1 | — | [[Eplerenone (drug)]] 0.5 µM 0.0584× (z -8.6) |
| [[LoVo (line)]] | wt | 4.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.8× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 2.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H2030 (line)]] | alt | 4.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0733× (z -9.2) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0458× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +10.1) | — |
| [[A-172 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19A-DT]] | +0.83 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.79 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.79 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.78 | +0.80 / +0.53 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.77 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.77 | +0.82 / +0.45 | both halves | 3e-05 |  |
| [[LINC02951]] | +0.77 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[PSMG3-AS1]] | +0.77 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[ZCWPW1]] | +0.77 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[ZNF236-DT]] | +0.77 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.76 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[SPEN-AS1]] | +0.76 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PJVK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR1915HG]] | B | MIR1915HG activity raises PJVK's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without MIR1915HG | 0.012 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[ABCA17P]] | B | ABCA17P activity raises PJVK's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without ABCA17P | 0.076 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.878). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.4, 21.0); signed map (30.5, -3.5). **Vector** length 54.1, 7.48% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | pejvakin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:178,451,346-178,462,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB59 |
| Gene groups (HGNC) | Gasdermins |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0ZLH3](https://www.uniprot.org/uniprotkb/Q0ZLH3) (Pejvakin):

> Peroxisome-associated protein required to protect auditory hair cells against noise-induced damage. Acts by regulating noise-induced peroxisome proliferation in auditory hair cells and neurons, and promoting autophagic degradation of damaged peroxisomes (pexophagy). Noise overexposure increases reactive oxygen species (ROS) levels, causing oxidative damage to auditory hair cells and resulting in hearing loss. PJVK acts as a ROS sensor that recruits the autophagy machinery to trigger pexophagy …

**Summary**, from NCBI Gene [494513](https://www.ncbi.nlm.nih.gov/gene/494513):

> The protein encoded by this gene is a member of the gasdermin family, a family which is found only in vertebrates. The encoded protein is required for the proper function of auditory pathway neurons. Defects in this gene are a cause of non-syndromic sensorineural deafness autosomal recessive type 59 (DFNB59). [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:29502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29502) · Entrez [494513](https://www.ncbi.nlm.nih.gov/gene/494513) · UniProt [Q0ZLH3](https://www.uniprot.org/uniprotkb/Q0ZLH3) · Ensembl [ENSG00000204311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204311)

## Data

Gene col 12850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12850); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12850]; `tensor/DDL_lfc|DDL_z.npy` [12850]; `embed/gene_vectors.npy` [12850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12850 or target_col == 12850). Every well: [[PJVK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PJVK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
