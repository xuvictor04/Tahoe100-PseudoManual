---
symbol: "KCTD6"
type: "gene"
col: 9633
ensembl_id: "ENSG00000168301"
name: "potassium channel tetramerization domain containing 6"
location: "3p14.3"
module: 65
arm: "+"
pooled_cpm: 4.9
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# KCTD6

*potassium channel tetramerization domain containing 6* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.25× (z +9.8, q 7e-20, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.619× (z -5.8, q 3e-06, down in 22 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0812×, SW1417 0.0860×, HS-578T 0.0735×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0521×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 5 µM in 1 line (NCI-H460 0.274×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0768×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.76, fdr 7e-06), [[ALG9]] (+0.71, fdr 7e-06), [[FAM168A]] (+0.70, fdr 1e-05); moves opposite to [[DGKH]] (-0.65, fdr 3e-05), [[LINC00571]] (-0.63, fdr 1e-05), [[GTF2H1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRP12]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +9.8 | 7e-20 | 31/46 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.96×** | +8.1 | 2e-13 | 24/47 (SW1417, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +7.1 | 2e-10 | 22/44 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.2 | 2e-05 | 9/47 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +4.8 | 2e-04 | 11/38 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +4.7 | 3e-04 | 10/44 (SHP-77, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.6 | 4e-04 | 10/29 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.004 | 9/45 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.007 | 10/45 (PANC-1, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.010 | 8/45 (SNU-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.015 | 8/46 (HS-578T, CHP-212, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.015 | 12/47 (H4, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +3.4 | 0.029 | 7/39 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.2 | 0.056 | 0/13 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.21×** | +3.2 | 0.058 | 8/40 (A549, A498, …) | top dose only | composition shift |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.084 | 1/47 (HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0812×, SW1417 0.0860×, HS-578T 0.0735×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0521×; ⚠ toxic; transcription drop); [[Cepharanthine (drug)]] 5 µM in 1 line (NCI-H460 0.274×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (NCI-H23 0.0768×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -5.8 | 3e-06 | 22/44 (HS-578T, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -4.9 | 3e-04 | 17/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.821× | -3.4 | 0.13 | 4/45 (SHP-77, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.763× | -3.3 | 0.14 | 12/24 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.782× | -3.0 | 0.30 | 3/47 (NCI-H2030, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0735× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0812× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 4.21 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0768× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 8.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.17 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.274× (z -10.5) |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 7.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0860× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[ALG9]] | +0.71 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FAM168A]] | +0.70 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[HACE1]] | +0.68 | +0.64 / +0.50 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[VDAC3]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[HSF2]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[KIF3A]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ORC4]] | +0.66 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[FAM234B]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[UNC119]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ATG4C]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.65 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.63 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[GTF2H1]] | -0.63 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.58 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[AVEN]] | -0.58 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[MSRA]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ACAD9]] | -0.57 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[WSB2]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 | pathway: Neddylation |
| [[LINC01004]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ANKLE2]] | -0.57 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZHX2]] | -0.56 | -0.53 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP12]] | B | LRP12 activity raises KCTD6's level | lines that do not express LRP12 (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without LRP12 | 0.085 | ⚠ within organs, on part of the lines; also absent: CFAP54, RNF217, RNF217-AS1 |
| [[HACE1]] | C | HACE1 activity raises KCTD6's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without HACE1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | KCTD6's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | KCTD6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.409 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (2.9, -9.6); signed map (-32.2, -7.4). **Vector** length 52.3, 6.69% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +2.1 | +9.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +1.7 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +1.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.4 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,492,096-58,502,360 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC27385, KCASH3 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Reactome | 9 pathways, smallest: RUNX1 regulates estrogen receptor mediated transcription; Estrogen-dependent gene expression; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC69](https://www.uniprot.org/uniprotkb/Q8NC69) (BTB/POZ domain-containing protein KCTD6):

> Probable substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex mediating the ubiquitination and subsequent proteasomal degradation of target proteins. Promotes the ubiquitination of HDAC1; the function seems to depend on KCTD11:KCTD6 oligomerization. Can function as antagonist of the Hedgehog pathway by affecting the nuclear transfer of transcription factor GLI1; the function probably occurs via HDAC1 down-regulation, keeping GLI1 acetylated and inactive. …

**Summary**, from NCBI Gene [200845](https://www.ncbi.nlm.nih.gov/gene/200845):

> Enables ankyrin binding activity; cullin family protein binding activity; and identical protein binding activity. Involved in negative regulation of smoothened signaling pathway and ubiquitin-dependent protein catabolic process. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22235) · Entrez [200845](https://www.ncbi.nlm.nih.gov/gene/200845) · UniProt [Q8NC69](https://www.uniprot.org/uniprotkb/Q8NC69) · Ensembl [ENSG00000168301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168301)

## Data

Gene col 9633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9633); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9633]; `tensor/DDL_lfc|DDL_z.npy` [9633]; `embed/gene_vectors.npy` [9633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9633 or target_col == 9633). Every well: [[KCTD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
