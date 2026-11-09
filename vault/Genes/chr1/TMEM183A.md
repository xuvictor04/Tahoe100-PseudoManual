---
symbol: "TMEM183A"
type: "gene"
col: 8691
ensembl_id: "ENSG00000163444"
name: "transmembrane protein 183A"
location: "1q32.1"
module: 171
arm: "+"
pooled_cpm: 24.11
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# TMEM183A

*transmembrane protein 183A* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.22× (z +10.6, q 2e-23, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0923×); [[Alpelisib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0618×); [[AZD2858 (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0955×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.0861×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRS2]] (+0.71, fdr 7e-06), [[VPS26B]] (+0.69, fdr 7e-06), [[UBAC1]] (+0.68, fdr 7e-06); moves opposite to [[TUBB4B]] (-0.65, fdr 7e-06), [[ERCC6L2]] (-0.58, fdr 4e-05), [[PPP1R1C]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PPP1R1C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.22×** | +10.6 | 2e-23 | 44/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.02×** | +9.3 | 3e-18 | 33/42 (NCI-H1573, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.95×** | +8.8 | 2e-16 | 43/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.94×** | +8.8 | 2e-16 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.81×** | +7.3 | 4e-11 | 29/38 (SW480, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.6 | 3e-09 | 33/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.65×** | +6.4 | 2e-08 | 32/45 (LoVo, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +6.3 | 2e-08 | 32/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.1 | 6e-08 | 33/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.61×** | +6.1 | 7e-08 | 23/33 (PANC-1, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +5.9 | 2e-07 | 28/46 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +5.8 | 2e-07 | 30/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.48×** | +5.2 | 9e-06 | 26/45 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 3e-05 | 26/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.8 | 6e-05 | 23/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 5e-04 | 21/47 (PANC-1, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.007 | 16/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Aliskiren (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.008 | 15/48 (J82, A498, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.026 | 11/47 (AsPC-1, A549, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.026 | 12/47 (PANC-1, HT-29, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.030 | 14/47 (AsPC-1, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8691.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0923×); [[Alpelisib (drug)]] 0.05 µM in 1 line (NCI-H661 0.0618×); [[AZD2858 (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0955×; ⚠ toxic); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (AN3 CA 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.785× | -3.2 | 0.39 | 11/47 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.792× | -3.1 | 0.39 | 10/47 (AsPC-1, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | 0.793× | -3.1 | 0.39 | 15/46 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 16.1 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0923× (z -10.1) |
| [[A-427 (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +8.9) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0861× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0955× (z -9.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0618× (z -9.7) |
| [[PANC-1 (line)]] | alt | 19.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.163× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.81× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRS2]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[VPS26B]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[COPS4]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[BAG4]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[GPD1L]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FBXO7]] | +0.64 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[BLTP1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SNX4]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | -0.65 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.58 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PPP1R1C]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TUT7]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[IER5]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TUBA1C]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[PFN1]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GOLT1A]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity lowers TMEM183A's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.26× higher at baseline in the lines without PPP1R1C | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-9.1, -13.4); signed map (-36.5, -14.1). **Vector** length 70.7, 13.7% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.1 | +9.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +3.8 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +0.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.7 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 183A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,007,374-203,024,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf37 |
| Matched by | ensembl_id |

UniProt [Q8IXX5](https://www.uniprot.org/uniprotkb/Q8IXX5) carries no function annotation.

**Summary**, from NCBI Gene [92703](https://www.ncbi.nlm.nih.gov/gene/92703):

> Predicted to be located in membrane. Predicted to be part of SCF ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20173) · Entrez [92703](https://www.ncbi.nlm.nih.gov/gene/92703) · UniProt [Q8IXX5](https://www.uniprot.org/uniprotkb/Q8IXX5) · Ensembl [ENSG00000163444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163444)

## Data

Gene col 8691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8691); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8691]; `tensor/DDL_lfc|DDL_z.npy` [8691]; `embed/gene_vectors.npy` [8691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8691 or target_col == 8691). Every well: [[TMEM183A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM183A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
