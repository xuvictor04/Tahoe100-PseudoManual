---
symbol: "C2orf72"
type: "gene"
col: 12815
ensembl_id: "ENSG00000204128"
name: "chromosome 2 open reading frame 72"
location: "2q37.1"
module: 103
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 44
n_dd_up: 0
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# C2orf72

*chromosome 2 open reading frame 72* — 2q37.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.224× (z -24.1, q 0e+00, down in 31 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM74B]] (+0.71, fdr 7e-06), [[ISM2]] (+0.57, fdr 1e-05), [[DHRS13]] (+0.57, fdr 1e-05); moves opposite to [[ARHGEF12]] (-0.46, fdr 1e-04), [[ITGAV]] (-0.44, fdr 7e-05), [[FAP]] (-0.43, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RASGEF1C]] → it (grade B ⚠); 2 go from it, the strongest it → [[GABBR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.57× | +3.7 | 0.13 | 5/22 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.4 | 0.18 | 5/30 (RKO, HOP62, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.22 | 5/37 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.31× | +3.2 | 0.22 | 6/36 (PANC-1, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.224×** | -24.1 | 0e+00 | 31/33 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.209×** | -17.8 | 0e+00 | 28/34 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.207×** | -17.2 | 0e+00 | 34/37 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -12.4 | 5e-33 | 32/40 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -11.9 | 2e-30 | 27/40 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -11.4 | 4e-28 | 23/37 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.386×** | -10.8 | 2e-25 | 26/38 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.400×** | -10.4 | 2e-23 | 30/37 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.413×** | -9.7 | 3e-20 | 19/28 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -8.9 | 3e-17 | 19/32 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.464×** | -8.7 | 2e-16 | 25/37 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -6.9 | 3e-10 | 19/37 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -6.2 | 3e-08 | 17/32 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -5.5 | 2e-06 | 18/37 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -5.3 | 4e-06 | 17/37 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -4.8 | 7e-05 | 15/33 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -4.4 | 4e-04 | 15/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.0 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0424× (z -27.1) |
| [[NCI-H460 (line)]] | wt | 8.10 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -24.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 8 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0436× (z -17.8) |
| [[HOP62 (line)]] | alt | 8.40 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0416× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.5) |
| [[LoVo (line)]] | wt | 7.63 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.4) |
| [[SW480 (line)]] | alt | 4.51 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.3) |
| [[A549 (line)]] | wt | 5.04 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0216× (z -15.1) |
| [[HCT15 (line)]] | alt | 9.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0704× (z -13.8) |
| [[LS 180 (line)]] | wt | 7.60 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 4.41 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0422× (z -10.7) |
| [[PANC-1 (line)]] | alt | 2.15 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -9.2) |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0409× (z -12.4) |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0252× (z -10.7) |
| [[C32 (line)]] | wt | 2.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0637× (z -9.8) |
| [[KATO III (line)]] | alt | 3.64 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0764× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 3.93 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0483× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 1.93 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0473× (z -9.8) |
| [[SW 900 (line)]] | alt | 6.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0756× (z -13.9) |
| [[A-427 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM74B]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ISM2]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[DHRS13]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MAP3K15]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TFR2]] | +0.51 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[SHANK3]] | +0.51 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[HDHD5]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RIMKLA]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ANO7]] | +0.50 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[TLE6]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.49 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[PPFIA4]] | +0.47 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF12]] | -0.46 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[ITGAV]] | -0.44 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[FAP]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PTPRK]] | -0.43 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NRP1]] | -0.43 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[LMO7]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[SPAG16]] | -0.41 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[ZBTB20]] | -0.41 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB10]] | -0.41 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[STPG2]] | -0.41 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[EIF1AY]] | -0.40 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ALPK1]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1C]] | B | RASGEF1C activity raises C2orf72's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without RASGEF1C | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[PARD6G]] | B | PARD6G activity strengthens C2orf72's drug response | lines that do not express PARD6G (8) vs lines expressing it (33) | the lines without PARD6G respond 0.54× as strongly (z diff +2.27); strongest at Niclosamide (olamine) 5 µM: 0.65x vs 0.25x (z diff +3.6) | 0.039 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAP3K15]] | B | MAP3K15 activity raises C2orf72's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without MAP3K15 | 0.070 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[BTNL9]] | B | BTNL9 activity raises C2orf72's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without BTNL9 | 0.095 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABBR2]] | B | C2orf72 activity lowers GABBR2's level | lines that do not express C2orf72 (6) vs lines expressing it (44) | 1.93× higher at baseline in the lines without C2orf72 | 0.021 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CMBL, TPPP |
| [[BTNL9]] | B | C2orf72 activity raises BTNL9's level | lines that do not express C2orf72 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without C2orf72 | 0.087 | ⚠ within organs, on part of the lines; also absent: ARRDC4, CMBL, TPPP |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.5, 45.0); signed map (-29.5, 35.1). **Vector** length 57.9, 8.94% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +1.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | -0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -17.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.8 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -17.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.3 | -24.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -5.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 72 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,037,523-231,049,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC257407 |
| Matched by | ensembl_id |

UniProt [A6NCS6](https://www.uniprot.org/uniprotkb/A6NCS6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27418) · Entrez [257407](https://www.ncbi.nlm.nih.gov/gene/257407) · UniProt [A6NCS6](https://www.uniprot.org/uniprotkb/A6NCS6) · Ensembl [ENSG00000204128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204128)

## Data

Gene col 12815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12815); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12815]; `tensor/DDL_lfc|DDL_z.npy` [12815]; `embed/gene_vectors.npy` [12815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12815 or target_col == 12815). Every well: [[C2orf72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
