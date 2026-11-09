---
symbol: "H3-3A-DT"
type: "gene"
col: 15727
ensembl_id: "ENSG00000272562"
name: "H3-3A divergent transcript"
location: "1q42.12"
module: 15
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# H3-3A-DT

*H3-3A divergent transcript* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +8.2, q 1e-13, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.214× (z -11.8, q 2e-29, down in 38 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.407× (z -6.9, q 8e-10, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCMTD1]] (+0.65, fdr 6e-05), [[DPY19L2P3]] (+0.64, fdr 7e-06), [[BICRAL]] (+0.63, fdr 1e-05); moves opposite to [[DPF1]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RDM1P5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +8.2 | 1e-13 | 24/32 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +7.2 | 2e-10 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +4.8 | 2e-04 | 13/31 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.85×** | +4.8 | 3e-04 | 16/45 (SNU-423, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.020 | 7/44 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.020 | 12/42 (CFPAC-1, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +3.6 | 0.022 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.052 | 5/47 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.57×** | +3.3 | 0.062 | 4/43 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.2 | 0.072 | 6/32 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.094 | 3/43 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.53× | +3.0 | 0.11 | 2/45 (NCI-H2030, SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.214×** | -11.8 | 2e-29 | 38/45 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.284×** | -9.6 | 1e-19 | 37/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.407×** | -6.9 | 8e-10 | 25/41 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.407×** | -6.9 | 8e-10 | 24/42 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.395×** | -6.8 | 9e-10 | 26/42 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.424×** | -6.6 | 4e-09 | 23/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.217×** | -6.1 | 7e-08 | 20/32 (NCI-H460, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.586×** | -5.8 | 6e-07 | 18/35 (PANC-1, A549, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.249×** | -5.6 | 2e-06 | 19/24 (PANC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.362×** | -5.6 | 2e-06 | 21/46 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.503×** | -5.3 | 8e-06 | 18/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.509×** | -5.2 | 1e-05 | 15/24 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.492×** | -5.1 | 1e-05 | 19/39 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.295×** | -4.9 | 4e-05 | 16/29 (NCI-H460, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.303×** | -4.8 | 7e-05 | 16/23 (NCI-H1573, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -3.8 | 0.004 | 18/35 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -3.7 | 0.006 | 13/38 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.540×** | -3.4 | 0.019 | 7/36 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.549×** | -3.3 | 0.025 | 5/39 (SW480, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.658×** | -3.1 | 0.048 | 13/40 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.467×** | -3.0 | 0.050 | 11/29 (A549, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0256× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.105× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 4.00 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0558× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0649× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Raltitrexed (drug)]] 0.5 µM 0.0806× (z -8.6) |
| [[A-172 (line)]] | wt | 3.19 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0586× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 2.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 2.31 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0310× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0709× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.967 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMTD1]] | +0.65 | +0.38 / +0.67 | both halves | 6e-05 |  |
| [[DPY19L2P3]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[BICRAL]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 | same gene group |
| [[PPP1CB-DT]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 | same gene group |
| [[SPESP1]] | +0.62 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[FRG1HP]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CRTC3-AS1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB44]] | +0.59 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CDNF]] | +0.59 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[GOT1-DT]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | -0.46 | -0.40 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises H3-3A-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without RDM1P5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.7, 22.3); signed map (33.1, -7.6). **Vector** length 53.5, 7.39% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +3.6 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -11.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.7 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | H3-3A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q42.12 — chr1:226,045,561-226,061,898 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55210) · Entrez [118568813](https://www.ncbi.nlm.nih.gov/gene/118568813) · Ensembl [ENSG00000272562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272562)

## Data

Gene col 15727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15727); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15727]; `tensor/DDL_lfc|DDL_z.npy` [15727]; `embed/gene_vectors.npy` [15727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15727 or target_col == 15727). Every well: [[H3-3A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H3-3A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
