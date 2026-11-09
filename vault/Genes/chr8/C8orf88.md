---
symbol: "C8orf88"
type: "gene"
col: 14793
ensembl_id: "ENSG00000253250"
name: "chromosome 8 open reading frame 88"
location: "8q21.3"
module: 119
arm: "+"
pooled_cpm: 6.41
n_lines_expressing: 38
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# C8orf88

*chromosome 8 open reading frame 88* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +9.5, q 9e-19, up in 12 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +7.6, q 8e-12, up in 16 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0605×); [[Decitabine (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0691×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0693×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM171B]] (+0.50, fdr 9e-05), [[PLAC1]] (+0.48, fdr 2e-04), [[WASF1]] (+0.48, fdr 5e-05); moves opposite to [[ZNF7]] (-0.51, fdr 3e-05), [[WDR53]] (-0.50, fdr 4e-05), [[DDX28]] (-0.50, fdr 3e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM171B]] → it (grade B ⚠); 2 go from it, the strongest it → [[MLYCD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.5 | 9e-19 | 12/23 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +7.6 | 8e-12 | 16/36 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +7.5 | 1e-11 | 9/16 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.4 | 3e-08 | 11/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.2 | 5e-08 | 3/12 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.2 | 5e-08 | 14/35 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.8 | 6e-07 | 10/28 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.7 | 9e-07 | 8/31 (H4, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +5.3 | 9e-06 | 12/35 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 4e-05 | 2/23 (A498, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 13/35 (A498, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 4e-04 | 13/31 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 4/35 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 3/31 (A549, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 9/35 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.044 | 7/32 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.071 | 2/35 (J82, HOP62) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.073 | 7/30 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14793.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0605×); [[Decitabine (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0691×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.771× | -3.7 | 0.13 | 8/33 (Panc 03.27, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erdafitinib (drug)]] 0.05 µM |  | 0.797× | -3.0 | 0.50 | 1/36 (NCI-H1792) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.91 | 0 | 2 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0605× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 4.29 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0693× (z -8.6) |
| [[A-172 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM171B]] | +0.50 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[PLAC1]] | +0.48 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[WASF1]] | +0.48 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[RADX]] | +0.45 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SNX30]] | +0.45 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CCN3]] | +0.44 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SDCBP]] | +0.44 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[CD302]] | +0.44 | +0.23 / +0.53 | both halves | 5e-04 |  |
| [[LCORL]] | +0.44 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[RTN3]] | +0.44 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[BCAT1]] | +0.43 | +0.41 / +0.36 | both halves | 9e-05 |  |
| [[EFCAB12]] | +0.43 | +0.38 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF7]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[WDR53]] | -0.50 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[DDX28]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MMAA]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[L3MBTL2]] | -0.48 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PHF5A]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[MTG2]] | -0.47 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ZNF41]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[CPSF3]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CNOT11]] | -0.45 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[GTPBP10]] | -0.45 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[CIAPIN1]] | -0.45 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171B]] | B | FAM171B activity raises C8orf88's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 3.00× lower at baseline in the lines without FAM171B | 0.089 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLYCD]] | B | C8orf88 activity lowers MLYCD's level | lines that do not express C8orf88 (12) vs lines expressing it (38) | 1.37× higher at baseline in the lines without C8orf88 | 0.020 | ⚠ within organs, on part of the lines; also absent: TUSC3, MAP9, BVES-AS1; maybe low, not absent |
| [[FAM171B]] | B | C8orf88 activity raises FAM171B's level | lines that do not express C8orf88 (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without C8orf88 | 0.060 | ⚠ within organs, on part of the lines; also absent: TUSC3, MAP9, BVES-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction -0.351). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.8, 5.8); signed map (6.2, 8.0). **Vector** length 43.0, 5.50% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 88 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:90,958,471-90,985,238 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [P0DMB2](https://www.uniprot.org/uniprotkb/P0DMB2) carries no function annotation.

**Summary**, from NCBI Gene [100127983](https://www.ncbi.nlm.nih.gov/gene/100127983):

> Predicted to enable eukaryotic initiation factor 4E binding activity and translation repressor activity. Predicted to be involved in negative regulation of translational initiation. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:44672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44672) · Entrez [100127983](https://www.ncbi.nlm.nih.gov/gene/100127983) · UniProt [P0DMB2](https://www.uniprot.org/uniprotkb/P0DMB2) · Ensembl [ENSG00000253250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253250)

## Data

Gene col 14793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14793); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14793]; `tensor/DDL_lfc|DDL_z.npy` [14793]; `embed/gene_vectors.npy` [14793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14793 or target_col == 14793). Every well: [[C8orf88 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf88.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
