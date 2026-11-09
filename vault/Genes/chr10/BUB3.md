---
symbol: "BUB3"
type: "gene"
col: 7808
ensembl_id: "ENSG00000154473"
name: "BUB3 mitotic checkpoint protein"
location: "10q26.13"
module: 22
arm: "+"
pooled_cpm: 110.2
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BUB3

*BUB3 mitotic checkpoint protein* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +11.9, q 6e-30, up in 42 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.31× (z +3.5, q 0.027, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.811× (z -5.4, q 5e-05, down in 28 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.438×, SNU-1 0.382×, A498 0.575×, NCI-H1573 0.539×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (RKO 0.514×, LS 180 0.533×; ⚠ cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SW 1088 0.0990×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNA2]] (+0.76, fdr 7e-06), [[KIF23]] (+0.75, fdr 7e-06), [[ARHGAP11A]] (+0.75, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AURKB]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.93×** | +11.9 | 6e-30 | 42/49 (SNU-423, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.65×** | +8.4 | 1e-14 | 38/45 (MIA PaCa-2, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.56×** | +7.7 | 2e-12 | 31/44 (HT-29, A549, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.45×** | +6.5 | 1e-08 | 35/47 (Panc 03.27, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.34×** | +5.3 | 1e-05 | 29/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.28×** | +4.5 | 7e-04 | 31/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.51×** | +3.9 | 0.007 | 24/47 (C32, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.9 | 0.008 | 25/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.027 | 22/48 (RKO, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.21×** | +3.5 | 0.027 | 21/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.033 | 21/48 (PANC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.034 | 19/48 (SW 900, H4, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.041 | 11/49 (SW 900, LOX-IMVI, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.2 | 0.054 | 6/48 (NCI-H1792, C32, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.18× | +3.1 | 0.079 | 16/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.438×, SNU-1 0.382×, A498 0.575×, NCI-H1573 0.539×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (RKO 0.514×, LS 180 0.533×; ⚠ cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (SW 1088 0.0990×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.811×** | -5.4 | 5e-05 | 28/48 (RKO, LS 180, …) | rises with dose | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.784×** | -4.2 | 0.006 | 34/48 (SHP-77, NCI-H1573, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.873× | -3.5 | 0.078 | 15/48 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.827×** | -3.5 | 0.078 | 21/48 (RKO, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.832×** | -3.3 | 0.089 | 23/49 (Hs 766T, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.3 | 0.089 | 22/48 (PANC-1, J82, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.786× | -3.1 | 0.15 | 18/48 (HEC-1-A, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.846× | -3.0 | 0.17 | 12/48 (A498, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 109 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 173 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.91× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 95.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A498 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.46× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[LS 180 (line)]] | wt | 92.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.533× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 97.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.514× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW 1088 (line)]] | alt | 87.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0990× (z -9.1) |
| [[SW1417 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNA2]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 787 |
| [[KIF23]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 536 |
| [[ARHGAP11A]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[CKAP5]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 748 |
| [[CIT]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[TPX2]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[BUB1]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[KIF4A]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 407 |
| [[BIRC5]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 659 |
| [[NUF2]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 864 |
| [[KNL1]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 996 |
| [[CCNB1]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 880 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AURKB]] | C | AURKB activity raises BUB3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.38× lower at baseline in the lines without AURKB | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises BUB3's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without PBK | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises BUB3's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.40× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -55.2); signed map (-48.9, -43.0). **Vector** length 93.8, 26.5% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.67 to 28); *E2F targets* (hallmark, mean cos +0.58 to 46); *mitotic spindle* (hallmark, mean cos +0.61 to 38).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +2.7 | +2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +2.6 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.9 | +2.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -0.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.3 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BUB3 mitotic checkpoint protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:123,154,402-123,170,467 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BUB3L |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 27 pathways, smallest: Inactivation of APC/C via direct inhibition of the APC/C complex; Inhibition of the proteolytic activity of APC/C required for the onset of anaphase by mitotic spindle checkpoint components; APC-Cdc20 mediated degradation of Nek2A |
| Matched by | ensembl_id |

**Function**, from UniProt [O43684](https://www.uniprot.org/uniprotkb/O43684) (Mitotic checkpoint protein BUB3):

> Has a dual function in spindle-assembly checkpoint signaling and in promoting the establishment of correct kinetochore-microtubule (K-MT) attachments. Promotes the formation of stable end-on bipolar attachments. Necessary for kinetochore localization of BUB1. Regulates chromosome segregation during oocyte meiosis. The BUB1/BUB3 complex plays a role in the inhibition of anaphase-promoting complex or cyclosome (APC/C) when spindle-assembly checkpoint is activated and inhibits the ubiquitin ligase …

**Summary**, from NCBI Gene [9184](https://www.ncbi.nlm.nih.gov/gene/9184):

> This gene encodes a protein involved in spindle checkpoint function. The encoded protein contains four WD repeat domains and has sequence similarity with the yeast BUB3 protein. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1151) · Entrez [9184](https://www.ncbi.nlm.nih.gov/gene/9184) · UniProt [O43684](https://www.uniprot.org/uniprotkb/O43684) · Ensembl [ENSG00000154473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154473)

## Data

Gene col 7808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7808); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7808]; `tensor/DDL_lfc|DDL_z.npy` [7808]; `embed/gene_vectors.npy` [7808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7808 or target_col == 7808). Every well: [[BUB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BUB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
