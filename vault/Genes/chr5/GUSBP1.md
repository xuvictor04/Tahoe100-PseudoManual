---
symbol: "GUSBP1"
type: "gene"
col: 11432
ensembl_id: "ENSG00000183666"
name: "GUSB pseudogene 1"
location: "5p14.3"
module: 57
arm: "+"
pooled_cpm: 22.64
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# GUSBP1

*GUSB pseudogene 1* — 5p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.96× (z +10.0, q 9e-21, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.437× (z -12.3, q 7e-32, down in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.654× (z -8.7, q 6e-16, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSBP18]] (+0.73, fdr 7e-06), [[IFT172]] (+0.66, fdr 2e-05), [[PRUNE1]] (+0.66, fdr 1e-05); moves opposite to [[GCNT4]] (-0.69, fdr 2e-05), [[CYREN]] (-0.64, fdr 3e-05), [[ENO3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +10.0 | 9e-21 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +9.6 | 2e-19 | 39/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +6.9 | 1e-09 | 33/47 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 1.18× | +3.5 | 0.072 | 18/48 (RKO, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Rifaximin (drug)]] 5 µM |  | 1.25× | +3.2 | 0.18 | 8/47 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.21 | 6/48 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.437×** | -12.3 | 7e-32 | 35/42 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -8.7 | 6e-16 | 32/47 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.549×** | -8.5 | 3e-15 | 35/48 (AN3 CA, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -8.0 | 2e-13 | 21/32 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -7.4 | 1e-11 | 33/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -6.4 | 2e-08 | 26/47 (RPMI-7951, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -6.0 | 1e-07 | 25/38 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.772×** | -5.4 | 6e-06 | 23/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -4.9 | 7e-05 | 20/47 (HOP62, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.782×** | -3.6 | 0.016 | 16/46 (NCI-H2347, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.023 | 14/47 (H4, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.791×** | -3.5 | 0.026 | 13/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.805×** | -3.2 | 0.062 | 17/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.857× | -3.1 | 0.066 | 10/48 (LS 180, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 32.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.248× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.4) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 36.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.6) |
| [[A498 (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -8.8) |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -12.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 2 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0965× (z -9.9) |
| [[SW480 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.130× (z -9.2) |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.104× (z -10.7) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.122× (z -10.6) |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.6) |
| [[J82 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.372× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -9.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0746× (z -12.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 35.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.6) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP18]] | +0.73 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[IFT172]] | +0.66 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PRUNE1]] | +0.66 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MED23]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[POT1]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SDHB]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CROT]] | +0.61 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[IMMP1L]] | +0.60 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[ACACB]] | +0.59 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[ARL6]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[EDRF1]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MRPS31P5-1]] | +0.58 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | -0.69 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CYREN]] | -0.64 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ENO3]] | -0.62 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.62 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GPR137]] | -0.61 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[SPHK1]] | -0.61 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.59 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SOCS2-AS1]] | -0.59 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[GRK4]] | -0.59 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[CPEB2-DT]] | -0.59 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[LINC00667]] | -0.58 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[KRCC1]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GUSBP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (10.9, 9.0); signed map (-29.6, -10.0). **Vector** length 67.6, 11.9% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +0.8 | -0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.4 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.8 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | GUSB pseudogene 1 |
| Locus type | pseudogene |
| Location | 5p14.3 — chr5:21,459,560-21,501,826 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

UniProt [Q15486](https://www.uniprot.org/uniprotkb/Q15486) carries no function annotation.

**Summary**, from NCBI Gene [728411](https://www.ncbi.nlm.nih.gov/gene/728411):

> Predicted to be involved in nervous system development and skeletal system development. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13670) · Entrez [728411](https://www.ncbi.nlm.nih.gov/gene/728411) · UniProt [Q15486](https://www.uniprot.org/uniprotkb/Q15486) · Ensembl [ENSG00000183666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183666)

## Data

Gene col 11432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11432); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11432]; `tensor/DDL_lfc|DDL_z.npy` [11432]; `embed/gene_vectors.npy` [11432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11432 or target_col == 11432). Every well: [[GUSBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUSBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
