---
symbol: "PDE3A"
type: "gene"
col: 10269
ensembl_id: "ENSG00000172572"
name: "phosphodiesterase 3A"
location: "12p12.2"
module: 19
arm: "+"
pooled_cpm: 76.46
n_lines_expressing: 16
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 44
direction_downstream: 43
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE3A

*phosphodiesterase 3A* — 12p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +10.0, q 5e-21, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +5.0, q 8e-05, up in 2 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 6.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 5.09×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.509× (z -6.8, q 7e-09, down in 8 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF4]] (+0.77, fdr 7e-06), [[KCNE4]] (+0.77, fdr 7e-06), [[SLCO1C1]] (+0.75, fdr 7e-06, ⚠ read-through risk), [[NALF1]] (+0.68, fdr 7e-06); moves opposite to [[ARHGEF34P]] (-0.50, fdr 3e-04), [[ARHGEF5]] (-0.50, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[KCNMB2]] → it (grade B ⚠); 43 go from it, the strongest it → [[SLCO1C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HOP62 6.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HOP62 5.09×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.0 | 5e-21 | 4/14 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.1 | 1e-13 | 4/12 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.1 | 2e-10 | 3/12 (HOP62, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.0 | 8e-05 | 2/15 (LoVo, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.37× | +3.2 | 0.17 | 3/14 (LoVo, NCI-H661, …) | two highest doses | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | 1.36× | +3.1 | 0.17 | 4/15 (HS-578T, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -6.8 | 7e-09 | 8/13 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.609×** | -5.0 | 2e-04 | 9/14 (LOX-IMVI, HS-578T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.613×** | -4.9 | 2e-04 | 12/14 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.637×** | -4.5 | 9e-04 | 10/13 (LOX-IMVI, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.732×** | -4.4 | 0.001 | 10/13 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.485×** | -3.8 | 0.014 | 7/14 (NCI-H460, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.690×** | -3.7 | 0.017 | 3/14 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.691×** | -3.6 | 0.027 | 7/13 (LOX-IMVI, LoVo, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -3.4 | 0.035 | 9/14 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.050 | 9/15 (C32, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.731×** | -3.1 | 0.088 | 10/14 (NCI-H460, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.714×** | -3.1 | 0.088 | 0/14 | inconsistent across doses |  |
| [[Menadione (drug)]] 5 µM |  | 0.728× | -3.0 | 0.10 | 3/13 (AN3 CA, HOP62, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.740× | -3.0 | 0.10 | 3/14 (HOP62, hTERT-HPNE, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 771 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 937 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -14.5) |
| [[CHP-212 (line)]] | wt | 444 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0740× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.6) |
| [[HS-578T (line)]] | alt | 244 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.5) |
| [[HOP62 (line)]] | alt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.134× (z -8.7) |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.2) |
| [[H4 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0817× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF4]] | +0.77 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[KCNE4]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SLCO1C1]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 | STRING 565; ⚠ **readthrough risk**: SLCO1C1 lies 6.7 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[NALF1]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ADGRB3]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PDE7B]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 | same gene group; pathway: G alpha (s) signalling events |
| [[CDH7]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[BAALC]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PDGFRB]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PDE4B]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[COL4A6]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SDC2]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF34P]] | -0.50 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[ARHGEF5]] | -0.50 | -0.55 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 4, C 40. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | KCNMB2 activity raises PDE3A's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without KCNMB2 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity lowers PDE3A's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.09× higher at baseline in the lines without ARHGEF5, ARHGEF34P | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[CPA6]] | B | CPA6 activity raises PDE3A's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 2.87× lower at baseline in the lines without CPA6 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[TMEM178B]] | B | TMEM178B activity raises PDE3A's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without TMEM178B | 0.096 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2 |
| [[EDNRB]] | C | EDNRB activity raises PDE3A's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 4.61× lower at baseline in the lines without EDNRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[UTY]] | C | UTY activity raises PDE3A's level | lines that do not express UTY (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without UTY | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises PDE3A's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 4.43× lower at baseline in the lines without COL3A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises PDE3A's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without TTTY10 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises PDE3A's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without LOXL3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises PDE3A's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 4.08× lower at baseline in the lines without KCNE4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises PDE3A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.21× lower at baseline in the lines without PDGFRB | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[EPB41L3]] | C | EPB41L3 activity raises PDE3A's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 4.16× lower at baseline in the lines without EPB41L3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 4, C 39. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1C1]] | B | PDE3A activity raises SLCO1C1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without PDE3A | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[CPA6]] | B | PDE3A activity raises CPA6's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without PDE3A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[RNF152]] | B | PDE3A activity raises RNF152's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.00× lower at baseline in the lines without PDE3A | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[BMPER]] | B | PDE3A activity raises BMPER's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without PDE3A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[ADGRB3]] | C | PDE3A activity raises ADGRB3's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 5.54× lower at baseline in the lines without PDE3A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[NALF1]] | C | PDE3A activity raises NALF1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 5.72× lower at baseline in the lines without PDE3A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[NID2]] | C | PDE3A activity raises NID2's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.75× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[KCNE4]] | C | PDE3A activity raises KCNE4's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 5.35× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[RARB]] | C | PDE3A activity raises RARB's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 4.38× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[PAPPA2]] | C | PDE3A activity raises PAPPA2's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[PAPPA]] | C | PDE3A activity raises PAPPA's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 4.36× lower at baseline in the lines without PDE3A | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[EPB41L3]] | C | PDE3A activity raises EPB41L3's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without PDE3A | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 21.2); signed map (36.6, 43.9). **Vector** length 59.6, 21.4% of its response variance represented; |z| ≥ 3 in 422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.2 — chr12:20,368,537-20,688,583 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-PDE |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14432](https://www.uniprot.org/uniprotkb/Q14432) (cGMP-inhibited 3',5'-cyclic phosphodiesterase 3A):

> Cyclic nucleotide phosphodiesterase with specificity for the second messengers cAMP and cGMP, which are key regulators of many important physiological processes. Also has activity toward cUMP. Independently of its catalytic activity it is part of an E2/17beta-estradiol-induced pro-apoptotic signaling pathway. E2 stabilizes the PDE3A/SLFN12 complex in the cytosol, promoting the dephosphorylation of SLFN12 and activating its pro-apoptotic ribosomal RNA/rRNA ribonuclease activity. This apoptotic …

**Summary**, from NCBI Gene [5139](https://www.ncbi.nlm.nih.gov/gene/5139):

> This gene encodes a member of the cGMP-inhibited cyclic nucleotide phosphodiesterase (cGI-PDE) family. cGI-PDE enzymes hydrolyze both cAMP and cGMP, and play critical roles in many cellular processes by regulating the amplitude and duration of intracellular cyclic nucleotide signals. The encoded protein mediates platelet aggregation and also plays important roles in cardiovascular function by regulating vascular smooth muscle contraction and relaxation. Inhibitors of the encoded protein may be …

**Accessions** — [HGNC:8778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8778) · Entrez [5139](https://www.ncbi.nlm.nih.gov/gene/5139) · UniProt [Q14432](https://www.uniprot.org/uniprotkb/Q14432) · Ensembl [ENSG00000172572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172572)

## Data

Gene col 10269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10269); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10269]; `tensor/DDL_lfc|DDL_z.npy` [10269]; `embed/gene_vectors.npy` [10269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10269 or target_col == 10269). Every well: [[PDE3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
