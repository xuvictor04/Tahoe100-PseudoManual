---
symbol: "PSMB3"
type: "gene"
col: 15900
ensembl_id: "ENSG00000277791"
name: "proteasome 20S subunit beta 3"
location: "17q12"
module: 72
arm: "+"
pooled_cpm: 37.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMB3

*proteasome 20S subunit beta 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.81× (z +13.3, q 9e-38, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -6.9, q 3e-09, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.189×, BT-474 0.400×, NCI-H23 0.341×, C-33 A 0.240×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.223×); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.297×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BABAM1]] (+0.74, fdr 7e-06), [[PSMA2]] (+0.74, fdr 7e-06), [[PSMB2]] (+0.73, fdr 7e-06); moves opposite to [[APLF]] (-0.53, fdr 5e-05), [[NR1D1]] (-0.52, fdr 4e-05), [[BMI1]] (-0.52, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.81×** | +13.3 | 9e-38 | 47/47 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.46×** | +12.4 | 1e-32 | 48/48 (HOP62, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.04×** | +11.1 | 3e-26 | 40/44 (NCI-H460, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.90×** | +10.0 | 2e-21 | 48/48 (NCI-H2030, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **2.14×** | +7.3 | 4e-11 | 30/38 (NCI-H460, A-172, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.98×** | +6.3 | 3e-08 | 31/43 (A549, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.87×** | +6.2 | 4e-08 | 39/47 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.4 | 8e-04 | 33/47 (C32, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.48×** | +3.9 | 0.007 | 31/46 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.014 | 29/48 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.44×** | +3.6 | 0.015 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.2 | 0.072 | 21/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.075 | 26/45 (J82, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.35× | +3.0 | 0.11 | 25/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15900.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.189×, BT-474 0.400×, NCI-H23 0.341×, C-33 A 0.240×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.223×); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.297×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -6.9 | 3e-09 | 38/47 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.786× | -3.4 | 0.19 | 26/48 (CHP-212, SW1417, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.535× | -3.1 | 0.32 | 21/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 63.2 | 2 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.8) |
| [[SW480 (line)]] | alt | 30.0 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +10.6) | — |
| [[A549 (line)]] | wt | 27.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.06× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 296 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.56× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) |
| [[KATO III (line)]] | alt | 46.9 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.85× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.47× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.297× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 19.3 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.11× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 80.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.42× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 46.0 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.84× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 26.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.62× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 26.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.28× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 29.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.05× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.23× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 25.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.56× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 48.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.60× (z +11.4) | — |
| [[LoVo (line)]] | wt | 21.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.64× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.60× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 32.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.63× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 19.0 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.26× (z +9.9) | — |
| [[SW48 (line)]] | wt | 32.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.78× (z +8.9) | — |
| [[A-172 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.3) |
| [[C32 (line)]] | wt | 23.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.80× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.47× (z +8.5) | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.01× (z +8.8) | — |
| [[J82 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[Panc 03.27 (line)]] | alt | 43.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 24.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +8.6) | — |
| [[A498 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM1]] | +0.74 | +0.80 / +0.64 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMA2]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMB2]] | +0.73 | +0.80 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TALDO1]] | +0.72 | +0.78 / +0.64 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[PSMD13]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[RAB5IF]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[NPLOC4]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 543 |
| [[UFD1]] | +0.68 | +0.79 / +0.56 | both halves | 1e-05 | pathway: Cellular response to chemical stress; STRING 664 |
| [[ANKRD39]] | +0.68 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[ABCB8]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[PSMB4]] | +0.67 | +0.73 / +0.52 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TMEM161A]] | +0.66 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLF]] | -0.53 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[NR1D1]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 | pathway: Circadian clock |
| [[BMI1]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[FAM200B]] | -0.52 | -0.61 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, -9.1); signed map (-27.1, -25.4). **Vector** length 90.3, 26.9% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.6 | +13.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.2 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.1 | +12.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,752,741-38,764,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HC10-II, MGC4147 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P49720](https://www.uniprot.org/uniprotkb/P49720) (Proteasome subunit beta type-3):

> Non-catalytic component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or …

**Summary**, from NCBI Gene [5691](https://www.ncbi.nlm.nih.gov/gene/5691):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9540) · Entrez [5691](https://www.ncbi.nlm.nih.gov/gene/5691) · UniProt [P49720](https://www.uniprot.org/uniprotkb/P49720) · Ensembl [ENSG00000277791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277791)

## Data

Gene col 15900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15900); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15900]; `tensor/DDL_lfc|DDL_z.npy` [15900]; `embed/gene_vectors.npy` [15900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15900 or target_col == 15900). Every well: [[PSMB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
