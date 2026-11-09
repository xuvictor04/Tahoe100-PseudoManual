---
symbol: "NUDT13"
type: "gene"
col: 9282
ensembl_id: "ENSG00000166321"
name: "nudix hydrolase 13"
location: "10q22.2"
module: 15
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NUDT13

*nudix hydrolase 13* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.85× (z +8.7, q 2e-15, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.34× (z +4.1, q 0.006, up in 6 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.633× (z -9.5, q 1e-18, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1CB-DT]] (+0.65, fdr 1e-05), [[VPS13B-DT]] (+0.61, fdr 1e-05), [[PHC2-AS1]] (+0.59, fdr 4e-05); moves opposite to [[DPF1]] (-0.55, fdr 5e-05), [[EPHB1]] (-0.52, fdr 1e-04), [[MAP1S]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DLX6-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.7 | 2e-15 | 1/7 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.3 | 7e-08 | 9/26 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +5.3 | 3e-05 | 2/12 (MIA PaCa-2, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.006 | 6/44 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.052 | 11/42 (SW480, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.052 | 13/41 (SW48, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.081 | 4/43 (SW480, HT-29, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.12 | 5/44 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.16× | +3.1 | 0.12 | 3/45 (COLO 205, SNU-1, …) | top dose only | low cells (technical?) |
| [[Triamcinolone (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.15 | 3/45 (A549, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -9.5 | 1e-18 | 21/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.594×** | -7.6 | 6e-12 | 20/46 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.612×** | -7.2 | 1e-10 | 21/47 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.601×** | -7.1 | 1e-10 | 19/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -6.9 | 5e-10 | 21/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -6.4 | 2e-08 | 17/38 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.688×** | -5.5 | 3e-06 | 15/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.744×** | -4.2 | 0.002 | 12/33 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.002 | 14/47 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.773×** | -3.8 | 0.009 | 11/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.798×** | -3.3 | 0.050 | 5/46 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.811× | -3.1 | 0.10 | 8/47 (SW480, CHP-212, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.10 | 0 | 2 (1 ⚠) | — | [[Trimetrexate (drug)]] 0.5 µM 0.0731× (z -10.6) |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.4) |
| [[C-33 A (line)]] | alt | 7.45 | 0 | 1 | — | [[Altretamine (drug)]] 0.05 µM 0.0666× (z -8.9) |
| [[HT-29 (line)]] | alt | 3.94 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0826× (z -8.6) |
| [[J82 (line)]] | alt | 2.94 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0984× (z -8.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 6.06 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0961× (z -9.0) |
| [[SW480 (line)]] | alt | 8.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.4) |
| [[A-172 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CB-DT]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PHC2-AS1]] | +0.59 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SEC24B-AS1]] | +0.59 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[COPS8-DT]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDNF]] | +0.57 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[NIFK-AS1]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[INHA]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[C14orf93]] | +0.57 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[PRDX6-AS1]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.56 | +0.40 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[EPHB1]] | -0.52 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MAP1S]] | -0.52 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[TIAM1]] | -0.52 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LRWD1]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GDPD5]] | -0.51 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ORAI1]] | -0.50 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[PGBD5]] | -0.49 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[C3orf52]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TMCC3]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[RMC1]] | -0.48 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[CIAO1]] | -0.47 | -0.35 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises NUDT13's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.21× lower at baseline in the lines without DLX6-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[SMPD3]] | B | SMPD3 activity raises NUDT13's level | lines that do not express SMPD3 (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without SMPD3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with NF1; maybe low, not absent |
| [[FLJ12825]] | B | FLJ12825 activity raises NUDT13's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 1.15× lower at baseline in the lines without FLJ12825 | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent |
| [[HOXC4]] | B | HOXC4 activity raises NUDT13's level | lines that do not express HOXC4 (11) vs lines expressing it (39) | 1.22× lower at baseline in the lines without HOXC4 | 0.095 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.3, 23.7); signed map (34.2, -14.8). **Vector** length 44.2, 4.57% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -9.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.0 | -7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.0 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -0.9 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,110,375-73,131,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586P2219 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X67](https://www.uniprot.org/uniprotkb/Q86X67) (NAD(P)H pyrophosphatase NUDT13, mitochondrial):

> NAD(P)H pyrophosphatase that hydrolyzes NADH into NMNH and AMP, and NADPH into NMNH and 2',5'-ADP. Has a marked preference for the reduced pyridine nucleotides. Does not show activity toward NAD-capped RNAs; the NAD-cap is an atypical cap present at the 5'-end of some RNAs.

**Summary**, from NCBI Gene [25961](https://www.ncbi.nlm.nih.gov/gene/25961):

> Predicted to enable NADH pyrophosphatase activity. Predicted to be involved in nucleobase-containing small molecule interconversion. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18827) · Entrez [25961](https://www.ncbi.nlm.nih.gov/gene/25961) · UniProt [Q86X67](https://www.uniprot.org/uniprotkb/Q86X67) · Ensembl [ENSG00000166321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166321)

## Data

Gene col 9282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9282); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9282]; `tensor/DDL_lfc|DDL_z.npy` [9282]; `embed/gene_vectors.npy` [9282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9282 or target_col == 9282). Every well: [[NUDT13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
