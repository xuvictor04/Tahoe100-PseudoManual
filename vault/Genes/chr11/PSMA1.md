---
symbol: "PSMA1"
type: "gene"
col: 4947
ensembl_id: "ENSG00000129084"
name: "proteasome 20S subunit alpha 1"
location: "11p15.2"
module: 72
arm: "+"
pooled_cpm: 104.95
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMA1

*proteasome 20S subunit alpha 1* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.58× (z +15.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.623× (z -7.5, q 5e-11, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB2]] (+0.80, fdr 7e-06), [[PSMA3]] (+0.76, fdr 7e-06), [[CASP6]] (+0.70, fdr 1e-05); moves opposite to [[SDC4]] (-0.59, fdr 1e-05), [[TNRC6C]] (-0.56, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.58×** | +15.0 | 0e+00 | 48/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.40×** | +13.8 | 4e-41 | 47/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +11.1 | 2e-26 | 46/48 (LOX-IMVI, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.82×** | +9.0 | 2e-17 | 37/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.60×** | +7.1 | 1e-10 | 33/44 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +6.2 | 4e-08 | 43/48 (C32, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.47×** | +5.4 | 6e-06 | 34/45 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.39×** | +5.0 | 4e-05 | 31/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.8 | 1e-04 | 37/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.30×** | +4.1 | 0.002 | 27/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +3.7 | 0.009 | 29/49 (Panc 03.27, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.018 | 31/49 (LOX-IMVI, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.23×** | +3.3 | 0.044 | 22/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.2 | 0.062 | 25/45 (LOX-IMVI, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.623×** | -7.5 | 5e-11 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -7.0 | 1e-09 | 39/48 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.754×** | -4.4 | 0.002 | 27/48 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.2 | 0.16 | 22/48 (AN3 CA, NCI-H460, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.823× | -3.1 | 0.26 | 22/48 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 138 | 3 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 109 | 2 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -8.6) |
| [[A498 (line)]] | wt | 136 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.50× (z +9.3) | — |
| [[A549 (line)]] | wt | 92.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 90.4 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +10.2) | — |
| [[SW480 (line)]] | alt | 126 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 57.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[C32 (line)]] | wt | 86.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.81× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 86.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.05× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 143 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 63.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.69× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 46.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.17× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 103 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 190 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.81× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 50.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.95× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 121 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.97× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 69.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.25× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 84.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.53× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 98.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.60× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 81.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.56× (z +9.6) | — |
| [[J82 (line)]] | alt | 127 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +9.3) | — |
| [[KATO III (line)]] | alt | 55.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[LoVo (line)]] | wt | 90.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.07× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 117 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 70.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.35× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 99.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +10.1) | — |
| [[A-427 (line)]] | wt | 128 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 82.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.29× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 102 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 189 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB2]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMA3]] | +0.76 | +0.80 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[CASP6]] | +0.70 | +0.77 / +0.53 | both halves | 1e-05 | pathway: Apoptosis |
| [[EPDR1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.68 | +0.66 / +0.73 | both halves | 7e-06 | STRING 596 |
| [[HSPE1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 411 |
| [[PSMC1]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB4]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[SOD1]] | +0.67 | +0.72 / +0.58 | both halves | 8e-06 | pathway: Cellular response to chemical stress; STRING 754 |
| [[TMEM161A]] | +0.66 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[PIR]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TYW3]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDC4]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.56 | -0.61 / -0.52 | both halves | 1e-05 | pathway: Adherens junctions interactions |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PSMA1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.6, -8.8); signed map (-26.1, -23.6). **Vector** length 94.1, 29.0% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.6 | +13.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.2 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.1 | +15.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.4 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | -1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | -4.0 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -0.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,504,874-14,643,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HC2, NU, PROS30, MGC14542, MGC14575, MGC14751, MGC1667, MGC21459 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25786](https://www.uniprot.org/uniprotkb/P25786) (Proteasome subunit alpha type-1):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5682](https://www.ncbi.nlm.nih.gov/gene/5682):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9530) · Entrez [5682](https://www.ncbi.nlm.nih.gov/gene/5682) · UniProt [P25786](https://www.uniprot.org/uniprotkb/P25786) · Ensembl [ENSG00000129084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129084)

## Data

Gene col 4947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4947); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4947]; `tensor/DDL_lfc|DDL_z.npy` [4947]; `embed/gene_vectors.npy` [4947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4947 or target_col == 4947). Every well: [[PSMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
