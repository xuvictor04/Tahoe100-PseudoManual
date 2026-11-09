---
symbol: "ZNF518B"
type: "gene"
col: 10903
ensembl_id: "ENSG00000178163"
name: "zinc finger protein 518B"
location: "4p16.1"
module: 16
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 34
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF518B

*zinc finger protein 518B* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.86× (z +6.2, q 3e-07, up in 20 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.596× (z -5.2, q 1e-04, down in 17 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.649× (z -4.3, q 0.003, down in 12 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0837×, C-33 A 0.0435×; ⚠ cell-cycle shift, explains ~56% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0803×, SNU-1 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.114×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF260]] (+0.78, fdr 7e-06), [[CENPBD1P]] (+0.76, fdr 7e-06), [[LIG4]] (+0.75, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.68, fdr 7e-06), [[CBFA2T2]] (-0.68, fdr 7e-06), [[DPM1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF845]] → it (grade B ⚠); 6 go from it, the strongest it → [[COG7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.86×** | +6.2 | 3e-07 | 20/31 (PANC-1, SNU-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +6.0 | 7e-07 | 18/30 (NCI-H1792, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +5.9 | 7e-07 | 16/30 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.7 | 4e-04 | 14/31 (BT-474, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.7 | 0.028 | 5/14 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.028 | 13/30 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.028 | 7/16 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.37× | +3.1 | 0.12 | 7/31 (A-427, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.24× | +3.0 | 0.15 | 10/32 (A498, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10903.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0837×, C-33 A 0.0435×; ⚠ cell-cycle shift, explains ~56% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (J82 0.0803×, SNU-1 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.596×** | -5.2 | 1e-04 | 17/28 (J82, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.639×** | -4.5 | 0.002 | 12/31 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -4.3 | 0.003 | 12/31 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.770×** | -3.7 | 0.030 | 14/30 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.700×** | -3.6 | 0.039 | 11/31 (SNU-423, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0435× (z -14.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 8.84 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0837× (z -15.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.539 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF260]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | same gene group |
| [[CENPBD1P]] | +0.76 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[LIG4]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 | same gene group |
| [[C7orf25]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[PUF60]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PPP2CA]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SLC35F6]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[VEZF1]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 | same gene group |
| [[BBS10]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[COA7]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.68 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.68 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[DPM1]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.66 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[TMEM50B]] | -0.65 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[GMCL1]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.63 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[GNRH1]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[COG7]] | -0.63 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[NARF]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.62 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PTMA]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF845]] | B | ZNF845 activity raises ZNF518B's level | lines that do not express ZNF845 (5) vs lines expressing it (45) | 3.39× lower at baseline in the lines without ZNF845 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF160, ZNF468, ZNF761 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COG7]] | B | ZNF518B activity raises COG7's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without ZNF518B | 0.014 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[DNAJA2]] | B | ZNF518B activity lowers DNAJA2's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.32× higher at baseline in the lines without ZNF518B | 0.034 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[KIF7]] | B | ZNF518B activity raises KIF7's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without ZNF518B | 0.053 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[ZSCAN30]] | B | ZNF518B activity raises ZSCAN30's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ZNF518B | 0.062 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[PUF60]] | B | ZNF518B activity lowers PUF60's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.20× higher at baseline in the lines without ZNF518B | 0.072 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[GDAP1]] | B | ZNF518B activity lowers GDAP1's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without ZNF518B | 0.084 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.3, 12.7); signed map (2.4, -29.9). **Vector** length 59.6, 12.3% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.1 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 518B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:10,439,880-10,457,426 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1729 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D4](https://www.uniprot.org/uniprotkb/Q9C0D4) (Zinc finger protein 518B):

> Through its association with the EHMT1-EHMT2/G9A and PRC2/EED-EZH2 histone methyltransferase complexes may function in gene silencing, regulating repressive post-translational methylation of histone tails at promoters of target genes.

**Summary**, from NCBI Gene [85460](https://www.ncbi.nlm.nih.gov/gene/85460):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29365) · Entrez [85460](https://www.ncbi.nlm.nih.gov/gene/85460) · UniProt [Q9C0D4](https://www.uniprot.org/uniprotkb/Q9C0D4) · Ensembl [ENSG00000178163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178163)

## Data

Gene col 10903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10903); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10903]; `tensor/DDL_lfc|DDL_z.npy` [10903]; `embed/gene_vectors.npy` [10903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10903 or target_col == 10903). Every well: [[ZNF518B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF518B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
