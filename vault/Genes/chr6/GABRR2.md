---
symbol: "GABRR2"
type: "gene"
col: 3302
ensembl_id: "ENSG00000111886"
name: "gamma-aminobutyric acid type A receptor subunit rho2"
location: "6q15"
module: 39
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# GABRR2

*gamma-aminobutyric acid type A receptor subunit rho2* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.95× (z +6.1, q 8e-07, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.265× (z -12.1, q 9e-31, down in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.264× (z -6.3, q 2e-08, down in 24 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL9]] (+0.82, fdr 7e-06), [[LINC02936]] (+0.81, fdr 7e-06), [[HCLS1]] (+0.80, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.95×** | +6.1 | 8e-07 | 26/46 (SW480, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.008 | 17/45 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.011 | 15/42 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cinacalcet (drug)]] 5 µM |  | 1.42× | +3.2 | 0.18 | 4/46 (HOP62, NCI-H2030, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.44× | +3.2 | 0.18 | 7/46 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.27× | +3.1 | 0.18 | 7/45 (LoVo, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.0 | 0.20 | 7/46 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.265×** | -12.1 | 9e-31 | 38/46 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.330×** | -10.1 | 2e-21 | 36/46 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.331×** | -10.0 | 2e-21 | 30/42 (NCI-H1792, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.349×** | -9.6 | 2e-19 | 41/45 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.442×** | -7.4 | 1e-11 | 29/46 (KATO III, NCI-H1573, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.264×** | -6.3 | 2e-08 | 24/36 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.512×** | -6.1 | 1e-07 | 23/44 (J82, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.539×** | -5.6 | 1e-06 | 24/40 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.567×** | -5.1 | 2e-05 | 23/46 (SW 900, LoVo, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.677×** | -5.0 | 3e-05 | 20/46 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.376×** | -4.6 | 2e-04 | 22/43 (HT-29, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.600×** | -4.4 | 6e-04 | 17/42 (KATO III, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.633×** | -4.2 | 0.001 | 22/45 (H4, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.626×** | -4.1 | 0.002 | 19/45 (HS-578T, hTERT-HPNE, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.423×** | -4.1 | 0.002 | 15/38 (BT-474, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.027 | 11/46 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.703×** | -3.1 | 0.065 | 12/45 (HS-578T, AsPC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.714×** | -2.9 | 0.098 | 13/44 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Ligustrazine (drug)]] 0.5 µM |  | **0.725×** | -2.9 | 0.099 | 8/45 (C-33 A, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.6 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0556× (z -12.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0358× (z -14.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 6.01 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0618× (z -9.8) |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0495× (z -10.1) |
| [[KATO III (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0746× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 8.11 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0863× (z -8.6) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -9.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0682× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0652× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0996× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 5.00 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0341× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL9]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LINC02936]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.80 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.79 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[IMPA1P1]] | +0.79 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.78 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.78 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Neuronal System |
| [[MYOCOS]] | +0.77 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[LINC03016]] | +0.76 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MSH4]] | +0.76 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM3B]] | B | FAM3B activity raises GABRR2's level | lines that do not express FAM3B (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without FAM3B | 0.056 | ⚠ within organs, on part of the lines; also absent: TXNIP, CADPS2, PLAC4; maybe low, not absent |
| [[CADPS2]] | B | CADPS2 activity raises GABRR2's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without CADPS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.3, -16.5); signed map (14.5, 7.7). **Vector** length 97.5, 21.4% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.4 |
| fall | [[Radotinib (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.8 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -12.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.6 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit rho2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,254,464-89,315,299 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Reactome | 4 pathways, smallest: GABA receptor activation; Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P28476](https://www.uniprot.org/uniprotkb/P28476) (Gamma-aminobutyric acid receptor subunit rho-2):

> Rho subunit of the pentameric ligand-gated chloride channels responsible for mediating the effects of gamma-aminobutyric acid (GABA), the major inhibitory neurotransmitter in the brain (By similarity). Rho-containing GABA-gated chloride channels are a subclass of GABA(A) receptors (GABAARs) entirely composed of rho subunits, where GABA molecules bind at the rho intersubunit interfaces (By similarity). When activated by GABA, rho-GABAARs selectively allow the flow of chloride anions across the …

**Summary**, from NCBI Gene [2570](https://www.ncbi.nlm.nih.gov/gene/2570):

> Gamma-aminobutyric acid (GABA) is the major inhibitory neurotransmitter in the mammalian brain where it acts at GABA receptors, which are ligand-gated chloride channels. The protein encoded by this gene is a member of the rho subunit family and is a component of the GABA type A receptor complex. This gene exists on chromosome 6q next to the gene encoding the rho 1 subunit of the GABA type A receptor, in a region thought to be associated with susceptibility for psychiatric disorders and …

**Accessions** — [HGNC:4091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4091) · Entrez [2570](https://www.ncbi.nlm.nih.gov/gene/2570) · UniProt [P28476](https://www.uniprot.org/uniprotkb/P28476) · Ensembl [ENSG00000111886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111886)

## Data

Gene col 3302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3302); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3302]; `tensor/DDL_lfc|DDL_z.npy` [3302]; `embed/gene_vectors.npy` [3302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3302 or target_col == 3302). Every well: [[GABRR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
