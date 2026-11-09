---
symbol: "SEMA7A"
type: "gene"
col: 6197
ensembl_id: "ENSG00000138623"
name: "semaphorin 7A (JohnMiltonHagen blood group)"
location: "15q24.1"
module: 34
arm: "+"
pooled_cpm: 14.14
n_lines_expressing: 37
n_dd_up: 20
n_dd_down: 27
n_dd_up_clean: 15
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 12
direction_downstream: 7
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# SEMA7A

*semaphorin 7A (JohnMiltonHagen blood group)* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.16× (z +11.1, q 9e-26, up in 23 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.625× (z -5.2, q 1e-04, down in 15 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMCC3]] (+0.74, fdr 7e-06), [[PLAUR]] (+0.72, fdr 7e-06), [[RAC2]] (+0.68, fdr 1e-05); moves opposite to [[SNX13]] (-0.65, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); 7 go from it, the strongest it → [[PPARD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +11.1 | 9e-26 | 23/34 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +10.3 | 2e-22 | 23/34 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +8.6 | 2e-15 | 22/33 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +8.6 | 2e-15 | 15/29 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +6.8 | 1e-09 | 19/34 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.55×** | +6.0 | 2e-07 | 15/34 (HT-29, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.84×** | +5.9 | 3e-07 | 16/33 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.72×** | +5.2 | 1e-05 | 16/32 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +5.1 | 2e-05 | 13/34 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 8e-05 | 15/33 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.61×** | +4.6 | 2e-04 | 16/33 (LoVo, HT-29, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.40×** | +4.4 | 5e-04 | 13/29 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.3 | 9e-04 | 13/34 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +4.1 | 0.002 | 15/29 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 6/33 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.006 | 9/32 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +3.3 | 0.026 | 15/31 (PANC-1, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.070 | 11/33 (HT-29, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, none with an alert; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.625×** | -5.2 | 1e-04 | 15/34 (HOP62, RKO, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.645×** | -5.0 | 1e-04 | 14/34 (HOP62, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.595×** | -5.0 | 1e-04 | 15/33 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.637×** | -4.8 | 2e-04 | 14/35 (HOP62, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.602×** | -4.5 | 8e-04 | 12/33 (HOP62, RKO, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.711×** | -4.5 | 8e-04 | 16/35 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.621×** | -4.4 | 9e-04 | 18/33 (RKO, HOP62, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.635×** | -4.4 | 1e-03 | 17/33 (HOP62, RKO, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.009 | 13/35 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled); position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -3.8 | 0.009 | 12/33 (NCI-H2347, HS-578T, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.478×** | -3.7 | 0.011 | 15/28 (KATO III, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.681×** | -3.7 | 0.011 | 13/32 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.011 | 17/34 (RKO, SW 1088, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.685×** | -3.6 | 0.012 | 13/33 (HOP62, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.772×** | -3.5 | 0.021 | 10/34 (HOP62, RKO, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 67.1 | 0 | 11 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.339× (z -20.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.217× (z -9.9) |
| [[RKO (line)]] | wt | 27.6 | 0 | 6 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0300× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 73.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.176× (z -8.5) |
| [[A498 (line)]] | wt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0814× (z -9.1) |
| [[A-172 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCC3]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 | same gene group |
| [[PLAUR]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |
| [[RAC2]] | +0.68 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[RASA3]] | +0.68 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PPARD]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GDPD5]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BCL2A1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ZNF185]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PXN]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX13]] | -0.65 | -0.52 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises SEMA7A's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without G0S2 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[LAMB3]] | B | LAMB3 activity raises SEMA7A's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.98× lower at baseline in the lines without LAMB3 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[BCL2A1]] | B | BCL2A1 activity raises SEMA7A's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without BCL2A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[IL11]] | B | IL11 activity raises SEMA7A's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without IL11 | 0.024 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[G0S2]] | B | G0S2 activity weakens SEMA7A's drug response | lines that do not express G0S2 (22) vs lines expressing it (13) | the lines without G0S2 respond 1.45× as strongly (z diff -0.83); strongest at Panobinostat 0.5 µM: 2.52x vs 1.44x (z diff -2.3) | 0.039 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; target measured in part of the lines; both ways; artifact flags |
| [[COL6A2]] | B | COL6A2 activity raises SEMA7A's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without COL6A2 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[NR3C1]] | B | NR3C1 activity lowers SEMA7A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[IRF6]] | B | IRF6 activity strengthens SEMA7A's drug response | lines that do not express IRF6 (22) vs lines expressing it (13) | the lines without IRF6 respond 0.65× as strongly (z diff +0.71); strongest at Vinblastine (sulfate) 5 µM: 1.17x vs 2.26x (z diff +3.4) | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |
| [[F3]] | B | F3 activity raises SEMA7A's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without F3 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[MICAL2]] | B | MICAL2 activity raises SEMA7A's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without MICAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[CSF1R]] | B | CSF1R activity raises SEMA7A's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without CSF1R | 0.094 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[KCNN3]] | B | KCNN3 activity lowers SEMA7A's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 1.95× higher at baseline in the lines without KCNN3 | 0.098 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPARD]] | B | SEMA7A activity raises PPARD's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without SEMA7A | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NGRN]] | B | SEMA7A activity raises NGRN's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without SEMA7A | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HBEGF]] | B | SEMA7A activity raises HBEGF's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without SEMA7A | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARID3B]] | B | SEMA7A activity raises ARID3B's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without SEMA7A | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FNDC3A]] | B | SEMA7A activity lowers FNDC3A's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.47× higher at baseline in the lines without SEMA7A | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP20DC]] | B | SEMA7A activity raises CFAP20DC's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without SEMA7A | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[APBB2]] | B | SEMA7A activity raises APBB2's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without SEMA7A | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 1.2); signed map (0.4, 46.4). **Vector** length 104, 28.8% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +10.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -5.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 7A (JohnMiltonHagen blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,409,289-74,433,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H-Sema-L, CD108; previously SEMAL |
| Gene groups (HGNC) | Blood group antigens; CD molecules; Immunoglobulin like domain containing; Semaphorins; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O75326](https://www.uniprot.org/uniprotkb/O75326) (Semaphorin-7A):

> Plays an important role in integrin-mediated signaling and functions both in regulating cell migration and immune responses. Promotes formation of focal adhesion complexes, activation of the protein kinase PTK2/FAK1 and subsequent phosphorylation of MAPK1 and MAPK3. Promotes production of pro-inflammatory cytokines by monocytes and macrophages. Plays an important role in modulating inflammation and T-cell-mediated immune responses. Promotes axon growth in the embryonic olfactory bulb. Promotes …

**Summary**, from NCBI Gene [8482](https://www.ncbi.nlm.nih.gov/gene/8482):

> This gene encodes a member of the semaphorin family of proteins. The encoded preproprotein is proteolytically processed to generate the mature glycosylphosphatidylinositol (GPI)-anchored membrane glycoprotein. The encoded protein is found on activated lymphocytes and erythrocytes and may be involved in immunomodulatory and neuronal processes. The encoded protein carries the John Milton Hagen (JMH) blood group antigens. Mutations in this gene may be associated with reduced bone mineral density …

**Accessions** — [HGNC:10741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10741) · Entrez [8482](https://www.ncbi.nlm.nih.gov/gene/8482) · UniProt [O75326](https://www.uniprot.org/uniprotkb/O75326) · Ensembl [ENSG00000138623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138623)

## Data

Gene col 6197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6197); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6197]; `tensor/DDL_lfc|DDL_z.npy` [6197]; `embed/gene_vectors.npy` [6197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6197 or target_col == 6197). Every well: [[SEMA7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
