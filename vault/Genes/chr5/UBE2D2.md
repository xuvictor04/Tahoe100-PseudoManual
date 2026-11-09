---
symbol: "UBE2D2"
type: "gene"
col: 5222
ensembl_id: "ENSG00000131508"
name: "ubiquitin conjugating enzyme E2 D2"
location: "5q31.2"
module: 3
arm: "+"
pooled_cpm: 179.42
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# UBE2D2

*ubiquitin conjugating enzyme E2 D2* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.24× (z +5.0, q 1e-04, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.779× (z -5.5, q 2e-05, down in 30 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.814× (z -4.7, q 6e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.411×, HEC-1-A 0.458×, A-172 0.476×, A498 0.468×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.467×, AN3 CA 0.358×, J82 0.533×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (BT-474 0.0720×, Panc 03.27 0.240×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.360×, A-172 0.489×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-172 0.585×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAHD1]] (+0.67, fdr 7e-06), [[UBE2R2]] (+0.67, fdr 7e-06), [[CCT6P3-1]] (+0.63, fdr 1e-05); moves opposite to [[HNRNPK]] (-0.64, fdr 7e-06), [[BBS10]] (-0.61, fdr 7e-06), [[DDX3X]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.0 | 1e-04 | 29/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +5.0 | 1e-04 | 27/48 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +4.2 | 0.004 | 24/48 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.012 | 19/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.036 | 8/49 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.17× | +3.6 | 0.036 | 15/47 (NCI-H2030, hTERT-HPNE, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.051 | 21/48 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.054 | 18/48 (NCI-H23, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.28× | +3.0 | 0.16 | 22/49 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5222.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SK-MEL-2 0.411×, HEC-1-A 0.458×, A-172 0.476×, A498 0.468×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.467×, AN3 CA 0.358×, J82 0.533×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (BT-474 0.0720×, Panc 03.27 0.240×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 0.360×, A-172 0.489×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-172 0.585×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.779×** | -5.5 | 2e-05 | 30/45 (SK-MEL-2, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.814×** | -4.7 | 6e-04 | 23/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -4.7 | 6e-04 | 18/48 (A-427, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~1% of this change | 0.852× | -3.8 | 0.019 | 19/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.869× | -3.2 | 0.14 | 19/47 (A-427, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | 0.877× | -3.1 | 0.14 | 23/49 (SW 1088, A-172, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.1 | 0.14 | 13/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.879× | -3.1 | 0.14 | 5/48 (LOX-IMVI, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 278 | 1 (1 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.67× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.360× (z -15.7) |
| [[A-172 (line)]] | wt | 203 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.476× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.489× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 271 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 247 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 213 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.657× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0720× (z -17.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.458× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[HT-29 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.560× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[LOX-IMVI (line)]] | wt | 131 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.05× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.589× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.589× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[Panc 03.27 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.240× (z -11.3) ⚠ toxic |
| [[RKO (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.418× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0634× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[SW 900 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.61× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 178 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 183 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 202 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAHD1]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[UBE2R2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 626 |
| [[CCT6P3-1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SRGAP2D]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ZNF500]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[RAB11FIP3]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[SDHAP4-1]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TRPC4AP]] | +0.60 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[E4F1]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[BBS10]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[DDX3X]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CHRAC1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PRKAR1A]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[BACE1-AS]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 | pathway: Death Receptor Signaling |
| [[ALG10]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[FAT1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[EIF4G2]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers UBE2D2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.8, -4.7); signed map (-39.3, 4.2). **Vector** length 132, 38.3% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -2.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Busulfan (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,526,431-139,628,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH5B, UBC4 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 47 pathways, smallest: Enterobacterial factors antagonize host defense; TICAM1, RIP1-mediated IKK complex recruitment; IKK complex recruitment mediated by RIP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P62837](https://www.uniprot.org/uniprotkb/P62837) (Ubiquitin-conjugating enzyme E2 D2):

> E2 ubiquitin-conjugating enzyme that accepts ubiquitin from the ubiquitin-activating enzyme E1 and transfers it to a E3 ubiquitin-protein ligase. Catalyzes 'Lys-48'-linked polyubiquitination. Mediates the selective degradation of short-lived and abnormal proteins. Functions in the E6/E6-AP-induced ubiquitination of p53/TP53. Mediates ubiquitination of PEX5 and SQSTM1 and autoubiquitination of STUB1 and TRAF6. Involved in the signal-induced conjugation and subsequent degradation of NFKBIA, …

**Summary**, from NCBI Gene [7322](https://www.ncbi.nlm.nih.gov/gene/7322):

> Regulated degradation of misfolded, damaged or short-lived proteins in eukaryotes occurs via the ubiquitin (Ub)-proteasome system (UPS). An integral part of the UPS system is the ubiquitination of target proteins and covalent linkage of Ub-containing proteins to form polymeric chains, marking them as targets for 26S proteasome-mediated degradation. Ubiquitination of proteins is mediated by a cascade of enzymes which includes E1 (ubiquitin activating), E2 (ubiquitin conjugating), and E3 …

**Accessions** — [HGNC:12475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12475) · Entrez [7322](https://www.ncbi.nlm.nih.gov/gene/7322) · UniProt [P62837](https://www.uniprot.org/uniprotkb/P62837) · Ensembl [ENSG00000131508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131508)

## Data

Gene col 5222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5222); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5222]; `tensor/DDL_lfc|DDL_z.npy` [5222]; `embed/gene_vectors.npy` [5222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5222 or target_col == 5222). Every well: [[UBE2D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
