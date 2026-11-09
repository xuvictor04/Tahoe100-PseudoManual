---
symbol: "GCSH"
type: "gene"
col: 6461
ensembl_id: "ENSG00000140905"
name: "glycine cleavage system protein H"
location: "16q23.2"
module: 188
arm: "+"
pooled_cpm: 5.55
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# GCSH

*glycine cleavage system protein H* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.79× (z +10.7, q 4e-24, up in 21 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.63× (z +10.1, q 2e-21, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.840× (z -6.3, q 1e-07, down in 26 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.745× (z -4.3, q 0.004, down in 20 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0880×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0896×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTUD6B]] (+0.72, fdr 7e-06), [[PMS2P3-1]] (+0.68, fdr 1e-05), [[BRAT1]] (+0.67, fdr 1e-05); moves opposite to [[SON]] (-0.70, fdr 7e-06), [[C6orf62]] (-0.68, fdr 1e-05), [[NLGN3]] (-0.68, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[C21orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.79×** | +10.7 | 4e-24 | 21/27 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +10.1 | 2e-21 | 41/46 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.55×** | +9.8 | 3e-20 | 38/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.54×** | +9.7 | 3e-20 | 41/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +8.6 | 1e-15 | 8/14 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.25×** | +8.2 | 3e-14 | 8/11 (A498, SNU-423, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +7.5 | 4e-12 | 21/30 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.75×** | +5.8 | 4e-07 | 15/39 (SW480, LoVo, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.42×** | +5.2 | 1e-05 | 15/45 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.1 | 2e-05 | 14/31 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +4.8 | 8e-05 | 15/46 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.57×** | +4.7 | 1e-04 | 12/46 (A-427, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.002 | 12/43 (RPMI-7951, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 16/45 (NCI-H2347, PANC-1, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.010 | 6/40 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.012 | 13/41 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.018 | 8/45 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.018 | 4/46 (SK-MEL-2, KATO III, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.039 | 4/42 (SHP-77, NCI-H23, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.0 | 0.065 | 5/38 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6461.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0880×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0896×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.840× | -6.3 | 1e-07 | 26/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -4.3 | 0.004 | 20/38 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.727× | -3.3 | 0.17 | 4/47 (A-172, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.744× | -3.1 | 0.25 | 3/47 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.745× | -3.1 | 0.25 | 12/37 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.41 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0896× (z -8.8) |
| [[KATO III (line)]] | alt | 4.14 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0880× (z -9.1) |
| [[A-172 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD6B]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.68 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.67 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[FAR1]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.66 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[GPD1L]] | +0.66 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[METAP1]] | +0.65 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[WDR5]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MMS19]] | +0.65 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SON]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[C6orf62]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.68 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.67 | -0.73 / -0.44 | both halves | 3e-05 |  |
| [[GARIN1A]] | -0.64 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[LINC01191]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[SLC22A1]] | -0.63 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[RBM23]] | -0.63 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[MEPCE]] | -0.63 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[MZF1-AS1]] | -0.63 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[LINC01934]] | -0.63 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.63 | -0.65 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91]] | B | C21orf91 activity lowers GCSH's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 1.70× higher at baseline in the lines without C21orf91 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[LRP3]] | B | LRP3 activity raises GCSH's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without LRP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.7, -5.8); signed map (-40.1, -13.9). **Vector** length 64.6, 10.8% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.5 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.2 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.1 | +9.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +9.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | glycine cleavage system protein H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:81,081,945-81,096,395 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Glycine degradation; Protein lipoylation; Glyoxylate metabolism and glycine degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23434](https://www.uniprot.org/uniprotkb/P23434) (Glycine cleavage system H protein, mitochondrial):

> The glycine cleavage system catalyzes the degradation of glycine. The H protein (GCSH) shuttles the methylamine group of glycine from the P protein (GLDC) to the T protein (GCST). Has a pivotal role in the lipoylation of enzymes involved in cellular energetics such as the mitochondrial dihydrolipoyllysine-residue acetyltransferase component of pyruvate dehydrogenase complex (DLAT), and the mitochondrial dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase …

**Summary**, from NCBI Gene [2653](https://www.ncbi.nlm.nih.gov/gene/2653):

> Degradation of glycine is brought about by the glycine cleavage system, which is composed of four mitochondrial protein components: P protein (a pyridoxal phosphate-dependent glycine decarboxylase), H protein (a lipoic acid-containing protein), T protein (a tetrahydrofolate-requiring enzyme), and L protein (a lipoamide dehydrogenase). The protein encoded by this gene is the H protein, which transfers the methylamine group of glycine from the P protein to the T protein. Defects in this gene are …

**Accessions** — [HGNC:4208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4208) · Entrez [2653](https://www.ncbi.nlm.nih.gov/gene/2653) · UniProt [P23434](https://www.uniprot.org/uniprotkb/P23434) · Ensembl [ENSG00000140905](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140905)

## Data

Gene col 6461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6461); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6461]; `tensor/DDL_lfc|DDL_z.npy` [6461]; `embed/gene_vectors.npy` [6461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6461 or target_col == 6461). Every well: [[GCSH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCSH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
