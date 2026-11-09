---
symbol: "SDHAF2"
type: "gene"
col: 9570
ensembl_id: "ENSG00000167985"
name: "succinate dehydrogenase complex assembly factor 2"
location: "11q12.2"
module: 156
arm: "+"
pooled_cpm: 22.66
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# SDHAF2

*succinate dehydrogenase complex assembly factor 2* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.31× (z +5.3, q 7e-05, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.631× (z -13.6, q 3e-39, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2J2]] (+0.69, fdr 7e-06), [[RPP14]] (+0.69, fdr 7e-06), [[FAF2]] (+0.67, fdr 7e-06); moves opposite to [[H3-3A]] (-0.64, fdr 9e-06), [[TWSG1]] (-0.57, fdr 3e-05), [[SIAE]] (-0.57, fdr 4e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MATN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 7e-05 | 17/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 0.007 | 15/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.015 | 13/47 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.25× | +3.3 | 0.13 | 10/44 (A498, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.21 | 8/47 (HCT15, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.32× | +3.0 | 0.24 | 8/38 (HT-29, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -13.6 | 3e-39 | 38/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.655×** | -8.1 | 1e-13 | 17/35 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.682×** | -8.0 | 3e-13 | 30/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -7.6 | 4e-12 | 26/46 (C32, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.7 | 2e-09 | 25/46 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.732×** | -6.5 | 7e-09 | 27/47 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -6.1 | 9e-08 | 27/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -5.9 | 2e-07 | 20/48 (SW1417, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.776×** | -5.3 | 8e-06 | 19/48 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -5.1 | 2e-05 | 20/48 (SW 900, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.792×** | -4.7 | 2e-04 | 16/44 (NCI-H2030, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.666×** | -4.4 | 4e-04 | 15/45 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -4.1 | 0.002 | 13/47 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.827×** | -3.9 | 0.003 | 12/48 (SW480, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.830×** | -3.7 | 0.007 | 15/32 (SW480, AsPC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.856× | -3.1 | 0.074 | 9/47 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.865× | -3.0 | 0.074 | 10/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.860× | -3.0 | 0.074 | 6/47 (RPMI-7951, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.759×** | -3.0 | 0.074 | 8/48 (A498, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 37.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -12.8) |
| [[H4 (line)]] | wt | 20.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0960× (z -11.0) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A498 (line)]] | wt | 16.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -13.0) |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 22.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -12.7) |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.447× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.0) |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -8.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.0) |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -10.1) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2J2]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RPP14]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[FAF2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TRAPPC3]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TTC4]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[MAU2]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SRP19]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MRFAP1]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[NMT1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RRP7A]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3A]] | -0.64 | -0.57 / -0.65 | both halves | 9e-06 |  |
| [[TWSG1]] | -0.57 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[SIAE]] | -0.57 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CAPZA2]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ANP32A]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PRCP]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[STT3B]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[ERMP1]] | -0.54 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[PEBP1]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SCARB2]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RPS3A]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MATN3]] | B | MATN3 activity lowers SDHAF2's level | lines that do not express MATN3 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without MATN3 | 0.073 | ⚠ within organs, on part of the lines; also absent: LTBP2, DNAAF9, FSTL1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SDHAF2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.4, 2.8); signed map (-4.9, -15.4). **Vector** length 73.4, 12.0% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.0 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.9 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.9 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex assembly factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,430,042-61,446,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20487, SDH5; previously PGL2, C11orf79 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX18](https://www.uniprot.org/uniprotkb/Q9NX18) (Succinate dehydrogenase assembly factor 2, mitochondrial):

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Required for flavinylation (covalent attachment of FAD) of the flavoprotein subunit SDHA of the SDH catalytic dimer.

**Summary**, from NCBI Gene [54949](https://www.ncbi.nlm.nih.gov/gene/54949):

> This gene encodes a mitochondrial assembly factor needed for the flavination of a succinate dehydrogenase complex subunit (SDHA), which is required for activity of the succinate dehydrogenase complex. Mutations in this gene are associated with paraganglioma. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:26034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26034) · Entrez [54949](https://www.ncbi.nlm.nih.gov/gene/54949) · UniProt [Q9NX18](https://www.uniprot.org/uniprotkb/Q9NX18) · Ensembl [ENSG00000167985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167985)

## Data

Gene col 9570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9570); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9570]; `tensor/DDL_lfc|DDL_z.npy` [9570]; `embed/gene_vectors.npy` [9570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9570 or target_col == 9570). Every well: [[SDHAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
