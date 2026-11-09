---
symbol: "TERT"
type: "gene"
col: 8938
ensembl_id: "ENSG00000164362"
name: "telomerase reverse transcriptase"
location: "5p15.33"
module: 6
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 37
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 48
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TERT

*telomerase reverse transcriptase* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +11.0, q 2e-25, up in 1 of 3 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +9.7, q 7e-20, up in 10 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.543× (z -5.8, q 5e-06, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTPS1]] (+0.65, fdr 7e-06), [[UHRF1]] (+0.64, fdr 1e-05), [[C19orf48]] (+0.64, fdr 1e-05); moves opposite to [[YPEL5]] (-0.61, fdr 1e-05), [[ATP6V1G1]] (-0.60, fdr 7e-05), [[ZFYVE1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MSRB3-AS1]] → it (grade B ⚠); 48 go from it, the strongest it → [[TSEN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.39×** | +11.0 | 2e-25 | 1/3 (hTERT-HPNE) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +9.7 | 7e-20 | 10/26 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.62×** | +8.4 | 1e-14 | 1/5 (hTERT-HPNE) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.25×** | +7.6 | 3e-12 | 15/32 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +6.2 | 7e-08 | 8/29 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +4.7 | 3e-04 | 11/32 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.59×** | +4.4 | 0.001 | 9/30 (HOP62, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.57×** | +4.2 | 0.002 | 2/14 (HEC-1-A, hTERT-HPNE) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.54×** | +4.0 | 0.003 | 7/31 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.26×** | +4.0 | 0.004 | 5/20 (NCI-H460, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.48×** | +3.6 | 0.019 | 0/14 | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.01×** | +3.4 | 0.028 | 2/19 (NCI-H460, NCI-H23) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.033 | 2/22 (NCI-H1573, NCI-H2030) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.43×** | +3.3 | 0.035 | 3/32 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.040 | 1/21 (LoVo) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.085 | 4/20 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.098 | 1/27 (Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.543×** | -5.8 | 5e-06 | 15/30 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.703×** | -4.7 | 7e-04 | 11/32 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.632×** | -4.3 | 0.003 | 9/27 (SNU-1, HS-578T, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.718×** | -3.9 | 0.011 | 9/30 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.688×** | -3.9 | 0.011 | 11/32 (A-427, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.674×** | -3.7 | 0.017 | 12/29 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.7 | 0.017 | 15/27 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.765×** | -3.6 | 0.025 | 12/31 (A-427, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.052 | 7/29 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.055 | 9/31 (A-427, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -12.1) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0907× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -10.4) |
| [[KATO III (line)]] | alt | 3.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 5.15 | 0 | 2 | — | [[Artemether (drug)]] 0.5 µM 0.0462× (z -11.6) |
| [[BT-474 (line)]] | alt | 1.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.8× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 3.57 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0656× (z -8.8) |
| [[SW48 (line)]] | wt | 2.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.9× (z +11.2) | — |
| [[SW480 (line)]] | alt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +10.7) | — |
| [[A-172 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.390 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS1]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.64 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[C19orf48]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 | STRING 426 |
| [[DNMT1]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 | STRING 530 |
| [[PFAS]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[POLE]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 | STRING 461 |
| [[CDC7]] | +0.58 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[CEP83]] | +0.58 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[BRME1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MCM4]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[POLA1]] | +0.57 | +0.36 / +0.70 | both halves | 9e-05 | pathway: Chromosome Maintenance |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.60 | -0.37 / -0.63 | both halves | 7e-05 | pathway: MITF-M-dependent gene expression |
| [[ZFYVE1]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NPC2]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ATP6V1E1]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 | pathway: MITF-M-dependent gene expression |
| [[TMEM59]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PSAP]] | -0.53 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[UBE2H]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RNASEK]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[NEU1]] | -0.52 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PRR13]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[WBP1]] | -0.52 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSRB3-AS1]] | B | MSRB3-AS1 activity raises TERT's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 1.94× lower at baseline in the lines without MSRB3-AS1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[NT5M]] | B | NT5M activity raises TERT's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without NT5M | 0.082 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[KCNQ5]] | B | KCNQ5 activity raises TERT's level | lines that do not express KCNQ5 (25) vs lines expressing it (25) | 1.45× lower at baseline in the lines without KCNQ5 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, PRR16, FAP |
| [[VASH1]] | B | VASH1 activity raises TERT's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without VASH1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[GCG]] | C | GCG activity raises TERT's level | lines that do not express GCG (46) vs lines expressing it (4) | 2.95× lower at baseline in the lines without GCG | 0.088 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 43, C 5. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | B | TERT activity raises TSEN2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without TERT | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[TMEM59]] | B | TERT activity lowers TMEM59's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.47× higher at baseline in the lines without TERT | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[SLFNL1-AS1]] | B | TERT activity raises SLFNL1-AS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without TERT | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CTPS1]] | B | TERT activity raises CTPS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without TERT | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[WDR4]] | B | TERT activity raises WDR4's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without TERT | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[TRAP1]] | B | TERT activity raises TRAP1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[URB2]] | B | TERT activity raises URB2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[NT5M]] | B | TERT activity raises NT5M's level | lines that do not express TERT (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CAD]] | B | TERT activity raises CAD's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[SF3B3]] | B | TERT activity raises SF3B3's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[RAD51D]] | B | TERT activity raises RAD51D's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CEP83]] | B | TERT activity weakens CEP83's drug response | lines that do not express TERT (13) vs lines expressing it (37) | the lines without TERT respond 1.29× as strongly (z diff -0.54); strongest at Homoharringtonine 0.5 µM: 2.38x vs 1.40x (z diff -3.4) | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-23.9, -45.6); signed map (-33.2, -50.8). **Vector** length 60.8, 11.7% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.0 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +1.9 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.0 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.0 | -3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.9 | -4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.8 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | telomerase reverse transcriptase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,253,147-1,295,068 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRT, TP2, TCS1, hEST2, EST2 |
| Gene groups (HGNC) | Telomerase holoenzyme subunits |
| Reactome | 11 pathways, smallest: Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence; Telomere Extension By Telomerase; Formation of the beta-catenin:TCF transactivating complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O14746](https://www.uniprot.org/uniprotkb/O14746) (Telomerase reverse transcriptase):

> Telomerase is a ribonucleoprotein enzyme essential for the replication of chromosome termini in most eukaryotes. Active in progenitor and cancer cells. Inactive, or very low activity, in normal somatic cells. Catalytic component of the teleromerase holoenzyme complex whose main activity is the elongation of telomeres by acting as a reverse transcriptase that adds simple sequence repeats to chromosome ends by copying a template sequence within the RNA component of the enzyme. Catalyzes the …

**Summary**, from NCBI Gene [7015](https://www.ncbi.nlm.nih.gov/gene/7015):

> Telomerase is a ribonucleoprotein polymerase that maintains telomere ends by addition of the telomere repeat TTAGGG. The enzyme consists of a protein component with reverse transcriptase activity, encoded by this gene, and an RNA component which serves as a template for the telomere repeat. Telomerase expression plays a role in cellular senescence, as it is normally repressed in postnatal somatic cells resulting in progressive shortening of telomeres. Deregulation of telomerase expression in …

**Accessions** — [HGNC:11730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11730) · Entrez [7015](https://www.ncbi.nlm.nih.gov/gene/7015) · UniProt [O14746](https://www.uniprot.org/uniprotkb/O14746) · Ensembl [ENSG00000164362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164362)

## Data

Gene col 8938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8938); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8938]; `tensor/DDL_lfc|DDL_z.npy` [8938]; `embed/gene_vectors.npy` [8938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8938 or target_col == 8938). Every well: [[TERT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TERT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
