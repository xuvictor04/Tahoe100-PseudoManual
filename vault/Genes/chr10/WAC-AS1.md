---
symbol: "WAC-AS1"
type: "gene"
col: 14888
ensembl_id: "ENSG00000254635"
name: "WAC antisense RNA 1"
location: "10p12.1"
module: 68
arm: "+"
pooled_cpm: 19.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# WAC-AS1

*WAC antisense RNA 1* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +11.7, q 1e-28, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.497× (z -7.2, q 3e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM19]] (+0.78, fdr 7e-06), [[ERCC6L2-AS1]] (+0.77, fdr 4e-05), [[PATL2]] (+0.76, fdr 5e-05); moves opposite to [[LPCAT1]] (-0.72, fdr 3e-05), [[ST6GALNAC4]] (-0.69, fdr 1e-04), [[PHKA2]] (-0.67, fdr 1e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TBX20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +11.7 | 1e-28 | 42/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +8.2 | 8e-14 | 26/31 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.0 | 5e-10 | 33/47 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.3 | 5e-08 | 35/43 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.003 | 28/48 (A-172, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.003 | 28/48 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +3.9 | 0.010 | 18/35 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.020 | 18/47 (C32, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.037 | 17/48 (SW480, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.32× | +3.1 | 0.13 | 16/46 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.497×** | -7.2 | 3e-10 | 35/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.519×** | -7.1 | 3e-10 | 39/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -6.8 | 2e-09 | 33/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -6.7 | 2e-09 | 39/48 (A-427, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.541×** | -6.7 | 3e-09 | 35/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -6.6 | 5e-09 | 32/47 (SNU-423, SW480, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.328×** | -6.3 | 2e-08 | 35/45 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -5.7 | 6e-07 | 25/47 (LS 180, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -5.4 | 4e-06 | 32/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.615×** | -5.3 | 8e-06 | 32/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.661×** | -4.5 | 4e-04 | 25/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -4.2 | 0.001 | 24/47 (SNU-1, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -3.9 | 0.004 | 24/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.538×** | -3.5 | 0.017 | 18/39 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.728×** | -3.4 | 0.022 | 21/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.636×** | -3.2 | 0.045 | 9/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.757×** | -3.0 | 0.085 | 12/47 (SNU-1, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 16.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +8.6) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.104× (z -9.1) |
| [[HOP62 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0559× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.230× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.195× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +9.2) | — |
| [[RKO (line)]] | wt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.5) | — |
| [[A-172 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM19]] | +0.78 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ERCC6L2-AS1]] | +0.77 | +0.77 / +0.41 | both halves | 4e-05 | same gene group |
| [[PATL2]] | +0.76 | +0.80 / +0.39 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | +0.76 | +0.78 / +0.33 | both halves | 1e-04 | same gene group |
| [[PCNX4-DT]] | +0.75 | +0.81 / +0.31 | both halves | 2e-04 |  |
| [[AHI1-DT]] | +0.75 | +0.72 / +0.38 | both halves | 6e-05 |  |
| [[PPP1R12A-AS2]] | +0.74 | +0.76 / +0.33 | both halves | 1e-04 | same gene group |
| [[AK9]] | +0.74 | +0.79 / +0.39 | both halves | 6e-05 |  |
| [[BDNF-AS]] | +0.74 | +0.81 / +0.32 | both halves | 2e-04 | same gene group |
| [[PBLD]] | +0.74 | +0.73 / +0.26 | both halves | 4e-04 |  |
| [[RAP2C-AS1]] | +0.74 | +0.80 / +0.58 | both halves | 8e-06 | same gene group |
| [[PKN2-AS1]] | +0.74 | +0.77 / +0.19 | ⚠ one half (not replicated) | 9e-04 | same gene group |
| [[NUTM2E]] | +0.74 | +0.75 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.72 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.69 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[PHKA2]] | -0.67 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[MAST3]] | -0.67 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[ANKRD27]] | -0.67 | -0.66 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[GNB1L]] | -0.66 | -0.55 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX20]] | B | TBX20 activity raises WAC-AS1's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.37× lower at baseline in the lines without TBX20 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[TOP2A]] | B | TOP2A activity lowers WAC-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.817). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (3.0, 13.6); signed map (22.9, -15.0). **Vector** length 87.1, 20.9% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.5 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.4 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.2 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | WAC antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p12.1 — chr10:28,522,652-28,533,066 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27347) · Entrez [220906](https://www.ncbi.nlm.nih.gov/gene/220906) · Ensembl [ENSG00000254635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254635)

## Data

Gene col 14888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14888); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14888]; `tensor/DDL_lfc|DDL_z.npy` [14888]; `embed/gene_vectors.npy` [14888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14888 or target_col == 14888). Every well: [[WAC-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WAC-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
