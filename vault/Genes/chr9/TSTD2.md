---
symbol: "TSTD2"
type: "gene"
col: 5937
ensembl_id: "ENSG00000136925"
name: "thiosulfate sulfurtransferase like domain containing 2"
location: "9q22.33"
module: 148
arm: "+"
pooled_cpm: 26.98
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# TSTD2

*thiosulfate sulfurtransferase like domain containing 2* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +11.7, q 9e-29, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.574× (z -9.9, q 3e-20, down in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.721× (z -5.8, q 1e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS52]] (+0.69, fdr 1e-05), [[SP2]] (+0.68, fdr 1e-05), [[PSME3IP1]] (+0.68, fdr 1e-05); moves opposite to [[SUFU]] (-0.69, fdr 1e-05), [[NFRKB]] (-0.67, fdr 7e-06), [[STX7]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +11.7 | 9e-29 | 40/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.1 | 2e-07 | 27/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.3 | 2e-05 | 23/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.1 | 6e-05 | 22/47 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.8 | 0.016 | 14/35 (A-172, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.016 | 20/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.026 | 16/48 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +3.5 | 0.026 | 17/40 (SW 900, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +3.5 | 0.026 | 13/47 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +3.4 | 0.040 | 13/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5937.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -9.9 | 3e-20 | 37/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -6.3 | 1e-07 | 26/47 (J82, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -5.8 | 1e-06 | 26/48 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -5.2 | 4e-05 | 24/48 (NCI-H460, J82, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.756×** | -5.0 | 7e-05 | 25/48 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.793×** | -4.2 | 0.003 | 22/47 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.803×** | -3.9 | 0.007 | 18/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.824×** | -3.5 | 0.037 | 18/47 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.11 | 8/48 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.12 | 13/48 (SK-MEL-2, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 49.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.289× (z -10.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -9.0) |
| [[PANC-1 (line)]] | alt | 19.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.270× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.244× (z -10.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SHP-77 (line)]] | alt | 45.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.315× (z -8.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.405× (z -8.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -15.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.3) | — |
| [[SW48 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.481× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | +0.69 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SP2]] | +0.68 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PSME3IP1]] | +0.68 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PBLD]] | +0.67 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[AP4S1]] | +0.66 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PEF1]] | +0.66 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | +0.66 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[HCG18]] | +0.65 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CSTF3]] | +0.65 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[MAEA]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MCTS1]] | +0.63 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C8orf33]] | +0.63 | +0.55 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUFU]] | -0.69 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NFRKB]] | -0.67 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[STX7]] | -0.65 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[MAST3]] | -0.64 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[DPY30]] | -0.62 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TMEM185A]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.61 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[CFD]] | -0.60 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[CDC14B]] | -0.60 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[RNF114]] | -0.60 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[AHDC1]] | -0.60 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSTD2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRSS8]] | B | PRSS8 activity lowers TSTD2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.31× higher at baseline in the lines without PRSS8 | 0.039 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[RASAL1]] | B | RASAL1 activity lowers TSTD2's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.27× higher at baseline in the lines without RASAL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[HDAC6]] | B | HDAC6 activity raises TSTD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-7.1, 4.9); signed map (16.6, -28.3). **Vector** length 89.8, 18.3% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | thiosulfate sulfurtransferase like domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,600,080-97,633,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP4189; previously C9orf97 |
| Matched by | ensembl_id |

UniProt [Q5T7W7](https://www.uniprot.org/uniprotkb/Q5T7W7) carries no function annotation.

**Summary**, from NCBI Gene [158427](https://www.ncbi.nlm.nih.gov/gene/158427):

> Predicted to enable transferase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30087) · Entrez [158427](https://www.ncbi.nlm.nih.gov/gene/158427) · UniProt [Q5T7W7](https://www.uniprot.org/uniprotkb/Q5T7W7) · Ensembl [ENSG00000136925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136925)

## Data

Gene col 5937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5937); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5937]; `tensor/DDL_lfc|DDL_z.npy` [5937]; `embed/gene_vectors.npy` [5937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5937 or target_col == 5937). Every well: [[TSTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
