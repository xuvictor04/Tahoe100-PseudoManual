---
symbol: "ABCA17P"
type: "gene"
col: 14168
ensembl_id: "ENSG00000238098"
name: "ATP binding cassette subfamily A member 17, pseudogene"
location: "16p13.3"
module: 10
arm: "+"
pooled_cpm: 3.39
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 16
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ABCA17P

*ATP binding cassette subfamily A member 17, pseudogene* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.70× (z +13.2, q 5e-37, up in 11 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.519× (z -5.7, q 8e-06, down in 16 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0546×, PANC-1 0.151×, A498 0.0761×; ⚠ cell-cycle shift, explains ~22% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.0872×, NCI-H2030 0.0602×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.139×, A498 0.0699×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP2]] (+0.70, fdr 7e-06), [[LINC00466]] (+0.69, fdr 3e-05), [[LINC02026]] (+0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM66C]] → it (grade B ⚠); 16 go from it, the strongest it → [[KATNAL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +13.2 | 5e-37 | 11/22 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.26×** | +13.1 | 7e-37 | 3/4 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +11.7 | 3e-29 | 5/9 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +8.3 | 1e-14 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.0 | 2e-07 | 11/32 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +4.5 | 6e-04 | 5/26 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +4.2 | 0.002 | 7/28 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.023 | 9/28 (NCI-H2347, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.070 | 2/12 (NCI-H2347, A-172) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14168.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.0546×, PANC-1 0.151×, A498 0.0761×; ⚠ cell-cycle shift, explains ~22% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.0872×, NCI-H2030 0.0602×); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.139×, A498 0.0699×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -5.7 | 8e-06 | 16/31 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.605×** | -4.7 | 6e-04 | 15/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.611×** | -4.5 | 0.001 | 16/30 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.725× | -3.0 | 0.34 | 7/31 (NCI-H1792, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.09 | 0 | 9 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0872× (z -11.8) |
| [[SNU-1 (line)]] | wt | 75.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.90 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 3.67 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0699× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[HEC-1-A (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0546× (z -11.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H2030 (line)]] | alt | 4.43 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0602× (z -8.9) |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP2]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LINC00466]] | +0.69 | +0.69 / +0.44 | both halves | 3e-05 | **novel candidate** |
| [[LINC02026]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[TMEM139-AS1]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TMCC1-DT]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[DMXL1-DT]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RFPL1S]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[LINC01013]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TMLHE-AS1]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[LINC03036]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM66C]] | B | FAM66C activity raises ABCA17P's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without FAM66C | 0.082 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | ABCA17P activity raises KATNAL2's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without ABCA17P | 0.014 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[PPEF1]] | B | ABCA17P activity raises PPEF1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without ABCA17P | 0.025 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[ZNF48]] | B | ABCA17P activity raises ZNF48's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without ABCA17P | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[DGCR5]] | B | ABCA17P activity raises DGCR5's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without ABCA17P | 0.031 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[SYT9-AS1]] | B | ABCA17P activity raises SYT9-AS1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without ABCA17P | 0.032 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[TMEM266]] | B | ABCA17P activity raises TMEM266's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without ABCA17P | 0.039 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[LINC00466]] | B | ABCA17P activity raises LINC00466's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without ABCA17P | 0.040 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[TMEM139-AS1]] | B | ABCA17P activity raises TMEM139-AS1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without ABCA17P | 0.051 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[ZFP2]] | B | ABCA17P activity raises ZFP2's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without ABCA17P | 0.051 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[MIR1915HG]] | B | ABCA17P activity raises MIR1915HG's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without ABCA17P | 0.063 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[ANKRD20A11P]] | B | ABCA17P activity raises ANKRD20A11P's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without ABCA17P | 0.064 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[GPLD1]] | B | ABCA17P activity raises GPLD1's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without ABCA17P | 0.075 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.5, 31.1); signed map (36.4, -9.5). **Vector** length 45.6, 6.93% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.2 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 17, pseudogene |
| Locus type | pseudogene |
| Location | 16p13.3 — chr16:2,361,144-2,425,685 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | ATP binding cassette subfamily A; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [650655](https://www.ncbi.nlm.nih.gov/gene/650655):

> Predicted to act upstream of or within neutral lipid metabolic process. Predicted to be located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32972) · Entrez [650655](https://www.ncbi.nlm.nih.gov/gene/650655) · Ensembl [ENSG00000238098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238098)

## Data

Gene col 14168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14168); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14168]; `tensor/DDL_lfc|DDL_z.npy` [14168]; `embed/gene_vectors.npy` [14168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14168 or target_col == 14168). Every well: [[ABCA17P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA17P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
