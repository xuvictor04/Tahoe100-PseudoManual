---
symbol: "GINS3"
type: "gene"
col: 11228
ensembl_id: "ENSG00000181938"
name: "GINS complex subunit 3"
location: "16q21"
module: 6
arm: "+"
pooled_cpm: 5.62
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GINS3

*GINS complex subunit 3* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +12.2, q 3e-31, up in 30 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.121×; ⚠ toxic; cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.100×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SNU-423 0.0516×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F2]] (+0.73, fdr 7e-06), [[DCLRE1B]] (+0.70, fdr 7e-06), [[FAM111B]] (+0.67, fdr 7e-06); moves opposite to [[CCNI]] (-0.53, fdr 4e-05), [[CHP1]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +12.2 | 3e-31 | 30/40 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +11.6 | 2e-28 | 16/26 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +8.8 | 3e-16 | 26/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.76×** | +7.4 | 2e-11 | 20/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +7.2 | 8e-11 | 22/42 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.70×** | +6.7 | 3e-09 | 2/9 (NCI-H2030, NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.62×** | +6.3 | 2e-08 | 15/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-07 | 18/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.5 | 3e-06 | 9/45 (SW480, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.57×** | +5.5 | 3e-06 | 1/13 (J82) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 4e-06 | 17/44 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.88×** | +4.3 | 7e-04 | 2/33 (MIA PaCa-2, A-427) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.001 | 10/41 (SW 900, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.81×** | +4.1 | 0.002 | 3/35 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.35×** | +3.9 | 0.004 | 9/43 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.004 | 15/38 (NCI-H2030, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +3.9 | 0.004 | 5/34 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 12/43 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.007 | 7/37 (CFPAC-1, A498, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.025 | 3/37 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.038 | 5/38 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.121×; ⚠ toxic; cell-cycle shift, explains ~65% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 0.100×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SNU-423 0.0516×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.677× | -3.7 | 0.15 | 6/46 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.3 | 0.26 | 10/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.789× | -3.1 | 0.35 | 4/45 (KATO III, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 6.17 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.38× (z +10.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.4) | — |
| [[J82 (line)]] | alt | 7.56 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~65% of this change |
| [[NCI-H2030 (line)]] | alt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 2.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.38 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0516× (z -9.7) |
| [[A-427 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F2]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[DCLRE1B]] | +0.70 | +0.63 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FAM111B]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.66 | +0.66 / +0.71 | both halves | 7e-06 | STRING 446 |
| [[UHRF1]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[E2F3]] | +0.65 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[CDC25A]] | +0.65 | +0.57 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[E2F1]] | +0.65 | +0.65 / +0.71 | both halves | 7e-06 | pathway: S Phase |
| [[POLA2]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 622 |
| [[ORC6]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 595 |
| [[CENPO]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[PIGW]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNI]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CHP1]] | -0.52 | -0.39 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises GINS3's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without E2F2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[SIRPA]] | B | SIRPA activity raises GINS3's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without SIRPA | 0.037 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[FAXC]] | B | FAXC activity raises GINS3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without FAXC | 0.038 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ZNF724]] | B | ZNF724 activity raises GINS3's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without ZNF724 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[ZNF66]] | B | ZNF66 activity raises GINS3's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without ZNF66 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[BRME1]] | C | BRME1 activity raises GINS3's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without BRME1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.5, -42.6); signed map (-38.6, -50.0). **Vector** length 60.2, 9.01% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.50 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.52 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.51 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.9 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +4.1 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.9 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | GINS complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,295,080-58,406,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13912, PSF3 |
| Gene groups (HGNC) | GINS complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 7 pathways, smallest: Unwinding of DNA; DNA strand elongation; Synthesis of DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRX5](https://www.uniprot.org/uniprotkb/Q9BRX5) (DNA replication complex GINS protein PSF3):

> Required for correct functioning of the GINS complex, a complex that plays an essential role in the initiation of DNA replication, and progression of DNA replication forks. GINS complex is a core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built.

**Summary**, from NCBI Gene [64785](https://www.ncbi.nlm.nih.gov/gene/64785):

> This gene encodes a protein subunit of the GINS heterotetrameric complex, which is essential for the initiation of DNA replication and replisome progression in eukaryotes. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25851) · Entrez [64785](https://www.ncbi.nlm.nih.gov/gene/64785) · UniProt [Q9BRX5](https://www.uniprot.org/uniprotkb/Q9BRX5) · Ensembl [ENSG00000181938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181938)

## Data

Gene col 11228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11228); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11228]; `tensor/DDL_lfc|DDL_z.npy` [11228]; `embed/gene_vectors.npy` [11228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11228 or target_col == 11228). Every well: [[GINS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GINS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
