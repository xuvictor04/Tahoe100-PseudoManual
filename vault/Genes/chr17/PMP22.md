---
symbol: "PMP22"
type: "gene"
col: 3027
ensembl_id: "ENSG00000109099"
name: "peripheral myelin protein 22"
location: "17p12"
module: 88
arm: "-"
pooled_cpm: 65.82
n_lines_expressing: 40
n_dd_up: 3
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 20
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# PMP22

*peripheral myelin protein 22* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PF-06260933 (drug)]] 5 µM: 1.53× (z +3.9, q 0.042, up in 14 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.233× (z -36.7, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD19]] (+0.59, fdr 3e-05), [[LYPD3]] (+0.57, fdr 2e-05), [[LTBP4]] (+0.55, fdr 3e-05); moves opposite to [[VPS52]] (-0.53, fdr 3e-04), [[DPP8]] (-0.53, fdr 5e-05), [[GABPB2]] (-0.52, fdr 3e-04).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RASA3]] → it (grade B ⚠); 20 go from it, the strongest it → [[LTBP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.042 | 14/38 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.042 | 10/38 (A-172, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.042 | 16/37 (H4, SW480, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.233×** | -36.7 | 0e+00 | 35/38 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.258×** | -24.1 | 0e+00 | 36/38 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.408×** | -22.6 | 0e+00 | 34/38 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -17.1 | 0e+00 | 34/38 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.464×** | -13.7 | 1e-40 | 28/38 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.471×** | -13.4 | 6e-39 | 30/38 (SK-MEL-2, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.444×** | -12.0 | 2e-31 | 24/30 (C32, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.457×** | -11.6 | 3e-29 | 29/38 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -11.0 | 2e-26 | 29/38 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.575×** | -9.8 | 4e-21 | 25/36 (HOP62, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -9.2 | 2e-18 | 29/39 (A-172, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.731×** | -7.9 | 1e-13 | 27/38 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.644×** | -7.8 | 2e-13 | 23/38 (A549, SK-MEL-2, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.600×** | -7.6 | 2e-12 | 27/40 (C32, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -7.2 | 2e-11 | 21/38 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.718×** | -5.6 | 9e-07 | 20/38 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -5.5 | 1e-06 | 15/38 (A549, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.730×** | -4.7 | 9e-05 | 16/37 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.774×** | -4.6 | 1e-04 | 21/38 (HOP62, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -4.2 | 5e-04 | 18/39 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.865× | -3.7 | 0.005 | 11/39 (C32, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 275 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -30.3) |
| [[HOP62 (line)]] | alt | 167 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -23.8) |
| [[A-172 (line)]] | wt | 138 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -28.3) |
| [[SW 900 (line)]] | alt | 222 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -25.4) |
| [[CFPAC-1 (line)]] | alt | 48.7 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -26.6) |
| [[H4 (line)]] | wt | 120 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -22.8) |
| [[NCI-H1792 (line)]] | alt | 83.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -22.9) |
| [[A549 (line)]] | wt | 169 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.3) |
| [[HS-578T (line)]] | alt | 123 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 105 | 1 (1 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.42× (z +12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.4) |
| [[RPMI-7951 (line)]] | alt | 78.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -22.9) |
| [[SK-MEL-2 (line)]] | alt | 91.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.7) |
| [[A498 (line)]] | wt | 115 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -26.3) |
| [[AsPC-1 (line)]] | alt | 43.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -14.3) |
| [[LoVo (line)]] | wt | 152 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -19.6) |
| [[Hs 766T (line)]] | wt | 78.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -26.3) |
| [[KATO III (line)]] | alt | 33.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.9) |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -18.4) |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.2) |
| [[SW480 (line)]] | alt | 32.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -17.3) |
| [[SNU-423 (line)]] | alt | 52.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -27.5) |
| [[SW1417 (line)]] | alt | 29.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -19.5) |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -12.0) |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -8.9) |
| [[CHP-212 (line)]] | wt | 73.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.5) |
| [[J82 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.6) |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.9) |
| [[SW 1088 (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.8) |
| [[SW 1271 (line)]] | alt | 75.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0642× (z -14.3) |
| [[SW48 (line)]] | wt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.5) |
| [[A-427 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | +0.59 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LYPD3]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[LTBP4]] | +0.55 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | +0.55 | +0.58 / +0.29 | both halves | 3e-04 |  |
| [[ZFYVE28]] | +0.54 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[FCHO1]] | +0.54 | +0.54 / +0.25 | both halves | 4e-04 |  |
| [[SFXN3]] | +0.54 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[TNS1]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 | same gene group |
| [[ETHE1]] | +0.53 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[ZNRF1]] | +0.53 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[CSNK1E]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FLNB]] | +0.52 | +0.59 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | -0.53 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[DPP8]] | -0.53 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[GABPB2]] | -0.52 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[TXNRD2]] | -0.52 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[DCUN1D1]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.51 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ZFP91]] | -0.51 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[ARFGAP2]] | -0.51 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[TIA1]] | -0.50 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[KDM3B]] | -0.50 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[NFYC]] | -0.50 | -0.53 / -0.32 | both halves | 2e-04 | same gene group |
| [[CHMP3]] | -0.50 | -0.48 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | RASA3 activity raises PMP22's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.99× lower at baseline in the lines without RASA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[HMGCR]] | B | HMGCR activity lowers PMP22's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[TOP2A]] | B | TOP2A activity raises PMP22's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP4]] | B | PMP22 activity raises LTBP4's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without PMP22 | 0.014 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[DCUN1D1]] | B | PMP22 activity lowers DCUN1D1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.38× higher at baseline in the lines without PMP22 | 0.017 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | PMP22 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express PMP22 (10) vs lines expressing it (38) | the lines without PMP22: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[ZFYVE28]] | B | PMP22 activity raises ZFYVE28's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without PMP22 | 0.030 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[ZNRF1]] | B | PMP22 activity raises ZNRF1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PMP22 | 0.043 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| cells under [[Afatinib (drug)]] 5 µM | B | PMP22 activity raises the cells' numbers under Afatinib 5 µM (protects the cells) | lines that do not express PMP22 (10) vs lines expressing it (38) | the lines without PMP22: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[SLC2A13]] | B | PMP22 activity raises SLC2A13's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without PMP22 | 0.054 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[HACE1]] | B | PMP22 activity raises HACE1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without PMP22 | 0.055 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[IMPDH1]] | B | PMP22 activity raises IMPDH1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PMP22 | 0.063 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[RASA3]] | B | PMP22 activity raises RASA3's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without PMP22 | 0.067 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | PMP22 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express PMP22 (10) vs lines expressing it (38) | the lines without PMP22: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[RAB30-DT]] | B | PMP22 activity lowers RAB30-DT's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without PMP22 | 0.072 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (9.1, 3.1); signed map (-4.2, 45.5). **Vector** length 109, 30.7% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.9 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.9 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | -2.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -17.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -24.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -5.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | peripheral myelin protein 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,229,773-15,272,292 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HNPP, GAS3, Sp110, HMSNIA; previously CMT1A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01453](https://www.uniprot.org/uniprotkb/Q01453) (Peripheral myelin protein 22):

> Might be involved in growth regulation, and in myelinization in the peripheral nervous system.

**Summary**, from NCBI Gene [5376](https://www.ncbi.nlm.nih.gov/gene/5376):

> This gene encodes an integral membrane protein that is a major component of myelin in the peripheral nervous system. Studies suggest two alternately used promoters drive tissue-specific expression. Various mutations of this gene are causes of Charcot-Marie-Tooth disease Type IA, Dejerine-Sottas syndrome, and hereditary neuropathy with liability to pressure palsies. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:9118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9118) · Entrez [5376](https://www.ncbi.nlm.nih.gov/gene/5376) · UniProt [Q01453](https://www.uniprot.org/uniprotkb/Q01453) · Ensembl [ENSG00000109099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109099)

## Data

Gene col 3027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3027); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3027]; `tensor/DDL_lfc|DDL_z.npy` [3027]; `embed/gene_vectors.npy` [3027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3027 or target_col == 3027). Every well: [[PMP22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMP22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
