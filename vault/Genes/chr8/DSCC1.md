---
symbol: "DSCC1"
type: "gene"
col: 5952
ensembl_id: "ENSG00000136982"
name: "DNA replication and sister chromatid cohesion 1"
location: "8q24.12"
module: 6
arm: "+"
pooled_cpm: 7.94
n_lines_expressing: 46
n_dd_up: 26
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 94
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DSCC1

*DNA replication and sister chromatid cohesion 1* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (20 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.96× (z +12.0, q 1e-30, up in 36 of 43 measured lines) ⚠ cell-cycle shift, explains ~79% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.43× (z +3.7, q 0.008, up in 7 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.478× (z -11.6, q 3e-28, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.92, fdr 7e-06), [[RFC4]] (+0.91, fdr 7e-06), [[MMS22L]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 94 go from it, the strongest it → [[DDX12P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.96×** | +12.0 | 1e-30 | 36/43 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.56×** | +10.4 | 6e-23 | 33/43 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **2.47×** | +10.0 | 3e-21 | 34/43 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.36×** | +9.5 | 3e-19 | 18/27 (HT-29, A498, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.20×** | +8.7 | 2e-16 | 28/43 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **2.03×** | +7.2 | 5e-11 | 18/32 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.85×** | +6.8 | 8e-10 | 21/43 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.80×** | +6.0 | 1e-07 | 20/39 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.71×** | +5.9 | 2e-07 | 19/41 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.70×** | +5.4 | 4e-06 | 6/13 (HT-29, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.67×** | +5.2 | 8e-06 | 7/15 (HS-578T, HT-29, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.64×** | +5.0 | 2e-05 | 16/38 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.8 | 6e-05 | 12/38 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.50×** | +4.1 | 0.001 | 14/41 (A-427, SHP-77, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +3.9 | 0.003 | 14/43 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.008 | 7/38 (A-427, SHP-77, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.021 | 5/41 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.026 | 6/42 (A-427, HT-29, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.029 | 7/44 (SW480, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.066 | 6/43 (SW480, SW1417, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.094 | 3/40 (SW480, HT-29, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.478×** | -11.6 | 3e-28 | 26/37 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.611×** | -5.5 | 1e-05 | 22/36 (A498, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.616×** | -5.4 | 1e-05 | 22/41 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.525×** | -5.1 | 5e-05 | 17/44 (COLO 205, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.656×** | -4.0 | 0.006 | 15/41 (A-427, KATO III, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.503×** | -4.0 | 0.006 | 14/42 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.787×** | -3.8 | 0.013 | 12/43 (Hs 766T, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.714×** | -3.7 | 0.013 | 12/42 (A498, LS 180, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.682×** | -3.7 | 0.015 | 10/44 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.799×** | -3.5 | 0.024 | 15/42 (A498, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.713×** | -3.5 | 0.028 | 16/40 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.748×** | -3.2 | 0.055 | 9/41 (PANC-1, RKO, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.730×** | -3.2 | 0.055 | 12/41 (SW480, NCI-H460, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.733×** | -3.2 | 0.060 | 15/41 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.585×** | -3.1 | 0.072 | 12/37 (A498, Panc 03.27, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.076 | 14/43 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.53 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.126× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.3) |
| [[A498 (line)]] | wt | 11.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.164× (z -15.1) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H460 (line)]] | wt | 4.10 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.115× (z -9.4) |
| [[PANC-1 (line)]] | alt | 9.12 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.6) |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.108× (z -10.3) |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.185× (z -10.7) ⚠ cell-cycle shift, explains ~80% of this change |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0961× (z -12.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 6.39 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0873× (z -9.0) |
| [[RKO (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0643× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.256× (z -8.6) |
| [[SW48 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0826× (z -9.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.4) |
| [[A-172 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | STRING 727 |
| [[RFC4]] | +0.91 | +0.87 / +0.89 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 998 |
| [[MMS22L]] | +0.90 | +0.86 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[BLM]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 451 |
| [[RAD54L]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | STRING 502 |
| [[DTL]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | STRING 639 |
| [[CDC45]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | STRING 795 |
| [[WDR76]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | STRING 463 |
| [[WDHD1]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | STRING 880 |
| [[FANCI]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 |  |
| [[GINS2]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | STRING 718 |
| [[NCAPD3]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DSCC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYTL4]] | B | SYTL4 activity lowers DSCC1's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.26× higher at baseline in the lines without SYTL4 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[E2F2]] | B | E2F2 activity raises DSCC1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without E2F2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | C | CDC25A activity raises DSCC1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without CDC25A | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*94 arrows, 94 of them with an alert ⚠; grade A 0, B 0, C 94. Shown: the 12 strongest; 82 more arrows (82 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDX12P]] | C | DSCC1 activity raises DDX12P's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[LIN9]] | C | DSCC1 activity raises LIN9's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ZNF519]] | C | DSCC1 activity raises ZNF519's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[TICRR]] | C | DSCC1 activity raises TICRR's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[XRCC2]] | C | DSCC1 activity raises XRCC2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without DSCC1 | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[BLM]] | C | DSCC1 activity raises BLM's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without DSCC1 | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[FANCI]] | C | DSCC1 activity raises FANCI's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without DSCC1 | 0.013 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[GINS1]] | C | DSCC1 activity raises GINS1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without DSCC1 | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CASP8AP2]] | C | DSCC1 activity raises CASP8AP2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without DSCC1 | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ATAD5]] | C | DSCC1 activity raises ATAD5's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without DSCC1 | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[POLQ]] | C | DSCC1 activity raises POLQ's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without DSCC1 | 0.015 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[L2HGDH]] | C | DSCC1 activity raises L2HGDH's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without DSCC1 | 0.016 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.920). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.9, -45.0); signed map (-37.2, -42.9). **Vector** length 100, 25.2% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.72 to 40); *E2F G1/S* (control, mean cos +0.72 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +5.5 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | +3.8 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.2 | +12.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +10.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | +4.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Irinotecan (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.5 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.9 | -5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -3.6 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | DNA replication and sister chromatid cohesion 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.12 — chr8:119,833,976-119,855,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCC1, hDCC1, MGC5528 |
| Hallmark sets | E2F_TARGETS |
| Reactome | 6 pathways, smallest: Polymerase switching on the C-strand of the telomere; Telomere C-strand (Lagging Strand) Synthesis; Extension of Telomeres |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVC3](https://www.uniprot.org/uniprotkb/Q9BVC3) (Sister chromatid cohesion protein DCC1):

> Loads PCNA onto primed templates regulating velocity, spacing and restart activity of replication forks. May couple DNA replication to sister chromatid cohesion through regulation of the acetylation of the cohesin subunit SMC3.

**Summary**, from NCBI Gene [79075](https://www.ncbi.nlm.nih.gov/gene/79075):

> CHTF18 (MIM 613201), CHTF8 (MIM 613202), and DSCC1 are components of an alternative replication factor C (RFC) (see MIM 600404) complex that loads PCNA (MIM 176740) onto DNA during S phase of the cell cycle (Merkle et al., 2003 [PubMed 12766176]; Bermudez et al., 2003 [PubMed 12930902]).[supplied by OMIM, Dec 2009]

**Accessions** — [HGNC:24453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24453) · Entrez [79075](https://www.ncbi.nlm.nih.gov/gene/79075) · UniProt [Q9BVC3](https://www.uniprot.org/uniprotkb/Q9BVC3) · Ensembl [ENSG00000136982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136982)

## Data

Gene col 5952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5952); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5952]; `tensor/DDL_lfc|DDL_z.npy` [5952]; `embed/gene_vectors.npy` [5952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5952 or target_col == 5952). Every well: [[DSCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
