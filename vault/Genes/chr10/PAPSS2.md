---
symbol: "PAPSS2"
type: "gene"
col: 12641
ensembl_id: "ENSG00000198682"
name: "3'-phosphoadenosine 5'-phosphosulfate synthase 2"
location: "10q23.2-q23.31"
module: 56
arm: "+"
pooled_cpm: 72.29
n_lines_expressing: 35
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PAPSS2

*3'-phosphoadenosine 5'-phosphosulfate synthase 2* — 10q23.2-q23.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.51×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.290× (z -25.3, q 0e+00, down in 33 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CA12]] (+0.55, fdr 1e-05), [[ADAMTS2]] (+0.53, fdr 1e-05), [[P3H2]] (+0.52, fdr 2e-05); moves opposite to [[VPS8]] (-0.46, fdr 3e-05), [[PARD3]] (-0.41, fdr 1e-04), [[AGO2]] (-0.40, fdr 1e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CA12]] → it (grade B ⚠); 8 go from it, the strongest it → [[B4GALT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.51×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.14× | +3.4 | 0.21 | 13/35 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.21 | 13/33 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.3 | 0.21 | 13/33 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.32 | 3/33 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.290×** | -25.3 | 0e+00 | 33/33 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.345×** | -21.7 | 0e+00 | 31/33 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.395×** | -19.0 | 0e+00 | 31/33 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -16.6 | 0e+00 | 31/33 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -15.4 | 0e+00 | 24/33 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -15.3 | 0e+00 | 31/33 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.509×** | -13.2 | 4e-38 | 26/33 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.575×** | -11.3 | 1e-27 | 25/33 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -11.0 | 3e-26 | 24/33 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -10.9 | 7e-26 | 27/33 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.600×** | -10.4 | 1e-23 | 26/33 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -10.2 | 1e-22 | 26/32 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.644×** | -9.0 | 1e-17 | 25/33 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -8.8 | 4e-17 | 27/33 (LoVo, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -8.6 | 2e-16 | 22/33 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -8.6 | 3e-16 | 23/33 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.663×** | -8.4 | 2e-15 | 21/33 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 299 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0916× (z -25.4) |
| [[AsPC-1 (line)]] | alt | 74.2 | 0 | 13 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -17.1) |
| [[RPMI-7951 (line)]] | alt | 189 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -16.9) |
| [[HS-578T (line)]] | alt | 92.6 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -20.9) |
| [[HT-29 (line)]] | alt | 156 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0691× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -19.7) |
| [[A498 (line)]] | wt | 260 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -20.6) |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -15.8) |
| [[LoVo (line)]] | wt | 50.1 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -16.2) |
| [[HOP62 (line)]] | alt | 129 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -19.8) |
| [[A-172 (line)]] | wt | 112 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -19.5) |
| [[A549 (line)]] | wt | 58.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -14.7) |
| [[LS 180 (line)]] | wt | 53.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -13.9) |
| [[SNU-423 (line)]] | alt | 61.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -13.8) |
| [[J82 (line)]] | alt | 169 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -20.2) |
| [[A-427 (line)]] | wt | 29.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.1) |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0365× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 69.9 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.8) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 52.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -9.2) |
| [[SW 1088 (line)]] | alt | 158 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 68.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -10.8) |
| [[HCT15 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.217× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 35.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.350× (z -8.6) |
| [[AN3 CA (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA12]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ADAMTS2]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[P3H2]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LOX]] | +0.51 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PDXDC2P]] | +0.50 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PDXDC1]] | +0.50 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[DZIP1L]] | +0.49 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[SLC10A7]] | +0.47 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[GPR173]] | +0.47 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TRIQK]] | +0.46 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[PDXDC2P-NPIPB14P]] | +0.46 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LPAR1]] | +0.46 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS8]] | -0.46 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PARD3]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[AGO2]] | -0.40 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[TOR4A]] | -0.40 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[RHBDD1]] | -0.38 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[HLCS]] | -0.38 | -0.44 / -0.31 | both halves | 2e-04 | pathway: Diseases of metabolism |
| [[RRP1]] | -0.38 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[VHL]] | -0.37 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[PRMT3]] | -0.37 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[DYNLT2B]] | -0.37 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[TRIM66]] | -0.37 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[RASGRF2]] | -0.37 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA12]] | B | CA12 activity raises PAPSS2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without CA12 | 0.003 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[PDGFRB]] | B | PDGFRB activity raises PAPSS2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.67× lower at baseline in the lines without PDGFRB | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SLC8A1]] | B | SLC8A1 activity raises PAPSS2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without SLC8A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[RARB]] | B | RARB activity raises PAPSS2's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without RARB | 0.024 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[NID2]] | B | NID2 activity raises PAPSS2's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without NID2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[ABI3BP]] | B | ABI3BP activity raises PAPSS2's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.67× lower at baseline in the lines without ABI3BP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[NID2]] | B | NID2 activity strengthens PAPSS2's drug response | lines that do not express NID2 (20) vs lines expressing it (13) | the lines without NID2 respond 0.72× as strongly (z diff +1.62); strongest at Digitoxin 5 µM: 0.43x vs 0.32x (z diff +2.9) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; target measured in part of the lines; artifact flags |
| [[CA12]] | B | CA12 activity strengthens PAPSS2's drug response | lines that do not express CA12 (18) vs lines expressing it (15) | the lines without CA12 respond 0.64× as strongly (z diff +2.19); strongest at Panobinostat 0.5 µM: 0.40x vs 0.18x (z diff +3.4) | 0.036 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; target measured in part of the lines; artifact flags |
| [[PTGFR]] | B | PTGFR activity raises PAPSS2's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without PTGFR | 0.074 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALT1]] | B | PAPSS2 activity raises B4GALT1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without PAPSS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[ADD3]] | B | PAPSS2 activity raises ADD3's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without PAPSS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[SLC8A1]] | B | PAPSS2 activity raises SLC8A1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 3.24× lower at baseline in the lines without PAPSS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[PTGFR]] | B | PAPSS2 activity raises PTGFR's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 2.57× lower at baseline in the lines without PAPSS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[SAR1A]] | B | PAPSS2 activity raises SAR1A's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without PAPSS2 | 0.071 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[ADD3-AS1]] | B | PAPSS2 activity raises ADD3-AS1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without PAPSS2 | 0.072 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[RAB2A]] | B | PAPSS2 activity strengthens RAB2A's drug response | lines that do not express PAPSS2 (15) vs lines expressing it (34) | the lines without PAPSS2 respond 0.74× as strongly (z diff +1.22); strongest at Homoharringtonine 5 µM: 0.77x vs 0.57x (z diff +3.4) | 0.074 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E; target measured in part of the lines; artifact flags |
| [[LPAR1]] | C | PAPSS2 activity raises LPAR1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 5.02× lower at baseline in the lines without PAPSS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E; co-absent with the target |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.409). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.0, 20.6); signed map (27.4, 46.2). **Vector** length 90.9, 23.5% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -10.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.9 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -8.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | 3'-phosphoadenosine 5'-phosphosulfate synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2-q23.31 — chr10:87,659,613-87,747,705 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPSK2 |
| Hallmark sets | XENOBIOTIC_METABOLISM, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: Metabolism of ingested H2SeO4 and H2SeO3 into H2Se; Transport and metabolism of PAPS; Diseases associated with glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95340](https://www.uniprot.org/uniprotkb/O95340) (Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 2):

> Bifunctional enzyme with both ATP sulfurylase and APS kinase activity, which mediates two steps in the sulfate activation pathway. The first step is the transfer of a sulfate group to ATP to yield adenosine 5'-phosphosulfate (APS), and the second step is the transfer of a phosphate group from ATP to APS yielding 3'-phosphoadenylylsulfate/PAPS, the activated sulfate donor used by sulfotransferases. In mammals, PAPS is the sole source of sulfate while APS appears to only be an intermediate in the …

**Summary**, from NCBI Gene [9060](https://www.ncbi.nlm.nih.gov/gene/9060):

> Sulfation is a common modification of endogenous (lipids, proteins, and carbohydrates) and exogenous (xenobiotics and drugs) compounds. In mammals, the sulfate source is 3'-phosphoadenosine 5'-phosphosulfate (PAPS), created from ATP and inorganic sulfate. Two different tissue isoforms encoded by different genes synthesize PAPS. This gene encodes one of the two PAPS synthetases. Defects in this gene cause the Pakistani type of spondyloepimetaphyseal dysplasia. Two alternatively spliced …

**Accessions** — [HGNC:8604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8604) · Entrez [9060](https://www.ncbi.nlm.nih.gov/gene/9060) · UniProt [O95340](https://www.uniprot.org/uniprotkb/O95340) · Ensembl [ENSG00000198682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198682)

## Data

Gene col 12641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12641); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12641]; `tensor/DDL_lfc|DDL_z.npy` [12641]; `embed/gene_vectors.npy` [12641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12641 or target_col == 12641). Every well: [[PAPSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
