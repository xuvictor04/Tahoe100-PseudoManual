---
symbol: "LIG3"
type: "gene"
col: 69
ensembl_id: "ENSG00000005156"
name: "DNA ligase 3"
location: "17q12"
module: 20
arm: "+"
pooled_cpm: 24.43
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# LIG3

*DNA ligase 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +7.3, q 2e-10, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 3.70×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -16.4, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPAGT1]] (+0.72, fdr 7e-06), [[HCFC1]] (+0.66, fdr 1e-05), [[ZNF587B]] (+0.66, fdr 7e-06); moves opposite to [[CTR9]] (-0.62, fdr 9e-06), [[SUMO4]] (-0.61, fdr 8e-05), [[FRG1]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 69.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 3.70×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.3 | 2e-10 | 28/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.2 | 1e-07 | 20/44 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.8 | 2e-04 | 19/45 (LS 180, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.8 | 3e-04 | 16/35 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 5e-04 | 14/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 69.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -16.4 | 0e+00 | 41/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.563×** | -11.2 | 2e-26 | 42/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -9.7 | 9e-20 | 37/47 (NCI-H661, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -9.5 | 2e-19 | 35/48 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -9.5 | 2e-19 | 34/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.0 | 2e-17 | 35/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -8.3 | 1e-14 | 32/47 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.724×** | -6.3 | 2e-08 | 26/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.728×** | -6.2 | 4e-08 | 23/46 (NCI-H460, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -5.0 | 4e-05 | 17/48 (SW480, HT-29, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.786×** | -4.7 | 1e-04 | 23/47 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -4.3 | 9e-04 | 19/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.818×** | -3.9 | 0.004 | 16/47 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.9 | 0.004 | 16/48 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.821×** | -3.8 | 0.005 | 12/48 (NCI-H661, BT-474, …) | two highest doses |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.837× | -3.3 | 0.028 | 7/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 69. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.6) |
| [[SHP-77 (line)]] | alt | 30.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.5) ⚠ toxic; transcription drop | [[Saquinavir (drug)]] 0.5 µM 0.277× (z -9.8) |
| [[A498 (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.4) |
| [[A549 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.1) |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.205× (z -10.0) |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.6) |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -8.5) |
| [[HT-29 (line)]] | alt | 37.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.4) |
| [[LoVo (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.0) |
| [[PANC-1 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -8.7) |
| [[RKO (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.195× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.4) |
| [[SW48 (line)]] | wt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0416× (z -17.8) |
| [[SW480 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.3) |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 69), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPAGT1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.66 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ZNF587B]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MAN2C1]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.66 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[POLR3E]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RPUSD4]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MFN2]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.61 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[LY6G5B]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTR9]] | -0.62 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[SUMO4]] | -0.61 | -0.37 / -0.69 | both halves | 8e-05 |  |
| [[FRG1]] | -0.59 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[ANKRD12]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[PITPNA-AS1]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PIM3]] | -0.58 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[JUND]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[BTG1]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[UGCG]] | -0.55 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[SSH2]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TRAPPC5]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises LIG3's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.16× lower at baseline in the lines without ADCY3 | 0.053 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[SRRM3]] | B | SRRM3 activity raises LIG3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without SRRM3 | 0.054 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.5, -27.3); signed map (-24.1, -43.5). **Vector** length 83.5, 15.8% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -16.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -9.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | DNA ligase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:34,980,512-35,009,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIG3alpha; previously LIG2 |
| Gene groups (HGNC) | Zinc fingers PARP-type; DNA ligases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 15 pathways, smallest: Resolution of AP sites via the single-nucleotide replacement pathway; APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; Strand-asynchronous mitochondrial DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [P49916](https://www.uniprot.org/uniprotkb/P49916) (DNA ligase 3):

> Isoform 3 functions as a heterodimer with DNA-repair protein XRCC1 in the nucleus and can correct defective DNA strand-break repair and sister chromatid exchange following treatment with ionizing radiation and alkylating agents. Isoform 1 is targeted to mitochondria, where it functions as a DNA ligase in mitochondrial base-excision DNA repair.

**Summary**, from NCBI Gene [3980](https://www.ncbi.nlm.nih.gov/gene/3980):

> This gene is a member of the DNA ligase family. Each member of this family encodes a protein that catalyzes the joining of DNA ends but they each have a distinct role in DNA metabolism. The protein encoded by this gene is involved in excision repair and is located in both the mitochondria and nucleus, with translation initiation from the upstream start codon allowing for transport to the mitochondria and translation initiation from a downstream start codon allowing for transport to the nucleus. …

**Accessions** — [HGNC:6600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6600) · Entrez [3980](https://www.ncbi.nlm.nih.gov/gene/3980) · UniProt [P49916](https://www.uniprot.org/uniprotkb/P49916) · Ensembl [ENSG00000005156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005156)

## Data

Gene col 69: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 69); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 69, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 69]; `tensor/DDL_lfc|DDL_z.npy` [69]; `embed/gene_vectors.npy` [69]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 69 or target_col == 69). Every well: [[LIG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
