---
symbol: "ZFYVE19"
type: "gene"
col: 9244
ensembl_id: "ENSG00000166140"
name: "zinc finger FYVE-type containing 19"
location: "15q15.1"
module: 30
arm: "+"
pooled_cpm: 13.5
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ZFYVE19

*zinc finger FYVE-type containing 19* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +6.4, q 1e-07, up in 17 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.93× (z +5.4, q 2e-05, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.411× (z -16.3, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBG2]] (+0.64, fdr 3e-05), [[TCIRG1]] (+0.64, fdr 1e-05), [[CCHCR1]] (+0.63, fdr 1e-05); moves opposite to [[SLC39A10]] (-0.62, fdr 1e-05), [[BCL2]] (-0.58, fdr 9e-05), [[PSMD6-AS1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PRSS8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.4 | 1e-07 | 17/35 (HEC-1-A, PANC-1, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +5.4 | 2e-05 | 28/42 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 1e-04 | 17/43 (LoVo, HCT15, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.6 | 5e-04 | 10/26 (NCI-H2030, SW1417, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +3.7 | 0.027 | 14/41 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.4 | 0.057 | 6/26 (HT-29, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.067 | 7/43 (SNU-423, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.075 | 9/45 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.16 | 8/43 (HS-578T, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.411×** | -16.3 | 0e+00 | 41/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.467×** | -9.9 | 2e-20 | 36/43 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -7.2 | 9e-11 | 28/46 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.286×** | -7.1 | 1e-10 | 30/46 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.304×** | -6.8 | 1e-09 | 34/42 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.580×** | -6.8 | 1e-09 | 25/46 (COLO 205, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.8 | 4e-07 | 23/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -4.9 | 6e-05 | 24/47 (SW1417, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.5 | 5e-04 | 22/44 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -4.2 | 0.001 | 18/46 (C-33 A, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -4.2 | 0.001 | 19/46 (NCI-H1792, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -3.9 | 0.005 | 17/46 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.742×** | -3.6 | 0.013 | 16/46 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.016 | 6/48 (SW1417, SK-MEL-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -3.4 | 0.023 | 14/47 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.774×** | -3.0 | 0.083 | 3/47 (SNU-423, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.1) |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.7) |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.9) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.5) |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0628× (z -11.1) |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.1) |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0752× (z -11.7) |
| [[HS-578T (line)]] | alt | 8.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.9) |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0889× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.6) |
| [[PANC-1 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 9.38 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -8.8) |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.7) |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -8.5) |
| [[SW48 (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -9.9) |
| [[A-172 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBG2]] | +0.64 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[TCIRG1]] | +0.64 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CCHCR1]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SEMA6C]] | +0.60 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[NFRKB]] | +0.59 | +0.52 / +0.49 | both halves | 2e-05 |  |
| [[XKR8]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[UNC45A]] | +0.57 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RANBP10]] | +0.55 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[MAST3]] | +0.55 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[FN3KRP]] | +0.54 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[KLHL26]] | +0.54 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[PLEKHH3]] | +0.54 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A10]] | -0.62 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[BCL2]] | -0.58 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[PSMD6-AS1]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[NPAS3]] | -0.53 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[EPM2A]] | -0.53 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[TENM3]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SEMA6A-AS1]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ITPR2-AS1]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[OTUD4]] | -0.52 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RGS5]] | -0.52 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[TENM3-AS1]] | -0.51 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[PARD3B]] | -0.51 | -0.42 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS8]] | B | PRSS8 activity raises ZFYVE19's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without PRSS8 | 0.038 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[TMEM92]] | B | TMEM92 activity raises ZFYVE19's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without TMEM92 | 0.050 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CCDC120]] | B | CCDC120 activity raises ZFYVE19's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without CCDC120 | 0.077 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[SERPINA5]] | B | SERPINA5 activity raises ZFYVE19's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.34× lower at baseline in the lines without SERPINA5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (4.2, -5.2); signed map (-31.4, 0.1). **Vector** length 63.9, 10.9% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,807,086-40,815,084 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14840, ANCHR, MPFYVE |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96K21](https://www.uniprot.org/uniprotkb/Q96K21) (Abscission/NoCut checkpoint regulator):

> Key regulator of abscission step in cytokinesis: part of the cytokinesis checkpoint, a process required to delay abscission to prevent both premature resolution of intercellular chromosome bridges and accumulation of DNA damage. Together with CHMP4C, required to retain abscission-competent VPS4 (VPS4A and/or VPS4B) at the midbody ring until abscission checkpoint signaling is terminated at late cytokinesis. Deactivation of AURKB results in dephosphorylation of CHMP4C followed by its dissociation …

**Summary**, from NCBI Gene [84936](https://www.ncbi.nlm.nih.gov/gene/84936):

> Enables phosphatidylinositol-3-phosphate binding activity. Involved in midbody abscission; mitotic cytokinesis checkpoint signaling; and negative regulation of cytokinesis. Located in centrosome; cleavage furrow; and midbody. Implicated in progressive familial intrahepatic cholestasis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20758) · Entrez [84936](https://www.ncbi.nlm.nih.gov/gene/84936) · UniProt [Q96K21](https://www.uniprot.org/uniprotkb/Q96K21) · Ensembl [ENSG00000166140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166140)

## Data

Gene col 9244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9244); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9244]; `tensor/DDL_lfc|DDL_z.npy` [9244]; `embed/gene_vectors.npy` [9244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9244 or target_col == 9244). Every well: [[ZFYVE19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
