---
symbol: "PARL"
type: "gene"
col: 10577
ensembl_id: "ENSG00000175193"
name: "presenilin associated rhomboid like"
location: "3q27.1"
module: 49
arm: "+"
pooled_cpm: 57.69
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PARL

*presenilin associated rhomboid like* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.97× (z +7.6, q 2e-11, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (SW480 1.47×; ⚠ cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.619× (z -10.2, q 8e-22, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.663× (z -8.8, q 2e-16, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRG1]] (+0.78, fdr 7e-06), [[ALG5]] (+0.75, fdr 7e-06), [[CWF19L1]] (+0.72, fdr 7e-06); moves opposite to [[WWC2]] (-0.57, fdr 1e-05), [[PKNOX1]] (-0.53, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (SW480 1.47×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +7.6 | 2e-11 | 32/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +7.4 | 5e-11 | 32/48 (SW480, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +5.5 | 7e-06 | 27/48 (Hs 766T, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.3 | 2e-05 | 28/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.13 | 9/48 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Salicylic acid (drug)]] 5 µM |  | 1.11× | +3.1 | 0.19 | 2/49 (SW 900, HCT15) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.0 | 0.19 | 19/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.619×** | -10.2 | 8e-22 | 37/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -9.5 | 5e-19 | 38/47 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -8.9 | 2e-16 | 33/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.663×** | -8.8 | 2e-16 | 33/48 (HS-578T, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -8.8 | 2e-16 | 30/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.670×** | -8.6 | 1e-15 | 36/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.693×** | -7.8 | 4e-13 | 34/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -7.0 | 2e-10 | 31/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.746×** | -6.0 | 1e-07 | 25/48 (HS-578T, A498, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -5.7 | 5e-07 | 21/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.780×** | -5.3 | 6e-06 | 26/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.804×** | -4.7 | 2e-04 | 23/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.824×** | -4.1 | 0.002 | 23/48 (NCI-H460, H4, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.878× | -3.9 | 0.004 | 20/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.885× | -3.7 | 0.009 | 20/48 (SNU-423, MIA PaCa-2, …) | top dose only | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.058 | 9/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.902× | -3.1 | 0.061 | 5/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.905× | -3.0 | 0.080 | 5/48 (SNU-423, H4, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.080 | 10/48 (CFPAC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 66.2 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -10.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 74.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 93.6 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 35.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -15.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.355× (z -11.8) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 41.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.415× (z -9.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 79.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib (drug)]] 5 µM 0.112× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.223× (z -10.3) ⚠ toxic · without an alert: [[Pimozide (drug)]] 0.05 µM 0.242× (z -10.1) |
| [[LS 180 (line)]] | wt | 51.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 75.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.544× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.424× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 84.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 64.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -11.7) |
| [[CHP-212 (line)]] | wt | 59.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 88.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.257× (z -10.3) |
| [[KATO III (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -12.4) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 75.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRG1]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[ALG5]] | +0.75 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CWF19L1]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[AARSD1]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MIGA1]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[RINT1]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PYROXD1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[DERL2]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF708]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[C18orf25]] | +0.64 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[KLHL12]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WWC2]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises PARL's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without ZNF675 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.5, -6.7); signed map (-13.8, -13.6). **Vector** length 119, 32.4% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.3 | +7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.5 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +1.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -8.2 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.8 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.5 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.1 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.8 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | presenilin associated rhomboid like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,829,271-183,884,933 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2207, PSARL1, RHBDS1; previously PSARL |
| Gene groups (HGNC) | Rhomboid family |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H300](https://www.uniprot.org/uniprotkb/Q9H300) (Presenilin-associated rhomboid-like protein, mitochondrial):

> Required for the control of apoptosis during postnatal growth. Essential for proteolytic processing of an antiapoptotic form of OPA1 which prevents the release of mitochondrial cytochrome c in response to intrinsic apoptotic signals (By similarity). Required for the maturation of PINK1 into its 52kDa mature form after its cleavage by mitochondrial-processing peptidase (MPP). Promotes cleavage of serine/threonine-protein phosphatase PGAM5 in damaged mitochondria in response to loss of …

**Summary**, from NCBI Gene [55486](https://www.ncbi.nlm.nih.gov/gene/55486):

> This gene encodes a member of the rhomboid family of intramembrane serine proteases that is localized to the inner mitochondrial membrane. The encoded protein regulates mitochondrial remodeling and apoptosis through regulated substrate proteolysis. Proteolytic processing of the encoded protein results in the release of a small peptide, P-beta, which may transit to the nucleus. Mutations in this gene may be associated with Parkinson's disease. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:18253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18253) · Entrez [55486](https://www.ncbi.nlm.nih.gov/gene/55486) · UniProt [Q9H300](https://www.uniprot.org/uniprotkb/Q9H300) · Ensembl [ENSG00000175193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175193)

## Data

Gene col 10577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10577); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10577]; `tensor/DDL_lfc|DDL_z.npy` [10577]; `embed/gene_vectors.npy` [10577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10577 or target_col == 10577). Every well: [[PARL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
