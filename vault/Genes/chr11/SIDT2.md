---
symbol: "SIDT2"
type: "gene"
col: 7392
ensembl_id: "ENSG00000149577"
name: "SID1 transmembrane family member 2"
location: "11q23.3"
module: 38
arm: "+"
pooled_cpm: 19.55
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SIDT2

*SID1 transmembrane family member 2* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +6.7, q 1e-08, up in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 2.17×, SW1417 2.86×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.499× (z -11.3, q 8e-27, down in 36 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.617× (z -7.8, q 7e-13, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TINCR]] (+0.65, fdr 1e-05), [[LAG3]] (+0.62, fdr 1e-05), [[LRRC23]] (+0.62, fdr 1e-05); moves opposite to [[DTD2]] (-0.52, fdr 4e-05), [[EEF1E1]] (-0.50, fdr 2e-05), [[CHCHD3]] (-0.50, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NPAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7392.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 2.17×, SW1417 2.86×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.7 | 1e-08 | 27/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | 1.49× | +3.4 | 0.22 | 11/46 (NCI-H1573, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -11.3 | 8e-27 | 36/46 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -10.4 | 7e-23 | 32/46 (NCI-H1792, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.588×** | -8.6 | 1e-15 | 26/41 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -7.8 | 7e-13 | 31/47 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -7.6 | 3e-12 | 25/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.607×** | -7.5 | 7e-12 | 22/37 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.682×** | -6.2 | 4e-08 | 26/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -6.0 | 1e-07 | 20/31 (Hs 766T, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -6.0 | 1e-07 | 25/48 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.684×** | -5.9 | 2e-07 | 28/47 (LoVo, NCI-H1792, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -5.8 | 4e-07 | 23/47 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.5 | 2e-06 | 25/48 (KATO III, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -5.0 | 2e-05 | 21/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.741×** | -4.9 | 4e-05 | 22/47 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.604×** | -4.3 | 7e-04 | 16/45 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.9 | 0.003 | 18/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.019 | 14/47 (Panc 03.27, A-172, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.070 | 18/45 (CHP-212, A498, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.880× | -2.9 | 0.083 | 12/48 (LS 180, CHP-212, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 0.838× | -2.9 | 0.098 | 10/47 (NCI-H2030, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 27.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0371× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0904× (z -16.9) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.255× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -9.5) |
| [[A-427 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 1 | — | [[Ranolazine (drug)]] 0.5 µM 0.0854× (z -9.3) |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -11.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.274× (z -9.5) |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -9.0) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0615× (z -15.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -13.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -8.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0746× (z -9.2) |
| [[SW1417 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[SW480 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TINCR]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[LAG3]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LRRC23]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PYGM]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[EFEMP2]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[AVIL]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[RFPL3S]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ARF4]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[VWCE]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TRIM3]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTD2]] | -0.52 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[EEF1E1]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[CHCHD3]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RPE]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[OTUD6B]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RPP30]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS1]] | B | NPAS1 activity raises SIDT2's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without NPAS1 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.5, -18.3); signed map (15.1, 12.9). **Vector** length 83.4, 16.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.3 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.5 | -3.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | SID1 transmembrane family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,178,736-117,197,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-40 |
| Gene groups (HGNC) | SID1 transmembrane family |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBJ9](https://www.uniprot.org/uniprotkb/Q8NBJ9) (SID1 transmembrane family member 2):

> Mediates the translocation of RNA and DNA across the lysosomal membrane during RNA and DNA autophagy (RDA), a process in which RNA or DNA is directly imported into lysosomes in an ATP-dependent manner, and degraded. Involved in the uptake of single-stranded oligonucleotides by living cells, a process called gymnosis. In vitro, mediates the uptake of linear DNA more efficiently than that of circular DNA, but exhibits similar uptake efficacy toward RNA and DNA. Binds long double-stranded RNA …

**Summary**, from NCBI Gene [51092](https://www.ncbi.nlm.nih.gov/gene/51092):

> Predicted to enable several functions, including AP-1 adaptor complex binding activity; AP-2 adaptor complex binding activity; and RNA transmembrane transporter activity. Involved in RNA transport. Located in lysosomal membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24272) · Entrez [51092](https://www.ncbi.nlm.nih.gov/gene/51092) · UniProt [Q8NBJ9](https://www.uniprot.org/uniprotkb/Q8NBJ9) · Ensembl [ENSG00000149577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149577)

## Data

Gene col 7392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7392); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7392]; `tensor/DDL_lfc|DDL_z.npy` [7392]; `embed/gene_vectors.npy` [7392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7392 or target_col == 7392). Every well: [[SIDT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIDT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
