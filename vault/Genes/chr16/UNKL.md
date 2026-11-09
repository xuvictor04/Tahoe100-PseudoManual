---
symbol: "UNKL"
type: "gene"
col: 671
ensembl_id: "ENSG00000059145"
name: "unk like zinc finger"
location: "16p13.3"
module: 64
arm: "+"
pooled_cpm: 20.38
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# UNKL

*unk like zinc finger* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.59× (z +14.5, q 1e-44, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.591× (z -8.5, q 1e-14, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.785× (z -5.5, q 4e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.63, fdr 1e-05), [[IGHMBP2]] (+0.58, fdr 2e-05), [[PTOV1-AS1]] (+0.57, fdr 8e-05); moves opposite to [[SDHAF3]] (-0.56, fdr 3e-05), [[GRB14]] (-0.54, fdr 4e-05), [[ATP5MC3]] (-0.54, fdr 3e-05, ⚠ ATP5MC3 in the vector space only through flagged drug-doses), [[BIRC3]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.59×** | +14.5 | 1e-44 | 43/48 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +8.7 | 1e-15 | 30/47 (NCI-H1573, KATO III, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.7 | 2e-12 | 29/47 (LoVo, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +7.4 | 2e-11 | 29/47 (H4, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.6 | 4e-04 | 23/47 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.004 | 15/47 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.004 | 18/48 (COLO 205, NCI-H1792, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.030 | 10/47 (A498, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.057 | 6/48 (A-427, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 13/47 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.591×** | -8.5 | 1e-14 | 31/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.600×** | -8.2 | 6e-14 | 29/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.611×** | -7.9 | 5e-13 | 32/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -6.3 | 4e-08 | 26/47 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -5.5 | 4e-06 | 26/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -5.3 | 1e-05 | 26/48 (SNU-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.732×** | -5.0 | 4e-05 | 26/48 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.733×** | -5.0 | 4e-05 | 23/43 (Panc 03.27, hTERT-HPNE, …) | two highest doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.7 | 2e-04 | 5/48 (J82, HepG2/C3A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.787×** | -3.7 | 0.012 | 21/46 (A-427, BT-474, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.021 | 13/47 (LS 180, C32, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.022 | 16/47 (SW48, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -3.3 | 0.036 | 16/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.044 | 14/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.090 | 13/48 (HCT15, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -11.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -12.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 16.9 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.37× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0782× (z -10.2) |
| [[LoVo (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~67% of this change |
| [[HS-578T (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.216× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 23.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.173× (z -8.5) |
| [[A-172 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[IGHMBP2]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PTOV1-AS1]] | +0.57 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[MAFG]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[NPIPB2]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RCC1L]] | +0.56 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[CCDC117]] | +0.56 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[RAB4B]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.54 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[DVL3]] | +0.54 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[BSDC1]] | +0.54 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GAS8]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GRB14]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ATP5MC3]] ⚠ | -0.54 | -0.43 / -0.48 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BIRC3]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[RIOK1]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[ZHX3]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[EID1]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[LINC00540]] | -0.48 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[PKP2]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[GPR37]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MFSD3]] | -0.47 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ABHD10]] | -0.47 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[NUP62CL]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UNKL's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.9, 12.5); signed map (4.4, -2.5). **Vector** length 89.8, 18.2% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +8.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.7 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.2 | -8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | unk like zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,363,205-1,414,751 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZC3HDC5L, ZC3H5L, FLJ23360; previously C16orf28 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9P5](https://www.uniprot.org/uniprotkb/Q9H9P5) (Putative E3 ubiquitin-protein ligase UNKL):

> May participate in a protein complex showing an E3 ligase activity regulated by RAC1. Ubiquitination is directed towards itself and possibly other substrates, such as SMARCD2/BAF60b. Intrinsic E3 ligase activity has not been proven.

**Summary**, from NCBI Gene [64718](https://www.ncbi.nlm.nih.gov/gene/64718):

> This gene encodes a RING finger protein that may function in Rac signaling. It can bind to Brg/Brm-associated factor 60b and can promote its ubiquitination. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:14184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14184) · Entrez [64718](https://www.ncbi.nlm.nih.gov/gene/64718) · UniProt [Q9H9P5](https://www.uniprot.org/uniprotkb/Q9H9P5) · Ensembl [ENSG00000059145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059145)

## Data

Gene col 671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 671); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 671]; `tensor/DDL_lfc|DDL_z.npy` [671]; `embed/gene_vectors.npy` [671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 671 or target_col == 671). Every well: [[UNKL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNKL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
