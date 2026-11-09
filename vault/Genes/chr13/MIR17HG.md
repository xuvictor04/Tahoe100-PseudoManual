---
symbol: "MIR17HG"
type: "gene"
col: 13262
ensembl_id: "ENSG00000215417"
name: "miR-17-92a-1 cluster host gene"
location: "13q31.3"
module: 5
arm: "+"
pooled_cpm: 9.1
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MIR17HG

*miR-17-92a-1 cluster host gene* — 13q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +9.9, q 3e-20, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.444× (z -8.6, q 6e-15, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A19]] (+0.65, fdr 7e-06), [[POLR1C]] (+0.62, fdr 1e-05), [[TXLNG]] (+0.61, fdr 1e-05); moves opposite to [[SYNJ2BP]] (-0.56, fdr 2e-05), [[EXOC5]] (-0.54, fdr 5e-05), [[ATP6V1A]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +9.9 | 3e-20 | 31/41 (Panc 03.27, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.029 | 19/45 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.042 | 17/45 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.099 | 10/45 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.35× | +3.2 | 0.15 | 14/45 (AsPC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.16 | 2/48 (NCI-H1792, COLO 205) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 1.23× | +3.1 | 0.16 | 18/42 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.444×** | -8.6 | 6e-15 | 29/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.515×** | -7.0 | 8e-10 | 21/30 (LOX-IMVI, SW1417, …) | two highest doses | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.547×** | -6.1 | 2e-07 | 25/44 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.575×** | -5.8 | 8e-07 | 22/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.628×** | -4.9 | 9e-05 | 22/47 (SW480, SHP-77, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.605×** | -4.9 | 9e-05 | 17/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.643×** | -4.8 | 1e-04 | 20/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.654×** | -4.3 | 0.001 | 19/45 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -4.2 | 0.001 | 20/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 0.001 | 18/46 (RKO, KATO III, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.446×** | -4.2 | 0.001 | 15/46 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.683×** | -4.0 | 0.003 | 15/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.007 | 14/46 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.705×** | -3.7 | 0.010 | 13/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.023 | 17/47 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 16.9 | 0 | 4 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.108× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.492× (z -11.1) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.132× (z -8.7) |
| [[SW480 (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -9.1) |
| [[A498 (line)]] | wt | 8.01 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 8.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0407× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.141× (z -9.1) |
| [[PANC-1 (line)]] | alt | 8.31 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -8.5) |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 5.91 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 5 µM 0.0618× (z -10.3) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0819× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A19]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[POLR1C]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TXLNG]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[USP2-AS1]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[NOP16]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[GART]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[AXIN1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[BEND3]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PAM16]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TEX10]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TAF4B]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNJ2BP]] | -0.56 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[EXOC5]] | -0.54 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[ATP6V1A]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GTF3C1]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[IFT22]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MDH1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[DYNC1LI2]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[C4orf33]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[DLD]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[TMTC3]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RAB14]] | -0.47 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[ALAD]] | -0.47 | -0.39 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MIR17HG's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.8, -42.7); signed map (-0.4, -55.9). **Vector** length 101, 23.0% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | miR-17-92a-1 cluster host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q31.3 — chr13:91,347,686-91,397,592 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ14178, MIRH1, MIHG1, NCRNA00048, miR-17-92, LINC00048; previously C13orf25, MIRHG1 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

UniProt [Q75NE6](https://www.uniprot.org/uniprotkb/Q75NE6) carries no function annotation.

**Summary**, from NCBI Gene [407975](https://www.ncbi.nlm.nih.gov/gene/407975):

> This gene is the host gene for the MIR17-92 cluster, a group of at least six microRNAs (miRNAs) that may be involved in cell survival, proliferation, differentiation, and angiogenesis. Amplification of this gene has been found in several lymphomas and solid tumors. Two non-protein coding transcript variants have been found for this host gene, but only the longest is a polycistronic transcript containing the MIR17-92 cluster. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:23564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23564) · Entrez [407975](https://www.ncbi.nlm.nih.gov/gene/407975) · UniProt [Q75NE6](https://www.uniprot.org/uniprotkb/Q75NE6) · Ensembl [ENSG00000215417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215417)

## Data

Gene col 13262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13262); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13262]; `tensor/DDL_lfc|DDL_z.npy` [13262]; `embed/gene_vectors.npy` [13262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13262 or target_col == 13262). Every well: [[MIR17HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR17HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
