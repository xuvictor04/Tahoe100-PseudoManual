---
symbol: "TRDMT1"
type: "gene"
col: 2863
ensembl_id: "ENSG00000107614"
name: "tRNA aspartic acid methyltransferase 1"
location: "10p13"
module: 3
arm: "-"
pooled_cpm: 11.02
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRDMT1

*tRNA aspartic acid methyltransferase 1* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +8.9, q 4e-16, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.582× (z -6.7, q 1e-08, down in 22 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.640× (z -5.7, q 3e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YWHAE]] (+0.61, fdr 1e-05), [[CBX5]] (+0.53, fdr 3e-05), [[CDK6]] (+0.53, fdr 4e-05); moves opposite to [[IL17RA]] (-0.53, fdr 3e-05), [[SLC25A29]] (-0.52, fdr 1e-05), [[C1orf122]] (-0.52, fdr 2e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CUBN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +8.9 | 4e-16 | 36/48 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +8.3 | 2e-14 | 36/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +8.3 | 2e-14 | 31/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +6.7 | 3e-09 | 23/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +5.7 | 2e-06 | 25/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +5.0 | 6e-05 | 21/47 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.001 | 15/48 (HS-578T, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.009 | 13/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.013 | 13/47 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.037 | 15/44 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.3 | 0.043 | 11/34 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Folic acid (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.065 | 3/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.1 | 0.078 | 5/21 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +3.0 | 0.095 | 12/29 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -6.7 | 1e-08 | 22/39 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -5.7 | 3e-06 | 22/47 (A-427, J82, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -5.4 | 1e-05 | 21/44 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.669×** | -5.1 | 4e-05 | 20/46 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -5.0 | 8e-05 | 21/47 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.692×** | -4.7 | 2e-04 | 18/47 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -4.6 | 4e-04 | 19/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -4.0 | 0.004 | 17/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.764×** | -3.3 | 0.057 | 11/45 (NCI-H460, COLO 205, …) | top dose only | composition shift |
| [[Terfenadine (drug)]] 5 µM |  | 0.834× | -3.2 | 0.091 | 10/48 (A498, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.789× | -3.0 | 0.12 | 11/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.270× (z -9.3) |
| [[C32 (line)]] | wt | 11.4 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0776× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -8.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 8.55 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -9.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0718× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 7.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -8.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 5.30 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0900× (z -8.7) |
| [[SHP-77 (line)]] | alt | 9.16 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.113× (z -9.1) |
| [[SW1417 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CBX5]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[CDK6]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[LCP1]] | +0.51 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[CUBN]] | +0.51 | +0.59 / +0.57 | both halves | 1e-05 | ⚠ same locus (7.5 kb, same strand: neighbours can correlate without regulation) |
| [[CDH2]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[LINC01776]] | +0.51 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[LINC02930]] | +0.50 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[SRP9]] | +0.50 | +0.37 / +0.33 | both halves | 1e-04 |  |
| [[VIM-AS1]] | +0.50 | +0.41 / +0.57 | both halves | 4e-05 | ⚠ same locus (12.2 kb, same strand: neighbours can correlate without regulation) |
| [[IL31RA]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[MYLK]] | +0.49 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[GLIPR1]] | +0.49 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[TMEM185B]] | +0.49 | +0.54 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SLC25A29]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[C1orf122]] | -0.52 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[COX14]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[ZNF823]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[CSNK1G2]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CDC37L1]] | -0.50 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[MRPS36]] ⚠ | -0.49 | -0.29 / -0.47 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | -0.48 | -0.16 / -0.51 | ⚠ one half (not replicated) | 0.001 |  |
| [[SOS1]] | -0.48 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[RAB11FIP3]] | -0.48 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ABHD18]] | -0.48 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[A1BG-AS1]] | -0.48 | -0.29 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUBN]] | B | CUBN activity raises TRDMT1's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without CUBN | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises TRDMT1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.9, -5.1); signed map (22.5, 18.9). **Vector** length 62.6, 9.33% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA aspartic acid methyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:17,137,336-17,202,054 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNMT1; previously DNMT2 |
| Gene groups (HGNC) | 7BS C5-cytosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O14717](https://www.uniprot.org/uniprotkb/O14717) (tRNA):

> Specifically methylates cytosine 38 in the anticodon loop of tRNA(Asp). Has higher activity on tRNA(Asp) modified with queuosine at position 34.

**Summary**, from NCBI Gene [1787](https://www.ncbi.nlm.nih.gov/gene/1787):

> This gene encodes a protein responsible for the methylation of aspartic acid transfer RNA, specifically at the cytosine-38 residue in the anticodon loop. This enzyme also possesses residual DNA-(cytosine-C5) methyltransferase activity. While similar in sequence and structure to DNA cytosine methyltransferases, this gene is distinct and highly conserved in its function among taxa. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:2977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2977) · Entrez [1787](https://www.ncbi.nlm.nih.gov/gene/1787) · UniProt [O14717](https://www.uniprot.org/uniprotkb/O14717) · Ensembl [ENSG00000107614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107614)

## Data

Gene col 2863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2863); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2863]; `tensor/DDL_lfc|DDL_z.npy` [2863]; `embed/gene_vectors.npy` [2863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2863 or target_col == 2863). Every well: [[TRDMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRDMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
