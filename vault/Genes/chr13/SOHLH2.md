---
symbol: "SOHLH2"
type: "gene"
col: 4200
ensembl_id: "ENSG00000120669"
name: "spermatogenesis and oogenesis specific basic helix-loop-helix 2"
location: "13q13.3"
module: 121
arm: "+"
pooled_cpm: 2.88
n_lines_expressing: 29
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# SOHLH2

*spermatogenesis and oogenesis specific basic helix-loop-helix 2* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.72× (z +12.7, q 4e-34, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +9.5, q 5e-19, up in 8 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0835×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.101×; ⚠ cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.227×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.417×); [[Simotinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0865×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC169]] (+0.71, fdr 7e-06, ⚠ same locus), [[SLC25A13]] (+0.62, fdr 1e-05), [[LINC00882]] (+0.59, fdr 1e-05), [[TLL1]] (+0.59, fdr 1e-05); moves opposite to [[TMEM50B]] (-0.59, fdr 2e-05), [[DZANK1]] (-0.53, fdr 7e-04), [[APAF1]] (-0.51, fdr 8e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01266]] → it (grade B ⚠); 2 go from it, the strongest it → [[CNTNAP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.72×** | +12.7 | 4e-34 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +11.1 | 5e-26 | 3/10 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +9.5 | 5e-19 | 8/18 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +7.8 | 1e-12 | 1/6 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.7 | 2e-09 | 2/17 (PANC-1, NCI-H2347) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +5.3 | 1e-05 | 4/23 (NCI-H460, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.0 | 4e-05 | 7/24 (HOP62, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +4.8 | 1e-04 | 7/16 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.4 | 7e-04 | 3/13 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.001 | 6/20 (A-172, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 4/24 (SW 900, J82, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +3.6 | 0.017 | 1/6 (NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.017 | 3/11 (SK-MEL-2, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.62×** | +3.4 | 0.027 | 3/15 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.3 | 0.032 | 2/9 (NCI-H1573, J82) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.033 | 6/20 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.068 | 3/20 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +2.9 | 0.093 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.51×** | +2.9 | 0.099 | 1/15 (A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4200.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0835×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.101×; ⚠ cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.227×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.417×); [[Simotinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0865×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Captopril (drug)]] 5 µM |  | 0.661× | -3.1 | 0.98 | 8/25 (LS 180, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 59.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.61 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +9.6) | [[Simotinib (drug)]] 0.05 µM 0.0865× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0835× (z -12.6) |
| [[A-172 (line)]] | wt | 1.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +8.5) | — |
| [[A-427 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.995 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.954 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.852 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.287 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC169]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | STRING 522; ⚠ same locus (7.4 kb, same strand: neighbours can correlate without regulation) |
| [[SLC25A13]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TLL1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DPY19L2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[COA7]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ACBD6]] | +0.57 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[KCNT2]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SNHG26]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[DNAH14]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ZNF317]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MGA]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DZANK1]] | -0.53 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[APAF1]] | -0.51 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[PIN1]] | -0.51 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[GDAP2]] | -0.50 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MXD4]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 | same gene group |
| [[ATP6AP2]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[IFI27L1]] | -0.49 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ARL3]] | -0.49 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[P3H1]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[DHTKD1]] | -0.49 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[MOSPD3]] | -0.49 | -0.59 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01266]] | B | LINC01266 activity raises SOHLH2's level | lines that do not express LINC01266 (35) vs lines expressing it (15) | 1.98× lower at baseline in the lines without LINC01266 | 0.091 | ⚠ within organs, on part of the lines; also absent: UNC5D, KHDRBS2, ENSG00000260958; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3]] | B | SOHLH2 activity lowers CNTNAP3's level | lines that do not express SOHLH2 (21) vs lines expressing it (29) | 1.50× higher at baseline in the lines without SOHLH2 | 0.084 | ⚠ within organs, on part of the lines; also absent: PRR16, LINC00839, GUCY1B1 |
| [[CCDC169]] | C | SOHLH2 activity raises CCDC169's level | lines that do not express SOHLH2 (21) vs lines expressing it (29) | 3.15× lower at baseline in the lines without SOHLH2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRR16, LINC00839, GUCY1B1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.3, 26.6); signed map (45.1, 26.4). **Vector** length 33.9, 5.18% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.9 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -0.7 | -1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis and oogenesis specific basic helix-loop-helix 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,168,217-36,214,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20449, TEB1, bHLHe81, SPATA28 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX45](https://www.uniprot.org/uniprotkb/Q9NX45) (Spermatogenesis- and oogenesis-specific basic helix-loop-helix-containing protein 2):

> Transcription regulator of both male and female germline differentiation. Suppresses genes involved in spermatogonial stem cells maintenance, and induces genes important for spermatogonial differentiation. Coordinates oocyte differentiation without affecting meiosis I (By similarity).

**Summary**, from NCBI Gene [54937](https://www.ncbi.nlm.nih.gov/gene/54937):

> This gene encodes one of testis-specific transcription factors which are essential for spermatogenesis, oogenesis and folliculogenesis. This gene is located on chromosome 13. The proteins encoded by this gene and another testis-specific transcription factor, SOHLH1, can form heterodimers, in addition to homodimers. There is a read-through locus (GeneID: 100526761) that shares sequence identity with this gene and the upstream CCDC169 (GeneID: 728591). Alternatively spliced transcript variants …

**Accessions** — [HGNC:26026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26026) · Entrez [54937](https://www.ncbi.nlm.nih.gov/gene/54937) · UniProt [Q9NX45](https://www.uniprot.org/uniprotkb/Q9NX45) · Ensembl [ENSG00000120669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120669)

## Data

Gene col 4200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4200); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4200]; `tensor/DDL_lfc|DDL_z.npy` [4200]; `embed/gene_vectors.npy` [4200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4200 or target_col == 4200). Every well: [[SOHLH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOHLH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
