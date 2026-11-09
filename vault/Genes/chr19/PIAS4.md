---
symbol: "PIAS4"
type: "gene"
col: 2567
ensembl_id: "ENSG00000105229"
name: "protein inhibitor of activated STAT 4"
location: "19p13.3"
module: 20
arm: "-"
pooled_cpm: 25.49
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PIAS4

*protein inhibitor of activated STAT 4* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.60× (z +8.0, q 9e-13, up in 33 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +6.5, q 2e-08, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.591× (z -12.6, q 2e-33, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2K7]] (+0.81, fdr 7e-06), [[CROCCP2-1]] (+0.71, fdr 7e-06), [[INAFM1]] (+0.68, fdr 7e-06); moves opposite to [[DR1]] (-0.63, fdr 1e-05), [[EMB]] (-0.63, fdr 1e-05), [[DHFR]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.0 | 9e-13 | 33/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.5 | 2e-08 | 31/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 2e-07 | 29/47 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +4.9 | 2e-04 | 23/46 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.22×** | +4.7 | 3e-04 | 19/47 (PANC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.5 | 7e-04 | 19/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **1.29×** | +4.3 | 0.001 | 21/44 (SW1417, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.007 | 12/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.061 | 9/48 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -12.6 | 2e-33 | 41/48 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -10.6 | 6e-24 | 24/35 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.518×** | -10.3 | 2e-22 | 29/40 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -8.8 | 2e-16 | 30/43 (hTERT-HPNE, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -5.5 | 4e-06 | 25/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.765×** | -4.4 | 0.001 | 20/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.854× | -3.8 | 0.013 | 18/48 (Panc 03.27, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.805×** | -3.7 | 0.018 | 16/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.867× | -3.4 | 0.038 | 12/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **0.818×** | -3.4 | 0.038 | 16/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.4 | 0.038 | 15/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.821×** | -3.3 | 0.040 | 12/48 (SNU-423, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 34.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -11.3) |
| [[A-172 (line)]] | wt | 40.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0654× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Imiquimod (maleate) (drug)]] 0.5 µM 0.183× (z -9.7) |
| [[C-33 A (line)]] | alt | 40.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[RKO (line)]] | wt | 30.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.1) |
| [[SW480 (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -14.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 14.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0996× (z -9.4) |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -16.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0805× (z -17.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.7) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.6) |
| [[A-427 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K7]] | +0.81 | +0.68 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CROCCP2-1]] | +0.71 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[CHMP1A]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[POLR2J4]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SAT2]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[TIMM29]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.64 | +0.53 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EGLN2]] | +0.64 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CDC34]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[EMB]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DHFR]] | -0.61 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[IPO5]] | -0.61 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[HNRNPA3]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[RPL6]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DARS2]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[ACTR3]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[FH]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIAS4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.9, -28.0); signed map (-14.8, -0.3). **Vector** length 96.5, 21.4% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.0 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +4.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +3.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.2 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.1 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein inhibitor of activated STAT 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,007,736-4,039,386 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Piasg, PIASY, FLJ12419, ZMIZ6 |
| Gene groups (HGNC) | Zinc fingers MIZ-type |
| Reactome | 25 pathways, smallest: Vitamin D (calciferol) metabolism; SUMOylation of immune response proteins; SUMOylation of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2W9](https://www.uniprot.org/uniprotkb/Q8N2W9) (E3 SUMO-protein ligase PIAS4):

> Functions as an E3-type small ubiquitin-like modifier (SUMO) ligase, stabilizing the interaction between UBE2I and the substrate, and as a SUMO-tethering factor. Mediates sumoylation of ALKBH5, AXIN1, CEBPA, KLF8, GATA2, PARK7, HERC2, MYB, TCF4 and RNF168. Plays a crucial role as a transcriptional coregulation in various cellular pathways, including the STAT pathway, the p53/TP53 pathway, the Wnt pathway and the steroid hormone signaling pathway. Involved in gene silencing. In Wnt signaling, …

**Summary**, from NCBI Gene [51588](https://www.ncbi.nlm.nih.gov/gene/51588):

> Enables SUMO ligase activity and ubiquitin protein ligase binding activity. Involved in several processes, including negative regulation of protein localization to chromatin; positive regulation of double-strand break repair via homologous recombination; and regulation of RNA metabolic process. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17002) · Entrez [51588](https://www.ncbi.nlm.nih.gov/gene/51588) · UniProt [Q8N2W9](https://www.uniprot.org/uniprotkb/Q8N2W9) · Ensembl [ENSG00000105229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105229)

## Data

Gene col 2567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2567); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2567]; `tensor/DDL_lfc|DDL_z.npy` [2567]; `embed/gene_vectors.npy` [2567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2567 or target_col == 2567). Every well: [[PIAS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIAS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
