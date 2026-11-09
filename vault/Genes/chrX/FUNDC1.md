---
symbol: "FUNDC1"
type: "gene"
col: 921
ensembl_id: "ENSG00000069509"
name: "FUN14 domain containing 1"
location: "Xp11.3"
module: 28
arm: "+"
pooled_cpm: 10.17
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# FUNDC1

*FUN14 domain containing 1* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.18× (z +9.0, q 1e-16, up in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.48× (z +6.6, q 4e-09, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.539× (z -7.4, q 7e-11, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.78, fdr 7e-06), [[ERAL1]] (+0.77, fdr 7e-06), [[TACO1]] (+0.77, fdr 7e-06); moves opposite to [[CORO7]] (-0.75, fdr 7e-06), [[GRK6]] (-0.64, fdr 1e-05), [[NME2]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.0 | 1e-16 | 15/18 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +8.6 | 3e-15 | 25/33 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +7.1 | 3e-10 | 20/28 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.6 | 4e-09 | 27/47 (KATO III, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.36×** | +5.2 | 2e-05 | 22/45 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +5.2 | 2e-05 | 23/45 (HEC-1-A, NCI-H1573, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 6e-04 | 17/42 (C32, A-427, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.45×** | +4.4 | 7e-04 | 19/39 (PANC-1, A549, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.002 | 19/45 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +3.7 | 0.011 | 18/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.015 | 16/47 (HEC-1-A, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.016 | 9/46 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.032 | 11/45 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.041 | 10/45 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -7.4 | 7e-11 | 32/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -6.4 | 4e-08 | 23/46 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -6.3 | 7e-08 | 31/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -6.2 | 7e-08 | 24/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -5.0 | 8e-05 | 19/43 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -4.8 | 1e-04 | 14/47 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.674×** | -4.7 | 2e-04 | 19/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -4.6 | 4e-04 | 17/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -4.3 | 0.001 | 20/44 (HepG2/C3A, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.775× | -3.1 | 0.12 | 15/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.2 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.6) |
| [[BT-474 (line)]] | alt | 7.68 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 4.87 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0633× (z -11.2) |
| [[A-172 (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.98× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.252× (z -8.7) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.78 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[ERAL1]] | +0.77 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[TACO1]] | +0.77 | +0.85 / +0.61 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.72 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.72 | +0.85 / +0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.72 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[PEX12]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.71 | +0.79 / +0.58 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[SDSL]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.70 | +0.77 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO7]] | -0.75 | -0.74 / -0.60 | both halves | 7e-06 |  |
| [[GRK6]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[NME2]] | -0.63 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[FOXK2]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises FUNDC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLP2]] | C | PLP2's natural level strengthens FUNDC1's drug response | PLP2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.44; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.7, 8.6); signed map (5.3, -26.3). **Vector** length 66.1, 11.7% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +6.2 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.4 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.2 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FUN14 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:44,523,639-44,542,859 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC51029 |
| Reactome | 5 pathways, smallest: Receptor Mediated Mitophagy; Mitophagy; Selective autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVP5](https://www.uniprot.org/uniprotkb/Q8IVP5) (FUN14 domain-containing protein 1):

> Integral mitochondrial outer-membrane protein that mediates the formation of mitochondria-associated endoplasmic reticulum membranes (MAMs). In turn, mediates angiogenesis and neoangiogenesis through interference with intracellular Ca(2+) communication and regulation of the vascular endothelial growth factor receptor KDR/VEGFR2 expression at both mRNA and protein levels. Also acts as an activator of hypoxia-induced mitophagy, an important mechanism for mitochondrial quality and homeostasis, by …

**Summary**, from NCBI Gene [139341](https://www.ncbi.nlm.nih.gov/gene/139341):

> This gene encodes a protein with a FUN14 superfamily domain. The function of the encoded protein is not known. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:28746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28746) · Entrez [139341](https://www.ncbi.nlm.nih.gov/gene/139341) · UniProt [Q8IVP5](https://www.uniprot.org/uniprotkb/Q8IVP5) · Ensembl [ENSG00000069509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069509)

## Data

Gene col 921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 921); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 921]; `tensor/DDL_lfc|DDL_z.npy` [921]; `embed/gene_vectors.npy` [921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 921 or target_col == 921). Every well: [[FUNDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUNDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
