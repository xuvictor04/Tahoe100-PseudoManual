---
symbol: "SUN3"
type: "gene"
col: 8999
ensembl_id: "ENSG00000164744"
name: "Sad1 and UNC84 domain containing 3"
location: "7p12.3"
module: 125
arm: "+"
pooled_cpm: 5.52
n_lines_expressing: 19
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# SUN3

*Sad1 and UNC84 domain containing 3* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.78× (z +14.1, q 3e-42, up in 6 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0262×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.240×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.266×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP0P2]] (+0.51, fdr 4e-05), [[HRK]] (+0.49, fdr 3e-05), [[ANK2]] (+0.47, fdr 5e-05); moves opposite to [[NPAT]] (-0.47, fdr 3e-05), [[C8orf58]] (-0.42, fdr 3e-04), [[CASP8AP2]] (-0.41, fdr 9e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC25A48]] → it (grade B ⚠); 4 go from it, the strongest it → [[ARHGAP40]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.78×** | +14.1 | 3e-42 | 6/11 (HEC-1-A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.10×** | +11.7 | 3e-29 | 3/6 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +8.7 | 4e-16 | 4/7 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.03×** | +8.3 | 2e-14 | 12/14 (A-172, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +7.1 | 1e-10 | 2/5 (NCI-H2030, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +6.9 | 4e-10 | 5/12 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +6.5 | 9e-09 | 11/16 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +5.9 | 2e-07 | 5/12 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.9 | 3e-07 | 2/9 (RKO, NCI-H2030) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.3 | 8e-06 | 10/13 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.1 | 2e-05 | 3/9 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +4.1 | 0.002 | 2/4 (NCI-H2030, AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +3.7 | 0.009 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.010 | 4/16 (NCI-H2030, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.011 | 5/14 (HS-578T, NCI-H2030, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.011 | 7/16 (A-172, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.032 | 3/12 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.038 | 1/15 (HS-578T) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.039 | 8/16 (RKO, HS-578T, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.085 | 2/12 (NCI-H661, RKO) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +2.9 | 0.086 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8999.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0262×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.240×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.266×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.862× | -4.0 | 0.035 | 6/17 (HCT15, HEC-1-A, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.637× | -3.4 | 0.21 | 1/16 (RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 36.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0262× (z -18.7) |
| [[A-427 (line)]] | wt | 66.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.793 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.688 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP0P2]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HRK]] | +0.49 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ANK2]] | +0.47 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[BEX2]] | +0.47 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[LY96]] | +0.46 | +0.24 / +0.60 | both halves | 5e-04 |  |
| [[CNST]] | +0.45 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[TOM1L1]] | +0.45 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[CDA]] | +0.45 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[PAQR3]] | +0.45 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[ADTRP]] | +0.45 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[MYO18B]] | +0.44 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[UPP1]] | +0.44 | +0.42 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAT]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[C8orf58]] | -0.42 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[CASP8AP2]] | -0.41 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[RAVER1]] | -0.41 | -0.24 / -0.47 | both halves | 5e-04 |  |
| [[ATRIP]] | -0.41 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[RANBP3]] | -0.41 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[FANCM]] | -0.41 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ZZEF1]] | -0.40 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[TEDC1]] | -0.40 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[USP1]] | -0.40 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[UBR3]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[KIF22]] | -0.39 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A48]] | B | SLC25A48 activity lowers SUN3's level | lines that do not express SLC25A48 (8) vs lines expressing it (42) | 2.39× higher at baseline in the lines without SLC25A48 | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP40]] | B | SUN3 activity raises ARHGAP40's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without SUN3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent |
| [[UPP1]] | B | SUN3 activity raises UPP1's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 2.09× lower at baseline in the lines without SUN3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent |
| [[LINC01322]] | C | SUN3 activity raises LINC01322's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without SUN3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent; co-absent with the target |
| [[LINC01610]] | C | SUN3 activity raises LINC01610's level | lines that do not express SUN3 (31) vs lines expressing it (19) | 1.11× lower at baseline in the lines without SUN3 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000250038, SFTA1P, PKD1L1-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 23.0); signed map (35.9, 23.4). **Vector** length 31.0, 6.56% of its response variance represented; |z| ≥ 3 in 331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +14.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | +0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -4.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.6 | -1.6 |
|  | [[Quinestrol (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.6 | -0.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.5 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | Sad1 and UNC84 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:47,987,148-48,029,119 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33329; previously SUNC1 |
| Gene groups (HGNC) | SUN family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAQ9](https://www.uniprot.org/uniprotkb/Q8TAQ9) (SUN domain-containing protein 3):

> As a probable component of the LINC (LInker of Nucleoskeleton and Cytoskeleton) complex, involved in the connection between the nuclear lamina and the cytoskeleton. The nucleocytoplasmic interactions established by the LINC complex play an important role in the transmission of mechanical forces across the nuclear envelope and in nuclear movement and positioning. May be involved in nuclear remodeling during sperm head formation in spermatogenesis. A probable SUN3:SYNE1 LINC complex may tether …

**Summary**, from NCBI Gene [256979](https://www.ncbi.nlm.nih.gov/gene/256979):

> Predicted to enable protein-membrane adaptor activity. Predicted to be located in nuclear inner membrane. Predicted to be part of meiotic nuclear membrane microtubule tethering complex. Predicted to be active in nuclear envelope. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:22429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22429) · Entrez [256979](https://www.ncbi.nlm.nih.gov/gene/256979) · UniProt [Q8TAQ9](https://www.uniprot.org/uniprotkb/Q8TAQ9) · Ensembl [ENSG00000164744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164744)

## Data

Gene col 8999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8999); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8999]; `tensor/DDL_lfc|DDL_z.npy` [8999]; `embed/gene_vectors.npy` [8999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8999 or target_col == 8999). Every well: [[SUN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
