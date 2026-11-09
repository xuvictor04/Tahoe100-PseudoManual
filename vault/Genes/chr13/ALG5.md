---
symbol: "ALG5"
type: "gene"
col: 4209
ensembl_id: "ENSG00000120697"
name: "ALG5 dolichyl-phosphate beta-glucosyltransferase"
location: "13q13.3"
module: 49
arm: "+"
pooled_cpm: 30.08
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# ALG5

*ALG5 dolichyl-phosphate beta-glucosyltransferase* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.21× (z +4.8, q 7e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.450× (z -14.0, q 9e-42, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARL]] (+0.75, fdr 7e-06), [[DERL2]] (+0.74, fdr 7e-06), [[RUSF1]] (+0.69, fdr 7e-06); moves opposite to [[JUN]] (-0.61, fdr 1e-05), [[ZSWIM6]] (-0.51, fdr 1e-05), [[TLE4]] (-0.51, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GABBR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.8 | 7e-04 | 23/48 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.22 | 10/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.2 | 0.22 | 8/48 (RKO, HOP62, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.22 | 11/47 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.30 | 11/48 (NCI-H1573, hTERT-HPNE, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -14.0 | 9e-42 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -12.6 | 5e-34 | 39/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -10.7 | 2e-24 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.701×** | -8.8 | 2e-16 | 33/47 (A498, AsPC-1, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -8.3 | 9e-15 | 33/47 (C-33 A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.691×** | -6.5 | 9e-09 | 27/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -6.1 | 1e-07 | 27/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -5.8 | 6e-07 | 26/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.735×** | -5.2 | 1e-05 | 23/48 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.763×** | -4.7 | 1e-04 | 23/48 (SW480, KATO III, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -4.5 | 4e-04 | 22/48 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.794×** | -4.0 | 0.002 | 16/48 (KATO III, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.799×** | -3.8 | 0.007 | 19/37 (MIA PaCa-2, SW48, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.817×** | -3.5 | 0.017 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.702×** | -3.2 | 0.046 | 14/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.833×** | -3.2 | 0.051 | 8/48 (NCI-H2030, SW48, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.880× | -3.2 | 0.053 | 10/48 (LS 180, HT-29, …) | top dose only | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.085 | 12/48 (HT-29, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.091 | 9/48 (SW 1088, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -14.2) |
| [[KATO III (line)]] | alt | 62.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -12.6) |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -8.6) |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -12.9) |
| [[A498 (line)]] | wt | 38.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.186× (z -9.1) |
| [[HOP62 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.5) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.2) |
| [[A-427 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -11.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A549 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -8.8) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -16.3) ⚠ toxic |
| [[C32 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -9.8) |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -10.5) |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARL]] | +0.75 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[DERL2]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 402 |
| [[RUSF1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[CWF19L1]] | +0.68 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.67 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[TGDS]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | STRING 487 |
| [[CRLS1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TMEM216]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SRPRB]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 | STRING 414 |
| [[UBA5]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NADK2]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZW10]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUN]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.51 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TLE4]] | -0.51 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[KLF12]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[MIR23AHG]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABBR1]] | B | GABBR1 activity lowers ALG5's level | lines that do not express GABBR1 (7) vs lines expressing it (43) | 1.87× higher at baseline in the lines without GABBR1 | 0.045 | ⚠ within organs, on part of the lines; also absent: BLVRA, TUBA1A, CABYR |
| [[ZNF419]] | C | ZNF419 activity raises ALG5's level | lines that do not express ZNF419 (4) vs lines expressing it (46) | 1.26× lower at baseline in the lines without ZNF419 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: UBA6-DT, ENSG00000251379, ZNF264 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.2, -6.8); signed map (-13.8, -13.7). **Vector** length 90.9, 19.5% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +2.9 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -12.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -10.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | ALG5 dolichyl-phosphate beta-glucosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,949,738-37,000,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA421P11.2 |
| Gene groups (HGNC) | Glycosyltransferase family 2 |
| Reactome | 3 pathways, smallest: Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y673](https://www.uniprot.org/uniprotkb/Q9Y673) (Dolichyl-phosphate beta-glucosyltransferase):

> Dolichyl-phosphate beta-glucosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including two GlcNAcs, nine …

**Summary**, from NCBI Gene [29880](https://www.ncbi.nlm.nih.gov/gene/29880):

> This gene encodes a member of the glycosyltransferase 2 family. The encoded protein participates in glucosylation of the oligomannose core in N-linked glycosylation of proteins. The addition of glucose residues to the oligomannose core is necessary to ensure substrate recognition, and therefore, effectual transfer of the oligomannose core to the nascent glycoproteins. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:20266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20266) · Entrez [29880](https://www.ncbi.nlm.nih.gov/gene/29880) · UniProt [Q9Y673](https://www.uniprot.org/uniprotkb/Q9Y673) · Ensembl [ENSG00000120697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120697)

## Data

Gene col 4209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4209); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4209]; `tensor/DDL_lfc|DDL_z.npy` [4209]; `embed/gene_vectors.npy` [4209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4209 or target_col == 4209). Every well: [[ALG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
