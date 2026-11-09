---
symbol: "DGCR2"
type: "gene"
col: 949
ensembl_id: "ENSG00000070413"
name: "DiGeorge syndrome critical region gene 2"
location: "22q11.21"
module: 15
arm: "+"
pooled_cpm: 43.0
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DGCR2

*DiGeorge syndrome critical region gene 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.66× (z +8.4, q 3e-14, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.569× (z -9.0, q 2e-16, down in 39 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.590× (z -8.7, q 8e-16, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCTN3]] (+0.60, fdr 1e-05), [[MFSD8]] (+0.59, fdr 1e-05), [[FBH1]] (+0.58, fdr 4e-05); moves opposite to [[SYNE1]] (-0.58, fdr 1e-05), [[FAM171B]] (-0.55, fdr 3e-05), [[IER3]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02967]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +8.4 | 3e-14 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.1 | 2e-10 | 34/49 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +7.1 | 2e-10 | 36/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.005 | 25/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +3.4 | 0.082 | 16/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.17 | 14/48 (AsPC-1, Panc 03.27, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | 1.42× | +3.1 | 0.18 | 13/49 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -9.0 | 2e-16 | 39/47 (HCT15, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.590×** | -8.7 | 8e-16 | 38/48 (C32, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.610×** | -8.2 | 5e-14 | 35/48 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.600×** | -8.1 | 7e-14 | 31/48 (Panc 03.27, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -7.9 | 3e-13 | 28/40 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -6.6 | 5e-09 | 37/49 (Panc 03.27, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -6.0 | 1e-07 | 23/42 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.740×** | -5.0 | 5e-05 | 30/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.617×** | -4.2 | 0.002 | 24/47 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.786×** | -4.0 | 0.004 | 21/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.661×** | -3.6 | 0.018 | 22/44 (RPMI-7951, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.833× | -3.0 | 0.12 | 17/48 (CFPAC-1, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 85.3 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.165× (z -9.2) |
| [[A-172 (line)]] | wt | 27.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 65.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -10.4) |
| [[H4 (line)]] | wt | 31.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -12.4) ⚠ toxic · without an alert: [[Alpelisib (drug)]] 5 µM 0.0887× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 30.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.390× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0635× (z -16.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -8.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.262× (z -11.8) ⚠ toxic |
| [[C32 (line)]] | wt | 36.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.228× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -13.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -14.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 50.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.199× (z -9.3) |
| [[HT-29 (line)]] | alt | 53.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.8) | — |
| [[KATO III (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -16.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.409× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.59 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[FBH1]] | +0.58 | +0.41 / +0.73 | both halves | 4e-05 |  |
| [[ZNF250]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[FAHD2A]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[WDR20]] | +0.54 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.54 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[C8orf76]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NUP133]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.52 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SMARCD2]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ZFYVE21]] | +0.52 | +0.31 / +0.63 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNE1]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[FAM171B]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[IER3]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.54 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[NFKBIZ]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[AZIN1]] | -0.52 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[NOCT]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PRECSIT]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ACAA2]] | -0.51 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[P2RY1]] | -0.50 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[BPGM]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[TSPAN2]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02967]] | B | LINC02967 activity raises DGCR2's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.42× lower at baseline in the lines without LINC02967 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[HDAC6]] | B | HDAC6 activity lowers DGCR2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNGT1]] | B | GNGT1 activity strengthens DGCR2's drug response | lines that do not express GNGT1 (30) vs lines expressing it (19) | the lines without GNGT1 respond 0.88× as strongly (z diff +0.14); strongest at Belinostat 5 µM: 1.37x vs 1.68x (z diff +1.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.339). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.7, 22.9); signed map (-45.3, -0.3). **Vector** length 84.2, 18.8% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.9 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DiGeorge syndrome critical region gene 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,036,282-19,122,454 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0163, LAN, IDD, DGS-C, SEZ-12 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P98153](https://www.uniprot.org/uniprotkb/P98153) (Integral membrane protein DGCR2/IDD):

> Putative adhesion receptor, that could be involved in cell-cell or cell-matrix interactions required for normal cell differentiation and migration.

**Summary**, from NCBI Gene [9993](https://www.ncbi.nlm.nih.gov/gene/9993):

> Deletions of the 22q11.2 have been associated with a wide range of developmental defects (notably DiGeorge syndrome, velocardiofacial syndrome, conotruncal anomaly face syndrome and isolated conotruncal cardiac defects) classified under the acronym CATCH 22. The DGCR2 gene encodes a novel putative adhesion receptor protein, which could play a role in neural crest cells migration, a process which has been proposed to be altered in DiGeorge syndrome. Alternative splicing results in multiple …

**Accessions** — [HGNC:2845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2845) · Entrez [9993](https://www.ncbi.nlm.nih.gov/gene/9993) · UniProt [P98153](https://www.uniprot.org/uniprotkb/P98153) · Ensembl [ENSG00000070413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070413)

## Data

Gene col 949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 949); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 949]; `tensor/DDL_lfc|DDL_z.npy` [949]; `embed/gene_vectors.npy` [949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 949 or target_col == 949). Every well: [[DGCR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGCR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
