---
symbol: "MYL12B"
type: "gene"
col: 4011
ensembl_id: "ENSG00000118680"
name: "myosin light chain 12B"
location: "18p11.31"
module: 120
arm: "+"
pooled_cpm: 201.72
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# MYL12B

*myosin light chain 12B* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.39× (z +8.5, q 1e-14, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.675× (z -3.8, q 0.074, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.323×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 0.327×; ⚠ cell-cycle shift, explains ~37% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.726×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYL12A]] (+0.69, fdr 7e-06, ⚠ same locus), [[TMSB10]] (+0.55, fdr 4e-05), [[CCN1]] (+0.54, fdr 3e-05), [[S100A1]] (+0.54, fdr 1e-04); moves opposite to [[MRPL9]] (-0.56, fdr 2e-05), [[BAG2]] (-0.51, fdr 5e-05), [[TARBP2]] (-0.51, fdr 9e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPHA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.39×** | +8.5 | 1e-14 | 49/49 (SNU-1, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.46×** | +8.3 | 2e-14 | 40/44 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.86×** | +8.1 | 9e-14 | 48/49 (HOP62, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.30×** | +8.0 | 1e-13 | 47/48 (HepG2/C3A, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.03×** | +6.3 | 3e-08 | 40/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.67×** | +4.9 | 8e-05 | 44/48 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.64×** | +4.8 | 1e-04 | 40/48 (HepG2/C3A, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.59×** | +4.5 | 5e-04 | 39/48 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.013 | 39/48 (HOP62, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.42×** | +3.3 | 0.046 | 30/48 (HepG2/C3A, NCI-H1573, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.048 | 31/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.323×; ⚠ cell-cycle shift, would explain all of this change); [[Trametinib (drug)]] 5 µM in 1 line (NCI-H23 0.327×; ⚠ cell-cycle shift, explains ~37% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.726×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.675×** | -3.8 | 0.074 | 45/48 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.767×** | -3.7 | 0.074 | 44/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.675× | -3.3 | 0.20 | 31/50 (NCI-H23, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.701× | -3.2 | 0.20 | 33/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.727× | -3.1 | 0.21 | 29/48 (SNU-1, C-33 A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.546× | -3.1 | 0.21 | 36/49 (BT-474, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 163 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.77× (z +9.7) | — |
| [[C32 (line)]] | wt | 81.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 188 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.81× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 192 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +10.5) | — |
| [[A549 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HOP62 (line)]] | alt | 240 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 500 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +9.1) | [[Trametinib (drug)]] 5 µM 0.327× (z -9.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 91.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.4× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.81× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.88× (z +8.8) | — |
| [[SW480 (line)]] | alt | 226 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +10.3) | — |
| [[A498 (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 277 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[C-33 A (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.77× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 247 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 239 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.32× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 170 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 71.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 320 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.9× (z +11.9) | — |
| [[A-172 (line)]] | wt | 217 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 798 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 199 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 266 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 168 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 219 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYL12A]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 | same gene group; pathway: EPH-Ephrin signaling; STRING 945; ⚠ same locus (5.2 kb, same strand: neighbours can correlate without regulation) |
| [[TMSB10]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CCN1]] | +0.54 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[S100A1]] | +0.54 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[LUZP1]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[POLR2L]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[FAAP20]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UGCG]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[DLC1]] | +0.50 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[MIDN]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ARHGEF18]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DRAP1]] | +0.50 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL9]] | -0.56 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[BAG2]] | -0.51 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TARBP2]] | -0.51 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[FBXO7]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TYW3]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[FECH]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TSR2]] | -0.50 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[FKBP4]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MTX3]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SPR]] | -0.49 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ACTR8]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[GPN1]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | EPHA2 activity raises MYL12B's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.91× lower at baseline in the lines without EPHA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[BCL2L1]] | B | BCL2L1 activity raises MYL12B's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without BCL2L1 | 0.039 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.6, 40.4); signed map (-4.2, 41.6). **Vector** length 94.5, 42.9% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.1 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.0 | +8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | +0.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:3,261,479-3,278,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRLC2 |
| Gene groups (HGNC) | Myosin light chains, class 2 |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 16 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [O14950](https://www.uniprot.org/uniprotkb/O14950) (Myosin regulatory light chain 12B):

> Myosin regulatory subunit that plays an important role in regulation of both smooth muscle and nonmuscle cell contractile activity via its phosphorylation. Phosphorylation triggers actin polymerization in vascular smooth muscle. Implicated in cytokinesis, receptor capping, and cell locomotion.

**Summary**, from NCBI Gene [103910](https://www.ncbi.nlm.nih.gov/gene/103910):

> The activity of nonmuscle myosin II (see MYH9; MIM 160775) is regulated by phosphorylation of a regulatory light chain, such as MRLC2. This phosphorylation results in higher MgATPase activity and the assembly of myosin II filaments (Iwasaki et al., 2001 [PubMed 11942626]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29827) · Entrez [103910](https://www.ncbi.nlm.nih.gov/gene/103910) · UniProt [O14950](https://www.uniprot.org/uniprotkb/O14950) · Ensembl [ENSG00000118680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118680)

## Data

Gene col 4011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4011); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4011]; `tensor/DDL_lfc|DDL_z.npy` [4011]; `embed/gene_vectors.npy` [4011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4011 or target_col == 4011). Every well: [[MYL12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
