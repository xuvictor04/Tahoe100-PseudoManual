---
symbol: "NUBP1"
type: "gene"
col: 2349
ensembl_id: "ENSG00000103274"
name: "NUBP iron-sulfur cluster assembly factor 1, cytosolic"
location: "16p13.13"
module: 51
arm: "+"
pooled_cpm: 15.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NUBP1

*NUBP iron-sulfur cluster assembly factor 1, cytosolic* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.51× (z +7.0, q 1e-09, up in 15 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.44× (z +6.5, q 3e-08, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.582× (z -9.6, q 3e-19, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMO]] (+0.70, fdr 7e-06), [[LANCL2]] (+0.69, fdr 9e-06), [[EPC2]] (+0.69, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.62, fdr 7e-06), [[GNRH1]] (-0.61, fdr 7e-06), [[STK32C]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.0 | 1e-09 | 15/29 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +6.5 | 3e-08 | 24/46 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.5 | 7e-06 | 22/39 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.1 | 5e-05 | 18/48 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +4.9 | 1e-04 | 20/47 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.9 | 1e-04 | 19/45 (A498, A549, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.8 | 2e-04 | 15/47 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 9e-04 | 13/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.001 | 9/44 (NCI-H1573, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.3 | 0.001 | 14/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 13/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.009 | 4/46 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.028 | 5/45 (NCI-H1792, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.030 | 7/44 (SW480, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -9.6 | 3e-19 | 31/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.631×** | -8.2 | 6e-14 | 30/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.673×** | -7.1 | 3e-10 | 25/48 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -7.0 | 3e-10 | 30/48 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -6.6 | 5e-09 | 24/46 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.702×** | -6.3 | 3e-08 | 25/48 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -5.2 | 2e-05 | 20/47 (SW 900, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.835× | -4.6 | 3e-04 | 19/46 (SW48, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.653×** | -4.0 | 0.005 | 12/48 (SNU-1, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sildenafil (drug)]] 0.05 µM |  | **0.816×** | -3.2 | 0.070 | 5/47 (BT-474, SW 1271, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.1 | 0.11 | 5/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.837× | -3.0 | 0.11 | 13/45 (Panc 03.27, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 16.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.8) |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0833× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 8.65 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0889× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.1) |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -10.3) |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -9.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SW480 (line)]] | alt | 18.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.412× (z -8.5) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMO]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.69 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[EPC2]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[LYRM2]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[COQ7]] | +0.67 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RABL3]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MRPS7]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[MIS12]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RBM23]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TOR1AIP1]] | +0.65 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.62 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[GNRH1]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[STK32C]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MAX]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.59 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RHEBL1]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MHENCR]] | -0.56 | -0.63 / -0.37 | both halves | 9e-05 |  |
| [[PTMA]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[PMS2P3-1]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NUBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.7, 11.2); signed map (12.1, -30.0). **Vector** length 68.5, 11.2% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.0 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | NUBP iron-sulfur cluster assembly factor 1, cytosolic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:10,743,786-10,769,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBP35, CIAO5; previously NBP1 |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P53384](https://www.uniprot.org/uniprotkb/P53384) (Cytosolic Fe-S cluster assembly factor NUBP1):

> Component of the cytosolic iron-sulfur (Fe/S) protein assembly (CIA) machinery. Required for maturation of extramitochondrial Fe-S proteins. The NUBP1-NUBP2 heterotetramer forms a Fe-S scaffold complex, mediating the de novo assembly of an Fe-S cluster and its transfer to target apoproteins. Implicated in the regulation of centrosome duplication (By similarity). Negatively regulates cilium formation and structure (By similarity).

**Summary**, from NCBI Gene [4682](https://www.ncbi.nlm.nih.gov/gene/4682):

> NUBP1 is a member of the NUBP/MRP subfamily of ATP-binding proteins (Nakashima et al., 1999 [PubMed 10486206]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:8041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8041) · Entrez [4682](https://www.ncbi.nlm.nih.gov/gene/4682) · UniProt [P53384](https://www.uniprot.org/uniprotkb/P53384) · Ensembl [ENSG00000103274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103274)

## Data

Gene col 2349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2349); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2349]; `tensor/DDL_lfc|DDL_z.npy` [2349]; `embed/gene_vectors.npy` [2349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2349 or target_col == 2349). Every well: [[NUBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
