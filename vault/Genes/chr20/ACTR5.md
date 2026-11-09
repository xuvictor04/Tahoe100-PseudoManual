---
symbol: "ACTR5"
type: "gene"
col: 2137
ensembl_id: "ENSG00000101442"
name: "actin related protein 5"
location: "20q11.23"
module: 26
arm: "-"
pooled_cpm: 11.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ACTR5

*actin related protein 5* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.21× (z +9.4, q 4e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.709× (z -5.7, q 6e-06, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -5.3, q 3e-05, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTPBP3]] (+0.74, fdr 7e-06), [[BRAT1]] (+0.74, fdr 7e-06), [[RSAD1]] (+0.73, fdr 1e-05); moves opposite to [[LINC02307]] (-0.72, fdr 1e-05), [[MZF1-AS1]] (-0.70, fdr 1e-05), [[PPP1R12A-AS2]] (-0.69, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +9.4 | 4e-18 | 41/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +8.7 | 8e-16 | 39/47 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.00×** | +8.2 | 5e-14 | 36/47 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.011 | 18/47 (NCI-H2347, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.2 | 0.16 | 1/48 (C-33 A) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.30× | +3.1 | 0.19 | 8/47 (SW1417, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.709×** | -5.7 | 6e-06 | 29/46 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -5.3 | 3e-05 | 28/47 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -5.2 | 3e-05 | 28/47 (SW480, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.6 | 5e-04 | 21/48 (A-172, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.686×** | -4.3 | 0.002 | 21/46 (PANC-1, A-172, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -4.1 | 0.003 | 25/45 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.018 | 19/47 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.019 | 18/44 (A-427, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.758×** | -3.3 | 0.071 | 17/37 (HEC-1-A, A-427, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.244× (z -9.1) |
| [[A-172 (line)]] | wt | 8.12 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.3) |
| [[A498 (line)]] | wt | 7.94 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.5) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -9.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 9.38 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0700× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.123× (z -8.7) ⚠ transcription drop |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H1792 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 8.55 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.113× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[RKO (line)]] | wt | 13.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.9) |
| [[SW480 (line)]] | alt | 16.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.319× (z -8.9) |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP3]] | +0.74 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BRAT1]] | +0.74 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.73 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[WDR5]] | +0.72 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.69 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[ELP1]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NOMO3]] | +0.68 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[DFFB]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ASB13]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[SDHAF3]] | +0.67 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.67 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[METAP1]] | +0.67 | +0.70 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02307]] | -0.72 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.70 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.69 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.68 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[ARHGAP15]] | -0.68 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | -0.68 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CCDC90B-AS1]] | -0.67 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[USP11]] | -0.67 | -0.60 / -0.53 | both halves | 1e-05 | pathway: Deubiquitination |
| [[MMADHC-DT]] | -0.67 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[FAM151B]] | -0.66 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[ANGPT2]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[LINC02955]] | -0.66 | -0.66 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ACTR5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers ACTR5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SATB1]] | B | SATB1 activity lowers ACTR5's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.41× higher at baseline in the lines without SATB1 | 0.039 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[ZHX2]] | B | ZHX2 activity lowers ACTR5's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.63× higher at baseline in the lines without ZHX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[TTC6]] | B | TTC6 activity lowers ACTR5's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.05× higher at baseline in the lines without TTC6 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.1, -2.1); signed map (-40.4, -13.8). **Vector** length 78.3, 14.2% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -8.2 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.7 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:38,748,460-38,772,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12785, Arp5, INO80M |
| Gene groups (HGNC) | INO80 complex subunits; Actin related proteins |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9F9](https://www.uniprot.org/uniprotkb/Q9H9F9) (Actin-related protein 5):

> Proposed core component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair. Involved in DNA double-strand break repair and UV-damage excision repair.

**Summary**, from NCBI Gene [79913](https://www.ncbi.nlm.nih.gov/gene/79913):

> Predicted to enable enzyme regulator activity. Involved in several processes, including DNA repair; positive regulation of DNA-templated transcription; and regulation of DNA metabolic process. Located in cytoplasm and nucleus. Part of Ino80 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14671) · Entrez [79913](https://www.ncbi.nlm.nih.gov/gene/79913) · UniProt [Q9H9F9](https://www.uniprot.org/uniprotkb/Q9H9F9) · Ensembl [ENSG00000101442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101442)

## Data

Gene col 2137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2137); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2137]; `tensor/DDL_lfc|DDL_z.npy` [2137]; `embed/gene_vectors.npy` [2137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2137 or target_col == 2137). Every well: [[ACTR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
