---
symbol: "PXDN"
type: "gene"
col: 5071
ensembl_id: "ENSG00000130508"
name: "peroxidasin"
location: "2p25.3"
module: 66
arm: "+"
pooled_cpm: 65.26
n_lines_expressing: 21
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 11
direction_downstream: 19
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# PXDN

*peroxidasin* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +17.6, q 0e+00, up in 13 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +4.1, q 0.005, up in 3 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.54×, HS-578T 2.87×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.21×, HS-578T 2.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.44×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.494× (z -10.8, q 2e-24, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A1]] (+0.71, fdr 7e-06), [[COL4A2]] (+0.58, fdr 3e-05), [[COL3A1]] (+0.58, fdr 1e-05); moves opposite to [[EPB41L4A-AS1]] (-0.52, fdr 2e-05), [[SNHG6]] (-0.51, fdr 2e-05), [[SNHG32]] (-0.48, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ITGA11]] → it (grade C ⚠); 19 go from it, the strongest it → [[EHD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.54×, HS-578T 2.87×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.21×, HS-578T 2.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.44×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +17.6 | 0e+00 | 13/17 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +17.2 | 0e+00 | 14/16 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +11.7 | 3e-29 | 8/17 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.8 | 2e-04 | 5/15 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.005 | 3/19 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.7 | 0.019 | 9/19 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.028 | 7/19 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.23× | +3.2 | 0.11 | 3/19 (NCI-H1573, A498, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.14 | 1/19 (NCI-H23) | all doses, flat |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.14 | 0/19 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -10.8 | 2e-24 | 15/19 (NCI-H2030, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.640×** | -9.7 | 1e-19 | 16/19 (NCI-H2030, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -6.7 | 3e-09 | 10/19 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -6.6 | 5e-09 | 16/19 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.676×** | -6.0 | 2e-07 | 13/19 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -5.5 | 4e-06 | 13/19 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.3 | 9e-06 | 7/19 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -4.8 | 1e-04 | 13/19 (HOP62, BT-474, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.745×** | -4.5 | 4e-04 | 7/19 (SHP-77, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.769×** | -4.0 | 0.003 | 11/19 (LS 180, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.771×** | -4.0 | 0.004 | 1/18 (NCI-H23) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.9 | 0.005 | 9/19 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.778×** | -3.8 | 0.005 | 5/18 (BT-474, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.779×** | -3.8 | 0.005 | 14/19 (H4, A-172, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.005 | 13/19 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.789×** | -3.6 | 0.010 | 1/19 (SHP-77) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.780×** | -3.5 | 0.014 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 56.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.1) |
| [[H4 (line)]] | wt | 266 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.2) |
| [[LS 180 (line)]] | wt | 64.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.6) |
| [[A498 (line)]] | wt | 337 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -31.3) |
| [[SHP-77 (line)]] | alt | 71.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.292× (z -9.4) |
| [[HS-578T (line)]] | alt | 372 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 38.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 293 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.2) |
| [[SW 900 (line)]] | alt | 79.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.0) |
| [[A-172 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 229 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A1]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 545 |
| [[COL4A2]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 447 |
| [[COL3A1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 488 |
| [[ANPEP]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 | STRING 414 |
| [[FN1]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 | pathway: Extracellular matrix organization; STRING 853 |
| [[ITGA4]] | +0.56 | +0.43 / +0.64 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[ARHGDIB]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[DKK3]] | +0.55 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[FKBP1A]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ACTB]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 | pathway: Extracellular matrix organization; STRING 925 |
| [[PCDHGC3]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ENPP1]] | +0.52 | +0.23 / +0.46 | both halves | 5e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SNHG6]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SNHG32]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZFAS1]] | -0.48 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[YBEY]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[SNHG8]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MRPL32]] | -0.46 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[SNHG7]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SMIM26]] ⚠ | -0.46 | -0.53 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSA2]] | -0.46 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[ADPRM]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[NDUFB9]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SNHG12]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA11]] | C | ITGA11 activity raises PXDN's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 10.86× lower at baseline in the lines without ITGA11 | 0.001 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises PXDN's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 8.74× lower at baseline in the lines without ITGA4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises PXDN's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 7.19× lower at baseline in the lines without PDGFRB | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises PXDN's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.38× lower at baseline in the lines without COL5A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises PXDN's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 5.71× lower at baseline in the lines without MMP2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises PXDN's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 4.23× lower at baseline in the lines without TCF4 | 0.044 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[TENM4]] | C | TENM4 activity raises PXDN's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 6.42× lower at baseline in the lines without TENM4 | 0.054 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises PXDN's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 6.16× lower at baseline in the lines without DKK3 | 0.069 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises PXDN's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 7.72× lower at baseline in the lines without COL1A1 | 0.076 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises PXDN's level | lines that do not express HHIP (33) vs lines expressing it (17) | 3.99× lower at baseline in the lines without HHIP | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |
| [[ITGA8]] | C | ITGA8 activity raises PXDN's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 7.74× lower at baseline in the lines without ITGA8 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD3]] | B | PXDN activity raises EHD3's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.22× lower at baseline in the lines without PXDN | 0.021 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11 |
| [[LTBP1]] | B | PXDN activity raises LTBP1's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without PXDN | 0.062 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11 |
| [[RNF152]] | B | PXDN activity raises RNF152's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.50× lower at baseline in the lines without PXDN | 0.078 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11 |
| [[ITGA11]] | C | PXDN activity raises ITGA11's level | lines that do not express PXDN (29) vs lines expressing it (21) | 6.26× lower at baseline in the lines without PXDN | 0.002 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[PCDHGC3]] | C | PXDN activity raises PCDHGC3's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without PXDN | 0.019 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[ITGA4]] | C | PXDN activity raises ITGA4's level | lines that do not express PXDN (29) vs lines expressing it (21) | 4.21× lower at baseline in the lines without PXDN | 0.022 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[ITGA8]] | C | PXDN activity raises ITGA8's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without PXDN | 0.032 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[MMP2]] | C | PXDN activity raises MMP2's level | lines that do not express PXDN (29) vs lines expressing it (21) | 5.62× lower at baseline in the lines without PXDN | 0.033 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[TENM4]] | C | PXDN activity raises TENM4's level | lines that do not express PXDN (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without PXDN | 0.033 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[PDGFRB]] | C | PXDN activity raises PDGFRB's level | lines that do not express PXDN (29) vs lines expressing it (21) | 4.58× lower at baseline in the lines without PXDN | 0.035 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[FBN1]] | C | PXDN activity raises FBN1's level | lines that do not express PXDN (29) vs lines expressing it (21) | 4.54× lower at baseline in the lines without PXDN | 0.039 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[DKK3]] | C | PXDN activity raises DKK3's level | lines that do not express PXDN (29) vs lines expressing it (21) | 4.15× lower at baseline in the lines without PXDN | 0.053 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.1, 22.5); signed map (24.8, 41.9). **Vector** length 69.2, 21.7% of its response variance represented; |z| ≥ 3 in 529 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Fibronectin matrix formation* (reactome, mean cos +0.53 to 6); *Collagen chain trimerization* (reactome, mean cos +0.50 to 7); *Collagen degradation* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +17.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | -0.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -1.8 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | peroxidasin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:1,631,887-1,744,852 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0230, PRG2, MG50, D2S448, D2S448E, PXN |
| Gene groups (HGNC) | I-set domain containing; Heme peroxidase family |
| Reactome | 7 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; Crosslinking of collagen fibrils; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92626](https://www.uniprot.org/uniprotkb/Q92626) (Peroxidasin homolog):

> Catalyzes the two-electron oxidation of bromide by hydrogen peroxide and generates hypobromite as a reactive intermediate which mediates the formation of sulfilimine cross-links between methionine and hydroxylysine residues within an uncross-linked collagen IV/COL4A1 NC1 hexamer. In turns, directly contributes to the collagen IV network-dependent fibronectin/FN and laminin assembly, which is required for full extracellular matrix (ECM)-mediated signaling. Thus, sulfilimine cross-links are …

**Summary**, from NCBI Gene [7837](https://www.ncbi.nlm.nih.gov/gene/7837):

> This gene encodes a heme-containing peroxidase that is secreted into the extracellular matrix. It is involved in extracellular matrix formation, and may function in the physiological and pathological fibrogenic response in fibrotic kidney. Mutations in this gene cause corneal opacification and other ocular anomalies, and also microphthalmia and anterior segment dysgenesis. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:14966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14966) · Entrez [7837](https://www.ncbi.nlm.nih.gov/gene/7837) · UniProt [Q92626](https://www.uniprot.org/uniprotkb/Q92626) · Ensembl [ENSG00000130508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130508)

## Data

Gene col 5071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5071); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5071]; `tensor/DDL_lfc|DDL_z.npy` [5071]; `embed/gene_vectors.npy` [5071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5071 or target_col == 5071). Every well: [[PXDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
