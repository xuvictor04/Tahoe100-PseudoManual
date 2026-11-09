---
symbol: "TMEM64"
type: "gene"
col: 11123
ensembl_id: "ENSG00000180694"
name: "transmembrane protein 64"
location: "8q21.3"
module: 25
arm: "+"
pooled_cpm: 16.39
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TMEM64

*transmembrane protein 64* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.89× (z +10.7, q 5e-24, up in 18 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.61× (z +8.4, q 5e-15, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.932× (z -4.2, q 0.013, down in 5 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.808× (z -3.7, q 0.053, down in 18 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.399×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3HAV1L]] (+0.66, fdr 1e-05), [[LRRC58]] (+0.65, fdr 7e-06), [[SLC35G1]] (+0.63, fdr 1e-05); moves opposite to [[VRK3]] (-0.63, fdr 7e-06), [[SAP30BP]] (-0.57, fdr 1e-05), [[PMM1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PTGFRN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +10.7 | 5e-24 | 18/26 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +10.3 | 2e-22 | 27/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +8.6 | 2e-15 | 22/37 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.4 | 5e-15 | 26/46 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +8.4 | 8e-15 | 27/47 (A498, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +8.1 | 5e-14 | 29/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +7.9 | 3e-13 | 30/43 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.6 | 2e-12 | 25/45 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +6.4 | 8e-09 | 21/46 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +6.0 | 1e-07 | 22/46 (A498, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.9 | 2e-07 | 19/45 (A498, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 8e-07 | 20/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.5 | 2e-06 | 22/47 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.3 | 5e-06 | 18/43 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 16/44 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.005 | 6/46 (C32, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 11/46 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 13/46 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.062 | 4/47 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.092 | 4/46 (C-33 A, SNU-423, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.092 | 7/46 (C32, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.36×** | +2.8 | 0.096 | 5/45 (AsPC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.12× | +2.8 | 0.097 | 2/47 (NCI-H1792, SW1417) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.399×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.2 | 0.013 | 5/47 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.808×** | -3.7 | 0.053 | 18/45 (CHP-212, NCI-H1573, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.099 | 12/46 (NCI-H1573, A-427, …) | two highest doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.766× | -3.3 | 0.12 | 8/46 (NCI-H2030, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.785× | -3.0 | 0.28 | 12/45 (SW 900, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.80× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +10.5) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[J82 (line)]] | alt | 22.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.1) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HAV1L]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LRRC58]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SLC35G1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SLC25A30]] | +0.60 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[PON2]] | +0.59 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[MANEA]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[RAVER2]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CIPC]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[FUT10]] | +0.57 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[USP46]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NCS1]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PM20D2]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK3]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[SAP30BP]] | -0.57 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PMM1]] | -0.57 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[GON4L]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ZNF324]] | -0.55 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[POLD4]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[POLR2J4]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZER1]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[OSBPL2]] | -0.54 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[DNTTIP1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ENDOV]] | -0.53 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[TECPR1]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGFRN]] | B | PTGFRN activity lowers TMEM64's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.27× higher at baseline in the lines without PTGFRN | 0.031 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[NCS1]] | B | NCS1 activity raises TMEM64's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without NCS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[STEAP2]] | B | STEAP2 activity lowers TMEM64's level | lines that do not express STEAP2 (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without STEAP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP1, FCGRT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-15.7, -5.5); signed map (-14.0, -40.7). **Vector** length 86.1, 17.5% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 64 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:90,621,995-90,791,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762C1112 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6YI46](https://www.uniprot.org/uniprotkb/Q6YI46) (Transmembrane protein 64):

> Positively regulates TNFSF11-induced osteoclast differentiation. Acts as a regulator of TNFSF11-mediated Ca(2+) signaling pathways via its interaction with SERCA2 which is critical for the TNFSF11-induced CREB1 activation and mitochondrial ROS generation necessary for proper osteoclast generation. Association between TMEM64 and SERCA2 in the ER leads to cytosolic Ca (2+) spiking for activation of NFATC1 and production of mitochondrial ROS, thereby triggering Ca (2+) signaling cascades that …

**Summary**, from NCBI Gene [169200](https://www.ncbi.nlm.nih.gov/gene/169200):

> Predicted to be involved in several processes, including negative regulation of canonical Wnt signaling pathway; negative regulation of osteoblast differentiation; and positive regulation of cell differentiation. Predicted to act upstream of or within regulation of ATP-dependent activity. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25441) · Entrez [169200](https://www.ncbi.nlm.nih.gov/gene/169200) · UniProt [Q6YI46](https://www.uniprot.org/uniprotkb/Q6YI46) · Ensembl [ENSG00000180694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180694)

## Data

Gene col 11123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11123); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11123]; `tensor/DDL_lfc|DDL_z.npy` [11123]; `embed/gene_vectors.npy` [11123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11123 or target_col == 11123). Every well: [[TMEM64 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM64.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
