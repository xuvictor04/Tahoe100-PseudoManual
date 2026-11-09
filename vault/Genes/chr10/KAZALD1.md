---
symbol: "KAZALD1"
type: "gene"
col: 2885
ensembl_id: "ENSG00000107821"
name: "Kazal type serine peptidase inhibitor domain 1"
location: "10q24.31"
module: 15
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# KAZALD1

*Kazal type serine peptidase inhibitor domain 1* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +7.6, q 1e-11, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.297× (z -10.1, q 2e-21, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPER2P1-1]] (+0.67, fdr 7e-06), [[COPZ2]] (+0.58, fdr 1e-05), [[IST1]] (+0.57, fdr 6e-05); moves opposite to [[HUS1]] (-0.52, fdr 1e-04), [[MTG1]] (-0.50, fdr 1e-04), [[HIF1AN]] (-0.46, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SSPOP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.6 | 1e-11 | 19/31 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +7.3 | 7e-11 | 2/4 (HS-578T, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +6.9 | 1e-09 | 14/20 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +3.7 | 0.028 | 3/18 (NCI-H1573, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +3.7 | 0.028 | 6/9 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.4 | 0.059 | 3/11 (A-172, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.50× | +3.1 | 0.14 | 9/34 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.45× | +3.0 | 0.18 | 7/32 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2885.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.297×** | -10.1 | 2e-21 | 35/47 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.320×** | -9.5 | 6e-19 | 33/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -8.8 | 2e-16 | 24/33 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.498×** | -8.2 | 3e-14 | 24/33 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.418×** | -7.3 | 4e-11 | 26/41 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -7.1 | 1e-10 | 29/44 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -7.0 | 2e-10 | 23/34 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.434×** | -7.0 | 2e-10 | 26/43 (SW480, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -6.7 | 1e-09 | 29/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.480×** | -6.1 | 5e-08 | 22/46 (LoVo, H4, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.494×** | -5.9 | 2e-07 | 22/45 (HT-29, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.528×** | -5.3 | 5e-06 | 20/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.530×** | -5.3 | 5e-06 | 23/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.548×** | -5.0 | 2e-05 | 20/46 (LoVo, AN3 CA, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.575×** | -4.6 | 1e-04 | 18/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.569×** | -4.5 | 2e-04 | 18/42 (HS-578T, HT-29, …) | two highest doses | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -4.3 | 5e-04 | 17/40 (A-427, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 7.25 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -11.0) |
| [[SW480 (line)]] | alt | 6.11 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.150× (z -10.4) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.100× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 5.83 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.71 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.106× (z -11.2) |
| [[HT-29 (line)]] | alt | 2.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0390× (z -13.1) |
| [[PANC-1 (line)]] | alt | 3.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.125× (z -9.0) |
| [[SW 900 (line)]] | alt | 4.16 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0487× (z -9.3) |
| [[A-427 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPER2P1-1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[COPZ2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[IST1]] | +0.57 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[PROCA1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PRRT1]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CATSPER2P1]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SATB2-AS1]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[DNAJC3-DT]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[PIP5K1A]] | +0.51 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[PJVK]] | +0.51 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HOXB4]] | +0.51 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[RAF1]] | +0.50 | +0.38 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUS1]] | -0.52 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[MTG1]] | -0.50 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[HIF1AN]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[HARS1]] | -0.45 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[RSC1A1]] | -0.44 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[TAF1B]] | -0.44 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[MPHOSPH6]] | -0.44 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[DFFA]] | -0.44 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[EFTUD2]] | -0.44 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[IDH3A]] | -0.44 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[GLO1]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[WDCP]] | -0.43 | -0.29 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | SSPOP activity raises KAZALD1's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without SSPOP | 0.038 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[INHA]] | B | INHA activity raises KAZALD1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without INHA | 0.047 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.314). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.7, 24.2); signed map (34.3, -4.9). **Vector** length 54.2, 7.77% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +6.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | Kazal type serine peptidase inhibitor domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:101,061,989-101,068,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG40, FKSG28 |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I82](https://www.uniprot.org/uniprotkb/Q96I82) (Kazal-type serine protease inhibitor domain-containing protein 1):

> Involved in the proliferation of osteoblasts during bone formation and bone regeneration. Promotes matrix assembly (By similarity).

**Summary**, from NCBI Gene [81621](https://www.ncbi.nlm.nih.gov/gene/81621):

> This gene encodes a secreted member of the insulin growth factor-binding protein (IGFBP) superfamily. The protein contains an insulin growth factor-binding domain in its N-terminal region, a Kazal-type serine protease inhibitor and follistatin-like domain in its central region, and an immunoglobulin-like domain in its C-terminal region. Studies of the mouse ortholog suggest that this protein may function in bone development and bone regeneration. This gene is hypomethylated and over-expressed …

**Accessions** — [HGNC:25460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25460) · Entrez [81621](https://www.ncbi.nlm.nih.gov/gene/81621) · UniProt [Q96I82](https://www.uniprot.org/uniprotkb/Q96I82) · Ensembl [ENSG00000107821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107821)

## Data

Gene col 2885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2885); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2885]; `tensor/DDL_lfc|DDL_z.npy` [2885]; `embed/gene_vectors.npy` [2885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2885 or target_col == 2885). Every well: [[KAZALD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAZALD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
