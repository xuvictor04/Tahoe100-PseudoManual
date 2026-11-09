---
symbol: "NAGA"
type: "gene"
col: 12753
ensembl_id: "ENSG00000198951"
name: "alpha-N-acetylgalactosaminidase"
location: "22q13.2"
module: 50
arm: "+"
pooled_cpm: 5.94
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NAGA

*alpha-N-acetylgalactosaminidase* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.09× (z +12.6, q 2e-33, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +7.9, q 4e-13, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.463× (z -12.6, q 2e-33, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENON]] (+0.76, fdr 7e-06), [[ADAM15]] (+0.74, fdr 7e-06), [[SLC25A39]] (+0.73, fdr 7e-06); moves opposite to [[NSRP1]] (-0.70, fdr 1e-05), [[SNHG8]] (-0.68, fdr 7e-06), [[PPIG]] (-0.66, fdr 8e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +12.6 | 2e-33 | 9/9 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +10.3 | 3e-22 | 22/28 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +8.6 | 2e-15 | 9/15 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +7.9 | 4e-13 | 27/43 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.90×** | +7.4 | 1e-11 | 24/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.68×** | +6.0 | 2e-07 | 25/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.61×** | +5.3 | 9e-06 | 20/41 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.46×** | +4.4 | 9e-04 | 17/47 (SW480, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.7 | 0.015 | 10/33 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.040 | 9/45 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.045 | 6/48 (NCI-H2347, KATO III, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.087 | 2/48 (NCI-H460, NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.463×** | -12.6 | 2e-33 | 31/40 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -10.6 | 1e-23 | 32/39 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.560×** | -6.4 | 3e-08 | 23/43 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -6.1 | 1e-07 | 24/46 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.0 | 0.007 | 9/48 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.009 | 13/46 (A549, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -3.6 | 0.023 | 19/45 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.035 | 17/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.753× | -3.1 | 0.11 | 14/43 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.763× | -3.1 | 0.11 | 14/43 (J82, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.767× | -3.1 | 0.12 | 11/46 (SHP-77, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 6.10 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0946× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 7.63 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0980× (z -11.8) |
| [[HOP62 (line)]] | alt | 7.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.8) |
| [[Hs 766T (line)]] | wt | 7.11 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.102× (z -9.5) |
| [[HT-29 (line)]] | alt | 3.57 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0848× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 6.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0559× (z -9.9) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 4.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0928× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 5.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0883× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.5) |
| [[SW1417 (line)]] | alt | 3.67 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0709× (z -8.9) |
| [[A-172 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENON]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.73 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[BSG]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[GPAA1]] | +0.69 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[LMF2]] | +0.69 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC16]] | +0.68 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[TUBG1]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.70 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[PPIG]] | -0.66 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[CCDC174]] | -0.66 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ATF4]] | -0.66 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[PRPF38B]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SEC62]] | -0.65 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[DNAJC2]] | -0.64 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NDUFB9]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[DCTN6]] | -0.61 | -0.57 / -0.49 | both halves | 2e-05 |  |
| [[MRPS18B]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NAGA's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -24.2); signed map (-27.6, -39.6). **Vector** length 62.3, 8.81% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.56 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.54 to 7); *epithelial mesenchymal transition* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -12.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -6.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | alpha-N-acetylgalactosaminidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,058,334-42,070,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D22S674 |
| Gene groups (HGNC) | Galactosidases alpha |
| Matched by | ensembl_id |

**Function**, from UniProt [P17050](https://www.uniprot.org/uniprotkb/P17050) (Alpha-N-acetylgalactosaminidase):

> Removes terminal alpha-N-acetylgalactosamine residues from glycolipids such as neolactosides and globoside Forssman, as well as glycopeptides, helping degrade glycoconjugates in the lysosome.

**Summary**, from NCBI Gene [4668](https://www.ncbi.nlm.nih.gov/gene/4668):

> NAGA encodes the lysosomal enzyme alpha-N-acetylgalactosaminidase, which cleaves alpha-N-acetylgalactosaminyl moieties from glycoconjugates. Mutations in NAGA have been identified as the cause of Schindler disease types I and II (type II also known as Kanzaki disease). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7631) · Entrez [4668](https://www.ncbi.nlm.nih.gov/gene/4668) · UniProt [P17050](https://www.uniprot.org/uniprotkb/P17050) · Ensembl [ENSG00000198951](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198951)

## Data

Gene col 12753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12753); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12753]; `tensor/DDL_lfc|DDL_z.npy` [12753]; `embed/gene_vectors.npy` [12753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12753 or target_col == 12753). Every well: [[NAGA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAGA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
