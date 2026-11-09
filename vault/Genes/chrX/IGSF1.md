---
symbol: "IGSF1"
type: "gene"
col: 7168
ensembl_id: "ENSG00000147255"
name: "immunoglobulin superfamily member 1"
location: "Xq26.1"
module: 19
arm: "+"
pooled_cpm: 21.59
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# IGSF1

*immunoglobulin superfamily member 1* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +13.6, q 4e-39, up in 1 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +11.2, q 1e-26, up in 10 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.648× (z -5.5, q 2e-05, down in 13 of 15 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Dexamethasone (drug)]] 0.5 µM: 0.717× (z -4.2, q 0.004, down in 6 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02211]] (+0.69, fdr 7e-06), [[MIR3171HG]] (+0.63, fdr 7e-06), [[ZSCAN31]] (+0.63, fdr 7e-06); moves opposite to [[TMEM181]] (-0.54, fdr 3e-05), [[SFXN2]] (-0.54, fdr 2e-05), [[BDH1]] (-0.53, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HDX]] → it (grade B ⚠); 6 go from it, the strongest it → [[ADAMTS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +13.6 | 4e-39 | 1/15 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +11.2 | 1e-26 | 10/15 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.4 | 5e-23 | 1/14 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +7.9 | 4e-13 | 1/14 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.8 | 7e-13 | 1/16 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.6 | 4e-09 | 5/15 (KATO III, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 1e-04 | 9/15 (AsPC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 1e-03 | 5/16 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 10/15 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 7/15 (AsPC-1, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 9/15 (A549, AsPC-1, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.005 | 0/16 | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.005 | 9/16 (AsPC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.008 | 8/15 (A-427, KATO III, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.008 | 13/15 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.012 | 7/15 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.039 | 12/15 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.043 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.648×** | -5.5 | 2e-05 | 13/15 (LOX-IMVI, SHP-77, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.677×** | -4.9 | 2e-04 | 14/15 (KATO III, SHP-77, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.717×** | -4.2 | 0.004 | 6/15 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.729×** | -4.0 | 0.009 | 14/15 (SHP-77, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.016 | 6/15 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.765×** | -3.4 | 0.058 | 3/15 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.765×** | -3.4 | 0.058 | 0/15 | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.774×** | -3.3 | 0.081 | 7/15 (A549, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.785× | -3.1 | 0.13 | 7/15 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.632× | -3.0 | 0.13 | 0/16 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.789× | -3.0 | 0.13 | 8/15 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.782× | -3.0 | 0.13 | 11/16 (NCI-H460, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 45.5 | 2 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 60.2 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.105× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -13.6) |
| [[KATO III (line)]] | alt | 29.6 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.149× (z -13.2) |
| [[A549 (line)]] | wt | 195 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -20.1) |
| [[RPMI-7951 (line)]] | alt | 57.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0514× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 59.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -14.5) |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 96.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.5) |
| [[HS-578T (line)]] | alt | 91.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0918× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -9.2) |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.227× (z -8.9) |
| [[A-172 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02211]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MIR3171HG]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZSCAN31]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PDE7B]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TLR6]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CDH7]] | +0.62 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CDH8]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.61 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[SLC6A7]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM181]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SFXN2]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BDH1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TBC1D16]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SRD5A1]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DPY19L3]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[IMPDH1]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SNX25]] | -0.50 | -0.40 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDX]] | B | HDX activity lowers IGSF1's level | lines that do not express HDX (16) vs lines expressing it (34) | 1.03× higher at baseline in the lines without HDX | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: LOXL2, SDK2, WIPF1 |
| [[HDAC6]] | B | HDAC6 activity raises IGSF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers IGSF1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[GNGT1]] | C | GNGT1 activity raises IGSF1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without GNGT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; co-absent with the target |
| [[LSAMP]] | C | LSAMP activity raises IGSF1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 4.09× lower at baseline in the lines without LSAMP | 0.075 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent; co-absent with the target |
| [[ANKRD30A]] | C | ANKRD30A activity raises IGSF1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.80× lower at baseline in the lines without ANKRD30A | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises IGSF1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.99× lower at baseline in the lines without CDH12 | 0.0999 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS3]] | B | IGSF1 activity lowers ADAMTS3's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 1.70× higher at baseline in the lines without IGSF1 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358 |
| [[GNGT1]] | C | IGSF1 activity raises GNGT1's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without IGSF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[MSR1]] | C | IGSF1 activity raises MSR1's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 3.06× lower at baseline in the lines without IGSF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[CDH12]] | C | IGSF1 activity raises CDH12's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without IGSF1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[SEMA3D]] | C | IGSF1 activity raises SEMA3D's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without IGSF1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[KCNH5]] | C | IGSF1 activity raises KCNH5's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without IGSF1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.0, 31.4); signed map (40.9, 32.5). **Vector** length 56.0, 17.2% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +4.0 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.7 | -5.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:131,273,506-131,578,899 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0364, IGDC1, IGCD1, INHBP, MGC75490, PGSF2 |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6C5](https://www.uniprot.org/uniprotkb/Q8N6C5) (Immunoglobulin superfamily member 1):

> Seems to be a coreceptor in inhibin signaling, but seems not to be a high-affinity inhibin receptor. Antagonizes activin A signaling in the presence or absence of inhibin B (By similarity). Necessary to mediate a specific antagonistic effect of inhibin B on activin-stimulated transcription.

**Summary**, from NCBI Gene [3547](https://www.ncbi.nlm.nih.gov/gene/3547):

> This gene encodes a member of the immunoglobulin-like domain-containing superfamily. Proteins in this superfamily contain varying numbers of immunoglobulin-like domains and are thought to participate in the regulation of interactions between cells. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:5948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5948) · Entrez [3547](https://www.ncbi.nlm.nih.gov/gene/3547) · UniProt [Q8N6C5](https://www.uniprot.org/uniprotkb/Q8N6C5) · Ensembl [ENSG00000147255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147255)

## Data

Gene col 7168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7168); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7168]; `tensor/DDL_lfc|DDL_z.npy` [7168]; `embed/gene_vectors.npy` [7168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7168 or target_col == 7168). Every well: [[IGSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
