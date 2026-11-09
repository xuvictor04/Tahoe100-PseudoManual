---
symbol: "GTF2IRD2"
type: "gene"
col: 12169
ensembl_id: "ENSG00000196275"
name: "GTF2I repeat domain containing 2"
location: "7q11.23"
module: 23
arm: "+"
pooled_cpm: 14.34
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GTF2IRD2

*GTF2I repeat domain containing 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.86× (z +6.4, q 8e-08, up in 17 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +4.6, q 0.001, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.215× (z -16.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IRD2B]] (+0.91, fdr 7e-06), [[LINC01004]] (+0.80, fdr 1e-05), [[MFF-DT]] (+0.77, fdr 1e-05); moves opposite to [[METAP1]] (-0.67, fdr 2e-05), [[WASF3]] (-0.66, fdr 2e-04), [[SDHAF3]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PYROXD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.4 | 8e-08 | 17/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.6 | 0.001 | 20/44 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.0 | 0.012 | 13/32 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.6 | 0.050 | 14/38 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.050 | 15/47 (LoVo, NCI-H1792, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.057 | 12/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.087 | 17/46 (HEC-1-A, NCI-H1792, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.18 | 12/48 (HT-29, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.215×** | -16.4 | 0e+00 | 46/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.308×** | -12.6 | 8e-34 | 42/48 (C32, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.318×** | -12.2 | 5e-32 | 42/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.349×** | -10.2 | 3e-22 | 44/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.387×** | -10.1 | 5e-22 | 41/45 (SNU-423, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.496×** | -7.5 | 7e-12 | 35/48 (H4, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.513×** | -7.1 | 9e-11 | 31/47 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.295×** | -6.8 | 6e-10 | 38/48 (CFPAC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.539×** | -6.3 | 1e-08 | 28/40 (COLO 205, C32, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -6.2 | 4e-08 | 34/48 (RPMI-7951, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.575×** | -5.9 | 2e-07 | 29/46 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.577×** | -5.6 | 8e-07 | 27/47 (H4, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -5.2 | 9e-06 | 26/42 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.611×** | -5.0 | 3e-05 | 25/46 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.634×** | -4.9 | 4e-05 | 23/47 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.724×** | -4.9 | 4e-05 | 22/48 (NCI-H23, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.051 | 17/47 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | **0.733×** | -3.0 | 0.076 | 13/47 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 82.4 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -14.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.214× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0825× (z -16.4) |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.136× (z -13.5) |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0751× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.118× (z -11.1) |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.134× (z -10.4) |
| [[SNU-423 (line)]] | alt | 9.16 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0513× (z -12.0) |
| [[A-427 (line)]] | wt | 4.61 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0627× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.152× (z -9.3) |
| [[LoVo (line)]] | wt | 12.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.12× (z +12.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0465× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0912× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0891× (z -12.2) |
| [[A-172 (line)]] | wt | 18.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.163× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -9.1) |
| [[H4 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.148× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0933× (z -8.8) |
| [[J82 (line)]] | alt | 10.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -9.4) |
| [[KATO III (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 7.77 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0409× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.193× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 8.41 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0937× (z -10.3) |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | +0.91 | +0.93 / +0.84 | both halves | 7e-06 | same gene group; STRING 965 |
| [[LINC01004]] | +0.80 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.77 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.77 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.75 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[LINC02951]] | +0.74 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.73 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.73 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ERCC6L2-AS1]] | +0.72 | +0.68 / +0.33 | both halves | 1e-04 |  |
| [[CCDC30]] | +0.72 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[CASS4]] | +0.72 | +0.67 / +0.43 | both halves | 4e-05 |  |
| [[TBCE-1]] | +0.72 | +0.69 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.67 | -0.69 / -0.46 | both halves | 2e-05 |  |
| [[WASF3]] | -0.66 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[SDHAF3]] | -0.63 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[LRRC20]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYROXD2]] | B | PYROXD2 activity raises GTF2IRD2's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without PYROXD2 | 0.057 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.832). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.5, 15.6); signed map (23.9, -8.8). **Vector** length 96.0, 23.3% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.5 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -10.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.3 | -10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -16.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Lopinavir (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | GTF2I repeat domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,796,151-74,851,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37938, GTF2IRD2A |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

UniProt [Q86UP8](https://www.uniprot.org/uniprotkb/Q86UP8) carries no function annotation.

**Summary**, from NCBI Gene [84163](https://www.ncbi.nlm.nih.gov/gene/84163):

> This gene is one of several closely related genes on chromosome 7 encoding proteins containing helix-loop-helix motifs. These proteins may function as regulators of transcription. The encoded protein is unique in that its C-terminus is derived from CHARLIE8 transposable element sequence. This gene is located in a region of chromosome 7 that is deleted in Williams-Beuren syndrome, and loss of this locus may contribute to the cognitive phenotypes observed in this disease. Alternative splicing …

**Accessions** — [HGNC:30775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30775) · Entrez [84163](https://www.ncbi.nlm.nih.gov/gene/84163) · UniProt [Q86UP8](https://www.uniprot.org/uniprotkb/Q86UP8) · Ensembl [ENSG00000196275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196275)

## Data

Gene col 12169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12169); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12169]; `tensor/DDL_lfc|DDL_z.npy` [12169]; `embed/gene_vectors.npy` [12169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12169 or target_col == 12169). Every well: [[GTF2IRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2IRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
