---
symbol: "ARG2"
type: "gene"
col: 1312
ensembl_id: "ENSG00000081181"
name: "arginase 2"
location: "14q24.1"
module: 56
arm: "+"
pooled_cpm: 17.61
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# ARG2

*arginase 2* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.80× (z +11.0, q 3e-25, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.644× (z -4.7, q 0.001, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARF4]] (+0.63, fdr 1e-05), [[ERN1]] (+0.62, fdr 1e-05), [[BUD31]] (+0.62, fdr 2e-05); moves opposite to [[GTF2I]] (-0.59, fdr 2e-05), [[MTPAP]] (-0.52, fdr 4e-05), [[ZNF507]] (-0.52, fdr 9e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +11.0 | 3e-25 | 32/44 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +10.8 | 1e-24 | 27/42 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +10.6 | 4e-24 | 34/44 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +9.6 | 1e-19 | 28/43 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.9 | 3e-07 | 20/40 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +4.8 | 1e-04 | 23/44 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 18/44 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +4.1 | 0.002 | 20/43 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.010 | 17/44 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.018 | 12/40 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.021 | 15/44 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.039 | 12/41 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.37×** | +3.3 | 0.039 | 14/43 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.053 | 17/44 (SHP-77, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +3.2 | 0.054 | 11/42 (NCI-H2030, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.073 | 8/43 (LoVo, SHP-77, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.73×** | +3.0 | 0.076 | 13/39 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -4.7 | 0.001 | 20/43 (KATO III, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -4.6 | 0.001 | 24/41 (A-427, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.776×** | -3.8 | 0.025 | 19/44 (HepG2/C3A, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.689×** | -3.7 | 0.029 | 15/43 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.717×** | -3.6 | 0.033 | 16/43 (HepG2/C3A, NCI-H2347, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.718×** | -3.6 | 0.033 | 15/43 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.698×** | -3.2 | 0.097 | 19/44 (KATO III, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.097 | 15/43 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.739×** | -3.1 | 0.097 | 13/42 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.097 | 18/44 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | 0.818× | -3.1 | 0.11 | 16/44 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.747× | -3.0 | 0.12 | 13/42 (HepG2/C3A, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 68.5 | 0 | 4 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.143× (z -11.1) |
| [[KATO III (line)]] | alt | 41.0 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 9.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +12.5) | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0393× (z -16.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 5.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 8.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.0) |
| [[LoVo (line)]] | wt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 38.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.72× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 9.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +11.1) | — |
| [[A-172 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF4]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ERN1]] | +0.62 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[BUD31]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[DDIT3]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[GOT1]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[EAF2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SLC9A1]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SUCO]] | +0.57 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[MKNK2]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DIS3]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[POR]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MTPAP]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.52 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZFX]] | -0.51 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[SUCLA2]] | -0.51 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[ZZZ3]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ATF7IP]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[LINC01836]] | -0.50 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[SOCS4]] | -0.49 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[USP24]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[METAP1D]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[GFM1]] | -0.49 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTH]] | B | CTH activity raises ARG2's level | lines that do not express CTH (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without CTH | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, -7.4); signed map (-2.3, 29.7). **Vector** length 111, 28.3% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +10.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +9.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -3.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | arginase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,619,920-67,651,708 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Urea cycle; Mitochondrial protein degradation; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P78540](https://www.uniprot.org/uniprotkb/P78540) (Arginase-2, mitochondrial):

> May play a role in the regulation of extra-urea cycle arginine metabolism and also in down-regulation of nitric oxide synthesis. Extrahepatic arginase functions to regulate L-arginine bioavailability to nitric oxid synthase (NOS). Arginine metabolism is a critical regulator of innate and adaptive immune responses. Seems to be involved in negative regulation of the survival capacity of activated CD4(+) and CD8(+) T cells. May suppress inflammation-related signaling in asthmatic airway …

**Summary**, from NCBI Gene [384](https://www.ncbi.nlm.nih.gov/gene/384):

> Arginase catalyzes the hydrolysis of arginine to ornithine and urea. At least two isoforms of mammalian arginase exists (types I and II) which differ in their tissue distribution, subcellular localization, immunologic crossreactivity and physiologic function. The type II isoform encoded by this gene, is located in the mitochondria and expressed in extra-hepatic tissues, especially kidney. The physiologic role of this isoform is poorly understood; it is thought to play a role in nitric oxide and …

**Accessions** — [HGNC:664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:664) · Entrez [384](https://www.ncbi.nlm.nih.gov/gene/384) · UniProt [P78540](https://www.uniprot.org/uniprotkb/P78540) · Ensembl [ENSG00000081181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081181)

## Data

Gene col 1312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1312); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1312]; `tensor/DDL_lfc|DDL_z.npy` [1312]; `embed/gene_vectors.npy` [1312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1312 or target_col == 1312). Every well: [[ARG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
