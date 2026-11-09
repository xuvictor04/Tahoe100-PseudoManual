---
symbol: "AGTR1"
type: "gene"
col: 6942
ensembl_id: "ENSG00000144891"
name: "angiotensin II receptor type 1"
location: "3q24"
module: 13
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 13
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# AGTR1

*angiotensin II receptor type 1* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.64× (z +12.1, q 5e-31, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +11.6, q 7e-29, up in 0 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LOX-IMVI 0.0573×, HOP62 0.115×, CFPAC-1 0.139×, hTERT-HPNE 0.183×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.0997×, LOX-IMVI 0.113×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0982×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCA1]] (+0.64, fdr 1e-05), [[TREM1]] (+0.57, fdr 3e-05), [[ADAM28]] (+0.55, fdr 2e-04); moves opposite to [[TBC1D5]] (-0.47, fdr 5e-05), [[RCC2]] (-0.44, fdr 1e-04), [[LINC02099]] (-0.44, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GLIS3]] → it (grade B ⚠); 8 go from it, the strongest it → [[MEIS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.64×** | +12.1 | 5e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +11.6 | 7e-29 | 0/9 | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.73×** | +11.3 | 2e-27 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +9.6 | 8e-20 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +7.0 | 2e-10 | 8/10 (NCI-H1792, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.38×** | +6.3 | 3e-08 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +5.9 | 3e-07 | 5/9 (hTERT-HPNE, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.81×** | +5.4 | 6e-06 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.04×** | +5.2 | 2e-05 | 4/10 (hTERT-HPNE, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.0 | 3e-05 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +4.6 | 2e-04 | 8/10 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.3 | 7e-04 | 0/7 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +4.3 | 7e-04 | 0/9 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +4.3 | 7e-04 | 5/10 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.97×** | +4.1 | 0.001 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.9 | 0.003 | 0/9 | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.13×** | +3.9 | 0.003 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 3/10 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.011 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.92×** | +3.4 | 0.019 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.021 | 6/11 (LOX-IMVI, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +3.1 | 0.039 | 4/11 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.043 | 0/9 | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.044 | 1/9 (A-427) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6942.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LOX-IMVI 0.0573×, HOP62 0.115×, CFPAC-1 0.139×, hTERT-HPNE 0.183×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.0997×, LOX-IMVI 0.113×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.593× | -3.6 | 0.16 | 0/11 | inconsistent across doses |  |
| [[Delamanid (drug)]] 0.05 µM |  | 0.638× | -3.3 | 0.16 | 0/11 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.617× | -3.3 | 0.16 | 0/11 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.621× | -3.3 | 0.16 | 2/11 (NCI-H1792, CHP-212) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.656× | -3.1 | 0.20 | 3/11 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 52.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0982× (z -15.2) |
| [[HOP62 (line)]] | alt | 9.32 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0338× (z -14.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0573× (z -12.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 7.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0345× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.275 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCA1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[TREM1]] | +0.57 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ADAM28]] | +0.55 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[NDNF]] | +0.54 | +0.31 / +0.62 | both halves | 2e-04 |  |
| [[CD38]] | +0.51 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[THEMIS2]] | +0.51 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[CP]] | +0.50 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[ADAMTS9-AS2]] | +0.50 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[CA12]] | +0.49 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[LINC00540]] | +0.48 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[SLC15A1]] | +0.48 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[ITIH2]] | +0.48 | +0.61 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RCC2]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[LINC02099]] | -0.44 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[VSIG10]] | -0.42 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[MACROD1]] | -0.41 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[TNRC18]] | -0.41 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[SEPHS1]] | -0.41 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[SLC12A2-DT]] | -0.40 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[ZNF362]] | -0.40 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[GALNT7]] | -0.39 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[FBXL17]] | -0.39 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PAXIP1]] | -0.38 | -0.36 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[GSE1]] | -0.38 | -0.33 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLIS3]] | B | GLIS3 activity raises AGTR1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.99× lower at baseline in the lines without GLIS3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[TNS1]] | C | TNS1 activity raises AGTR1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without TNS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786; co-absent with the target |
| [[CA12]] | C | CA12 activity raises AGTR1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without CA12 | 0.015 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises AGTR1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without PEX5L | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises AGTR1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.41× lower at baseline in the lines without PAPPA | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[CD38]] | C | CD38 activity raises AGTR1's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.62× lower at baseline in the lines without CD38 | 0.056 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises AGTR1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without OR9Q1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[LOX]] | C | LOX activity raises AGTR1's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.31× lower at baseline in the lines without LOX | 0.092 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[NDNF]] | C | NDNF activity raises AGTR1's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without NDNF | 0.093 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS1]] | B | AGTR1 activity raises MEIS1's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.41× lower at baseline in the lines without AGTR1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN |
| [[TNS1]] | C | AGTR1 activity raises TNS1's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 6.08× lower at baseline in the lines without AGTR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[NDNF]] | C | AGTR1 activity raises NDNF's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.31× lower at baseline in the lines without AGTR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[TNIP3]] | C | AGTR1 activity raises TNIP3's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.38× lower at baseline in the lines without AGTR1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[CA12]] | C | AGTR1 activity raises CA12's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 5.20× lower at baseline in the lines without AGTR1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[LOX]] | C | AGTR1 activity raises LOX's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 4.43× lower at baseline in the lines without AGTR1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[PDLIM4]] | C | AGTR1 activity raises PDLIM4's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without AGTR1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |
| [[IGFBP1]] | C | AGTR1 activity raises IGFBP1's level | lines that do not express AGTR1 (37) vs lines expressing it (13) | 3.00× lower at baseline in the lines without AGTR1 | 0.0999 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, APBB1IP, CARMN; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.334). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.4, 10.5); signed map (19.9, 38.3). **Vector** length 33.4, 9.71% of its response variance represented; |z| ≥ 3 in 277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.4 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.2 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | angiotensin II receptor type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:148,697,784-148,743,008 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AT1, AT2R1, AGTR1A, AT2R1A, HAT1R, AG2S, AT2R1B, AT1B; previously AGTR1B |
| Gene groups (HGNC) | Angiotensin receptors |
| Reactome | 10 pathways, smallest: Peptide ligand-binding receptors; Cargo recognition for clathrin-mediated endocytosis; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P30556](https://www.uniprot.org/uniprotkb/P30556) (Type-1 angiotensin II receptor):

> Receptor for angiotensin II, a vasoconstricting peptide, which acts as a key regulator of blood pressure and sodium retention by the kidney. The activated receptor in turn couples to G-alpha proteins G(q) (GNAQ, GNA11, GNA14 or GNA15) and thus activates phospholipase C and increases the cytosolic Ca(2+) concentrations, which in turn triggers cellular responses such as stimulation of protein kinase C.; (Microbial infection) During SARS coronavirus-2/SARS-CoV-2 infection, it is able to recognize …

**Summary**, from NCBI Gene [185](https://www.ncbi.nlm.nih.gov/gene/185):

> Angiotensin II is a potent vasopressor hormone and a primary regulator of aldosterone secretion. It is an important effector controlling blood pressure and volume in the cardiovascular system. It acts through at least two types of receptors. This gene encodes the type 1 receptor which is thought to mediate the major cardiovascular effects of angiotensin II. This gene may play a role in the generation of reperfusion arrhythmias following restoration of blood flow to ischemic or infarcted …

**Accessions** — [HGNC:336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:336) · Entrez [185](https://www.ncbi.nlm.nih.gov/gene/185) · UniProt [P30556](https://www.uniprot.org/uniprotkb/P30556) · Ensembl [ENSG00000144891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144891)

## Data

Gene col 6942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6942); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6942]; `tensor/DDL_lfc|DDL_z.npy` [6942]; `embed/gene_vectors.npy` [6942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6942 or target_col == 6942). Every well: [[AGTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
