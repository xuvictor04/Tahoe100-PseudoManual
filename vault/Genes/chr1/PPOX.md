---
symbol: "PPOX"
type: "gene"
col: 6701
ensembl_id: "ENSG00000143224"
name: "protoporphyrinogen oxidase"
location: "1q23.3"
module: 40
arm: "+"
pooled_cpm: 8.24
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PPOX

*protoporphyrinogen oxidase* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.52× (z +5.6, q 1e-05, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -12.8, q 6e-35, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAX]] (+0.70, fdr 7e-06), [[ELP2]] (+0.70, fdr 7e-06), [[NPRL2]] (+0.69, fdr 7e-06); moves opposite to [[FAT1]] (-0.65, fdr 1e-05), [[AKIRIN1]] (-0.57, fdr 2e-05), [[PTPN11]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DCLK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-05 | 20/46 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.005 | 9/38 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.005 | 14/42 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.019 | 8/37 (NCI-H23, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.021 | 9/44 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.021 | 7/42 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.030 | 6/46 (A-427, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.038 | 8/44 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.038 | 17/43 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.056 | 6/42 (SK-MEL-2, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -12.8 | 6e-35 | 39/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -12.7 | 2e-34 | 32/43 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -10.5 | 1e-23 | 29/42 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -9.4 | 1e-18 | 29/42 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -8.7 | 3e-16 | 28/46 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.542×** | -8.1 | 4e-14 | 27/47 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -7.7 | 1e-12 | 29/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -7.3 | 2e-11 | 26/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -6.5 | 4e-09 | 26/43 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -6.5 | 5e-09 | 24/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -6.4 | 1e-08 | 24/45 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.2 | 3e-08 | 22/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.638×** | -5.6 | 7e-07 | 22/43 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -5.0 | 2e-05 | 18/45 (J82, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.002 | 15/45 (SW480, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.590×** | -3.7 | 0.009 | 8/43 (A498, A549, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.604×** | -3.5 | 0.015 | 10/44 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.45 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -14.5) |
| [[A-172 (line)]] | wt | 13.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.4) |
| [[HOP62 (line)]] | alt | 8.50 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.137× (z -11.4) |
| [[PANC-1 (line)]] | alt | 8.80 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -10.2) |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.2) |
| [[A498 (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 6.33 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.0) |
| [[SHP-77 (line)]] | alt | 8.26 | 0 | 2 (1 ⚠) | — | [[EX229 (drug)]] 0.05 µM 0.0837× (z -9.3) |
| [[A549 (line)]] | wt | 6.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.9) |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 8.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.2) |
| [[J82 (line)]] | alt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -11.1) |
| [[SW 900 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 7.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.169× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAX]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ELP2]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[HINFP]] | +0.65 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[GNRH1]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[IFT20]] | +0.65 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MAPKAPK5-AS1]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[C1orf174]] | +0.64 | +0.46 / +0.71 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT1]] | -0.65 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[AKIRIN1]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK1]] | B | DCLK1 activity raises PPOX's level | lines that do not express DCLK1 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without DCLK1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, VAT1L, ENSG00000283982 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (1.1, -18.6); signed map (-41.3, 11.9). **Vector** length 64.4, 10.1% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -12.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | protoporphyrinogen oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,166,056-161,178,013 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPO; previously VP |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P50336](https://www.uniprot.org/uniprotkb/P50336) (Protoporphyrinogen oxidase):

> Catalyzes the 6-electron oxidation of protoporphyrinogen-IX to form protoporphyrin-IX.

**Summary**, from NCBI Gene [5498](https://www.ncbi.nlm.nih.gov/gene/5498):

> This gene encodes the penultimate enzyme of heme biosynthesis, which catalyzes the 6-electron oxidation of protoporphyrinogen IX to form protoporphyrin IX. Mutations in this gene cause variegate porphyria, an autosomal dominant disorder of heme metabolism resulting from a deficiency in protoporphyrinogen oxidase, an enzyme located on the inner mitochondrial membrane. Alternatively spliced transcript variants encoding the same protein have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9280) · Entrez [5498](https://www.ncbi.nlm.nih.gov/gene/5498) · UniProt [P50336](https://www.uniprot.org/uniprotkb/P50336) · Ensembl [ENSG00000143224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143224)

## Data

Gene col 6701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6701); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6701]; `tensor/DDL_lfc|DDL_z.npy` [6701]; `embed/gene_vectors.npy` [6701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6701 or target_col == 6701). Every well: [[PPOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
