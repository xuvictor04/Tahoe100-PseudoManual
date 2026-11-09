---
symbol: "RNASEH2A"
type: "gene"
col: 2519
ensembl_id: "ENSG00000104889"
name: "ribonuclease H2 subunit A"
location: "19p13.13"
module: 6
arm: "+"
pooled_cpm: 4.74
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RNASEH2A

*ribonuclease H2 subunit A* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.73× (z +12.1, q 7e-31, up in 6 of 8 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.66× (z +4.7, q 2e-04, up in 14 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 7.58×; ⚠ cell-cycle shift, explains ~63% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0594×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SHP-77 0.122×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.294×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPH]] (+0.79, fdr 7e-06), [[TCF19]] (+0.79, fdr 7e-06), [[MYBL2]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 7.58×; ⚠ cell-cycle shift, explains ~63% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.73×** | +12.1 | 7e-31 | 6/8 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **3.34×** | +11.5 | 3e-28 | 20/21 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.65×** | +9.3 | 2e-18 | 40/47 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.64×** | +9.3 | 2e-18 | 38/47 (SW480, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.52×** | +8.2 | 3e-14 | 10/12 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.18×** | +7.5 | 8e-12 | 31/46 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **2.03×** | +6.5 | 6e-09 | 16/25 (SW480, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.59×** | +6.3 | 2e-08 | 20/38 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.78×** | +5.5 | 2e-06 | 14/29 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.43×** | +4.8 | 7e-05 | 17/39 (HS-578T, C32, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.69×** | +4.8 | 7e-05 | 14/30 (HS-578T, PANC-1, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.66×** | +4.7 | 2e-04 | 14/42 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.52×** | +4.0 | 0.003 | 11/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.31×** | +3.7 | 0.008 | 8/46 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.014 | 9/46 (J82, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2519.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0594×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SHP-77 0.122×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.294×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.624× | -3.2 | 0.57 | 7/47 (SW480, A-172, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.294× (z -8.8) |
| [[HCT15 (line)]] | alt | 6.59 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0600× (z -8.5) |
| [[HS-578T (line)]] | alt | 5.72 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +10.4) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 4.55 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM 0.0594× (z -10.4) |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.122× (z -9.0) |
| [[A-172 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPH]] | +0.79 | +0.86 / +0.76 | both halves | 7e-06 |  |
| [[TCF19]] | +0.79 | +0.67 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MYBL2]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[WDHD1]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 | STRING 549 |
| [[E2F1]] | +0.78 | +0.70 / +0.85 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.78 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[CDC6]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 413 |
| [[MCM10]] | +0.76 | +0.63 / +0.84 | both halves | 7e-06 | STRING 453 |
| [[GINS2]] | +0.76 | +0.60 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 520 |
| [[RFC2]] | +0.76 | +0.66 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 734 |
| [[ZWINT]] | +0.76 | +0.76 / +0.80 | both halves | 7e-06 | STRING 427 |
| [[E2F2]] | +0.75 | +0.71 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises RNASEH2A's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without TCF19 | 0.031 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises RNASEH2A's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without E2F2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises RNASEH2A's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without ZNF66 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[XKR7]] | B | XKR7 activity raises RNASEH2A's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.39× lower at baseline in the lines without XKR7 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[DSCC1]] | C | DSCC1 activity raises RNASEH2A's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.02× lower at baseline in the lines without DSCC1 | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises RNASEH2A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without AURKB | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises RNASEH2A's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.16× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises RNASEH2A's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises RNASEH2A's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.15× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises RNASEH2A's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without MCM10 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises RNASEH2A's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without CLSPN | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -44.4); signed map (-38.3, -45.6). **Vector** length 58.9, 8.79% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.63 to 28); *DNA Replication* (reactome, mean cos +0.62 to 40); *E2F G1/S* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +3.5 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +2.9 | +6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +2.8 | +9.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | +2.7 | +5.5 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +1.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease H2 subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,806,584-12,813,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNASEHI, RNHIA, RNHL, AGS4 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [O75792](https://www.uniprot.org/uniprotkb/O75792) (Ribonuclease H2 subunit A):

> Catalytic subunit of RNase HII, an endonuclease that specifically degrades the RNA of RNA:DNA hybrids. Participates in DNA replication, possibly by mediating the removal of lagging-strand Okazaki fragment RNA primers during DNA replication. Mediates the excision of single ribonucleotides from DNA:RNA duplexes.

**Summary**, from NCBI Gene [10535](https://www.ncbi.nlm.nih.gov/gene/10535):

> The protein encoded by this gene is a component of the heterotrimeric type II ribonuclease H enzyme (RNAseH2). RNAseH2 is the major source of ribonuclease H activity in mammalian cells and endonucleolytically cleaves ribonucleotides. It is predicted to remove Okazaki fragment RNA primers during lagging strand DNA synthesis and to excise single ribonucleotides from DNA-DNA duplexes. Mutations in this gene cause Aicardi-Goutieres Syndrome (AGS), a an autosomal recessive neurological disorder …

**Accessions** — [HGNC:18518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18518) · Entrez [10535](https://www.ncbi.nlm.nih.gov/gene/10535) · UniProt [O75792](https://www.uniprot.org/uniprotkb/O75792) · Ensembl [ENSG00000104889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104889)

## Data

Gene col 2519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2519); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2519]; `tensor/DDL_lfc|DDL_z.npy` [2519]; `embed/gene_vectors.npy` [2519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2519 or target_col == 2519). Every well: [[RNASEH2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEH2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
