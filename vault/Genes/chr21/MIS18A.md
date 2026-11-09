---
symbol: "MIS18A"
type: "gene"
col: 8210
ensembl_id: "ENSG00000159055"
name: "MIS18 kinetochore protein A"
location: "21q22.11"
module: 22
arm: "+"
pooled_cpm: 20.54
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MIS18A

*MIS18 kinetochore protein A* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +8.3, q 4e-14, up in 35 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.42× (z +3.3, q 0.047, up in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 2.98×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.575× (z -5.4, q 5e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP192]] (+0.71, fdr 2e-05), [[CEP295]] (+0.63, fdr 1e-05), [[KIF20B]] (+0.62, fdr 1e-05); moves opposite to [[PSAP]] (-0.62, fdr 7e-06), [[RTCA-AS1]] (-0.54, fdr 2e-04), [[BCL2L2]] (-0.53, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AHSG]], [[ALB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8210.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 2.98×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.36×** | +8.3 | 4e-14 | 35/40 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.35×** | +8.0 | 5e-13 | 27/31 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.66×** | +4.9 | 2e-04 | 30/44 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.59×** | +4.3 | 0.002 | 27/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.66×** | +4.3 | 0.002 | 24/37 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.55×** | +4.2 | 0.002 | 27/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.51×** | +4.0 | 0.006 | 21/48 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.30×** | +3.6 | 0.023 | 20/48 (SW1417, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.023 | 18/43 (H4, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.41×** | +3.3 | 0.047 | 21/48 (HS-578T, C32, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.047 | 19/46 (NCI-H2347, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +3.3 | 0.047 | 18/48 (LoVo, NCI-H1573, …) | rises with dose | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.25×** | +3.1 | 0.090 | 14/48 (SHP-77, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -5.4 | 5e-05 | 29/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -3.9 | 0.028 | 22/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.064 | 23/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.786× | -3.3 | 0.14 | 21/48 (HT-29, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.542× | -3.1 | 0.22 | 19/46 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.384× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0645× (z -11.0) |
| [[J82 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP192]] | +0.71 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CEP295]] | +0.63 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[KIF20B]] | +0.62 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[THSD8]] ⚠ | +0.62 | +0.61 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CIP2A]] | +0.61 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PARP2]] | +0.60 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[AGGF1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FIGNL1]] | +0.59 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SGO1]] | +0.59 | +0.55 / +0.69 | both halves | 1e-05 | STRING 490 |
| [[HAUS7]] | +0.59 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[GPATCH11]] | +0.58 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[PRIM1]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 | pathway: Chromosome Maintenance |
| [[SUV39H1]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAP]] | -0.62 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[RTCA-AS1]] | -0.54 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[BCL2L2]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[GNAS]] | -0.53 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[CTSD]] | -0.53 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CTTN]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SWT1]] | -0.52 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[HLA-C]] | -0.51 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[ZBTB20-AS5]] | -0.51 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[PACRG]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[YPEL5]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A53]] | -0.50 | -0.45 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHSG]], [[ALB]] | B | AHSG, ALB activity lowers MIS18A's level | lines that do not express AHSG, ALB (45) vs lines expressing them (5) | 1.27× higher at baseline in the lines without AHSG, ALB | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.1, -56.3); signed map (-48.4, -46.6). **Vector** length 74.1, 17.7% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +2.5 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +2.2 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +2.0 | +4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.1 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | MIS18 kinetochore protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,268,228-32,279,049 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B28, FASP1, hMis18alpha; previously C21orf46, C21orf45 |
| Reactome | 4 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Chromosome Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYP9](https://www.uniprot.org/uniprotkb/Q9NYP9) (Protein Mis18-alpha):

> Required for recruitment of CENPA to centromeres and normal chromosome segregation during mitosis.

**Summary**, from NCBI Gene [54069](https://www.ncbi.nlm.nih.gov/gene/54069):

> Enables identical protein binding activity. Predicted to be involved in CENP-A containing chromatin assembly. Predicted to act upstream of or within chromosome segregation; obsolete pericentric heterochromatin organization; and protein localization to chromosome, centromeric region. Predicted to be located in nucleoplasm. Predicted to be part of CENP-A recruiting complex. Predicted to be active in chromatin; chromosome, centromeric region; and nucleus. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:1286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1286) · Entrez [54069](https://www.ncbi.nlm.nih.gov/gene/54069) · UniProt [Q9NYP9](https://www.uniprot.org/uniprotkb/Q9NYP9) · Ensembl [ENSG00000159055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159055)

## Data

Gene col 8210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8210); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8210]; `tensor/DDL_lfc|DDL_z.npy` [8210]; `embed/gene_vectors.npy` [8210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8210 or target_col == 8210). Every well: [[MIS18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIS18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
