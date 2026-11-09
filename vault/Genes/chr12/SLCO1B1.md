---
symbol: "SLCO1B1"
type: "gene"
col: 5575
ensembl_id: "ENSG00000134538"
name: "solute carrier organic anion transporter family member 1B1"
location: "12p12.1"
module: 26
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 22
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SLCO1B1

*solute carrier organic anion transporter family member 1B1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.20× (z +12.7, q 2e-34, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.98× (z +12.4, q 8e-33, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.574× (z -4.5, q 0.004, down in 14 of 20 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.583× (z -4.4, q 0.004, down in 11 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (KATO III 0.101×, A-172 0.0959×, LS 180 0.150×; ⚠ cell-cycle shift, explains ~48% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.0498×, Hs 766T 0.0674×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.115×, A549 0.124×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.136×); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0420×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO1B3-SLCO1B7]] (+0.72, fdr 7e-06, ⚠ same locus), [[SLC26A7]] (+0.69, fdr 1e-05), [[LINC01208]] (+0.65, fdr 1e-05), [[LINC02977]] (+0.64, fdr 1e-05); moves opposite to [[FAM118A]] (-0.58, fdr 2e-05), [[COPG2]] (-0.55, fdr 3e-05), [[GNA12]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[HSD17B3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.20×** | +12.7 | 2e-34 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.98×** | +12.4 | 8e-33 | 9/14 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.00×** | +10.3 | 2e-22 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +10.2 | 5e-22 | 6/15 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +9.9 | 4e-21 | 1/13 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.02×** | +8.9 | 8e-17 | 10/15 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +7.0 | 3e-10 | 7/13 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +6.7 | 1e-09 | 7/15 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +6.5 | 6e-09 | 10/17 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.1 | 2e-05 | 9/19 (NCI-H2030, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.6 | 3e-04 | 1/15 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.84×** | +4.4 | 6e-04 | 1/5 (LoVo) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.9 | 0.005 | 1/13 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.005 | 9/18 (LoVo, Hs 766T, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.017 | 7/17 (LoVo, KATO III, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.017 | 2/16 (LS 180, A-172) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.021 | 4/17 (LoVo, A-172, …) | two highest doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **2.24×** | +3.4 | 0.021 | 4/11 (LS 180, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +2.9 | 0.096 | 7/16 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5575.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 3 lines (KATO III 0.101×, A-172 0.0959×, LS 180 0.150×; ⚠ cell-cycle shift, explains ~48% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.0498×, Hs 766T 0.0674×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.115×, A549 0.124×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.136×); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0420×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.574×** | -4.5 | 0.004 | 14/20 (LS 180, KATO III, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -4.4 | 0.004 | 11/17 (HEC-1-A, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.637×** | -3.6 | 0.068 | 7/19 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.4 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +20.9) | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0498× (z -14.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.9) |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0959× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 3.05 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0420× (z -9.6) |
| [[Hs 766T (line)]] | wt | 9.48 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0674× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.426 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO1B3-SLCO1B7]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | ⚠ same locus (40.9 kb, same strand: neighbours can correlate without regulation) |
| [[SLC26A7]] | +0.69 | +0.57 / +0.55 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[LINC01208]] | +0.65 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LINC02977]] | +0.64 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.64 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | +0.63 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | +0.63 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[PRR4]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[LINC02889]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[AEBP2]] | +0.62 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NEB]] | +0.61 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[MCPH1]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.58 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[COPG2]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GNA12]] | -0.55 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TPST2]] | -0.54 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ATP7B]] | -0.54 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[XYLT2]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[HACE1]] | -0.53 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MAST3]] | -0.53 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SLCO1B1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SLCO1B1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B3-SLCO1B7 activity raises SLCO1B1's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 3.89× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises SLCO1B1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.44× lower at baseline in the lines without TIMD4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises SLCO1B1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.11× lower at baseline in the lines without HAVCR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[POU5F1]] | C | POU5F1 activity raises SLCO1B1's level | lines that do not express POU5F1 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without POU5F1 | 0.024 | ⚠ within organs, on part of the lines; also absent: P2RY2, C4BPB, UGT1A6; co-absent with the target |
| [[RHEX]] | C | RHEX activity raises SLCO1B1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 1.89× lower at baseline in the lines without RHEX | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD17B3]] | B | SLCO1B1 activity raises HSD17B3's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without SLCO1B1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |
| [[MZF1-AS1]] | B | SLCO1B1 activity raises MZF1-AS1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.34× lower at baseline in the lines without SLCO1B1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |
| [[SLC38A4-AS1]] | B | SLCO1B1 activity raises SLC38A4-AS1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without SLCO1B1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |
| [[NAALADL2]] | B | SLCO1B1 activity strengthens NAALADL2's drug response | lines that do not express SLCO1B1 (20) vs lines expressing it (17) | the lines without SLCO1B1 respond 0.78× as strongly (z diff +1.64); strongest at Panobinostat 5 µM: 0.37x vs 0.18x (z diff +2.9) | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; target measured in part of the lines; artifact flags |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B1 activity raises SLCO1B3-SLCO1B7's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 8.01× lower at baseline in the lines without SLCO1B1 | 9e-06 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[POU5F1]] | C | SLCO1B1 activity raises POU5F1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without SLCO1B1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[HAVCR1]] | C | SLCO1B1 activity raises HAVCR1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without SLCO1B1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |
| [[TIMD4]] | C | SLCO1B1 activity raises TIMD4's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without SLCO1B1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.3, 16.3); signed map (22.3, 1.0). **Vector** length 47.3, 11.2% of its response variance represented; |z| ≥ 3 in 475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.3 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 1B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,131,194-21,239,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP-C, LST-1, OATP1B1; previously SLC21A6 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 14 pathways, smallest: Atorvastatin ADME; Organic anion transport by SLCO transporters; Recycling of bile acids and salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6L6](https://www.uniprot.org/uniprotkb/Q9Y6L6) (Solute carrier organic anion transporter family member 1B1):

> Mediates the Na(+)-independent uptake of organic anions. Shows broad substrate specificity, can transport both organic anions such as bile acid taurocholate (cholyltaurine) and conjugated steroids (dehydroepiandrosterone 3-sulfate, 17-beta-glucuronosyl estradiol, and estrone 3-sulfate), as well as eicosanoids (prostaglandin E2, thromboxane B2, leukotriene C4, and leukotriene E4), and thyroid hormones (T4/L-thyroxine, and T3/3,3',5'-triiodo-L-thyronine). Can take up bilirubin glucuronides from …

**Summary**, from NCBI Gene [10599](https://www.ncbi.nlm.nih.gov/gene/10599):

> This gene encodes a liver-specific member of the organic anion transporter family. The encoded protein is a transmembrane receptor that mediates the sodium-independent uptake of numerous endogenous compounds including bilirubin, 17-beta-glucuronosyl estradiol and leukotriene C4. This protein is also involved in the removal of drug compounds such as statins, bromosulfophthalein and rifampin from the blood into the hepatocytes. Polymorphisms in the gene encoding this protein are associated with …

**Accessions** — [HGNC:10959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10959) · Entrez [10599](https://www.ncbi.nlm.nih.gov/gene/10599) · UniProt [Q9Y6L6](https://www.uniprot.org/uniprotkb/Q9Y6L6) · Ensembl [ENSG00000134538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134538)

## Data

Gene col 5575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5575); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5575]; `tensor/DDL_lfc|DDL_z.npy` [5575]; `embed/gene_vectors.npy` [5575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5575 or target_col == 5575). Every well: [[SLCO1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
