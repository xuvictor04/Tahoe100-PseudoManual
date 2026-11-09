---
symbol: "GJA3"
type: "gene"
col: 4291
ensembl_id: "ENSG00000121743"
name: "gap junction protein alpha 3"
location: "13q12.11"
module: 132
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 33
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# GJA3

*gap junction protein alpha 3* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.92× (z +17.7, q 0e+00, up in 18 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.888× (z -5.3, q 5e-05, down in 11 of 31 measured lines) ⚠ position not correctable. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.719× (z -4.1, q 0.013, down in 13 of 28 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL17RD]] (+0.57, fdr 2e-05), [[RAB6B]] (+0.54, fdr 1e-04), [[SEPTIN3]] (+0.53, fdr 6e-05); moves opposite to [[GTF2IRD2]] (-0.51, fdr 1e-04), [[AGAP6]] (-0.49, fdr 1e-04), [[ANKHD1-EIF4EBP3]] (-0.47, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[STON2]] → it (grade B ⚠); 6 go from it, the strongest it → [[IMPDH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.92×** | +17.7 | 0e+00 | 18/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +17.1 | 0e+00 | 22/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.44×** | +15.4 | 0e+00 | 23/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.21×** | +15.2 | 0e+00 | 17/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +11.6 | 3e-29 | 17/28 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.36×** | +11.2 | 5e-27 | 21/31 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.80×** | +7.0 | 2e-10 | 6/30 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +6.7 | 1e-09 | 14/29 (SNU-423, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.1 | 6e-08 | 7/20 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.1 | 2e-05 | 7/16 (PANC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 6/31 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.5 | 3e-04 | 2/6 (PANC-1, NCI-H661) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.4 | 5e-04 | 6/26 (A549, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 5e-04 | 8/30 (LoVo, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.036 | 4/28 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.050 | 8/28 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.050 | 4/30 (A549, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.068 | 5/29 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.070 | 5/31 (A-427, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -5.3 | 5e-05 | 11/31 (C-33 A, HCT15, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -4.1 | 0.013 | 13/28 (NCI-H661, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -3.9 | 0.016 | 11/29 (HCT15, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.016 | 11/31 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.777× | -3.3 | 0.11 | 10/30 (SW48, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -13.8) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 6.19 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0887× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0743× (z -9.3) |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -10.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0766× (z -12.6) |
| [[HOP62 (line)]] | alt | 8.48 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0937× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.67 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0864× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RD]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[RAB6B]] | +0.54 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[SEPTIN3]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[TMOD2]] | +0.51 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[LPAR3]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[APBA1]] | +0.50 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[NAB2]] | +0.50 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[VSIR]] | +0.50 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[LHX6]] | +0.49 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[RYBP]] | +0.49 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[PTPRU]] | +0.49 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[STX6]] | +0.48 | +0.29 / +0.53 | both halves | 3e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[AGAP6]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.47 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[VPS45]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MEF2B]] | -0.46 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[GANC]] | -0.45 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CDK12]] | -0.44 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[GTF2IRD2B]] | -0.44 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[SPAG7]] | -0.44 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[GPATCH2]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[NPLOC4]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[IQCK]] | -0.42 | -0.37 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity lowers GJA3's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.79× higher at baseline in the lines without STON2 | 0.004 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[NPTXR]] | B | NPTXR activity raises GJA3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without NPTXR | 0.038 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises GJA3's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without SEPTIN3 | 0.044 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[RAB6B]] | B | RAB6B activity raises GJA3's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without RAB6B | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[NKD2]] | B | NKD2 activity raises GJA3's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 2.11× lower at baseline in the lines without NKD2 | 0.056 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[STON2]] | B | STON2 activity strengthens GJA3's drug response | lines that do not express STON2 (16) vs lines expressing it (15) | the lines without STON2 respond 0.53× as strongly (z diff +0.93); strongest at Belinostat 5 µM: 1.62x vs 3.35x (z diff +1.6) | 0.075 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3; target measured in part of the lines; the reference differs; artifact flags |
| [[ATP1A3]] | B | ATP1A3 activity raises GJA3's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without ATP1A3 | 0.086 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[PRRG1]] | C | PRRG1 activity lowers GJA3's level | lines that do not express PRRG1 (3) vs lines expressing it (47) | 5.80× higher at baseline in the lines without PRRG1 | 0.040 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPDH1]] | B | GJA3 activity raises IMPDH1's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without GJA3 | 0.034 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[ABRAXAS1]] | B | GJA3 activity raises ABRAXAS1's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without GJA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[IL17RD]] | B | GJA3 activity raises IL17RD's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without GJA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[JAG2]] | B | GJA3 activity raises JAG2's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without GJA3 | 0.065 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[RAB6B]] | B | GJA3 activity raises RAB6B's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 2.13× lower at baseline in the lines without GJA3 | 0.089 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[SNX30]] | B | GJA3 activity raises SNX30's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without GJA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: GBX1 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.6, 40.3); signed map (-25.4, 35.0). **Vector** length 45.0, 6.81% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +0.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.7 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | gap junction protein alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,138,255-20,161,052 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CX46; previously CZP3 |
| Gene groups (HGNC) | Gap junction proteins |
| Reactome | 5 pathways, smallest: Gap junction assembly; Gap junction trafficking; Gap junction trafficking and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6H8](https://www.uniprot.org/uniprotkb/Q9Y6H8) (Gap junction alpha-3 protein):

> Structural component of lens fiber gap junctions. Gap junctions are dodecameric channels that connect the cytoplasm of adjoining cells (By similarity). They are formed by the docking of two hexameric hemichannels, one from each cell membrane. Small molecules and ions diffuse from one cell to a neighboring cell via the central pore.

**Summary**, from NCBI Gene [2700](https://www.ncbi.nlm.nih.gov/gene/2700):

> The protein encoded by this gene is a connexin and is a component of lens fiber gap junctions. Defects in this gene are a cause of zonular pulverulent cataract type 3 (CZP3). [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:4277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4277) · Entrez [2700](https://www.ncbi.nlm.nih.gov/gene/2700) · UniProt [Q9Y6H8](https://www.uniprot.org/uniprotkb/Q9Y6H8) · Ensembl [ENSG00000121743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121743)

## Data

Gene col 4291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4291); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4291]; `tensor/DDL_lfc|DDL_z.npy` [4291]; `embed/gene_vectors.npy` [4291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4291 or target_col == 4291). Every well: [[GJA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GJA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
