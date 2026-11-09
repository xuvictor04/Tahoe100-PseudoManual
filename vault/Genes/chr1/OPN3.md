---
symbol: "OPN3"
type: "gene"
col: 606
ensembl_id: "ENSG00000054277"
name: "opsin 3"
location: "1q43"
module: 155
arm: "+"
pooled_cpm: 23.69
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# OPN3

*opsin 3* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 1.48× (z +6.1, q 5e-07, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.514× (z -10.1, q 2e-21, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGA]] (+0.58, fdr 2e-05), [[FGG]] (+0.55, fdr 2e-05), [[CHML]] (+0.53, fdr 2e-05, ⚠ same locus), [[CP]] (+0.52, fdr 4e-05); moves opposite to [[LTB]] (-0.50, fdr 2e-04), [[IL23A]] (-0.47, fdr 3e-05), [[PPP1R35]] (-0.44, fdr 4e-04, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[DAGLA]] (-0.44, fdr 5e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[NTN4]] → it (grade B ⚠); 4 go from it, the strongest it → [[NTN4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.48×** | +6.1 | 5e-07 | 19/44 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 2e-04 | 14/29 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 0.002 | 18/44 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.002 | 18/41 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.016 | 10/41 (SNU-423, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.028 | 10/40 (HT-29, C-33 A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.051 | 4/44 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.14 | 13/42 (NCI-H460, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.45× | +3.1 | 0.14 | 12/43 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.14 | 6/43 (CFPAC-1, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -10.1 | 2e-21 | 32/42 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -7.5 | 2e-11 | 22/39 (NCI-H1792, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -7.2 | 9e-11 | 23/43 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -6.4 | 3e-08 | 23/41 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.710×** | -5.1 | 3e-05 | 18/40 (SW48, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.733×** | -4.9 | 8e-05 | 20/44 (KATO III, NCI-H1792, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.002 | 15/43 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.830×** | -4.2 | 0.002 | 20/42 (PANC-1, AsPC-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.607×** | -4.1 | 0.002 | 15/43 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -3.7 | 0.014 | 12/41 (A549, A-172, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.731×** | -3.6 | 0.020 | 8/41 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.796×** | -3.5 | 0.023 | 13/41 (C32, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.023 | 13/42 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.2 | 0.051 | 11/38 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.069 | 11/44 (CFPAC-1, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.4) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -13.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.2) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -9.7) |
| [[A549 (line)]] | wt | 47.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.7) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.3) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.214× (z -10.2) |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0724× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 6.77 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0889× (z -9.9) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.247× (z -8.8) |
| [[BT-474 (line)]] | alt | 40.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.283× (z -9.1) |
| [[C32 (line)]] | wt | 10.7 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0503× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.4) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.5) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0628× (z -11.1) |
| [[KATO III (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.206× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 55.2 | 1 | 0 | [[Trametinib (drug)]] 0.5 µM 2.31× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -12.2) ⚠ cell-cycle shift, explains ~99% of this change |
| [[A-427 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGA]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FGG]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CHML]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 | STRING 974; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CP]] | +0.52 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[GALNT2]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FGB]] | +0.47 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[ATP2A2]] | +0.46 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[LINC02057]] | +0.45 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[ADAM15]] | +0.45 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[ITIH2]] | +0.45 | +0.39 / +0.20 | both halves | 7e-04 |  |
| [[OSMR]] | +0.44 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[NTN4]] | +0.44 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SLC16A7]] | +0.44 | +0.33 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTB]] | -0.50 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[IL23A]] | -0.47 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R35]] ⚠ | -0.44 | -0.24 / -0.43 | both halves | 4e-04 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[DAGLA]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SMG9]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[AMZ2P1-1]] | -0.42 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ARHGEF40]] | -0.42 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[LINC02566]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CD40]] | -0.41 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NEPRO]] | -0.41 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PLAU]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[KIF3B]] | -0.41 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CX3CL1]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 | pathway: Class A/1 (Rhodopsin-like receptors) |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NTN4 activity raises OPN3's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without NTN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LINC02057]] | B | LINC02057 activity raises OPN3's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.11× lower at baseline in the lines without LINC02057 | 0.022 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[FGB]] | B | FGB activity raises OPN3's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.45× lower at baseline in the lines without FGB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[NEURL3]] | B | NEURL3 activity raises OPN3's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without NEURL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[RHCG]] | B | RHCG activity raises OPN3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without RHCG | 0.069 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[CP]] | B | CP activity raises OPN3's level | lines that do not express CP (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without CP | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[FGA]] | B | FGA activity raises OPN3's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.35× lower at baseline in the lines without FGA | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG |
| [[FGG]] | B | FGG activity raises OPN3's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.52× lower at baseline in the lines without FGG | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | C | OPN3 activity raises NTN4's level | lines that do not express OPN3 (4) vs lines expressing it (46) | 5.25× lower at baseline in the lines without OPN3 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIAA2012, LAMB1, HIPK2; maybe low, not absent |
| [[B4GALT1]] | C | OPN3 activity raises B4GALT1's level | lines that do not express OPN3 (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without OPN3 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIAA2012, LAMB1, HIPK2; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | OPN3 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express OPN3 (4) vs lines expressing it (44) | the lines without OPN3: 0.26× the cells of the other lines | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIAA2012, LAMB1, HIPK2; maybe low, not absent |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM | C | OPN3 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express OPN3 (4) vs lines expressing it (44) | the lines without OPN3: 0.59× the cells of the other lines | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIAA2012, LAMB1, HIPK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.298). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.0, 47.3); signed map (53.8, 25.5). **Vector** length 89.5, 18.4% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -10.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -7.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | opsin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:241,590,102-241,677,376 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERO, NMO-1, encephalopsin, PPP1R116; previously ECPN |
| Gene groups (HGNC) | Opsin receptors; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1Y3](https://www.uniprot.org/uniprotkb/Q9H1Y3) (Opsin-3):

> G protein-coupled photoreceptor that selectively activates G(i/o) proteins in response to light, thereby decreasing intracellular cAMP levels. Activation occurs when the opsin-bound cis-retinal chromophore absorbs a photon and isomerizes to all-trans-retinal, inducing a conformational change in the opsin that triggers a G protein-mediated phototransduction cascade. Mediates blue light-induced pigmentation in melanocytes by activating calcium/CAMK2 signaling, followed by phosphorylation of CREB, …

**Summary**, from NCBI Gene [23596](https://www.ncbi.nlm.nih.gov/gene/23596):

> Opsins are members of the guanine nucleotide-binding protein (G protein)-coupled receptor superfamily. In addition to the visual opsins, mammals possess several photoreceptive non-visual opsins that are expressed in extraocular tissues. This gene, opsin 3, is strongly expressed in brain and testis and weakly expressed in liver, placenta, heart, lung, skeletal muscle, kidney, and pancreas. The gene may also be expressed in the retina. The protein has the canonical features of a photoreceptive …

**Accessions** — [HGNC:14007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14007) · Entrez [23596](https://www.ncbi.nlm.nih.gov/gene/23596) · UniProt [Q9H1Y3](https://www.uniprot.org/uniprotkb/Q9H1Y3) · Ensembl [ENSG00000054277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054277)

## Data

Gene col 606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 606); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 606]; `tensor/DDL_lfc|DDL_z.npy` [606]; `embed/gene_vectors.npy` [606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 606 or target_col == 606). Every well: [[OPN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
