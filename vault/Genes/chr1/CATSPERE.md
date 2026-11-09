---
symbol: "CATSPERE"
type: "gene"
col: 11028
ensembl_id: "ENSG00000179397"
name: "catsper channel auxiliary subunit epsilon"
location: "1q44"
module: 26
arm: "+"
pooled_cpm: 10.19
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CATSPERE

*catsper channel auxiliary subunit epsilon* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.84× (z +15.4, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.466× (z -6.6, q 2e-08, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACYP2]] (+0.80, fdr 7e-06), [[FBXL19-AS1]] (+0.78, fdr 8e-06), [[NEK11]] (+0.76, fdr 7e-06); moves opposite to [[MINK1]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.84×** | +15.4 | 0e+00 | 43/45 (C32, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +10.8 | 6e-25 | 23/27 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +8.7 | 7e-16 | 33/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.62×** | +5.9 | 4e-07 | 30/48 (Hs 766T, SW 900, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.8 | 1e-06 | 21/31 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.3 | 1e-05 | 6/20 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.3 | 1e-05 | 28/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +4.5 | 5e-04 | 22/47 (Hs 766T, J82, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +3.8 | 0.008 | 23/48 (Hs 766T, A-427, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.012 | 11/47 (NCI-H2347, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.033 | 13/46 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.062 | 16/47 (Hs 766T, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.1 | 0.072 | 14/38 (NCI-H2347, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.074 | 13/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.084 | 7/48 (A498, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.466×** | -6.6 | 2e-08 | 34/47 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.522×** | -5.7 | 4e-06 | 27/48 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.493×** | -5.6 | 4e-06 | 27/47 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -3.8 | 0.020 | 17/47 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -3.7 | 0.020 | 17/48 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.643×** | -3.5 | 0.044 | 18/43 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.693× | -3.2 | 0.12 | 19/48 (Panc 03.27, Hs 766T, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.602× | -3.2 | 0.12 | 14/48 (RPMI-7951, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.513× | -3.0 | 0.15 | 10/44 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.18 | 6 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.51× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0996× (z -10.4) |
| [[A-427 (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0469× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0600× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 9.53 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 9.75× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.0902× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 12.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.42× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.92× (z +8.7) | — |
| [[LoVo (line)]] | wt | 5.04 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 9.99× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 5.43 | 0 | 2 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0735× (z -8.9) ⚠ toxic · without an alert: [[Sunitinib (drug)]] 0.05 µM 0.0824× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.2× (z +12.9) | — |
| [[SW480 (line)]] | alt | 8.18 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.48× (z +11.3) | — |
| [[A-172 (line)]] | wt | 31.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 7.54 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0799× (z -9.2) |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 12.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 26.8× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -8.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HS-578T (line)]] | alt | 5.02 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.0× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 5.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 43.5× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 7.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.10× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.32 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0631× (z -10.6) ⚠ toxic; unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 8.75 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.5× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.72× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 17.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.58× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 6.70 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 5.21 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0695× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 8.20 | 1 | 0 | [[Auranofin (drug)]] 5 µM 21.1× (z +8.7) | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACYP2]] | +0.80 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[FBXL19-AS1]] | +0.78 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[NEK11]] | +0.76 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SUCLG2-DT]] | +0.73 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[CELF6]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SUMO2P17]] | +0.72 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.72 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[FAM174B]] | +0.72 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[PSMD7-DT]] | +0.71 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[NQO1-DT]] | +0.71 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CCDC30]] | +0.70 | +0.66 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINK1]] | -0.60 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CATSPERE's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HECTD2]] | B | HECTD2 activity raises CATSPERE's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without HECTD2 | 0.087 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CATSPERE's level | compounds that target TOP2A: 3 of 5 raise it (Amsacrine, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.7, 12.9); signed map (24.2, -4.3). **Vector** length 104, 24.4% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.0 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +5.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -3.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | catsper channel auxiliary subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,454,377-244,641,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33370; previously C1orf101 |
| Gene groups (HGNC) | CatSpermasome complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SY80](https://www.uniprot.org/uniprotkb/Q5SY80) (Cation channel sperm-associated auxiliary subunit epsilon):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization.

**Summary**, from NCBI Gene [257044](https://www.ncbi.nlm.nih.gov/gene/257044):

> Predicted to be involved in flagellated sperm motility and sperm capacitation. Located in sperm end piece; sperm midpiece; and sperm principal piece. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28491) · Entrez [257044](https://www.ncbi.nlm.nih.gov/gene/257044) · UniProt [Q5SY80](https://www.uniprot.org/uniprotkb/Q5SY80) · Ensembl [ENSG00000179397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179397)

## Data

Gene col 11028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11028); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11028]; `tensor/DDL_lfc|DDL_z.npy` [11028]; `embed/gene_vectors.npy` [11028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11028 or target_col == 11028). Every well: [[CATSPERE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPERE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
