---
symbol: "GAPDH"
type: "gene"
col: 3247
ensembl_id: "ENSG00000111640"
name: "glyceraldehyde-3-phosphate dehydrogenase"
location: "12p13.31"
module: 99
arm: "+"
pooled_cpm: 2012.19
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# GAPDH

*glyceraldehyde-3-phosphate dehydrogenase* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.25× (z +5.9, q 2e-06, up in 45 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.53× (z +3.5, q 0.079, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 4.04×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.241× (z -16.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDOA]] (+0.71, fdr 7e-06), [[AKR7A2]] (+0.69, fdr 1e-05), [[PGK1]] (+0.68, fdr 1e-05); moves opposite to [[FAIM]] (-0.62, fdr 4e-05), [[ITPA]] (-0.62, fdr 5e-05), [[ZC3H7B]] (-0.61, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 4.04×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +5.9 | 2e-06 | 45/50 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.3 | 0.004 | 37/49 (A498, KATO III, …) | two highest doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.55×** | +3.6 | 0.072 | 41/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.079 | 36/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.72× | +3.1 | 0.18 | 45/47 (C32, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.71× | +3.1 | 0.18 | 47/48 (COLO 205, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.241×** | -16.4 | 0e+00 | 48/48 (SW 1271, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -8.4 | 1e-14 | 48/48 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.452×** | -6.2 | 1e-07 | 46/48 (C-33 A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -4.8 | 2e-04 | 36/49 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.688×** | -4.3 | 0.002 | 41/48 (PANC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -3.7 | 0.018 | 36/47 (C-33 A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.643×** | -3.6 | 0.026 | 46/48 (SK-MEL-2, SNU-423, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.673×** | -3.2 | 0.083 | 41/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.083 | 31/48 (SW 1271, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 1,500 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.0) |
| [[HCT15 (line)]] | alt | 3,335 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 3,972 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 4,194 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 3,545 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.2) |
| [[A-172 (line)]] | wt | 1,900 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.2) |
| [[A-427 (line)]] | wt | 2,267 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.4) |
| [[A498 (line)]] | wt | 907 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 994 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.6) |
| [[BT-474 (line)]] | alt | 979 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.1) |
| [[C32 (line)]] | wt | 2,975 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.6) |
| [[CHP-212 (line)]] | wt | 1,965 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.6) |
| [[H4 (line)]] | wt | 3,706 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.9) |
| [[HS-578T (line)]] | alt | 2,185 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 3,138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.8) |
| [[LS 180 (line)]] | wt | 1,975 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.4) |
| [[NCI-H2347 (line)]] | alt | 2,019 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.9) |
| [[PANC-1 (line)]] | alt | 1,867 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.6) |
| [[SNU-1 (line)]] | wt | 2,527 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -20.8) |
| [[SW 1271 (line)]] | alt | 4,136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.9) |
| [[SW 900 (line)]] | alt | 3,320 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -17.5) |
| [[A549 (line)]] | wt | 1,932 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 1,766 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 1,680 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 1,007 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.9) |
| [[HOP62 (line)]] | alt | 4,524 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.9) |
| [[Hs 766T (line)]] | wt | 1,222 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.9) |
| [[HT-29 (line)]] | alt | 1,131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.1) |
| [[J82 (line)]] | alt | 1,701 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.3) |
| [[KATO III (line)]] | alt | 1,170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.4) |
| [[LoVo (line)]] | wt | 1,371 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 2,632 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 2,926 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 2,065 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.7) |
| [[NCI-H661 (line)]] | alt | 720 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 2,116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.1) |
| [[RKO (line)]] | wt | 1,027 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.6) |
| [[RPMI-7951 (line)]] | alt | 1,727 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.4) |
| [[SHP-77 (line)]] | alt | 615 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 1,425 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.8) |
| [[SNU-423 (line)]] | alt | 1,693 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.5) |
| [[SW 1088 (line)]] | alt | 3,269 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.6) |
| [[SW1417 (line)]] | alt | 1,001 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.0) |
| [[SW48 (line)]] | wt | 1,350 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.5) |
| [[SW480 (line)]] | alt | 1,367 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.5) |
| [[AN3 CA (line)]] | alt | 1,256 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 784 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1,854 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1,555 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2,058 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDOA]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 999 |
| [[AKR7A2]] | +0.69 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PGK1]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 999 |
| [[VKORC1]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[P4HA2]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 506 |
| [[WDR54]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[GLG1]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[EIF4A1]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 | STRING 689 |
| [[P4HA1]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 527 |
| [[RAB3A]] | +0.62 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[CDON]] | +0.62 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[HILPDA]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.62 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ITPA]] | -0.62 | -0.56 / -0.39 | both halves | 5e-05 | STRING 402 |
| [[ZC3H7B]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD18A]] | -0.60 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[ANKRD18B]] | -0.59 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[GTF3C6]] | -0.58 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[TMEM147-AS1]] | -0.56 | -0.56 / -0.32 | both halves | 1e-04 |  |
| [[TXNRD2]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 | STRING 423 |
| [[NIPAL2]] | -0.56 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CCAR1]] | -0.56 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[QTRT1]] | -0.56 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[U2SURP]] | -0.56 | -0.53 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GAPDH's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.4, -14.3); signed map (-37.5, 28.2). **Vector** length 142, 65.7% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.6 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +3.4 | +1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.3 | +0.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +3.1 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.2 | +4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.6 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.6 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | glyceraldehyde-3-phosphate dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,534,512-6,538,374 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GAPD |
| Gene groups (HGNC) | Glyceraldehyde-3-phosphate dehydrogenase family |
| Hallmark sets | HYPOXIA, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P04406](https://www.uniprot.org/uniprotkb/P04406) (Glyceraldehyde-3-phosphate dehydrogenase):

> Catalyzes the conversion of D-glyceraldehyde 3-phosphate (G3P) into 3-phospho-D-glyceroyl phosphate in glycolysis and the reverse reaction in gluconeogenesis. Also catalyzes the side reaction which converts D-erythrose 4-phosphate to 1,4-bisphosphoerythronate with 3500-fold lower catalytic efficiency than it displays with G3P (By similarity). 1,4-bisphosphoerythronate is subsequently converted to 4-phosphoerythronate which can be dephosphorylated by PGP, preventing the accumulation of high …

**Summary**, from NCBI Gene [2597](https://www.ncbi.nlm.nih.gov/gene/2597):

> This gene encodes a member of the glyceraldehyde-3-phosphate dehydrogenase protein family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. The product of this gene catalyzes an important energy-yielding step in carbohydrate metabolism, the reversible oxidative phosphorylation of glyceraldehyde-3-phosphate in the presence of inorganic phosphate and nicotinamide adenine dinucleotide (NAD). The encoded protein …

**Accessions** — [HGNC:4141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4141) · Entrez [2597](https://www.ncbi.nlm.nih.gov/gene/2597) · UniProt [P04406](https://www.uniprot.org/uniprotkb/P04406) · Ensembl [ENSG00000111640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111640)

## Data

Gene col 3247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3247); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3247]; `tensor/DDL_lfc|DDL_z.npy` [3247]; `embed/gene_vectors.npy` [3247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3247 or target_col == 3247). Every well: [[GAPDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAPDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
