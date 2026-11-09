---
symbol: "TSPYL5"
type: "gene"
col: 11115
ensembl_id: "ENSG00000180543"
name: "TSPY like 5"
location: "8q22.1"
module: 16
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 14
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TSPYL5

*TSPY like 5* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.15× (z +12.5, q 3e-33, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.90× (z +6.0, q 2e-07, up in 7 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (PANC-1 0.141×, SK-MEL-2 0.171×, HEC-1-A 0.326×, SHP-77 0.308×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.119×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF677]] (+0.63, fdr 1e-05), [[SLC6A17]] (+0.61, fdr 1e-05), [[RNF180]] (+0.61, fdr 1e-05); moves opposite to [[PMS2P4-1]] (-0.60, fdr 1e-05), [[TNXB]] (-0.51, fdr 2e-04), [[KPNB1-DT]] (-0.51, fdr 4e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCNYL2]], [[CCNYL2-1]] → it (grade C ⚠); 3 go from it, the strongest it → [[ZNF780A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.15×** | +12.5 | 3e-33 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +8.4 | 2e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +8.0 | 2e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.87×** | +6.2 | 6e-08 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +6.2 | 6e-08 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +6.0 | 2e-07 | 7/12 (A549, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +4.6 | 3e-04 | 1/8 (HEC-1-A) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.6 | 3e-04 | 1/7 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.97×** | +4.5 | 5e-04 | 0/8 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.36×** | +4.2 | 0.002 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.2 | 0.002 | 0/8 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +4.1 | 0.002 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.0 | 0.003 | 1/8 (NCI-H2347) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.8 | 0.005 | 0/9 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.85×** | +3.8 | 0.006 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.80×** | +3.6 | 0.012 | 0/8 | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.64×** | +3.3 | 0.036 | 1/8 (A549) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.066 | 5/11 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +3.0 | 0.068 | 1/9 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.074 | 1/9 (A549) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.077 | 0/9 | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.081 | 0/11 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (PANC-1 0.141×, SK-MEL-2 0.171×, HEC-1-A 0.326×, SHP-77 0.308×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.119×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.581× | -3.7 | 0.15 | 0/12 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.601× | -3.4 | 0.15 | 1/12 (C32) | two highest doses |  |
| [[XRK3F2 (drug)]] 5 µM |  | 0.384× | -3.3 | 0.15 | 0/11 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.42 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -13.3) |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.7) |
| [[A-172 (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.731 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.240 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF677]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SLC6A17]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RNF180]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NLRP2]] | +0.60 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ZNF354C]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[B3GALT9]] | +0.58 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SAYSD1]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RANBP2]] | +0.55 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[PDGFD]] | +0.55 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[MSL3P1]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PTPN20]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TRIM68]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TNXB]] | -0.51 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[KPNB1-DT]] | -0.51 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[TTC28-AS1]] | -0.51 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[USP49]] | -0.49 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[PPP1R15B-AS1]] | -0.48 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[TMEM91]] | -0.48 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[LEPR]] | -0.48 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[TMEM50B]] | -0.46 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[TRNAU1AP]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[EOGT-DT]] | -0.46 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNYL2]], [[CCNYL2-1]] | C | CCNYL2, CCNYL2-1 activity raises TSPYL5's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.77× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF780A]] | B | TSPYL5 activity raises ZNF780A's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 1.64× lower at baseline in the lines without TSPYL5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205 |
| [[TMEM50B]] | B | TSPYL5 activity lowers TMEM50B's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 1.21× higher at baseline in the lines without TSPYL5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205 |
| [[CARD18]] | C | TSPYL5 activity raises CARD18's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 2.10× lower at baseline in the lines without TSPYL5 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.4, 22.5); signed map (-4.7, -31.8). **Vector** length 21.5, 4.44% of its response variance represented; |z| ≥ 3 in 222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.7 | +6.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.7 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -3.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.6 | -1.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.5 | -0.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | TSPY like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:97,273,488-97,277,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1750 |
| Gene groups (HGNC) | TSPYL family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VY4](https://www.uniprot.org/uniprotkb/Q86VY4) (Testis-specific Y-encoded-like protein 5):

> Involved in modulation of cell growth and cellular response to gamma radiation probably via regulation of the Akt signaling pathway. Involved in regulation of p53/TP53. Suppresses p53/TP53 protein levels and promotes its ubiquitination; the function is dependent on USP7 and independent on MDM2. Proposed to displace p53/TP53 from interaction with USP7.

**Summary**, from NCBI Gene [85453](https://www.ncbi.nlm.nih.gov/gene/85453):

> Predicted to enable chromatin binding activity and histone binding activity. Involved in several processes, including cellular response to gamma radiation; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and protein homooligomerization. Predicted to be active in chromatin and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29367) · Entrez [85453](https://www.ncbi.nlm.nih.gov/gene/85453) · UniProt [Q86VY4](https://www.uniprot.org/uniprotkb/Q86VY4) · Ensembl [ENSG00000180543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180543)

## Data

Gene col 11115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11115); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11115]; `tensor/DDL_lfc|DDL_z.npy` [11115]; `embed/gene_vectors.npy` [11115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11115 or target_col == 11115). Every well: [[TSPYL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPYL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
