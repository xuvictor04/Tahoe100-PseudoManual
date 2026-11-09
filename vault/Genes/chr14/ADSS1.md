---
symbol: "ADSS1"
type: "gene"
col: 11624
ensembl_id: "ENSG00000185100"
name: "adenylosuccinate synthase 1"
location: "14q32.33"
module: 47
arm: "+"
pooled_cpm: 5.17
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# ADSS1

*adenylosuccinate synthase 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.01× (z +6.5, q 4e-08, up in 3 of 11 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.438× (z -8.0, q 8e-13, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[H19]] (+0.56, fdr 5e-05), [[PIP5KL1]] (+0.55, fdr 3e-05), [[NOTCH3]] (+0.53, fdr 3e-05); moves opposite to [[LINC02100]] (-0.47, fdr 2e-04), [[TMEM192]] (-0.46, fdr 3e-04), [[PAXIP1-AS2]] (-0.46, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PTGS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +6.5 | 4e-08 | 3/11 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.9 | 1e-06 | 8/23 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +3.8 | 0.030 | 4/14 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.40× | +3.2 | 0.16 | 11/44 (HCT15, PANC-1, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.26× | +3.2 | 0.16 | 4/43 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.438×** | -8.0 | 8e-13 | 28/43 (SHP-77, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.460×** | -7.5 | 2e-11 | 27/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.638×** | -6.2 | 1e-07 | 19/36 (HOP62, SHP-77, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -5.6 | 4e-06 | 23/40 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.670×** | -5.5 | 5e-06 | 19/43 (J82, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.576×** | -5.3 | 9e-06 | 21/42 (NCI-H460, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -4.6 | 3e-04 | 17/42 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -4.3 | 0.001 | 19/36 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 0.001 | 21/42 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -4.0 | 0.003 | 17/44 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.005 | 14/40 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.006 | 11/43 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -3.5 | 0.023 | 14/42 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -3.4 | 0.023 | 12/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.706×** | -3.4 | 0.029 | 14/44 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.711×** | -3.2 | 0.049 | 7/43 (SNU-1, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.738×** | -2.9 | 0.093 | 13/44 (HT-29, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0845× (z -14.3) |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0200× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.118× (z -10.5) |
| [[HT-29 (line)]] | alt | 9.62 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0339× (z -11.2) |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.7) |
| [[KATO III (line)]] | alt | 8.88 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~90% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.127× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0419× (z -12.5) |
| [[A-427 (line)]] | wt | 5.37 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0753× (z -10.4) |
| [[C-33 A (line)]] | alt | 7.92 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0928× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 3.43 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0605× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0819× (z -8.7) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H19]] | +0.56 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[PIP5KL1]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[NOTCH3]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[P2RY2]] | +0.52 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[GNB1L]] | +0.52 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[CUL9]] | +0.50 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[PLXND1]] | +0.49 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[SARDH]] | +0.49 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[SCART1]] | +0.49 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[NCOR2]] | +0.49 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[SEMA4A]] | +0.48 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[FSCN2]] | +0.48 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02100]] | -0.47 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[TMEM192]] | -0.46 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[PAXIP1-AS2]] | -0.46 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[P2RX4]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RAB9A]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TLCD5]] | -0.44 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[WBP4]] | -0.44 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[NKIRAS1]] | -0.44 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[SCYL3]] | -0.44 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[RNPC3]] | -0.43 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[UBXN2A]] | -0.43 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[SLC49A4]] | -0.43 | -0.37 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGS1]] | B | PTGS1 activity raises ADSS1's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without PTGS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[SERPINA5]] | B | SERPINA5 activity raises ADSS1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.68× lower at baseline in the lines without SERPINA5 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[SARDH]] | B | SARDH activity raises ADSS1's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.51× lower at baseline in the lines without SARDH | 0.087 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.0, -20.2); signed map (16.0, 17.5). **Vector** length 68.3, 10.5% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.1 | +3.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.9 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylosuccinate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,724,174-104,747,325 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38602; previously ADSSL1 |
| Gene groups (HGNC) | Adenylosuccinate synthase family |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N142](https://www.uniprot.org/uniprotkb/Q8N142) (Adenylosuccinate synthetase isozyme 1):

> Component of the purine nucleotide cycle (PNC), which interconverts IMP and AMP to regulate the nucleotide levels in various tissues, and which contributes to glycolysis and ammoniagenesis. Catalyzes the first committed step in the biosynthesis of AMP from IMP.

**Summary**, from NCBI Gene [122622](https://www.ncbi.nlm.nih.gov/gene/122622):

> This gene encodes a member of the adenylosuccinate synthase family of proteins. The encoded muscle-specific enzyme plays a role in the purine nucleotide cycle by catalyzing the first step in the conversion of inosine monophosphate (IMP) to adenosine monophosphate (AMP). Mutations in this gene may cause adolescent onset distal myopathy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:20093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20093) · Entrez [122622](https://www.ncbi.nlm.nih.gov/gene/122622) · UniProt [Q8N142](https://www.uniprot.org/uniprotkb/Q8N142) · Ensembl [ENSG00000185100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185100)

## Data

Gene col 11624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11624); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11624]; `tensor/DDL_lfc|DDL_z.npy` [11624]; `embed/gene_vectors.npy` [11624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11624 or target_col == 11624). Every well: [[ADSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
