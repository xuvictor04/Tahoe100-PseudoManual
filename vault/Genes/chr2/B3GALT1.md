---
symbol: "B3GALT1"
type: "gene"
col: 10239
ensembl_id: "ENSG00000172318"
name: "beta-1,3-galactosyltransferase 1"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 35.63
n_lines_expressing: 30
n_dd_up: 30
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# B3GALT1

*beta-1,3-galactosyltransferase 1* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 15.8× (z +49.6, q 0e+00, up in 25 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.906× (z -5.8, q 3e-06, down in 4 of 28 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.792× (z -5.7, q 3e-06, down in 11 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH17]] (+0.65, fdr 7e-06), [[NTRK3]] (+0.64, fdr 8e-06), [[TMPRSS15]] (+0.63, fdr 1e-05); moves opposite to [[CEP89]] (-0.48, fdr 3e-05), [[DZANK1]] (-0.45, fdr 9e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RGS7]] → it (grade B ⚠); 5 go from it, the strongest it → [[PPM1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **15.8×** | +49.6 | 0e+00 | 25/27 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **12.8×** | +45.7 | 0e+00 | 26/27 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **12.2×** | +44.9 | 0e+00 | 26/27 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **5.81×** | +43.3 | 0e+00 | 25/28 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.17×** | +40.0 | 0e+00 | 23/28 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **8.41×** | +38.2 | 0e+00 | 26/27 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.92×** | +24.5 | 0e+00 | 24/27 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.99×** | +19.6 | 0e+00 | 25/27 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **7.69×** | +19.1 | 0e+00 | 25/28 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +16.4 | 0e+00 | 21/28 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +12.1 | 6e-32 | 17/27 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +11.4 | 3e-28 | 20/28 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +10.0 | 5e-22 | 15/28 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.70×** | +9.6 | 5e-20 | 19/27 (C32, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.70×** | +9.5 | 5e-20 | 4/23 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.75×** | +9.5 | 8e-20 | 18/26 (LOX-IMVI, A-172, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10239.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -5.8 | 3e-06 | 4/28 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.792×** | -5.7 | 3e-06 | 11/28 (AN3 CA, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -5.6 | 3e-06 | 11/27 (NCI-H1573, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -4.8 | 2e-04 | 15/29 (LOX-IMVI, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.769×** | -4.5 | 6e-04 | 11/27 (SK-MEL-2, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 86.1 | 10 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.84× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 37.5 | 10 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.39× (z +25.1) | — |
| [[C32 (line)]] | wt | 45.8 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 16.6× (z +17.5) | — |
| [[LOX-IMVI (line)]] | wt | 152 | 6 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.20× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.182× (z -9.2) |
| [[A-172 (line)]] | wt | 33.9 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.72× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 18.9 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 21.6× (z +24.5) | — |
| [[HOP62 (line)]] | alt | 10.6 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 42.0× (z +18.7) | — |
| [[Panc 03.27 (line)]] | alt | 9.09 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 33.7× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 14.1× (z +18.1) | — |
| [[LS 180 (line)]] | wt | 11.7 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 15.7× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 6 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.62× (z +17.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0827× (z -14.1) ⚠ toxic; cell-cycle shift, explains ~82% of this change |
| [[SW 900 (line)]] | alt | 86.1 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.09× (z +16.1) | [[Docetaxel (drug)]] 0.05 µM 0.258× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~6% of this change |
| [[AN3 CA (line)]] | alt | 862 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.3) |
| [[HS-578T (line)]] | alt | 11.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 26.2× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 33.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 11.9× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 28.7× (z +15.9) | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 10.5× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 19.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +13.5) | — |
| [[H4 (line)]] | wt | 10.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 43.0× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 22.4× (z +12.7) | — |
| [[SNU-1 (line)]] | wt | 1,186 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0487× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.2) |
| [[A-427 (line)]] | wt | 42.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 105 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0752× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[CHP-212 (line)]] | wt | 290 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 12.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.98× (z +10.0) | — |
| [[A549 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH17]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NTRK3]] | +0.64 | +0.57 / +0.66 | both halves | 8e-06 |  |
| [[TMPRSS15]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[ERC2]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PCDH9]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TMEFF2]] | +0.59 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TMEM108]] | +0.59 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.59 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SYT1]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ELOVL4]] | +0.58 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[PCDH10]] | +0.58 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[FSTL5]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP89]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[DZANK1]] | -0.45 | -0.39 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS7]] | B | RGS7 activity raises B3GALT1's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without RGS7 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers B3GALT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM184A]] | B | FAM184A activity raises B3GALT1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without FAM184A | 0.046 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[EBF2]] | B | EBF2 activity raises B3GALT1's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without EBF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NRXN1]] | B | NRXN1 activity raises B3GALT1's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without NRXN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[NEGR1]] | C | NEGR1 activity raises B3GALT1's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without NEGR1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises B3GALT1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without NCAM2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |
| [[MMP16]] | C | MMP16 activity raises B3GALT1's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without MMP16 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |
| [[ST6GALNAC3]] | C | ST6GALNAC3 activity raises B3GALT1's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 2.55× lower at baseline in the lines without ST6GALNAC3 | 0.050 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent; co-absent with the target |
| [[SOX11]] | C | SOX11 activity raises B3GALT1's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.04× lower at baseline in the lines without SOX11 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1L]] | B | B3GALT1 activity raises PPM1L's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without B3GALT1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent |
| [[TMEM108]] | B | B3GALT1 activity raises TMEM108's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without B3GALT1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent |
| [[CD274]] | B | B3GALT1 activity strengthens CD274's drug response | lines that do not express B3GALT1 (12) vs lines expressing it (18) | the lines without B3GALT1 respond 0.48× as strongly (z diff +2.36); strongest at Homoharringtonine 5 µM: 1.19x vs 3.65x (z diff +5.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NEGR1]] | C | B3GALT1 activity raises NEGR1's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 4.01× lower at baseline in the lines without B3GALT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent; co-absent with the target |
| [[MMP16]] | C | B3GALT1 activity raises MMP16's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 5.73× lower at baseline in the lines without B3GALT1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.4, 29.5); signed map (37.9, 30.0). **Vector** length 75.5, 17.1% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +43.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +24.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +40.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.1 | +9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +38.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +19.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +4.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | +2.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-galactosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:167,293,001-167,874,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta3Gal-T1 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 3 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Z6](https://www.uniprot.org/uniprotkb/Q9Y5Z6) (Beta-1,3-galactosyltransferase 1):

> Beta-1,3-galactosyltransferase that transfers galactose from UDP-alpha-D-galactose to substrates with a terminal beta-N-acetylglucosamine (beta-GlcNAc) residue. Involved in the biosynthesis of the carbohydrate moieties of glycolipids and glycoproteins. Inactive towards substrates with terminal alpha-N-acetylglucosamine (alpha-GlcNAc) or alpha-N-acetylgalactosamine (alpha-GalNAc) residues.

**Summary**, from NCBI Gene [8708](https://www.ncbi.nlm.nih.gov/gene/8708):

> This gene is a member of the beta-1,3-galactosyltransferase (beta3GalT) gene family. This family encodes type II membrane-bound glycoproteins with diverse enzymatic functions using different donor substrates (UDP-galactose and UDP-N-acetylglucosamine) and different acceptor sugars (N-acetylglucosamine, galactose, N-acetylgalactosamine). The beta3GalT genes are distantly related to the Drosophila Brainiac gene and have the protein coding sequence contained in a single exon. The beta3GalT …

**Accessions** — [HGNC:916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:916) · Entrez [8708](https://www.ncbi.nlm.nih.gov/gene/8708) · UniProt [Q9Y5Z6](https://www.uniprot.org/uniprotkb/Q9Y5Z6) · Ensembl [ENSG00000172318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172318)

## Data

Gene col 10239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10239); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10239]; `tensor/DDL_lfc|DDL_z.npy` [10239]; `embed/gene_vectors.npy` [10239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10239 or target_col == 10239). Every well: [[B3GALT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
