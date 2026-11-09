---
symbol: "RBM18"
type: "gene"
col: 4069
ensembl_id: "ENSG00000119446"
name: "RNA binding motif protein 18"
location: "9q33.2"
module: 17
arm: "+"
pooled_cpm: 30.31
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RBM18

*RNA binding motif protein 18* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.96× (z +15.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -16.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC5]] (+0.70, fdr 7e-06), [[ABITRAM]] (+0.67, fdr 7e-06), [[DBT]] (+0.66, fdr 7e-06); moves opposite to [[TPTEP2-CSNK1E]] (-0.59, fdr 1e-05), [[PRDM10]] (-0.53, fdr 4e-05), [[ING2-DT]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.96×** | +15.5 | 0e+00 | 47/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +12.5 | 2e-33 | 39/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +11.4 | 1e-27 | 39/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +10.7 | 2e-24 | 35/47 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +10.1 | 8e-22 | 43/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +8.2 | 2e-14 | 22/36 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +8.0 | 1e-13 | 32/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.9 | 2e-13 | 34/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 3e-13 | 32/48 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.0 | 1e-10 | 26/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +7.0 | 1e-10 | 28/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.1 | 4e-08 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +6.1 | 5e-08 | 24/48 (A549, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +5.4 | 3e-06 | 25/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.3 | 7e-04 | 19/48 (RKO, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.010 | 17/47 (C32, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.047 | 11/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.1 | 0.047 | 9/48 (KATO III, SW480, …) | top dose only |  |
| [[Tolcapone (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.057 | 3/48 (SW480, H4, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -16.9 | 0e+00 | 44/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -9.1 | 2e-17 | 32/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -5.0 | 1e-04 | 20/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.769×** | -4.1 | 0.006 | 12/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.0 | 0.006 | 22/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.824×** | -4.0 | 0.006 | 15/48 (RPMI-7951, SW 900, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.891× | -3.6 | 0.027 | 8/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.848× | -3.5 | 0.036 | 15/47 (HOP62, C32, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.16 | 13/48 (PANC-1, KATO III, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.1 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 6.23× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -18.2) |
| [[RKO (line)]] | wt | 39.7 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.32× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -16.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.5) |
| [[COLO 205 (line)]] | alt | 56.1 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.41× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.1) |
| [[Hs 766T (line)]] | wt | 47.5 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.24× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 26.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +8.7) | — |
| [[A-172 (line)]] | wt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.102× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.8) |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -9.4) |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.207× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.5) |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 30.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.83× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 30.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.2) |
| [[SHP-77 (line)]] | alt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.6) |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -9.8) |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.9) |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC5]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DBT]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SRP68]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[COG2]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DRG2]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PABIR1]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ZNF510]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[IFTAP]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[PRDM10]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ING2-DT]] | -0.53 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[GATD1-DT]] | -0.52 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[MEMO1]] | -0.51 | -0.57 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBM18's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZFP82]] | B | ZFP82 activity lowers RBM18's level | lines that do not express ZFP82 (20) vs lines expressing it (30) | 1.32× higher at baseline in the lines without ZFP82 | 0.075 | ⚠ within organs, on part of the lines; also absent: UBE2Q2P13, TUB, MIR130AHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.7, 1.1); signed map (-21.1, -16.9). **Vector** length 98.0, 22.0% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -16.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,237,622-122,264,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2734 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q96H35](https://www.uniprot.org/uniprotkb/Q96H35) carries no function annotation.

**Summary**, from NCBI Gene [92400](https://www.ncbi.nlm.nih.gov/gene/92400):

> Predicted to enable RNA binding activity. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28413) · Entrez [92400](https://www.ncbi.nlm.nih.gov/gene/92400) · UniProt [Q96H35](https://www.uniprot.org/uniprotkb/Q96H35) · Ensembl [ENSG00000119446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119446)

## Data

Gene col 4069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4069); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4069]; `tensor/DDL_lfc|DDL_z.npy` [4069]; `embed/gene_vectors.npy` [4069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4069 or target_col == 4069). Every well: [[RBM18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
