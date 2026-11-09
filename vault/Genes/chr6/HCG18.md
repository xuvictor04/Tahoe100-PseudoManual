---
symbol: "HCG18"
type: "gene"
col: 13777
ensembl_id: "ENSG00000231074"
name: "HLA complex group 18"
location: "6p22.1"
module: 17
arm: "-"
pooled_cpm: 86.49
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# HCG18

*HLA complex group 18* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +6.5, q 3e-08, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.623× (z -10.8, q 1e-24, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.637× (z -7.3, q 6e-11, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNT1]] (+0.71, fdr 7e-06), [[ACAD9]] (+0.71, fdr 1e-05), [[KANSL1L-AS1]] (+0.68, fdr 1e-05); moves opposite to [[KBTBD3]] (-0.69, fdr 1e-05), [[ALAD]] (-0.67, fdr 1e-05), [[TMEM185A]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TSPAN15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.5 | 3e-08 | 30/49 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.1 | 8e-05 | 33/48 (HT-29, SHP-77, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.1 | 0.007 | 21/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.022 | 25/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.25 | 15/48 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.21× | +3.0 | 0.25 | 14/48 (A498, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13777.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.623×** | -10.8 | 1e-24 | 40/48 (PANC-1, RKO, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.624×** | -7.6 | 8e-12 | 40/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.637×** | -7.3 | 6e-11 | 38/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -6.7 | 2e-09 | 35/47 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -6.7 | 2e-09 | 38/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.660×** | -6.7 | 2e-09 | 38/48 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.735×** | -4.8 | 1e-04 | 30/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -4.4 | 9e-04 | 27/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.764×** | -4.3 | 9e-04 | 31/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.775×** | -4.1 | 0.002 | 27/48 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.841× | -4.0 | 0.004 | 23/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.795×** | -3.7 | 0.010 | 25/48 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.018 | 27/48 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.039 | 22/48 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.831× | -3.0 | 0.10 | 18/48 (KATO III, PANC-1, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 96.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -19.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 78.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A549 (line)]] | wt | 52.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 86.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.353× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -12.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[Panc 03.27 (line)]] | alt | 87.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 127 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.245× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 90.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.101× (z -10.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HOP62 (line)]] | alt | 113 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.78× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.119× (z -9.8) ⚠ toxic |
| [[HS-578T (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 95.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.465× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.408× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 97.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.415× (z -8.8) |
| [[SW480 (line)]] | alt | 96.1 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[A-172 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 99.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.71 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[HCG17]] | +0.68 | +0.53 / +0.58 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IDI2-AS1]] | +0.67 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PCBD2]] | +0.67 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PIGW]] | +0.66 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.65 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[TSTD2]] | +0.65 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ZNF26]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.64 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PIGG]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ALG8]] | +0.64 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.69 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[ALAD]] | -0.67 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.66 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[CAT]] | -0.66 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[HPF1]] | -0.64 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[TMEM14A]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[FAM229B]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MFSD13A]] | -0.60 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[HAUS4]] | -0.60 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ARNT]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SNX2]] | -0.60 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[RNF114]] | -0.59 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN15]] | B | TSPAN15 activity lowers HCG18's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.36× higher at baseline in the lines without TSPAN15 | 0.052 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[PIP4P2]] | C | PIP4P2 activity weakens HCG18's drug response | lines that do not express PIP4P2 (4) vs lines expressing it (45) | the lines without PIP4P2 respond 1.30× as strongly (z diff -1.01); strongest at Digitoxin 5 µM: 0.43x vs 0.65x (z diff -4.5) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[KCNJ14]] | C | KCNJ14's natural level strengthens HCG18's drug response | KCNJ14's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.07; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (8.5, -8.7); signed map (14.5, 1.0). **Vector** length 121, 36.1% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.5 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.8 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.8 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.6 | -10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex group 18 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p22.1 — chr6:30,286,690-30,327,382 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ31598, FLJ25550, Em:AB014087.1; previously HCG17 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31337) · Entrez [414777](https://www.ncbi.nlm.nih.gov/gene/414777) · Ensembl [ENSG00000231074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231074)

## Data

Gene col 13777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13777); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13777]; `tensor/DDL_lfc|DDL_z.npy` [13777]; `embed/gene_vectors.npy` [13777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13777 or target_col == 13777). Every well: [[HCG18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
