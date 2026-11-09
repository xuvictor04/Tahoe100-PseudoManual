---
symbol: "BMS1P23"
type: "gene"
col: 16206
ensembl_id: "ENSG00000286156"
name: "BMS1 pseudogene 23"
location: "2q11.1"
module: 24
arm: "-"
pooled_cpm: 3.56
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# BMS1P23

*BMS1 pseudogene 23* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.04× (z +7.2, q 4e-10, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +6.4, q 3e-08, up in 13 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.523× (z -6.6, q 3e-08, down in 18 of 39 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.593× (z -5.5, q 8e-06, down in 13 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSA2P]] (+0.62, fdr 1e-05), [[AIFM2]] (+0.54, fdr 3e-05), [[DNAJA4]] (+0.52, fdr 1e-04); moves opposite to [[TIMM17B]] (-0.55, fdr 3e-05, ⚠ TIMM17B in the vector space only through flagged drug-doses), [[DBP]] (-0.51, fdr 6e-05), [[TMEM205]] (-0.50, fdr 1e-04), [[BDKRB2]] (-0.50, fdr 7e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.2 | 4e-10 | 3/6 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.4 | 3e-08 | 13/30 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.50×** | +6.1 | 2e-07 | 8/42 (NCI-H23, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.3 | 2e-05 | 2/9 (Hs 766T, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.5 | 8e-04 | 11/22 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +4.1 | 0.005 | 5/38 (A549, A-172, …) | two highest doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.014 | 7/38 (AsPC-1, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.6 | 0.024 | 3/19 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.047 | 5/39 (PANC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.055 | 9/39 (HT-29, A498, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.074 | 9/43 (A498, AsPC-1, …) | two highest doses | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.074 | 4/42 (AsPC-1, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.074 | 7/41 (HOP62, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.523×** | -6.6 | 3e-08 | 18/39 (NCI-H23, SNU-423, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.673×** | -5.9 | 1e-06 | 17/32 (PANC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.593×** | -5.5 | 8e-06 | 13/43 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.631×** | -4.8 | 2e-04 | 12/42 (NCI-H23, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.643×** | -4.6 | 4e-04 | 18/42 (Panc 03.27, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.646×** | -4.6 | 4e-04 | 15/42 (PANC-1, NCI-H23, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -4.4 | 8e-04 | 13/42 (NCI-H23, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.658×** | -4.4 | 8e-04 | 11/42 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.678×** | -4.1 | 0.003 | 12/42 (SW1417, A-172, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.694×** | -3.8 | 0.007 | 14/36 (PANC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.702×** | -3.7 | 0.011 | 7/42 (MIA PaCa-2, NCI-H23, …) | all doses, flat | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.702×** | -3.4 | 0.027 | 7/40 (NCI-H2347, A549, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.741×** | -3.1 | 0.071 | 13/34 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.742×** | -3.1 | 0.071 | 13/31 (NCI-H460, NCI-H23, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.744×** | -3.1 | 0.072 | 11/37 (Hs 766T, Panc 03.27, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.32 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0829× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 5.38 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 4.85 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.4) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Allantoin (drug)]] 0.5 µM 0.205× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.132× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 4.38 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0741× (z -9.2) ⚠ toxic; unreliable plate only |
| [[A-172 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA2P]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[AIFM2]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DNAJA4]] | +0.52 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[SLC4A3]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[WDR13]] | +0.52 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[ARHGEF25]] | +0.52 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[SNHG22]] | +0.50 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ALKBH6]] | +0.50 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[UBXN8]] | +0.49 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[GMIP]] | +0.48 | +0.27 / +0.52 | both halves | 3e-04 |  |
| [[GPN1]] | +0.47 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[DHX38]] | +0.47 | +0.32 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM17B]] ⚠ | -0.55 | -0.45 / -0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DBP]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[TMEM205]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[BDKRB2]] | -0.50 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[NR3C2]] | -0.50 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[SYNGR2]] | -0.50 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[MRPL14]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CLDN3]] | -0.49 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[RSPH1]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[NR6A1]] | -0.49 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[CADM1]] | -0.48 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[WDPCP]] | -0.48 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[RNF24]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity weakens BMS1P23's drug response | lines that do not express NR3C2 (13) vs lines expressing it (30) | the lines without NR3C2 respond 1.78× as strongly (z diff -1.05); strongest at Homoharringtonine 5 µM: 0.46x vs 0.65x (z diff -2.8) | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RSPH1]] | B | RSPH1 activity raises BMS1P23's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without RSPH1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[NR3C2]] | B | NR3C2 activity lowers BMS1P23's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.45× higher at baseline in the lines without NR3C2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.303). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, 10.4); signed map (22.3, -24.6). **Vector** length 47.2, 5.37% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +2.2 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.7 | -6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -1.8 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -1.7 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -4.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -0.9 | -3.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -0.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | BMS1 pseudogene 23 |
| Locus type | pseudogene |
| Location | 2q11.1 — chr2:94,196,057-94,203,287 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55088) · Entrez [728034](https://www.ncbi.nlm.nih.gov/gene/728034) · Ensembl [ENSG00000286156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000286156)

## Data

Gene col 16206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16206); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16206]; `tensor/DDL_lfc|DDL_z.npy` [16206]; `embed/gene_vectors.npy` [16206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16206 or target_col == 16206). Every well: [[BMS1P23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
